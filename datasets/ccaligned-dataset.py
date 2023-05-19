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

# Load Full dataset
data = pd.read_csv('hindi/en_XX-hi_IN.tsv', delimiter='\t', encoding='utf-8', on_bad_lines='skip', header=None)
data.columns = ['Domain', 'Source_URL', 'Source_Content', 'Target_URL', 'Target_Content']

# Load the list of NSFW words from the file
with open('nsfw_en.txt', 'r') as file:
    nsfw_words = {word.strip().lower() for word in file}

# Filter out NSFW URLs
filtered_df = data[~data['Domain'].str.lower().str.contains('|'.join(nsfw_words))]

# Print the filtered DataFrame
print(filtered_df)

# Determine the population size
population_size = len(data)

# Determine the sample sizes
sample_sizes = [20000, 100000]

for sample_size in sample_sizes:
    # Sample the entire population if it's smaller than the desired sample size
    if sample_size >= population_size:
        sampled_data = data.copy()
    else:
        # Sample without replacement from the larger population
        sampled_data = data.sample(n=sample_size, replace=False)

    # Generate the filename based on the sample size
    filename = f"sample_{sample_size}.tsv"

    # Save the sampled data to a new TSV file
    sampled_data.to_csv(filename, sep='\t', index=False, encoding='utf-8')


##### TEST ######
# Load the sampled dataset
sampled_df = pd.read_csv('sampled_100000.tsv', delimiter='\t', encoding='utf-8')
# Rename the headers

print(len(sampled_df))
print("Sampled dataset:")
print(sampled_df.head())

