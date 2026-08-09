# UN General Debate NLP & Machine Learning

**Africa-Europe comparison with an Africa-focused topic-modeling and network-analysis extension**

This repository consolidates two master's coursework submissions built from the **United Nations General Debate Corpus (UNGDC)** into one research-oriented NLP portfolio project.

The work developed in two stages:

1. **Foundation - AI course:** compare African and European UN General Debate speeches using text similarity, topic modeling, clustering, supervised deep learning, sentiment analysis, and word clouds.
2. **Extension - Social Media & Web Analytics:** narrow the focus to African speeches and deepen the analysis with LDA, NMF, BERTopic, sentiment evolution, sentiment-specific word clouds, and a country-mention network.

The two submissions use the same underlying UNGD data and overlapping preprocessing ideas, so they are presented here as **one evolving project rather than two unrelated projects**.

> **Important:** numbers described as *coursework-reported* below reproduce the submitted analyses. The professional rebuild also documents implementation caveats and improves reproducibility rather than silently rewriting the original coursework.

---

## Research questions

### Part I - Africa vs Europe

> **How similar are African and European UN General Debate speeches, which themes distinguish them, and how accurately can text alone classify a statement as African or European?**

### Part II - Africa extension

> **What themes, sentiment patterns, and country-to-country relationships characterize African participation in the UN General Debate?**

---

## Project at a glance

| Component | AI course foundation | SMWA extension |
|---|---|---|
| Geographic focus | Africa vs Europe | Africa |
| Exploratory NLP | Yes | Yes |
| Regional word clouds | Africa + Europe | Africa |
| TF-IDF / cosine similarity | Yes | - |
| LDA | Yes, joint 10-topic model | Yes |
| K-means | Yes, 3 clusters | - |
| LSTM classification | Yes | - |
| VADER sentiment | Africa vs Europe | Africa over time |
| Positive/negative word clouds | Both continents | Africa |
| NMF | - | Yes |
| BERTopic | - | Yes |
| Coherence comparison | - | LDA / NMF / BERTopic |
| Country-mention network | - | Yes |

---

# Part I - AI course foundation: Africa vs Europe

The AI-course submission compares African and European statements after mapping UN country codes to continents and cleaning/tokenizing the speech text.

## 1. Exploratory text analysis

The analysis compares speech-length distributions and visualizes high-frequency vocabulary separately for Africa and Europe. The submitted word clouds show substantial shared diplomatic vocabulary while preserving region-specific differences.

The original figures are archived under [`coursework/ai_course/figures/`](coursework/ai_course/figures/).

## 2. TF-IDF and cosine similarity

The submission converts the two regional corpora to TF-IDF representations and computes their cosine similarity.

**Coursework-reported cosine similarity: `0.2640`.**

The submitted interpretation is that African and European speeches share some common diplomatic language but retain substantial differences in vocabulary and emphasis.

## 3. LDA topic comparison

A joint **10-topic Gensim LDA model** is estimated with vocabulary filtering, `passes=50`, and `random_state=0`, then topic prevalence is compared between African and European speeches.

The submitted interpretation highlights, among others:

- post-colonialism, racism and African regional conflicts;
- Kosovo, terrorism and Cold War-era European political themes;
- health, food, MDGs and development;
- governance, security and peacekeeping;
- historical and geopolitical issues around Bosnia/Yugoslavia, Cyprus and related regional politics.

These are source-derived interpretations of the original topic-word distributions; they are not causal claims.

## 4. K-means clustering

The AI project applies **K-means to TF-IDF features**. An elbow plot is used to motivate **three clusters**, followed by cluster-size, continent-by-cluster, and cluster-word-cloud diagnostics.

The clusters all retain core diplomatic language (`international`, `united`, `nations`, `development`, `peace`, `security`) but differ in the relative prominence of themes such as Africa, economic issues and human rights.

## 5. LSTM continent classification

The submission trains an LSTM to classify a speech as **Africa vs Europe** using tokenized/padded text sequences.

Coursework specification:

- 80/20 train-test split (`random_state=42`)
- vocabulary size: 10,000
- maximum sequence length: 100
- embedding dimension: 100
- LSTM units: 128
- Adam optimizer, learning rate 0.001
- batch size: 20
- 10 epochs

**Coursework-reported test accuracy: 85.1%** on 766 test speeches.

| Class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Europe | 0.86 | 0.90 | 0.88 | 452 |
| Africa | 0.84 | 0.78 | 0.81 | 314 |

The result shows that region is recoverable from textual patterns with meaningful but imperfect separation. It should be interpreted as a classification result, not as evidence that either region has a single homogeneous discourse.

## 6. Sentiment comparison and sentiment word clouds

The AI submission compares VADER sentiment distributions and trends for Africa and Europe and extracts the strongest positive and negative sentences to build four sentiment-specific word clouds:

- positive - Africa;
- negative - Africa;
- positive - Europe;
- negative - Europe.

The paper describes noticeably more negative African sentiment in parts of the 1970s to mid-1980s and changing patterns thereafter. Because the coursework contains more than one sentiment implementation, the professionalized code keeps the submitted output for provenance while using the corrected sentence-level implementation in [`src/sentiment.py`](src/sentiment.py).

---

# Part II - Social Media & Web Analytics extension: Africa deep dive

