'''
CCAligned: A Massive Collection of Cross-Lingual Web-Document Pairs

* https://aclanthology.org/2020.emnlp-main.480.pdf
* https://www.statmt.org/cc-aligned/

**Summary**

CCAligned consists of *parallel or comparable web-document pairs in 137 languages aligned with English*. 

These web-document pairs were constructed by performing language identification on raw web-documents, and ensuring corresponding language codes were corresponding in the URLs of web documents. 

This pattern matching approach yielded more than 100 million aligned documents paired with English. Recognizing that each English document was often aligned to mulitple documents in different target language, we can join on English documents to obtain aligned documents that directly pair two non-English documents (e.g., Arabic-French).
'''

import pandas as pd
from typing import List
from utils.dataset_processor import DatasetProcessor
import multiprocessing
from functools import partial

# Define the path to the datasets
dataset_tamil_path = "raw/en_XX-ta_IN.tsv.xz"

# Define parameter values
compression = "xz"
chunk_size  = 50000
nsfw_words_url = "https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/blob/master/en"

# Define the sample sizes
sample_sizes = [20000, 100000]

# Create an instance of DatasetProcessor for the Tamil dataset
processor_tamil = DatasetProcessor(dataset_tamil_path, header=None, delimiter='\t', language = 'en_ta')

# Load the Tamil dataset and filter NSFW words
print("\nLoading English-Tamil dataset...")

processor_tamil.load_data(filter_column='Domain', remove_nsfw=True, nsfw_words_filepath = nsfw_words_url,
                          compression=compression, chunk_size = chunk_size)

print("Loading complete!")

print(processor_tamil.data.head(5))

# Define a function for generating samples
def generate_samples(processor, sample_size, base_dir, file_format):
    processor.generate_samples([sample_size], base_dir=base_dir, file_format=file_format)

# Set the maximum number of concurrent processes
max_processes = multiprocessing.cpu_count() // 2

# Create a pool of worker processes
pool = multiprocessing.Pool(processes=max_processes)

# Generate samples for the Tamil dataset in parallel
generate_samples_tamil = partial(generate_samples, processor_tamil, base_dir='tamil', file_format='tsv')
pool.map(generate_samples_tamil, sample_sizes)

# Close the pool and wait for the processes to complete
pool.close()
pool.join()