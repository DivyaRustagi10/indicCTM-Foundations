#!/bin/bash
# code by ChatGPT

# Create directories to store Hindi and Tamil data
mkdir hindi
mkdir tamil

# Download Hindi-English Document Aligned Corpus
curl -O https://data.statmt.org/cc-aligned/en_XX-hi_IN.tsv.xz --output /downloads/

# Download Tamil-English Document Aligned Corpus
curl -O https://data.statmt.org/cc-aligned/en_XX-ta_IN.tsv.xz --output /downloads/

# Unzip Hindi-English Aligned Documents
xz -d -k -f -c en_XX-hi_IN.tsv.xz > hindi/en_XX-hi_IN.tsv

# Unzip Tamil-English Aligned Documents
xz -d -k -f -c en_XX-ta_IN.tsv.xz > tamil/en_XX-ta_IN.tsv
