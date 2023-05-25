'''
CCAligned: A Massive Collection of Cross-Lingual Web-Document Pairs

* https://aclanthology.org/2020.emnlp-main.480.pdf
* https://www.statmt.org/cc-aligned/

**Summary**

CCAligned consists of *parallel or comparable web-document pairs in 137 languages aligned with English*. 

These web-document pairs were constructed by performing language identification on raw web-documents, and ensuring corresponding language codes were corresponding in the URLs of web documents. 

This pattern matching approach yielded more than 100 million aligned documents paired with English. Recognizing that each English document was often aligned to mulitple documents in different target language, we can join on English documents to obtain aligned documents that directly pair two non-English documents (e.g., Arabic-French).
'''
import os
from utils.dataset_processor import DatasetProcessor, process_dataset

# Define the path to the datasets
data_filepath = "../../data/external/en_XX-hi_IN.tsv.xz"
filtered_dir = '../../data/interim'
samples_dir = '../../data/processed'


# Define parameter values
compression = "xz"
chunk_size = 50000
nsfw_words_url = "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en"
filter_column = 'Domain'
sample_sizes = [10, 50]
lang = 'en_hi'
extension_to_remove = "tsv.xz"


process_dataset(dataset_path = data_filepath, nsfw_words_url = nsfw_words_url, compression = compression, 
                base_dir = samples_dir, sample_sizes = sample_sizes, extension_to_remove = extension_to_remove,
                save_dir = filtered_dir, filter_column = filter_column, chunk_size = chunk_size, lang = lang)