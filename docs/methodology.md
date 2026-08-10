# Methodology and provenance

## Project evolution

This repository combines two master's coursework submissions using the same United Nations General Debate Corpus:

1. **AI course foundation:** Africa vs Europe comparison using EDA, TF-IDF/cosine similarity, LDA, K-means, LSTM classification and VADER sentiment.
2. **SMWA extension:** Africa-focused EDA, sentiment, LDA/NMF/BERTopic and country-mention network analysis.

The professional rebuild preserves this chronology and makes overlapping code reusable rather than presenting the assignments as unrelated projects.

## Source hierarchy

The QA pass used the following as authoritative coursework evidence:

- submitted AI-course PDF **`AI Project_ Africa - Europe Project`**;
- final source notebook **`AI project_Africa - Europe.ipynb`**;
- saved AI processed-data snapshot (3,826 Africa/Europe speeches);
- submitted SMWA paper **`898396.pdf`**;
- final **`Topic Modeling`** notebook;
- final **`Network Analysis`** notebook;
- raw UNGD CSV (7,507 speeches, 1970-2015 in the computational snapshot).

When two coursework artifacts disagree, the repository states the discrepancy rather than silently reconciling it.

## Shared preprocessing

The source workflows lowercase text, remove punctuation/non-text characters, tokenize, remove English stopwords and lemmatize. The professional implementation keeps these decisions while using portable paths and explicit functions.

`src/preprocessing.py` embeds the original Africa/Europe country-code choices and removes the need for a separate local continent-mapping spreadsheet.

## TF-IDF similarity

The original AI notebook fits TF-IDF over individual statements, computes a full cross-region cosine-similarity matrix, then prints only `cosine_sim[0][0]`. The submitted value 0.2640 is therefore a single speech-pair value.

The professional code deliberately exposes three estimands:

- first-pair similarity for exact coursework provenance;
- sampled mean cross-region speech-pair similarity;
- cosine between regional mean TF-IDF vectors.

This avoids assigning a corpus-level interpretation to a single matrix element.

## LDA

The AI comparison uses a joint 10-topic Gensim LDA model with vocabulary filtering (`no_above=0.30`, `no_below=10`), 50 passes and `random_state=0`. Topic prevalence is averaged by continent.

The SMWA extension independently estimates an Africa-only LDA and compares it with NMF and BERTopic.

## K-means

The AI workflow applies K-means to TF-IDF features, uses an elbow diagnostic and selects three clusters. The professional code adds reusable elbow and top-term helpers and reports cluster assignment counts from the saved processed-data snapshot.

## LSTM

The submitted classifier uses:

- 80/20 train-test split;
- vocabulary size 10,000;
- maximum sequence length 100;
- embedding dimension 100;
- LSTM units 128;
- Adam optimizer with learning rate 0.001;
- batch size 20;
- 10 epochs.

The original notebook uses the test set as validation data during training. The professional helper instead takes validation data from the training sample and keeps the held-out test sample for final evaluation. This is a deliberate methodological improvement and may produce different test accuracy from the submitted 85.1%.

## Sentiment

The course analyses use VADER. One original implementation tokenized text before later sentence processing, producing an inconsistent unit of analysis. The professional implementation scores sentence-like units directly from raw speech text and averages to speech-level compound sentiment.

Original sentiment figures and narrative interpretations remain available as provenance, but they are not silently relabeled as corrected results.

## Topic coherence

The SMWA paper reports LDA 0.3663, NMF 0.5464 and BERTopic 0.7768 using `c_v`. However, the original sections use different preprocessing/reference-corpus constructions. The professional functions allow model topic words to be evaluated against a common tokenized reference corpus; the original three numbers are therefore described as coursework-reported diagnostics, not a fully controlled model comparison.

## Network analysis

The submitted network code searches speech text for ISO3 country codes. The professional implementation instead matches country names and selected historical/orthographic aliases and counts a mentioned target at most once per speech. This improves construct validity but changes the network definition.

For that reason, the source-reported network claims and professional network reconstruction are shown separately.

## Reproducibility and dependencies

Core NLP dependencies are kept in `requirements.txt`. BERTopic and TensorFlow are split into optional files because they are heavy and unnecessary for the classical pipeline.

The repository includes automated tests and GitHub Actions CI. Raw and large processed data are intentionally excluded from Git history; the public UNGD CSV is downloaded locally and transformed by code.
