# UN General Debate NLP & Machine Learning

**Africa–Europe comparison with an Africa-focused topic-modeling and network-analysis extension**

A reproducible NLP and machine-learning portfolio project built from two master's coursework submissions using the **United Nations General Debate Corpus (UNGDC)**. The repository presents the work as one analytical progression:

1. **AI course foundation — Africa vs Europe:** EDA, TF-IDF similarity, LDA, K-means, LSTM classification, VADER sentiment and word clouds.
2. **Social Media & Web Analytics extension — Africa:** deeper EDA, sentiment over time, LDA/NMF/BERTopic, coherence diagnostics and a country-mention network.

> **Provenance rule:** values labeled *coursework-reported* reproduce the submitted analyses. Professional reconstructions and methodological fixes are labeled separately. See [`docs/qa.md`](docs/qa.md) for the final audit.

---

## Research questions

**Part I — Africa vs Europe**  
How similar are African and European UN General Debate statements, which themes distinguish them, and how much regional information can text models recover?

**Part II — Africa extension**  
What themes, sentiment patterns and country-to-country mention relationships characterize African participation in the UN General Debate?

---

## Data at a glance

<p align="center">
  <img src="figures/professional/sample_composition.svg" alt="UNGD sample composition" width="86%">
</p>

| Sample | Speeches |
|---|---:|
| Full computational UNGD corpus | **7,507** |
| Africa | **2,159** |
| Europe | **1,667** |
| Africa + Europe saved AI snapshot | **3,826** |
| Computational coverage | **1970–2015** |

The submitted AI PDF describes the source as extending to 2016, while the computational snapshot contains 1970–2015. The discrepancy is documented rather than silently changed.

---

# Part I — AI course foundation: Africa vs Europe

## 1. Exploratory text analysis and regional word clouds

The original workflow compares session participation, country coverage, statement length and high-frequency vocabulary by continent. Africa and Europe share a large diplomatic vocabulary while differing in the relative prominence of regional, historical and development-related terms.

**Original visual archive:** [`coursework/ai_course/figures.md`](coursework/ai_course/figures.md)

## 2. TF-IDF similarity — corrected interpretation

A key QA finding concerns the submitted **0.2640** cosine value. The original notebook computes a full Europe×Africa speech-pair matrix and then prints `cosine_sim[0][0]`. Therefore **0.2640 is one Europe–Africa speech-pair similarity, not a corpus-level similarity statistic**.

<p align="center">
  <img src="figures/professional/ai_similarity_diagnostics.svg" alt="TF-IDF similarity estimands" width="92%">
</p>

Using the saved AI processed-data snapshot:

| Similarity estimand | Value | Interpretation |
|---|---:|---|
| Coursework first speech pair | **0.264** | Reproduces the original `cosine_sim[0][0]` |
| Sampled cross-region pairwise mean | **~0.188** | Mean over a deterministic 300×300 speech-pair sample |
| Regional TF-IDF centroid cosine | **~0.906** | Similarity between mean regional TF-IDF vectors |

These are different estimands and are now reported separately. Exact definitions and values are in [`results/ai_similarity_audit.csv`](results/ai_similarity_audit.csv).

## 3. Joint LDA topic comparison

The submitted AI model estimates **10 topics** with `no_above=0.30`, `no_below=10`, **50 passes**, and `random_state=0`. Topic prevalence differs strongly across continents.

<p align="center">
  <img src="figures/professional/ai_lda_topic_prevalence.svg" alt="AI LDA topic prevalence by continent" width="94%">
</p>

Source topic-word patterns include:

- **Topic 1:** racism, colonialism, occupation, Zimbabwe, Pretoria — much more prevalent in African statements;
- **Topic 2:** Kosovo, terrorism prevention, Iraq, courts, globalization — much more prevalent in European statements;
- **Topic 3:** Somalia, Liberia, Sierra Leone, Congo, Uganda, Sudan, governance — Africa-heavy;
- **Topic 6:** Soviet/détente/socialist/Germany/armament language — Europe-heavy;
- **Topic 7:** Bosnia, Herzegovina, Yugoslavia, Cyprus, Croatia, Greece, Ukraine — Europe-heavy;
- **Topic 8:** food, health, education, water and MDGs — Africa-heavy.

