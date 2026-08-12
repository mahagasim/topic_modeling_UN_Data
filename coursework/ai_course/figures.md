# AI course — Africa–Europe visual analysis

This gallery presents the **portfolio-facing, validated PNG figures** for the Africa–Europe AI-course analysis. The original coursework source inventory contains **22 analytical plot files**; their filenames and provenance are preserved in [`../FIGURE_INDEX.md`](../FIGURE_INDEX.md). The live figures below are generated from clean repository sources so they render reliably on GitHub.

For model mechanics, source results and methodological caveats, see [`../../docs/models_and_interpretation.md`](../../docs/models_and_interpretation.md) and [`../../docs/qa.md`](../../docs/qa.md).

---

## 1. Regional vocabulary

![Africa-Europe vocabulary](../../figures/rendered/ai_regional_vocabulary_summary.png)

Both corpora are dominated by the institutional language of UN diplomacy. The Africa analysis gives relatively greater prominence to **development, developing countries, Africa/South Africa, peace and security**, while the Europe analysis gives relatively greater prominence to **human rights, Europe, Security Council and Cold-War/geopolitical vocabulary**.

**Interpretation.** The overlap is substantial: the regions do not have wholly separate vocabularies. The useful signal is the difference in **relative emphasis**. Vocabulary clouds/summaries are exploratory frequency displays rather than formal tests of policy priorities.

---

## 2. TF-IDF cosine similarity

![TF-IDF similarity diagnostics](../../figures/rendered/ai_similarity_diagnostics.png)

The source notebook constructs TF-IDF vectors and a Europe×Africa cosine-similarity matrix. A QA audit found that the submitted **0.2640** statistic is `cosine_sim[0][0]`, i.e. one Europe–Africa speech pair rather than a regional mean.

| Estimand | Value | Interpretation |
|---|---:|---|
| First coursework pair | **0.264** | similarity for one Europe–Africa speech pair |
| Sampled cross-region pairwise mean | **~0.188** | average individual-speech similarity in a deterministic 300×300 sample |
| Regional centroid cosine | **~0.906** | similarity between average regional TF-IDF vectors |

The combination of a lower pairwise mean and high centroid similarity suggests substantial speech-level heterogeneity within a broadly shared diplomatic vocabulary.

---

## 3. Joint 10-topic LDA

![Africa-Europe LDA topic prevalence](../../figures/rendered/ai_lda_topic_prevalence.png)

The joint LDA model estimates ten latent topics over the combined Africa–Europe sample and compares their average prevalence between regions.

The clearest source contrasts include:

- **Africa-heavy:** colonialism/apartheid; African conflict clusters; development, health and MDG language.
- **Europe-heavy:** Kosovo/Balkan politics; terrorism; Soviet/détente language; Bosnia/Yugoslavia/Cyprus-related discourse.

This is a mixed-membership model: each speech can contain several topics. Regional prevalence therefore reflects average topic weight, not mutually exclusive speech categories.

Full source terms and prevalence: [`../../results/ai_lda_topics_and_prevalence.csv`](../../results/ai_lda_topics_and_prevalence.csv).

---

## 4. K-means clustering

![K-means cluster composition](../../figures/rendered/ai_kmeans_by_continent.png)

The source workflow applies K-means to TF-IDF vectors and selects **k = 3** after an elbow diagnostic.

| Continent | Cluster 0 | Cluster 1 | Cluster 2 |
|---|---:|---:|---:|
| Africa | **1,194** | 51 | **914** |
| Europe | 8 | **1,140** | **519** |

The source terms are consistent with a development/security-heavy grouping, a governance/rights-heavy grouping and a mixed economic/international-relations grouping. Generic UN vocabulary appears throughout, so the clusters should **not** be read as three political ideologies.

Cluster counts and top terms are available in [`../../results/ai_kmeans_cluster_counts.csv`](../../results/ai_kmeans_cluster_counts.csv) and [`../../results/ai_kmeans_top_terms.csv`](../../results/ai_kmeans_top_terms.csv).

---

## 5. LSTM continent classification

### Confusion matrix

![LSTM confusion matrix](../../figures/rendered/ai_lstm_confusion_matrix.png)

### Training history

![LSTM training history](../../figures/rendered/ai_lstm_training_history.png)

The submitted network uses an 80/20 train/test split, a 10,000-word tokenizer vocabulary, sequence length 100, 100-dimensional embeddings and an LSTM(128).

**Coursework-reported held-out accuracy: 85.1%.** Europe has precision/recall/F1 of approximately **0.86/0.90/0.88**; Africa approximately **0.84/0.78/0.81**.

The training curve is important for interpretation: training accuracy approaches 100% while validation accuracy remains around the mid-80s. This indicates **overfitting**. The model demonstrates that speech text contains substantial regional information, but the headline accuracy should not be treated as evidence of perfect or invariant regional linguistic separation.

Source evaluation tables: [`../../results/ai_lstm_confusion_matrix.csv`](../../results/ai_lstm_confusion_matrix.csv) and [`../../results/ai_lstm_training_history.csv`](../../results/ai_lstm_training_history.csv).

---

## 6. Sentiment vocabulary

![Africa-Europe sentiment vocabulary](../../figures/rendered/ai_sentiment_vocabulary_summary.png)

The original coursework contains VADER sentiment distributions, annual sentiment trends and four sentiment-specific word clouds.

| Region / polarity | Prominent source vocabulary | Interpretation |
|---|---|---|
| Africa — positive | peace, security, justice, freedom, hope, progress, support, United Nations | cooperation, institutional aspiration and peace/security |
| Africa — negative | war, conflict, terrorism, violence, poverty, destruction, crisis, weapon | conflict, insecurity and hardship |
| Europe — positive | peace, freedom, security, cooperation, justice, support, United Nations | institutional cooperation, rights and peace |
| Europe — negative | war, terrorism, violence, conflict, weapon, mass destruction, crisis | conflict and security threats |

The submitted temporal interpretation emphasizes relatively more negative African sentiment in parts of the **1970s through the mid-1980s**, followed by improvement and continued variation. VADER remains a lexicon-based measurement; it should not be read as a direct measure of government welfare, ideology or latent preferences.

The professional implementation additionally corrects a source unit-of-analysis issue by scoring sentence-like units from the original speech text before aggregating to speech level.

---

## Source-output accounting

The final AI-course `Graphs` folder contains **22 analytical source files**: 8 EDA/regional-vocabulary plots, 1 LDA comparison, 6 K-means diagnostics/cluster plots, 1 LSTM confusion matrix, 2 sentiment distribution/trend plots and 4 positive/negative sentiment word clouds.

Those historical outputs remain part of the coursework provenance, while this page uses validated PNG reconstructions for dependable GitHub display. Every original filename is listed in [`../FIGURE_INDEX.md`](../FIGURE_INDEX.md).

The reproducible professional pipeline is in [`../../notebooks/02_africa_europe_ml.ipynb`](../../notebooks/02_africa_europe_ml.ipynb), with reusable code in [`../../src/comparative_analysis.py`](../../src/comparative_analysis.py), [`../../src/sentiment.py`](../../src/sentiment.py) and [`../../src/visualization.py`](../../src/visualization.py).
