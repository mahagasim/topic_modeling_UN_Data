# UN General Debate NLP & Machine Learning

**Africa–Europe comparison with an Africa-focused topic-modeling and network-analysis extension**

This repository combines two master's coursework projects that use the **United Nations General Debate Corpus (UNGDC)** as one research progression:

1. **AI course foundation — Africa vs Europe:** EDA, word clouds, TF-IDF/cosine similarity, LDA, K-means, LSTM classification and VADER sentiment.
2. **Social Media & Web Analytics extension — Africa:** deeper EDA, sentiment over time, LDA/NMF/BERTopic and country-mention network analysis.

> **Provenance:** original coursework outputs are kept separate from the professional reconstruction. Methodological corrections are documented rather than silently replacing submitted results.

For the full technical discussion, see **[Models, measurement and interpretation](docs/models_and_interpretation.md)** and **[QA audit](docs/qa.md)**.

---

## Visual results

The front page intentionally uses **ordinary JPEG/Markdown image embeds only**. This avoids the SVG/HTML rendering issue that affected the earlier version of the README.

### AI course — Africa vs Europe

#### 1. Corpus diagnostics and Africa/Europe word clouds

![AI course — EDA and Africa/Europe word clouds](figures/rendered/ai_regional_vocabulary_summary.png)

**Interpretation.** Both regions use a strong common UN diplomatic vocabulary. The Africa corpus gives relatively greater prominence to development, Africa/South Africa and regional language, while the Europe corpus contains relatively more human-rights, European and Cold-War/geopolitical vocabulary. Word clouds are exploratory frequency displays, not statistical tests.

#### 2. TF-IDF similarity and joint LDA topic comparison

![AI course — TF-IDF and LDA](figures/rendered/ai_lda_topic_prevalence.png)

The source notebook computes a Europe×Africa TF-IDF cosine-similarity matrix. The originally reported **0.2640** value is `cosine_sim[0][0]`: one Europe–Africa speech pair, not a regional average. The professional audit therefore distinguishes:

| Similarity estimand | Value | Meaning |
|---|---:|---|
| Coursework first speech pair | **0.264** | one Europe–Africa pair |
| Sampled cross-region pairwise mean | **~0.188** | mean over a deterministic 300×300 sample |
| Regional TF-IDF centroid cosine | **~0.906** | similarity between average regional TF-IDF vectors |

The joint **10-topic LDA** comparison shows strong regional differences. Colonial/apartheid and African conflict/development topics are Africa-heavy; Kosovo/Balkan, terrorism and Cold-War/European topics are Europe-heavy. Exact topic words and prevalence values are in [`results/ai_lda_topics_and_prevalence.csv`](results/ai_lda_topics_and_prevalence.csv).

#### 3. K-means clustering

![AI course — K-means diagnostics and cluster outputs](figures/rendered/ai_kmeans_by_continent.png)

The source workflow uses TF-IDF vectors and an elbow diagnostic, selecting **k = 3**. In the audited saved-data snapshot:

| Continent | Cluster 0 | Cluster 1 | Cluster 2 |
|---|---:|---:|---:|
| Africa | **1,194** | 51 | **914** |
| Europe | 8 | **1,140** | **519** |

The clusters broadly separate development/security-heavy African discourse, governance/rights-heavy European discourse, and a mixed economic/international-relations cluster. They should not be interpreted as ideological camps.

#### 4. LSTM classification and sentiment trends

![AI course — LSTM and sentiment analysis](figures/rendered/ai_lstm_confusion_matrix.png)

The submitted LSTM uses an 80/20 split, a 10,000-word tokenizer vocabulary, sequence length 100, 100-dimensional embeddings and an LSTM(128). **Coursework-reported held-out accuracy: 85.1%.** Europe has precision/recall/F1 of approximately **0.86/0.90/0.88**, while Africa has **0.84/0.78/0.81**. The training history also indicates overfitting because training accuracy approaches 100% while validation accuracy remains around the mid-80s.

The VADER sentiment plots show substantial year-to-year variation. The submitted interpretation emphasizes relatively negative African sentiment in parts of the 1970s through the mid-1980s, followed by improvement and continued fluctuation.

#### 5. Positive/negative sentiment word clouds

![AI course — sentiment-specific word clouds](figures/rendered/ai_sentiment_vocabulary_summary.png)

Across both regions, **positive** passages emphasize terms such as *peace, security, justice, freedom, cooperation, support* and *United Nations*. **Negative** passages emphasize *war, terrorism, violence, conflict, weapons, destruction, poverty* and *crisis*.

The professional sentiment implementation scores sentence-like units from the **original speech text** and aggregates to the speech level. This corrects a unit-of-analysis inconsistency found in one of the coursework sentiment paths.

**Full AI visual gallery:** [`coursework/ai_course/figures.md`](coursework/ai_course/figures.md)

---

### Social Media & Web Analytics — Africa extension

