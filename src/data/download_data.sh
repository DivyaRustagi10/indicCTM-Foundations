#!/bin/bash
# code by ChatGPT
# assumes cookiecutter folder structure

# Download Hindi-English Document Aligned Corpus
curl -O https://data.statmt.org/cc-aligned/en_XX-hi_IN.tsv.xz > data/external/en_XX-hi_IN.tsv.xz

# Download Tamil-English Document Aligned Corpus
curl -O https://data.statmt.org/cc-aligned/en_XX-ta_IN.tsv.xz > data/external/en_XX-ta_IN.tsv.xz

# Unzip Hindi-English Aligned Documents
xz -d -k -f -c en_XX-hi_IN.tsv.xz > data/raw/en_XX-hi_IN.tsv

# Unzip Tamil-English Aligned Documents
xz -d -k -f -c en_XX-ta_IN.tsv.xz > data/raw/en_XX-ta_IN.tsv
