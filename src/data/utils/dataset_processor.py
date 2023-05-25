import os
from pathlib import Path
from typing import List, Optional, Set, Union
import pandas as pd
import requests
import regex as re
import random
from tqdm import tqdm


# Default URL for auto-downloading NSFW words list
DEFAULT_NSFW_URL = "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en"


def process_dataset(dataset_path: str, nsfw_words_url: str, compression: str, base_dir: str, sample_sizes: List[int],
                    extension_to_remove: str, save_dir: str, filter_column: str, chunk_size: int = 10000,
                    lang: str = 'en'):
    """
    Process the dataset, filter NSFW words, save the filtered data, and generate samples.
    """
    # Create an instance of DatasetProcessor
    processor = DatasetProcessor(dataset_path, header=None, language=lang, delimiter='\t')

    # Load the dataset and filter NSFW words
    print(f"\nLoading dataset from {dataset_path}...")
    processor.load_data(filter_column=filter_column, remove_nsfw=True, nsfw_words_filepath=nsfw_words_url,
                        compression=compression, chunk_size=chunk_size)
    print("Loading complete!")
        
    # Save the loaded and filtered data with a descriptive label
    save_filepath = os.path.join(save_dir, f"filtered_{os.path.basename(dataset_path).replace('.' + extension_to_remove, '')}.txt")
    print(f"Saving filtered data to {save_filepath}...")
    processor.save_data(save_filepath)
    print("Saving complete!")

    # Generate samples
    print(f"Generating {sample_sizes} samples...")
    processor.generate_samples(sample_sizes, base_dir=base_dir, file_format='tsv')
    print("Sample generation complete!")


