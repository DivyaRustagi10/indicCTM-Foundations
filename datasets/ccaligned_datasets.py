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

# Define the path to the datasets
dataset_hindi_path = "downloads/en_XX-hi_IN.tsv.xz"
dataset_tamil_path = "downloads/en_XX-ta_IN.tsv.xz"

# Define the sample sizes
sample_sizes: List[int] = [20000, 100000]

# Define new column names
cols = ['Domain', 'Source_URL', 'Source_Content', 'Target_URL', 'Target_Content']

# Create an instance of DatasetProcessor for Hindi dataset
processor_hindi = DatasetProcessor(dataset_hindi_path, header=None, delimiter='\t')

# Load the Hindi dataset and filter NSFW words
processor_hindi.load_data(filter_column='Source_Content', remove_nsfw=True, compression='xz')

# Generate samples for Hindi dataset
processor_hindi.generate_samples(sample_sizes, base_dir='samples', file_format='tsv')

# Create an instance of DatasetProcessor for Tamil dataset
processor_tamil = DatasetProcessor(dataset_tamil_path, header=None, delimiter='\t')

# Load the Tamil dataset and filter NSFW words
processor_tamil.load_data(filter_column='Source_Content', remove_nsfw=True, compression='xz')

# Generate samples for Tamil dataset
processor_tamil.generate_samples(sample_sizes, base_dir='samples', file_format='tsv')