The second submission uses the same UNGD corpus but turns the Africa component into a deeper standalone analysis. This is treated as an **extension of Part I**.

## 7. Africa corpus diagnostics and word cloud

The submitted paper reports a right-skewed speech-length distribution and relatively consistent participation across UN sessions. Its Africa word cloud prominently features terms such as **United Nations**, **international community**, **developing country**, and **Security Council**.

## 8. Africa sentiment over time

The SMWA paper uses VADER sentiment and reports year-to-year fluctuations alongside a **gradual upward trend in sentiment** over 1970-2015.

Its sentiment word clouds emphasize:

- **positive:** peace, justice, people, hope and cooperation-related language;
- **negative:** war, conflict, terrorism, poverty and violence.

The submitted plots are preserved in the coursework archive. The professional code separately documents and corrects the original sentiment unit-of-analysis issue.

## 9. LDA, NMF and BERTopic

The Africa extension compares three unsupervised topic-modeling approaches:

- **LDA** - probabilistic bag-of-words topic model;
- **NMF** - non-negative factorization of a document-term representation;
- **BERTopic** - embedding-based topic discovery.

The paper interprets the models as recovering themes around **regional conflict, health, colonial history, apartheid, sustainable development, human rights, international cooperation and development**.

### Coursework-reported coherence scores

| Model | `c_v` coherence reported in submission |
|---|---:|
| LDA | 0.3663 |
| NMF | 0.5464 |
| BERTopic | 0.7768 |

The submitted paper ranks BERTopic highest on these reported values. In the professional methodological audit, however, these are retained as **coursework-reported diagnostics rather than an apples-to-apples benchmark**, because the original model sections did not construct the coherence reference corpus in exactly the same way. See [`docs/methodology.md`](docs/methodology.md).

## 10. Country-mention network analysis

The SMWA extension also builds a directed weighted network where African countries are nodes and mentions of one country in another country's speech generate edges.

Source-reported findings include:

- **Madagascar** as a particularly central node;
- important positions for **Namibia** and **Comoros**;
- **Somalia** as notable in the network, consistent with the prominence of conflict/humanitarian discourse;
- **South Sudan** appearing comparatively isolated;
- regional groupings discussed around East African and West African countries.

These are descriptive network patterns from the submitted analysis, not causal measures of diplomatic influence.

---

# How the two courses fit together

```text
UN General Debate Corpus
        |
        v
Shared cleaning + continent mapping
        |
        +------------------------------+
        |                              |
        v                              v
PART I: AI COURSE                 PART II: SMWA EXTENSION
Africa vs Europe                  Africa deep dive
        |                              |
TF-IDF similarity                 richer EDA
LDA comparison                    VADER sentiment
K-means                           LDA / NMF / BERTopic
LSTM classification               coherence diagnostics
sentiment comparison              country-mention network
regional/sentiment word clouds    Africa/sentiment word clouds
```

Part II is therefore best read as an **extension and specialization of Part I**, not as a duplicate project.

---

# Coursework archive

The original submissions are preserved separately so a reviewer can distinguish the work done for each course from the later professional rebuild:

```text
coursework/
├── ai_course/
│   ├── README.md
│   ├── AI_Project_Africa_Europe_submission.pdf
│   ├── AI_project_Africa_Europe_source.ipynb
│   └── figures/
└── social_media_web_analytics/
    ├── README.md
    ├── Social_Media_Web_Analytics_submission.pdf
    ├── Topic_Modeling_source.ipynb
    └── figures/
```

The original PDFs document the submitted narrative and outputs; the professional root-level code removes Colab-specific paths and makes the reusable parts of the workflow easier to reproduce.

---

# Professional rebuild

The repository root contains reusable code and a cleaned Africa-focused notebook:

```text
src/
├── preprocessing.py
├── sentiment.py
├── topic_models.py
└── visualization.py

notebooks/
└── 01_africa_ungd_nlp.ipynb
```

The professional rebuild improves:

- portable relative paths instead of Google Drive paths;
- reusable preprocessing/model functions;
- explicit random states where supported;
- sentence-level sentiment measurement from the original speech text;
- clearer separation between source-reported findings and revalidated results;
- more comparable topic-coherence evaluation;
- documentation of discrepancies across coursework snapshots;
- exclusion of the very large raw and processed datasets from Git history.

For the detailed audit, see [`docs/methodology.md`](docs/methodology.md). For a consolidated interpretation of the original results, see [`docs/findings.md`](docs/findings.md).

---

## Data

The project uses the public **United Nations General Debate Corpus**. Raw and processed data are intentionally excluded from the repository because the raw corpus is large and processed copies are redundant. See [`data/README.md`](data/README.md).

The coursework artifacts do not always describe the date coverage identically: the computational notebooks use **1970-2015**, while one submitted document describes the corpus through 2016. This discrepancy is documented rather than silently reconciled.

---

## Interpretation boundaries

This is primarily a **descriptive NLP and machine-learning project**. Topic prevalence, sentiment, cosine similarity, cluster membership, classification accuracy and network centrality are measurements derived from text; they do not identify causal effects. Topic labels and substantive interpretations require inspection of high-weight words and representative speeches.

---

## Author

**Maha Gasim**  
MSc Data Analytics for Business and Society, Ca' Foscari University of Venice
