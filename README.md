# UN General Debate NLP & Machine Learning

**Africa–Europe comparison with an Africa-focused topic-modeling and network-analysis extension**

This repository consolidates two master's coursework submissions built from the **United Nations General Debate Corpus (UNGDC)** into one research-oriented NLP portfolio project.

The work developed in two stages:

1. **Foundation — AI course:** compare African and European UN General Debate speeches using text similarity, topic modeling, clustering, supervised deep learning, sentiment analysis, and word clouds.
2. **Extension — Social Media & Web Analytics:** narrow the focus to African speeches and deepen the analysis with LDA, NMF, BERTopic, sentiment evolution, sentiment-specific word clouds, and a country-mention network.

The two submissions use the same underlying UNGD data and overlapping preprocessing ideas, so they are presented here as **one evolving project rather than two unrelated projects**.

> **Reading note:** values described as *coursework-reported* reproduce the submitted analyses. The professional rebuild also documents implementation caveats and improves reproducibility instead of silently rewriting the original work.

---

## Research questions

### Part I — Africa vs Europe

> **How similar are African and European UN General Debate speeches, which themes distinguish them, and how accurately can text alone classify a statement as African or European?**

### Part II — Africa extension

> **What themes, sentiment patterns, and country-to-country relationships characterize African participation in the UN General Debate?**

---

## Project at a glance

| Component | AI course foundation | SMWA extension |
|---|---|---|
| Geographic focus | Africa vs Europe | Africa |
| Exploratory NLP | ✓ | ✓ |
| Regional word clouds | Africa + Europe | Africa |
| TF-IDF / cosine similarity | ✓ | — |
| LDA | Joint 10-topic model | ✓ |
| K-means | 3 clusters | — |
| LSTM classification | ✓ | — |
| VADER sentiment | Africa vs Europe | Africa over time |
| Positive/negative word clouds | Both continents | Africa |
| NMF | — | ✓ |
| BERTopic | — | ✓ |
| Coherence comparison | — | LDA / NMF / BERTopic |
| Country-mention network | — | ✓ |

---

# Part I — AI course foundation: Africa vs Europe

The AI-course submission compares African and European statements after mapping UN country codes to continents and cleaning/tokenizing the speech text.

## 1. Exploratory text analysis & regional word clouds

The analysis compares speech-length distributions and visualizes high-frequency vocabulary separately for Africa and Europe. The submitted word clouds show extensive shared diplomatic vocabulary while preserving differences in relative word prominence.

A course-specific figure inventory is available in [`coursework/FIGURE_INDEX.md`](coursework/FIGURE_INDEX.md), and the first archival figure sheet is stored under [`coursework/ai_course/figures/`](coursework/ai_course/figures/).

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

The AI project applies **K-means to TF-IDF features**. An elbow diagnostic is used to motivate **three clusters**, followed by cluster-size, continent-by-cluster, and cluster-word-cloud diagnostics.

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

The result shows that region is recoverable from textual patterns with meaningful but imperfect separation. It should not be read as evidence that either region has a single homogeneous discourse.

## 6. Sentiment comparison & sentiment word clouds

The AI submission compares VADER sentiment distributions and trends for Africa and Europe and builds four sentiment-specific word clouds:

- positive — Africa;
- negative — Africa;
- positive — Europe;
- negative — Europe.

The submitted paper describes noticeably more negative African sentiment in parts of the 1970s to mid-1980s and changing patterns thereafter. Because the coursework contains more than one sentiment implementation, the professional code preserves the submitted outputs as provenance while using a corrected sentence-level implementation in [`src/sentiment.py`](src/sentiment.py).

---

# Part II — Social Media & Web Analytics extension: Africa deep dive

The second submission uses the same UNGD corpus but turns the Africa component into a deeper standalone analysis. It is therefore treated as an **extension and specialization of Part I**.

## 7. Africa corpus diagnostics & word cloud

The submitted paper reports a right-skewed speech-length distribution and relatively consistent participation across UN sessions. Its Africa word cloud prominently features terms such as **United Nations**, **international community**, **developing country**, and **Security Council**.

## 8. Africa sentiment over time

The SMWA paper uses VADER sentiment and reports year-to-year fluctuations alongside a **gradual upward trend in sentiment** over 1970–2015.

Its sentiment word clouds emphasize:

- **positive:** peace, justice, people, hope and cooperation-related language;
- **negative:** war, conflict, terrorism, poverty and violence.

The professional sentiment implementation explicitly scores sentence-like units from original speech text; the submitted figures remain documented as coursework outputs.

## 9. LDA, NMF & BERTopic

The Africa extension compares three unsupervised topic-modeling approaches:

