# UN General Debate NLP & Machine Learning

**Africa-Europe comparison with an Africa-focused topic-modeling and network-analysis extension**

A research-oriented NLP portfolio project built from two master's coursework submissions using the **United Nations General Debate Corpus (UNGDC)**.

The work developed in two connected stages:

1. **AI course foundation - Africa vs Europe:** text similarity, regional word clouds, LDA, K-means, LSTM classification and VADER sentiment.
2. **Social Media & Web Analytics extension - Africa deep dive:** richer EDA, sentiment over time, LDA/NMF/BERTopic and country-mention network analysis.

The two assignments use the same underlying corpus and overlapping preprocessing logic, so this repository presents them as **one evolving research project rather than two unrelated exercises**.

> **Reading note:** values labeled *coursework-reported* reproduce the original submissions. The professional rebuild documents implementation caveats and provides portable code rather than silently rewriting the original work.

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
| Word clouds | Africa + Europe | Africa + sentiment-specific |
| TF-IDF / cosine similarity | Yes | - |
| LDA | Joint 10-topic comparison | Yes |
| K-means | 3 clusters | - |
| LSTM classification | Yes | - |
| VADER sentiment | Africa vs Europe | Africa over time |
| NMF | - | Yes |
| BERTopic | - | Yes |
| Coherence comparison | - | LDA / NMF / BERTopic |
| Country-mention network | - | Yes |

### Key coursework-reported diagnostics

| Result | Value |
|---|---:|
| Africa-Europe TF-IDF cosine similarity | **0.2640** |
| LSTM held-out test accuracy | **85.1%** |
| LDA `c_v` coherence | **0.3663** |
| NMF `c_v` coherence | **0.5464** |
| BERTopic `c_v` coherence | **0.7768** |

The coherence values are preserved as coursework-reported diagnostics, not treated as a strict apples-to-apples benchmark because the original evaluation pipelines did not construct the reference corpus identically across all three models.

---

# Visual results

## AI course - Africa vs Europe

The original AI-course figures cover corpus diagnostics, Africa/Europe word clouds, LDA topic comparison, K-means diagnostics and clusters, LSTM classification, sentiment trends and positive/negative word clouds.

<p align="center">
  <img src="coursework/ai_course/figures/figure-sheet-01.jpg" alt="AI course figure preview" width="95%">
</p>

**[Browse all AI-course analytical figures ->](coursework/ai_course/figures.md)**

## Social Media & Web Analytics - Africa extension

The extension adds Africa-specific EDA, sentiment evolution, topic-model comparisons and a country-mention network.

<p align="center">
  <img src="coursework/social_media_web_analytics/figures/figure-sheet-01.jpg" alt="SMWA figure preview" width="95%">
</p>

**[Open the SMWA visual gallery ->](coursework/social_media_web_analytics/figures.md)**  
**[Download the complete seven-figure SMWA archive ->](coursework/social_media_web_analytics/SMWA_all_figures.pdf)**

A figure-by-figure provenance list is available in [`coursework/FIGURE_INDEX.md`](coursework/FIGURE_INDEX.md).

---

# Part I - AI course foundation: Africa vs Europe

## 1. Exploratory analysis and regional word clouds

The project compares speech-length distributions, session/country coverage and high-frequency vocabulary for African and European statements. The original word clouds show extensive shared diplomatic language while retaining differences in relative word prominence.

## 2. TF-IDF and cosine similarity

The two regional corpora are represented using TF-IDF and compared with cosine similarity.

**Coursework-reported cosine similarity: `0.2640`.**

The submitted interpretation is that the regions share some diplomatic vocabulary but retain substantial differences in thematic emphasis.

## 3. LDA topic comparison

A joint **10-topic Gensim LDA model** is estimated with vocabulary filtering, `passes=50` and `random_state=0`, then topic prevalence is compared by continent.

The submitted interpretations include themes around:

- post-colonialism, racism and African regional conflicts;
- Kosovo, terrorism and Cold War-era European politics;
- health, food, education and the MDGs;
- governance, security and peacekeeping;
- Bosnia/Yugoslavia, Cyprus and related geopolitical issues.

These are descriptive topic interpretations, not causal claims.

## 4. K-means clustering

K-means is applied to TF-IDF features. An elbow diagnostic motivates **three clusters**, followed by cluster-size, continent-by-cluster and cluster-word-cloud analysis.

The submitted interpretation emphasizes stronger African representation in security/development and economic-cooperation clusters, while European texts are more concentrated in the governance/human-rights cluster.

## 5. LSTM continent classification

The AI submission trains an LSTM to classify a statement as **Africa vs Europe**.

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

The result shows that regional information is recoverable from textual patterns with meaningful but imperfect separation; it does not imply homogeneous regional discourse.

## 6. Sentiment comparison

The AI submission uses VADER to compare sentiment distributions and trends for Africa and Europe and creates four sentiment-specific word clouds:

- positive - Africa;
- negative - Africa;
- positive - Europe;
- negative - Europe.

The submitted report describes noticeably more negative African sentiment in parts of the 1970s through the mid-1980s, followed by changing patterns over time.

---

# Part II - Social Media & Web Analytics extension: Africa deep dive

## 7. Africa corpus diagnostics and word cloud

