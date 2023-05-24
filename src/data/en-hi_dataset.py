'''
CCAligned: A Massive Collection of Cross-Lingual Web-Document Pairs

* https://aclanthology.org/2020.emnlp-main.480.pdf
* https://www.statmt.org/cc-aligned/

**Summary**

CCAligned consists of *parallel or comparable web-document pairs in 137 languages 
aligned with English*. 

These web-document pairs were constructed by performing language identification on raw web-documents, 
and ensuring corresponding language codes were corresponding in the URLs of web documents. 

This pattern matching approach yielded more than 100 million aligned documents paired with English. 
Recognizing that each English document was often aligned to mulitple documents in different target language, 
we can join on English documents to obtain aligned documents that directly pair two non-English documents (e.g., Arabic-French).
'''

from utils.dataset_processor import DatasetProcessor
import multiprocessing
from functools import partial

# Define the path to the datasets
dataset_hindi_path = "../../data/external/en_XX-hi_IN.tsv.xz"

# Define parameter values
compression = "xz"
chunk_size = 50000
nsfw_words_url = "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en"

# Define the sample sizes
sample_sizes = [20000, 100000]

# Create an instance of DatasetProcessor for the Hindi dataset
processor_hindi = DatasetProcessor(
    dataset_hindi_path, header=None, delimiter='\t', language='en_hi')

# Load the Hindi dataset and filter NSFW words
print("Loading English-Hindi dataset...")

processor_hindi.load_data(filter_column='Domain', remove_nsfw=True, nsfw_words_filepath=nsfw_words_url,
                          compression=compression, chunk_size=chunk_size)

print("Loading complete!\n")

print(processor_hindi.data.head(5))

# Define a function for generating samples


def generate_samples(processor, sample_size, base_dir, file_format):
    processor.generate_samples(
        [sample_size], base_dir=base_dir, file_format=file_format)


# Set the maximum number of concurrent processes
max_processes = multiprocessing.cpu_count() // 2

# Create a pool of worker processes
pool = multiprocessing.Pool(processes=max_processes)

# Generate samples for the Hindi dataset in parallel
generate_samples_hindi = partial(generate_samples, processor_hindi, base_dir='data/processed',
                                 file_format='tsv')
pool.map(generate_samples_hindi, sample_sizes)

# Close the pool and wait for the processes to complete
pool.close()
pool.join()
