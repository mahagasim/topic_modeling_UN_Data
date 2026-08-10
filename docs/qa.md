# Quality assurance and reproducibility audit

This document records the final QA pass for the combined UN General Debate project. The audit used the **submitted AI-course PDF**, the **final AI notebook**, the **submitted Social Media & Web Analytics (SMWA) paper**, the final topic-modeling and network notebooks, the raw 7,507-speech UNGD CSV, and the saved processed-data snapshots.

## What was checked

- repository source modules and notebook JSON structure;
- country-to-continent mapping against the original AI notebook;
- sample counts and analysis windows;
- TF-IDF/cosine-similarity implementation;
- joint LDA settings and source-reported topic words;
- K-means settings, cluster assignments and top terms;
- LSTM architecture, training history, confusion matrix and classification metrics;
- sentiment-analysis unit of analysis;
- LDA/NMF/BERTopic coherence comparability;
- country-mention network construction;
- visual clarity and figure provenance;
- dependency structure and automated tests.

## Reproduced from saved coursework data

The saved AI processed-data snapshot contains **3,826 Africa/Europe speeches**: 2,159 Africa and 1,667 Europe.

### TF-IDF similarity

The original notebook creates a full Europe-by-Africa cosine-similarity matrix and prints `cosine_sim[0][0]`. The reported **0.2640** is therefore one speech-pair similarity, not a corpus-level regional similarity. On the saved processed snapshot:

- original first-pair cosine: approximately **0.2640**;
- deterministic 300x300 sampled cross-region pairwise mean: approximately **0.188**;
- cosine between regional mean TF-IDF vectors: approximately **0.906**.

These numbers answer different questions and are now labeled separately throughout the repository.

### K-means

The saved AI processed snapshot contains the following three-cluster assignments:

| Continent | Cluster 0 | Cluster 1 | Cluster 2 |
|---|---:|---:|---:|
| Africa | 1,194 | 51 | 914 |
| Europe | 8 | 1,140 | 519 |

The submitted narrative PDF gives slightly different counts from another run. The repository preserves the saved-data counts and documents the discrepancy rather than silently rewriting history.

### LSTM

The submitted AI notebook reports held-out accuracy of **85.1%**. The source confusion matrix is:

| | Predicted Europe | Predicted Africa |
|---|---:|---:|
| Actual Europe | 406 | 46 |
| Actual Africa | 68 | 246 |

Training accuracy rises to roughly 99-100% while validation accuracy remains around 84-87%, which is consistent with substantial **overfitting**. The portfolio now states this explicitly.

## Methodological fixes

### 1. Similarity estimand clarified

`0.2640` is retained as a coursework output but no longer described as a corpus-level similarity. `src/comparative_analysis.py` now provides explicit first-pair, sampled pairwise and centroid estimands.

### 2. AI LDA section made executable

The previous professional notebook described the LDA step but did not execute it. `notebooks/02_africa_europe_ml.ipynb` now fits the joint 10-topic model and computes topic prevalence by continent.

### 3. LSTM workflow completed

The previous notebook only instantiated the neural-network architecture. It now includes optional end-to-end tokenization, splitting, training and evaluation. The professional helper also avoids using the held-out test set as validation data during fitting.

### 4. Sentiment unit corrected

The coursework contains a sentiment path that tokenized speech text before sentence-level VADER scoring. The professional pipeline instead scores sentence-like units from the original speech and aggregates to the speech level. Coursework sentiment plots and interpretations are preserved as source-reported results, not silently relabeled as corrected estimates.

### 5. Topic-model coherence caveat made explicit

The submitted SMWA paper reports LDA = 0.3663, NMF = 0.5464 and BERTopic = 0.7768. The original model sections do not build their coherence inputs identically, so those values are preserved as coursework diagnostics rather than treated as a strict model-selection benchmark. The professional functions can evaluate topic-word lists against a common reference corpus.

### 6. Network measurement rebuilt

The submitted network code searched speech text for ISO3 country codes. The professional reconstruction matches country names and historical/orthographic aliases instead. This changes the measurement rule and therefore the centrality ranking. Source-reported claims about Madagascar, Namibia, Comoros, Somalia and South Sudan remain documented as coursework findings; the professional reconstruction is displayed separately.

## Automated checks

The repository now includes:

- `tests/test_core.py` for continent mapping, similarity, K-means and network construction;
- `.github/workflows/ci.yml` to install dependencies, bootstrap NLTK, compile source modules and run pytest;
- split optional dependency files for BERTopic and TensorFlow so the core project remains lightweight.

The core test suite passed locally during this QA pass: **5 tests passed**.

## What is intentionally optional

BERTopic and TensorFlow/LSTM are computationally heavy. Their code paths are complete but disabled by default in the notebooks. Users who want them can install:

- `requirements-bertopic.txt` for BERTopic;
- `requirements-ai.txt` for TensorFlow/LSTM.

This keeps the default workflow reproducible without forcing large model downloads.

## Visual QA

The repository retains the original coursework figure archives for provenance, but the main README now uses sharp SVG figures for the key analytical results. This avoids blurry multi-panel screenshots and makes the portfolio readable at normal GitHub zoom levels.
