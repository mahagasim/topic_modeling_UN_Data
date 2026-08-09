# Methodology and provenance

This note documents how the professional repository was reconciled with **two original coursework submissions built from the same United Nations General Debate corpus**.

The goal is not to rewrite the coursework after the fact. The repository preserves the submitted analyses and figures while making clear which results are source-reported, which implementation choices need caution, and which parts were reorganized for reproducibility.

## Source hierarchy

### Part I - AI course foundation

Authoritative source artifacts:

- submitted PDF: **`AI Project_ Africa - Europe Project`**;
- final notebook: **`AI project_Africa - Europe.ipynb`**, last modified May 2024;
- original graph archive associated with the final notebook.

This submission is the foundation of the combined project and contains the Africa-Europe comparison: TF-IDF/cosine similarity, LDA, K-means, LSTM classification, VADER sentiment, and regional/sentiment word clouds.

### Part II - Social Media & Web Analytics extension

Authoritative source artifacts:

- submitted paper: **`898396.pdf`**;
- final notebook: **`Topic Modeling`**, last modified June 2024;
- paper figures and model outputs.

This submission is treated as an **Africa-focused extension** of the AI work. It adds a deeper Africa-only sentiment analysis, LDA/NMF/BERTopic comparison, coherence diagnostics, and country-mention network analysis.

## Shared data and overlapping snapshots

Both projects use the public UN General Debate Corpus with the core variables `country`, `session`, `year`, and `text`.

The original coursework artifacts are not perfectly synchronized:

- the computational notebooks use a 1970-2015 analysis window;
- one submitted AI document describes the source as extending through 2016;
- intermediate processed files differ in size and construction.

The rebuild therefore does **not** infer that every historical file is the same snapshot. It documents the discrepancy and uses code to reconstruct samples from a single local raw corpus whenever possible.

## AI-course specifications retained from the source

### TF-IDF cosine similarity

The submitted Africa-Europe comparison reports a cosine similarity of **0.2640** after TF-IDF vectorization. This is retained as a coursework result.

### LDA

The final AI notebook estimates a joint 10-topic Gensim LDA model with vocabulary filtering, `passes=50`, and `random_state=0`, then compares topic prevalence by continent.

### K-means

The AI notebook applies K-means to TF-IDF features, uses an elbow diagnostic, and proceeds with **three clusters**. The original cluster-distribution, continent-by-cluster heatmap, and cluster word clouds are preserved in the coursework archive.

### LSTM

The submitted classifier uses an 80/20 train-test split (`random_state=42`), a 10,000-word tokenizer vocabulary, sequence length 100, 100-dimensional embeddings, an LSTM layer with 128 units, Adam with learning rate 0.001, batch size 20, and 10 epochs.

The submission reports **85.1% test accuracy** on 766 test observations. This is retained as a source-reported result; the professional rebuild does not claim that the result has been independently re-estimated under a fully seeded TensorFlow environment unless a new run is explicitly recorded.

## Sentiment-analysis caveat

The coursework contains more than one sentiment implementation.

In the final AI notebook, one comparison routine operates on a preprocessed-text field, while a later routine returns to original speech text to identify strongest positive and negative sentences for the sentiment-specific word clouds.

In the SMWA notebook, the original workflow tokenizes speech text and subsequently applies sentence tokenization in a way that can effectively change the intended unit of analysis. For that reason, the professional implementation in [`src/sentiment.py`](../src/sentiment.py) computes VADER scores from sentence-like units of the **original speech text** and aggregates them to the speech level.

The original sentiment figures remain in the coursework archive because they are part of the submitted work, but they are labeled as **coursework outputs**, not silently presented as newly validated estimates.

## Topic-model coherence caveat

The SMWA submission reports:

| Model | Coursework-reported `c_v` coherence |
|---|---:|
| LDA | 0.3663 |
| NMF | 0.5464 |
| BERTopic | 0.7768 |

The submitted paper interprets BERTopic as the best-performing model on this comparison.

However, the original LDA, NMF, and BERTopic sections do not construct the coherence reference texts/dictionaries in exactly the same way. The professional rebuild therefore preserves these numbers as **submitted diagnostics** while providing utilities to evaluate extracted topic words against a common reference corpus. This distinction prevents an inconsistent evaluation setup from being presented as a definitive model benchmark.

## Topic interpretation

Topic labels in both submissions are substantive interpretations of high-weight terms. The professional repository preserves those interpretations but does not treat them as ground truth. Robust topic interpretation should inspect:

1. high-weight terms;
2. representative speeches/documents;
3. topic prevalence by group/time;
4. stability across preprocessing/model specifications.

## Network-analysis interpretation

The SMWA submission builds a directed weighted country-mention network. Source-reported centrality and clustering patterns are descriptive properties of the constructed mention network. They should not be interpreted as causal diplomatic influence or formal alliance structure.

## Changes made in the professional rebuild

### Portable project structure

The original notebooks rely on Colab installation cells and absolute Google Drive paths. Reusable code is moved into `src/` and local paths are documented under `data/`.

### Safe sample construction

Filtered samples are created explicitly with copies rather than relying on chained assignment.

### Reusable model functions

Preprocessing, sentiment measurement and topic-model estimation are separated into functions so assumptions are visible and easier to change.

### Large data excluded

Raw and processed datasets are intentionally not committed to Git. The public UNGD corpus should be downloaded locally; derived data should be regenerated from code.

### Coursework preserved separately

Original submissions, source notebooks and submitted figures are stored under `coursework/`, clearly separated by course. This preserves provenance while allowing the repository root to present one coherent research project.

## Interpretation boundary

This is a descriptive NLP and machine-learning project. Cosine similarity, clusters, topic prevalence, sentiment, classification performance and network centrality do not identify causal effects. Changes over time can also reflect UN membership, corpus availability and composition, not only changes in diplomatic rhetoric.
