import os
from pathlib import Path
from typing import List, Optional, Set, Union
import pandas as pd
import requests
import regex as re


# Default URL for auto-downloading NSFW words list
DEFAULT_NSFW_URL = "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en"


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
                  nsfw_words_filepath: Optional[str] = None, compression: Optional[str] = None, 
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
            print(len(chunk))

            filtered_chunks.append(chunk)

        self.data = pd.concat(filtered_chunks)

    def filter_nsfw(self, data, filter_column: str, nsfw_words: Union[str, Set[str], List[str]] = None) -> pd.DataFrame:
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
        
        if nsfw_words is None:
            nsfw_words = self.auto_download_nsfw_words(DEFAULT_NSFW_URL)

        elif isinstance(nsfw_words, str):
            if nsfw_words.startswith("http://") or nsfw_words.startswith("https://"):
                nsfw_words = self.auto_download_nsfw_words(nsfw_words)
            else:
                try:
                    with open(nsfw_words, 'r') as file:
                        nsfw_words = {word.strip().lower() for word in file}

                except FileNotFoundError:
                    raise ValueError(f"File with NSFW words {nsfw_words} not found.")
                
        elif isinstance(nsfw_words, (list, set)):
            nsfw_words = set([word.lower() for word in nsfw_words])
        else:
            raise ValueError("nsfw_words must be a string (file path), set, list, or URL.")

        if filter_column not in data.columns:
            raise ValueError(f"Column {filter_column} not found in data.")
        
        pattern = r'\b(?:' + '|'.join(map(re.escape, nsfw_words)) + r')\b'
        data = data[~data[filter_column].str.lower().str.contains(pattern, case=False, na=False)]

        return data

    def auto_download_nsfw_words(self, url: str) -> Set[str]:
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
            nsfw_words = set(response.text.strip().lower().split('\n'))
            nsfw_words = {word for word in nsfw_words if word}  # Remove empty strings
            return nsfw_words
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Failed to download NSFW words list from {url}. Error: {str(e)}")


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
        
        base_dir = base_dir or os.getcwd()
        Path(base_dir).mkdir(parents=True, exist_ok=True)

        for sample_size in sample_sizes:
            if sample_size >= len(self.data):
                # Sample all available unique rows without replacement
                sampled_data = self.data.copy()
            else:
                # Sample the requested number of rows with replacement
                sampled_data = self.data.sample(n=sample_size, replace=self.sample_with_replacement)

            filename = os.path.join(base_dir, f"{self.language}_sample_{sample_size}.{file_format}")
            sampled_data.to_csv(filename, index=False, sep=self.delimiter)