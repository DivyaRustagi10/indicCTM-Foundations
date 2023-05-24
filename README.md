# Contextualized Topic Models with Zero-shot Learning For Indic Languages (IndicCTM)

**Zero-shot Topic Modeling for Indic Languages is adapted from [Cross-lingual Contextualized Topic Models with Zero-shot Learning](https://aclanthology.org/2021.eacl-main.143) (Bianchi et al., EACL 2021)** *([implementation](https://github.com/DivyaRustagi10/contextualized-topic-models-ssl/blob/main/notebooks/ZeroshotTM_Parent_Paper_Implementation.ipynb))*.

Indic Topic Tagger is an upcoming frontend interface to interact with IndicCTM. Below is a glimpse of the prototype version. 
*Frontend and Azure deployment credits to Taylor Bostick!*

## Data
[PMIndia](https://data.statmt.org/pmindia/): Parallel corpus for En-Indian languages mined from Mann ki Baat speeches of the PM of India ([paper](https://arxiv.org/abs/2001.09907)).

## Models
*Versions*
* V 1.0: Base model for contextualized topic Models on same script languages (no accent support)
* V 2.0: Improved model for contextualized topic Models on same script languages (accent support added)

## Evaluation

*Metrics*

* Matches: % of times the predicted topic for the non-English test document is the same as for the respective test document in English. The higher the scores, the better.
* Centroid Embeddings: To also account for similar but not exactly equal topic predictions, we compute the centroid embeddings of the 5 words describing the predicted topic for both English and non-English documents. Then we compute the cosine similarity between those two centroids (CD).
* Distributional Similarity: Compute the KL divergence between the predicted topic distribution on the test document and the same test document in English. Lower scores are better, indicating that the distributions do not differ by much.

### Copyright
Copyright 2023 Divya Rustagi

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