The extension narrows the sample to African speeches, examines statement length and participation across UN sessions, and visualizes recurring vocabulary. The submitted Africa word cloud prominently includes **United Nations**, **international community**, **developing country** and **Security Council**.

## 8. Africa sentiment over time

The SMWA submission reports year-to-year fluctuations alongside a **gradual upward trend in sentiment** over 1970-2015.

Its sentiment word clouds emphasize:

- **positive:** peace, justice, people, hope and cooperation-related language;
- **negative:** war, conflict, terrorism, poverty and violence.

The professional code separately corrects the original sentiment unit-of-analysis issue by scoring sentence-like units from the original speech text; the submitted figures remain preserved as coursework provenance.

## 9. LDA, NMF and BERTopic

The Africa extension compares three unsupervised topic-modeling approaches:

- **LDA** - probabilistic bag-of-words topic model;
- **NMF** - non-negative factorization of a TF-IDF document-term matrix;
- **BERTopic** - embedding-based topic discovery.

The paper interprets the models as recovering themes around **regional conflict, health, colonial history, apartheid, sustainable development, human rights, international cooperation and development**.

### Coursework-reported coherence

| Model | `c_v` coherence |
|---|---:|
| LDA | 0.3663 |
| NMF | 0.5464 |
| BERTopic | 0.7768 |

The professional audit retains the original ranking as part of the coursework record while explicitly warning that the evaluation setups were not fully harmonized.

## 10. Country-mention network analysis

The extension also constructs a directed weighted network in which African countries are nodes and references to other African countries generate edges.

Source-reported findings include:

- **Madagascar** as a particularly central node;
- important positions for **Namibia** and **Comoros**;
- **Somalia** as notable in the network;
- **South Sudan** appearing comparatively isolated;
- regional structure around East and West African groups.

These are descriptive network patterns rather than causal measures of diplomatic influence. The professional reconstruction in [`src/network_analysis.py`](src/network_analysis.py) makes the text-matching rule explicit and uses country names/common historical aliases rather than silently relying on ISO-code strings inside speeches.

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

Part II is therefore best read as an **extension and specialization of Part I**.

---

## Reproducible notebooks

```text
notebooks/
├── 01_africa_ungd_nlp.ipynb
├── 02_africa_europe_ml.ipynb
└── 03_africa_network_extension.ipynb
```

- [`01_africa_ungd_nlp.ipynb`](notebooks/01_africa_ungd_nlp.ipynb) - Africa EDA, sentiment, LDA, NMF and optional BERTopic.
- [`02_africa_europe_ml.ipynb`](notebooks/02_africa_europe_ml.ipynb) - Africa/Europe word clouds, TF-IDF similarity, LDA specification, K-means, LSTM architecture and comparative sentiment.
- [`03_africa_network_extension.ipynb`](notebooks/03_africa_network_extension.ipynb) - directed country-mention network and descriptive centrality.

Reusable modules:

```text
src/
├── preprocessing.py
├── comparative_analysis.py
├── sentiment.py
├── topic_models.py
├── network_analysis.py
└── visualization.py
```

Install the classical NLP stack with `requirements.txt`; install `requirements-ai.txt` for the TensorFlow/LSTM component.

---

## Coursework provenance

The original analytical contributions remain separated by course:

```text
coursework/
├── README.md
├── STRUCTURE.md
├── FIGURE_INDEX.md
├── ai_course/
│   ├── README.md
│   ├── figures.md
│   └── figures/
└── social_media_web_analytics/
    ├── README.md
    ├── figures.md
    ├── SMWA_all_figures.pdf
    └── figures/
```

The authoritative submitted papers and source notebooks remain preserved in the coursework Google Drive archive and were read directly during the rebuild. Their methods, findings and implementation differences are documented in [`docs/methodology.md`](docs/methodology.md) and [`docs/findings.md`](docs/findings.md).

---

## What the professional rebuild improves

- presents the two assignments as one coherent research progression;
- removes Colab-specific paths and installation cells;
- separates preprocessing, similarity/clustering, sentiment, topic models, network analysis and visualization into reusable functions;
- makes random states explicit where supported;
- corrects the sentiment unit of analysis for future reproduction;
- makes topic-coherence comparison more defensible;
- distinguishes submitted results from independently reproducible code;
- documents the original network measurement and supplies a clearer reconstruction;
- excludes very large raw/processed datasets from Git history;
- preserves course-specific visuals with explicit provenance rather than mixing outputs together.

For the full source audit, see [`docs/methodology.md`](docs/methodology.md). For the consolidated substantive findings, see [`docs/findings.md`](docs/findings.md).

---

## Data

The project uses the public **United Nations General Debate Corpus**. Raw and processed data are intentionally excluded because the raw corpus is large and processed copies are redundant. See [`data/README.md`](data/README.md).

The coursework artifacts do not describe the date coverage identically: the computational notebooks use **1970-2015**, while one submitted document describes the source through 2016. The discrepancy is documented rather than silently reconciled.

---

## Interpretation boundaries

This is primarily a **descriptive NLP and machine-learning project**. Topic prevalence, sentiment, cosine similarity, cluster membership, classification accuracy and network centrality are measurements derived from text; they do not identify causal effects. Topic labels and substantive interpretations require inspection of high-weight words and representative speeches.

---

## Author

**Maha Gasim**  
MSc Data Analytics for Business and Society, Ca' Foscari University of Venice