![SMWA — submitted analytical figures](figures/rendered/smwa_lda_topic_shares.png)

The SMWA extension narrows the sample to **2,159 African statements** and adds:

- Africa corpus diagnostics and an overall Africa word cloud;
- VADER sentiment distribution and sentiment over time;
- positive and negative sentiment word clouds;
- LDA, NMF and BERTopic;
- topic-coherence diagnostics;
- a directed country-mention network.

The final Drive `Graphs` folder contains **21 individual analytical PNGs**. These include `sentiment_distribution.png`, `LDA_topic_distribution.png`, `topic_distribution_heatmap.png`, **ten NMF topic word clouds (`topic_0.png`–`topic_9.png`)**, and `network_plot.png`. The submitted-paper sheet above preserves the figures embedded in the paper; the complete source inventory is documented in [`coursework/FIGURE_INDEX.md`](coursework/FIGURE_INDEX.md).

#### Topic-model results

| Model | Coursework-reported `c_v` coherence | Main source interpretation |
|---|---:|---|
| LDA | **0.3663** | regional conflict, colonial/apartheid history, development and health |
| NMF | **0.5464** | apartheid, sustainable development/MDGs, human rights and country-specific topics |
| BERTopic | **0.7768** | broader contextual and country-specific themes |

The executed notebook contains **10 LDA topics, 10 NMF topics and 53 BERTopic topics (0–52)**. They are preserved as machine-readable outputs:

- [`results/smwa_lda_topics.csv`](results/smwa_lda_topics.csv)
- [`results/smwa_nmf_topics.csv`](results/smwa_nmf_topics.csv)
- [`results/smwa_bertopic_topics.csv`](results/smwa_bertopic_topics.csv)

The original coherence numbers are retained as coursework diagnostics, but they are **not a perfectly harmonized apples-to-apples benchmark** because the reference-corpus construction differs across model sections.

#### Network analysis

The submitted paper describes Madagascar, Namibia, Comoros and Somalia as prominent and South Sudan as relatively isolated. The original source code searches speech text for ISO3 country codes. The professional reconstruction instead matches country names and historical/orthographic aliases, counting a target at most once per speech. Because the measurement rule changes, the two networks are intentionally not expected to produce identical rankings.

**Full SMWA visual gallery:** [`coursework/social_media_web_analytics/figures.md`](coursework/social_media_web_analytics/figures.md)

---

## Data at a glance

| Sample | Speeches |
|---|---:|
| Full computational UNGD corpus | **7,507** |
| Africa | **2,159** |
| Europe | **1,667** |
| Africa + Europe saved AI snapshot | **3,826** |
| Computational coverage | **1970–2015** |

One submitted AI document describes the source as extending through 2016, while the final computational snapshot contains 1970–2015. The discrepancy is documented rather than silently reconciled.

---

## Reproducible notebooks

| Notebook | Scope |
|---|---|
| [`01_africa_ungd_nlp.ipynb`](notebooks/01_africa_ungd_nlp.ipynb) | Africa EDA, word cloud, corrected sentiment, LDA, NMF and optional BERTopic |
| [`02_africa_europe_ml.ipynb`](notebooks/02_africa_europe_ml.ipynb) | Africa/Europe EDA, similarity audit, LDA, K-means, optional LSTM and corrected sentiment |
| [`03_africa_network_extension.ipynb`](notebooks/03_africa_network_extension.ipynb) | original-network audit, professional country-name/alias network, centrality and strongest ties |

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

---

## Reproduce the project

```bash
python -m venv .venv
# activate the environment
pip install -r requirements.txt
python scripts/bootstrap_nltk.py
```

Place the public UNGD CSV at:

```text
data/un-general-debates.csv
```

Then run the notebooks in numerical order.

Optional heavy components:

```bash
pip install -r requirements-bertopic.txt
pip install -r requirements-ai.txt
```

---

## QA and methodological boundary

The repository includes core unit tests and GitHub Actions CI. The final analytical rebuild passed the core test suite. BERTopic and TensorFlow/LSTM are heavy optional paths; their submitted numerical outputs are retained as **coursework-reported** unless independently rerun.

This is a **descriptive NLP and machine-learning project**. Cosine similarity, topic prevalence, clustering, classifier accuracy, sentiment and network centrality are text-derived measurements. They do not identify causal effects and should not be interpreted as evidence of homogeneous political preferences within Africa or Europe.

See:

- [`docs/models_and_interpretation.md`](docs/models_and_interpretation.md) — detailed model mechanics and interpretation;
- [`docs/methodology.md`](docs/methodology.md) — methodological provenance;
- [`docs/qa.md`](docs/qa.md) — audit and corrections;
- [`results/README.md`](results/README.md) — machine-readable result tables;
- [`coursework/FIGURE_INDEX.md`](coursework/FIGURE_INDEX.md) — complete source-figure inventory.

## Author

**Maha Gasim**  
MSc Data Analytics for Business and Society, Ca' Foscari University of Venice