The exact ten-topic word lists and continent-level prevalence values are stored in [`results/ai_lda_topics_and_prevalence.csv`](results/ai_lda_topics_and_prevalence.csv). The professional AI notebook now **actually estimates the joint LDA model and computes prevalence by continent**, rather than merely describing the step.

## 4. K-means clustering

The source workflow uses TF-IDF, an elbow diagnostic and selects **k = 3**. The saved processed-data snapshot gives:

<p align="center">
  <img src="figures/professional/ai_kmeans_by_continent.svg" alt="K-means clusters by continent" width="86%">
</p>

| Continent | Cluster 0 | Cluster 1 | Cluster 2 |
|---|---:|---:|---:|
| Africa | **1,194** | 51 | **914** |
| Europe | 8 | **1,140** | **519** |

Source top terms suggest broad clusters around:

- **Cluster 0:** development, peace, security, Africa;
- **Cluster 1:** international governance, security, human/right language;
- **Cluster 2:** economic and international-relations vocabulary.

The submitted PDF contains slightly different cluster counts from another run. Both artifacts are preserved; the saved processed-data counts above are used for the audited chart. See [`results/ai_kmeans_cluster_counts.csv`](results/ai_kmeans_cluster_counts.csv) and [`results/ai_kmeans_top_terms.csv`](results/ai_kmeans_top_terms.csv).

## 5. LSTM continent classification

The submitted LSTM uses an 80/20 split, 10,000-word vocabulary, sequence length 100, 100-dimensional embeddings, LSTM(128), Adam learning rate 0.001, batch size 20 and 10 epochs.

**Coursework-reported held-out accuracy: 85.1%.**

<p align="center">
  <img src="figures/professional/ai_lstm_confusion_matrix.svg" alt="LSTM confusion matrix" width="66%">
</p>

| Class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Europe | 0.86 | 0.90 | 0.88 | 452 |
| Africa | 0.84 | 0.78 | 0.81 | 314 |

The training history also reveals a limitation:

<p align="center">
  <img src="figures/professional/ai_lstm_training_history.svg" alt="LSTM training history" width="84%">
</p>

Training accuracy approaches 100%, while validation accuracy remains around the mid-80s, which is consistent with **overfitting**. The original notebook also used the held-out test set as validation data during training. The professional helper now takes validation from the training sample and evaluates the test set only after fitting. Exact source training history and confusion-matrix data are under [`results/`](results/).

## 6. Africa–Europe sentiment

The AI submission compares VADER sentiment distributions/trends and generates positive/negative word clouds for both continents. The submitted narrative describes especially negative African sentiment in parts of the 1970s through the mid-1980s and shared negative vocabulary around **terrorism, war, violence and conflict**.

The coursework contains more than one sentiment implementation, including a path with an inconsistent token/sentence unit. For future reproduction, [`src/sentiment.py`](src/sentiment.py) scores sentence-like units from the **original speech text** and aggregates to the speech level. Original sentiment plots remain in the coursework archive as source provenance rather than being relabeled as corrected estimates.

---

# Part II — Social Media & Web Analytics extension: Africa

## 7. Africa corpus diagnostics

The submitted SMWA paper reports:

- a right-skewed statement-length distribution, with many statements around 5,000–20,000 characters and a peak near 10,000;
- relatively consistent engagement across sessions;
- frequent terms including **United Nations**, **international community**, **developing country**, and **Security Council**.

**Original visual archive:** [`coursework/social_media_web_analytics/figures.md`](coursework/social_media_web_analytics/figures.md)

## 8. Africa sentiment over time

The submitted paper reports year-to-year fluctuations together with a **gradual upward trend in positivity** from 1970–2015.

Source interpretations of sentiment word clouds:

- **positive:** United Nations, peace, justice, people, hope, cooperation/stability;
- **negative:** war, conflict, terrorism, poverty, violence, hardship/insecurity.

These remain coursework-reported findings. The professional sentiment code uses the corrected sentence-level definition described above.

## 9. LDA, NMF and BERTopic

The SMWA extension compares three unsupervised topic-modeling approaches.

<p align="center">
  <img src="figures/professional/smwa_topic_coherence.svg" alt="SMWA coursework coherence scores" width="76%">
