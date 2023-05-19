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

##### TEST ######
# Load the sampled dataset
sampled_df = pd.read_csv('hindi/en_XX-hi_IN.tsv', delimiter='\t', nrows=1000, encoding='utf-8')
# Rename the headers
sampled_df.columns = ['Domain', 'Source_URL', 'Source_Content', 'Target_URL', 'Target_Content']


print(len(sampled_df))
print("Sampled dataset:")
print(sampled_df['Domain'].head(10))
