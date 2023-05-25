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

# Define the chunk size
chunk_size = 50000

en_hi_20k_dir = '../../data/interim/en_hi_sample_20000.txt'
en_hi_100k_dir = '../../data/interim/en_hi_sample_100000.txt'
en_ta_20k_dir = '../../data/interim/en_ta_sample_20000.txt'
en_ta_100k_dir = '../../data/interim/en_ta_sample_100000.txt'

path_to_files = [en_hi_20k_dir, en_hi_100k_dir, en_ta_20k_dir, en_ta_100k_dir]
nrows = 1000
head = 5
encoding = 'utf-8'
delimiter = '\t'

def view_data(path_to_files: List[str] = None, nrows: int = 100, head: int = 5, 
              delimiter: str = '\t', encoding: str = 'utf-8') -> None:
    
    for dataset_path in path_to_files:
        print(f"\nLoading dataset from {dataset_path}...")
        file = pd.read_csv(dataset_path, delimiter=delimiter, 
                           encoding=encoding, nrows=nrows)
        print(f"Loading complete!")
        file = file.drop_duplicates()
        print(f"View top {head} in {nrows} rows...\n")
        print(file.head(head))
        print(f"End of file!\n")
    return None

view_data(path_to_files, nrows=nrows, head=head, 
              delimiter=delimiter, encoding=encoding)