class DatasetProcessor:
    """A class to process datasets.

    This class provides methods to load a dataset, filter out rows containing NSFW words,
    and generate samples from the dataset.

    Attributes:
        file_path (str): The path to the input file.
        header (int, optional): The row index to use as column names. Default is None.
        sample_with_replacement (bool, optional): Whether to sample with replacement. Default is False.
        delimiter (str, optional): The delimiter used in the input file. Default is '\t'.
        data (pd.DataFrame, optional): The loaded data. Default is None.
    """
    
    def __init__(self, file_path: str, header: Optional[int] = None, 
                 sample_with_replacement: bool = False, delimiter: str = '\t', language: str = 'en'):
        """Initialize DatasetProcessor.

        Args:
            file_path (str): The path to the input file.
            header (int, optional): The row index to use as column names. Default is None.
            sample_with_replacement (bool, optional): Whether to sample with replacement. Default is False.
            delimiter (str, optional): The delimiter used in the input file. Default is '\t'.
        """
        self.file_path = file_path
        self.header = header
        self.data = None
        self.sample_with_replacement = sample_with_replacement
        self.delimiter = delimiter
        self.language = language
        

    def load_data(self, filter_column: str = None, remove_nsfw: bool = True, 
                  nsfw_words_filepath: Union[str, Set[str], List[str]] = None, compression: Optional[str] = None, 
                  chunk_size: int = 50000) -> None:
        """Load the data from the input file and optionally filter out rows containing NSFW words using chunking.
        
        Args:
            filter_column (str, optional): The column to use for filtering. Default is None.
            remove_nsfw (bool, optional): Whether to remove rows containing NSFW words. Default is True.
            nsfw_words_filepath (str, optional): The path to the file containing NSFW words. Default is None.
            compression (str, optional): The compression algorithm used in the input file. Default is None.
            chunk_size (int, optional): The number of rows to read per chunk. Default is 50000.
        """
        if compression is not None:
            chunks = pd.read_csv(self.file_path, compression=compression, delimiter=self.delimiter, 
                                chunksize=chunk_size, on_bad_lines='skip', header=self.header)
        else:
            chunks = pd.read_csv(self.file_path, delimiter=self.delimiter, 
                                chunksize=chunk_size, on_bad_lines='skip', header=self.header)

        filtered_chunks = []

        for chunk in chunks:
            chunk.columns = ['Domain', 'Source_URL', 'Source_Content', 'Target_URL', 'Target_Content']

            if remove_nsfw and filter_column:
                if nsfw_words_filepath is None:
                    chunk = self.filter_nsfw(chunk, filter_column, nsfw_words=None)  # Pass nsfw_words as None
                else:
                    chunk = self.filter_nsfw(chunk, filter_column, nsfw_words=nsfw_words_filepath)
                    
            # Print the size of each chunk after filtering
            print(f"Filtered Chunk Size: {len(chunk)}")
            
            filtered_chunks.append(chunk)    

        self.data = pd.concat(filtered_chunks)
    

    def save_data(self, save_path: str) -> None:
            """Save the data to a file."""
            if self.data is None:
                raise ValueError("No data to save. Load data first.")
            self.data.to_csv(save_path, sep=self.delimiter, index=False) 


    @staticmethod 
    def auto_download_nsfw_words(url: str) -> Set[str]:
        """Auto-download the NSFW words list from the provided URL and remove empty strings.

        Args:
            url (str): The URL to download the NSFW words list.

        Returns:
            set: The set of NSFW words without empty strings.

        Raises:
            ConnectionError: If auto-download of NSFW words list fails.
        """
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            response.encoding = 'utf-8'  # ensure correct encoding
            nsfw_words = set(response.text.strip().lower().split('\n'))
            nsfw_words = {word for word in nsfw_words if word}  # Remove empty strings

            return nsfw_words
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to download NSFW words list from {url}. Error: {str(e)}")


    def filter_nsfw(self, data, filter_column: str, nsfw_words: Union[str, Set[str], List[str]] = DEFAULT_NSFW_URL) -> pd.DataFrame:
        """Filter the data to remove rows containing NSFW words.

        Args:
            data (pd.DataFrame): The input data.
            filter_column (str): The column to use for filtering.
            nsfw_words (str, set, list, optional): NSFW words to filter out. Can be a path to a text file, a set, a list of words, or a URL to auto-download the list. If not provided, it will be auto-downloaded from the provided URL or a default URL.

        Returns:
            pd.DataFrame: The filtered data.

        Raises:
            ValueError: If data is not loaded. Call load_data() first.
            ValueError: If nsfw_words doesn't match the expected formats.
            ConnectionError: If auto-download of NSFW words list fails.
        """
        if data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        if filter_column not in data.columns:
            raise ValueError(f"Column {filter_column} not found in data.") 
        
        # URL
        if isinstance(nsfw_words, str) and (nsfw_words.startswith("http://") or nsfw_words.startswith("https://")):
            nsfw_words = self.auto_download_nsfw_words(nsfw_words)
            
        # FILE PATH
        elif isinstance(nsfw_words, str):
            try:
                with open(nsfw_words, 'r') as file:
                    nsfw_words = {word.strip().lower() for word in file}
            except FileNotFoundError:
                raise ValueError(f"File with NSFW words {nsfw_words} not found.")
            
        # LIST OR SET
        elif isinstance(nsfw_words, (list, set)):
            nsfw_words = set([word.lower() for word in nsfw_words])
        else:
            raise ValueError("nsfw_words must be a string (file path), set, list, or URL.")
        
        pattern = r'(?:' + '|'.join(map(re.escape, nsfw_words)) + r')'
        data = data[~data[filter_column].str.lower().str.contains(pattern, case=False, na=False)]

        return data
        

    def generate_samples(self, sample_sizes: List[int], base_dir: str = os.getcwd(), file_format: str = 'tsv') -> None:
        """Generate samples from the data and save them to separate files.

        Args:
            sample_sizes (List[int]): A list of sample sizes.
            base_dir (str, optional): The base directory where sample files will be saved. Defaults to the current working directory.
            file_format (str, optional): The file format to save the samples. Defaults to 'tsv'.

        Raises:
            ValueError: If data is not loaded. Call load_data() first.
        """        
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        # Validate sample_sizes
        if any(sample_size <= 0 for sample_size in sample_sizes):
            raise TypeError("sample_sizes must contain positive integers.")

        base_dir = base_dir or os.getcwd()
        Path(base_dir).mkdir(parents=True, exist_ok=True)

        for sample_size in sample_sizes:
            
            if sample_size >= len(self.data):
                # Sample all available unique rows without replacement
                sampled_data = self.data.copy()
            else:
                # Perform reservoir sampling to generate the sample
                reservoir = []
                for i, row in enumerate(self.data.iterrows()):
                    if i < sample_size:
                        reservoir.append(row[1])
                    else:
                        j = random.randint(0, i)
                        if j < sample_size:
                            reservoir[j] = row[1]
                sampled_data = pd.DataFrame(reservoir)

            filename = os.path.join(base_dir, f"{self.language}_sample_{sample_size}.{file_format}")
            sampled_data.to_csv(filename, index=False, sep=self.delimiter)