- **LDA** — probabilistic bag-of-words topic model;
- **NMF** — non-negative factorization of a TF-IDF document-term representation;
- **BERTopic** — embedding-based topic discovery.

The paper interprets the models as recovering themes around **regional conflict, health, colonial history, apartheid, sustainable development, human rights, international cooperation and development**.

### Coursework-reported coherence scores

| Model | `c_v` coherence reported in submission |
|---|---:|
| LDA | 0.3663 |
| NMF | 0.5464 |
| BERTopic | 0.7768 |

The submitted paper ranks BERTopic highest on these values. The professional audit retains them as **coursework-reported diagnostics rather than an apples-to-apples benchmark**, because the original model sections did not construct their coherence reference corpora identically. See [`docs/methodology.md`](docs/methodology.md).

## 10. Country-mention network analysis

The SMWA extension builds a directed weighted network in which African countries are nodes and references to other African countries create edges.

Source-reported findings include:

- **Madagascar** as a particularly central node;
- important positions for **Namibia** and **Comoros**;
- **Somalia** as notable in the network;
- **South Sudan** appearing comparatively isolated;
- regional groupings discussed around East African and West African countries.

These are descriptive network patterns, not causal measures of diplomatic influence. The professional reconstruction in [`src/network_analysis.py`](src/network_analysis.py) makes the text-matching rule explicit and uses country names/common historical aliases rather than silently relying on ISO-code strings inside speech text.

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

Part II is therefore best read as an **extension of Part I**, not as a duplicate project.

---

## Reproducible notebooks

The professional rebuild now mirrors the analytical progression across both courses:

```text
notebooks/
├── 01_africa_ungd_nlp.ipynb
├── 02_africa_europe_ml.ipynb
└── 03_africa_network_extension.ipynb
```

- `01_africa_ungd_nlp.ipynb` — Africa EDA, sentiment, LDA, NMF and optional BERTopic.
- `02_africa_europe_ml.ipynb` — Africa/Europe word clouds, TF-IDF similarity, LDA specification, K-means, LSTM architecture and comparative sentiment.
- `03_africa_network_extension.ipynb` — directed country-mention network and descriptive centrality.

Reusable source modules:

```text
src/
├── preprocessing.py
├── comparative_analysis.py
├── sentiment.py
├── topic_models.py
├── network_analysis.py
└── visualization.py
```

Install the classical NLP stack with `requirements.txt`; install `requirements-ai.txt` when reproducing the TensorFlow/LSTM component.

---

# Coursework provenance

The two courses remain explicitly separated under [`coursework/`](coursework/) so a reviewer can distinguish the original analytical contributions from the later professional reorganization:

```text
coursework/
├── README.md
├── STRUCTURE.md
├── FIGURE_INDEX.md
├── ai_course/
│   ├── README.md
│   └── figures/
└── social_media_web_analytics/
    └── README.md
```

The original submission PDFs and notebooks remain preserved in the user's coursework archive in Google Drive. Their substantive methods, reported metrics, figure inventory, and findings are reconciled here in [`docs/methodology.md`](docs/methodology.md) and [`docs/findings.md`](docs/findings.md).

---

## What the professional rebuild improves

- presents the two assignments as one coherent research progression;
- removes Colab-specific paths and installation cells;
- separates preprocessing, similarity/clustering, sentiment, topic models, network analysis and visualization into reusable functions;
- makes random states explicit where supported;
- corrects the sentiment unit of analysis for future reproduction;
- makes topic-coherence comparison more defensible;
- distinguishes submitted results from independently reproducible code;
- documents the original network measurement and supplies a clearer name-based reconstruction;
- excludes very large raw/processed datasets from Git history;
- retains a complete course-specific figure inventory instead of mixing outputs without provenance.

For the full source audit, see [`docs/methodology.md`](docs/methodology.md). For the substantive findings, see [`docs/findings.md`](docs/findings.md).

---

## Data

The project uses the public **United Nations General Debate Corpus**. Raw and processed data are intentionally excluded because the raw corpus is large and processed copies are redundant. See [`data/README.md`](data/README.md).

The coursework artifacts do not describe the date coverage identically: the computational notebooks use **1970–2015**, while one submitted document describes the source through 2016. The discrepancy is documented rather than silently reconciled.

---

## Interpretation boundaries

This is primarily a **descriptive NLP and machine-learning project**. Topic prevalence, sentiment, cosine similarity, cluster membership, classification accuracy and network centrality are measurements derived from text; they do not identify causal effects. Topic labels and substantive interpretations require inspection of high-weight words and representative speeches.

---

## Author

**Maha Gasim**  
MSc Data Analytics for Business and Society, Ca' Foscari University of Venice
