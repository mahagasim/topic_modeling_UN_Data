# UN General Debate NLP & Topic Modeling

A reproducible natural-language-processing project using the **United Nations General Debate Corpus (UNGDC)** to study how themes in diplomatic speeches can be recovered with classical and embedding-based topic models.

> **Status:** professional rebuild of an original master's coursework project. The repository remains private while the analysis is being cleaned and validated.

## Project objective

The original coursework explored the UN General Debate corpus with exploratory text analysis, sentiment analysis, and three topic-modeling approaches:

- Latent Dirichlet Allocation (LDA)
- Non-negative Matrix Factorization (NMF)
- BERTopic

The clean rebuild focuses on making that workflow reproducible and portfolio-ready. The primary implemented analysis in the original notebook focuses on **African UN member-state speeches**, while the exploratory workflow also mapped speeches to continents and produced continent-level descriptive outputs.

## Data

The source corpus contains country-level General Debate statements with fields for country, session, year, and speech text. The original coursework used speeches spanning **1970-2015**.

The raw corpus is not committed to this repository because it is large. See [`data/README.md`](data/README.md) for instructions and provenance.

## Research workflow

1. Load and validate the UNGD corpus.
2. Map country codes to continents.
3. Clean and normalize speech text.
4. Explore speech counts and text-length distributions.
5. Estimate sentiment as a descriptive NLP feature.
6. Estimate topic models with LDA, NMF, and BERTopic.
7. Compare topic interpretability and coherence.
8. Export reproducible figures and model summaries.

## Methods

### LDA

The original implementation used Gensim LDA with 10 topics, filtered vocabulary, 50 passes, and a fixed random seed. Its recorded c_v coherence score was **0.3663** for the Africa-focused analysis.

### NMF

NMF was estimated from a TF-IDF document-term matrix with 10 components. The rebuilt code separates vectorization, model fitting, and topic extraction so the model can be evaluated consistently with LDA and BERTopic.

### BERTopic

The original workflow used BERTopic with sentence-transformer embeddings and n-grams. The rebuild preserves the method but removes Colab-specific setup and separates preprocessing from model estimation.

## Repository structure

```text
.
├── data/
│   └── README.md
├── src/
│   ├── preprocessing.py
│   └── topic_models.py
├── .gitignore
├── requirements.txt
└── README.md
```

A cleaned notebook will be added after the core functions are validated against the original coursework outputs.

## Reproducibility principles

- Raw and processed datasets are excluded from Git history.
- File paths are relative rather than hard-coded to Google Drive.
- Random states are set where supported.
- Preprocessing and model estimation are implemented as reusable functions.
- Network analysis is intentionally excluded from this repository and treated as a separate project.

## Original coursework vs. rebuild

The original notebooks were exploratory and contained repeated imports, notebook-specific installation commands, absolute Google Drive paths, intermediate output, and multiple NLP tasks in one file. This rebuild keeps the analytical substance while reorganizing the project into a clearer research pipeline suitable for review by researchers or technical hiring committees.

## Data source

The coursework used the public **UN General Debate Corpus** distributed through Kaggle / the UN General Debate dataset. Dataset files should be downloaded locally rather than committed to Git.

## Author

**Maha Gasim**  
MSc Data Analytics for Business and Society, Ca' Foscari University of Venice
