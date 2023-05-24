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
data_filepath = "../../data/external/en_XX-ta_IN.tsv.xz"
save_dir_filtered = '../../data/interim'
save_dir_samples = '../../data/processed'

# Define parameter values
compression = "xz"
chunk_size = 50000
nsfw_words_url = "https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en"
filter_column = 'Domain'
sample_sizes = [20, 100]
lang = 'en_ta'
extension_to_remove = "tsv.xz"

process_dataset(dataset_path = data_filepath, nsfw_words_url = nsfw_words_url, compression = compression, 
                save_dir_filtered = save_dir_filtered, save_dir_samples =  save_dir_samples, 
                sample_sizes = sample_sizes, extension_to_remove = extension_to_remove, 
                chunk_size = chunk_size, lang = lang, filter_column = filter_column)