</p>

| Model | Coursework-reported `c_v` |
|---|---:|
| LDA | **0.3663** |
| NMF | **0.5464** |
| BERTopic | **0.7768** |

The submitted paper interprets:

- **LDA:** regional conflicts, health and colonial history;
- **NMF:** apartheid, sustainable development and human rights;
- **BERTopic:** broader contextual themes around nations, international affairs and development.

The paper ranks BERTopic highest. The QA audit adds an important qualification: the original model sections do **not** construct the coherence reference corpus identically. These values are preserved as coursework diagnostics, while the professional functions support evaluation against a common reference corpus.

## 10. Country-mention network

The submitted paper describes Madagascar, Namibia, Comoros and Somalia as prominent, South Sudan as relatively isolated, and regional groupings in East and West Africa.

However, the original source code searches speech text for **ISO3 country codes**. The professional reconstruction instead matches country names plus historical/orthographic aliases and counts a target at most once per speech. Because this is a different measurement rule, the two networks should not have identical rankings.

<p align="center">
  <img src="figures/professional/smwa_network_top_mentions.svg" alt="Professional network top mentions" width="90%">
</p>

Under the professional name/alias rule, the most-mentioned countries differ from the submitted network—exactly why source-reported and reconstructed results are kept separate. The full reconstructed centrality table is in [`results/professional_network_top_mentions.csv`](results/professional_network_top_mentions.csv), while [`notebooks/03_africa_network_extension.ipynb`](notebooks/03_africa_network_extension.ipynb) visualizes the strongest directed mention ties.

---

## Reproducible notebooks

| Notebook | Scope |
|---|---|
| [`01_africa_ungd_nlp.ipynb`](notebooks/01_africa_ungd_nlp.ipynb) | Africa EDA, word cloud, corrected sentiment, LDA, NMF, optional BERTopic |
| [`02_africa_europe_ml.ipynb`](notebooks/02_africa_europe_ml.ipynb) | Africa/Europe EDA, similarity audit, executable LDA, K-means, optional full LSTM, corrected sentiment |
| [`03_africa_network_extension.ipynb`](notebooks/03_africa_network_extension.ipynb) | Original-network audit, professional country-name/alias network, centrality and strongest ties |

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

Optional components:

```bash
pip install -r requirements-bertopic.txt   # BERTopic
pip install -r requirements-ai.txt         # TensorFlow / LSTM
```

The heavy optional libraries are no longer forced into the core environment.

---

## Automated QA

The final rebuild includes:

- core unit tests for continent mapping, TF-IDF similarity, K-means and network construction;
- a GitHub Actions workflow that installs dependencies, downloads NLTK data, compiles `src/`, and runs pytest;
- explicit input validation and clearer dependency errors;
- JSON-valid professional notebooks;
- sharp SVG result figures for the main portfolio page.

**Local QA during the final rebuild: 5 core tests passed.**

BERTopic and TensorFlow/LSTM are computationally heavy optional paths. Their code paths are complete, but they were **not independently re-trained during this local QA pass**; the submitted model outputs are retained as coursework-reported results.

See [`docs/qa.md`](docs/qa.md) for the full audit, [`docs/methodology.md`](docs/methodology.md) for methodological provenance, [`docs/findings.md`](docs/findings.md) for consolidated findings, and [`figures/professional/README.md`](figures/professional/README.md) for figure provenance.

---

## Coursework archive and data policy

Original course-specific visuals remain under `coursework/` and are clearly separated from the professional result figures. The authoritative submitted papers and final source notebooks remain preserved in the coursework Google Drive archive and were read directly during the audit.

Large raw and processed datasets are intentionally excluded from Git history. The public UNGD CSV should be downloaded locally and derived data regenerated from code. See [`data/README.md`](data/README.md).

---

## Interpretation boundary

This is a **descriptive NLP and machine-learning project**. Cosine similarity, topic prevalence, cluster membership, classifier accuracy, sentiment and network centrality are measurements derived from text. They do not identify causal effects and should not be interpreted as evidence of homogeneous political preferences within Africa or Europe.

## Author

**Maha Gasim**  
MSc Data Analytics for Business and Society, Ca' Foscari University of Venice
