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
from typing import Union, List
import regex as re
# Define the chunk size
chunk_size = 50000

# Load the list of NSFW words from the file
with open('nsfw_en.txt', 'r') as file:
    nsfw_words = {word.strip().lower() for word in file}

# Create an empty list to store the filtered chunks
filtered_chunks = []
pattern = r'\b(?:' + '|'.join(map(re.escape, nsfw_words)) + r')\b'

dataset_hindi_path = "hindi/en_XX-hi_IN.tsv"
dataset_tamil_path = "tamil/en_XX-ta_IN.tsv"
# Iterate over the dataset in chunks
for chunk in pd.read_csv(dataset_hindi_path, delimiter='\t', chunksize=chunk_size, on_bad_lines='skip'):
    chunk.columns = ['Domain', 'Source_URL', 'Source_Content', 'Target_URL', 'Target_Content']
    # Apply the filtering to the "Domain" column of the chunk
    chunk = chunk[~chunk['Domain'].str.lower().str.contains(pattern, case=False, na=False)]
    # Append the filtered chunk to the list
    filtered_chunks.append(chunk)
    print(len(chunk))

# Concatenate the filtered chunks into a single DataFrame
filtered_df = pd.concat(filtered_chunks)

print(len(filtered_df))

# Determine the population size
population_size = len(filtered_df)

# Determine the sample sizes
sample_sizes = [20000, 100000]

for sample_size in sample_sizes:
    # Sample the entire population if it's smaller than the desired sample size
    if sample_size >= population_size:
        sampled_data = filtered_df.copy()
    else:
        # Sample without replacement from the larger population
        sampled_data = filtered_df.sample(n=sample_size, replace=False)

    # Generate the filename based on the sample size
    filename = f"sample_{sample_size}.tsv"

    # Save the sampled data to a new TSV file
    sampled_data.to_csv(filename, sep='\t', index=False, encoding='utf-8')


##### TEST ######
# Load the sampled dataset
sampled_df = pd.read_csv('sample_20000.tsv', delimiter='\t', encoding='utf-8')
# Rename the headers
sampled_df = sampled_df.drop_duplicates()

print(len(sampled_df))
print("Sampled dataset:")
print(sampled_df.head())

