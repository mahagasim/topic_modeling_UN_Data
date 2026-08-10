# Complete coursework figure index

This index separates the analytical outputs from the two original submissions and, after a second Google Drive audit, also inventories the **individual source image files kept in the final project `Graphs` folders**. Decorative university/UN logos and stock photographs are excluded.

> **Important distinction:** the submitted papers contain a selected subset of figures. The source `Graphs` folders contain additional diagnostics and topic visualizations. The GitHub galleries now describe both rather than treating the PDF-embedded set as the whole analysis.

---

# Part I — AI course foundation: Africa vs Europe

The final Africa-Europe `Graphs` folder contains **22 analytical PNG files**.

| # | Source filename | Analysis |
|---:|---|---|
| 1 | `sessions_distribution_Africa.png` | UN session participation — Africa |
| 2 | `countries_distribution_Africa.png` | speech counts by African country |
| 3 | `text_lengths_distribution_Africa.png` | statement-length distribution — Africa |
| 4 | `wordcloud_Africa.png` | overall Africa word cloud |
| 5 | `sessions_distribution_Europe.png` | UN session participation — Europe |
| 6 | `countries_distribution_Europe.png` | speech counts by European country |
| 7 | `text_lengths_distribution_Europe.png` | statement-length distribution — Europe |
| 8 | `wordcloud_Europe.png` | overall Europe word cloud |
| 9 | `LDA_topic_distribution_comparison.png` | 10-topic LDA prevalence: Africa vs Europe |
| 10 | `elbow_method_plot.png` | K-means elbow diagnostic |
| 11 | `kmeans_clusters_heatmap.png` | continent-by-cluster heatmap |
| 12 | `kmeans_clusters_distribution.png` | overall K-means cluster distribution |
| 13 | `word_cloud_cluster_0.png` | Cluster 0 vocabulary |
| 14 | `word_cloud_cluster_1.png` | Cluster 1 vocabulary |
| 15 | `word_cloud_cluster_2.png` | Cluster 2 vocabulary |
| 16 | `confusion_matrix_lstm.png` | LSTM Africa-Europe classification confusion matrix |
| 17 | `sentiment_distribution_comparison.png` | Africa-Europe VADER sentiment distribution |
| 18 | `sentiment_trends_over_time.png` | Africa-Europe sentiment trend by year |
| 19 | `positive_africa.png` | strongly positive sentence vocabulary — Africa |
| 20 | `negative_africa.png` | strongly negative sentence vocabulary — Africa |
| 21 | `positive_europe.png` | strongly positive sentence vocabulary — Europe |
| 22 | `negative_europe.png` | strongly negative sentence vocabulary — Europe |

The submitted AI PDF also reports the TF-IDF cosine output and LSTM classification metrics in text/table form. The `0.2640` cosine number is now correctly documented as `cosine_sim[0][0]` rather than a corpus-level mean.

The complete original visual sequence is grouped into five high-resolution archival sheets under [`ai_course/figures/`](ai_course/figures/) and explained in [`ai_course/figures.md`](ai_course/figures.md).

---

# Part II — Social Media & Web Analytics extension: Africa

## Figures embedded in the submitted paper

The submitted `898396.pdf` contains **seven analytical figures**:

1. Africa speech-length distribution;
2. Africa participation across UN sessions;
3. Africa overall word cloud;
4. positive-sentiment Africa word cloud;
5. negative-sentiment Africa word cloud;
6. average compound sentiment over time, 1970–2015;
7. directed African country-mention network.

## Full source `Graphs` folder

The final SMWA source folder is richer than the submitted PDF and contains **21 analytical PNG files**:

| # | Source filename | Analysis |
|---:|---|---|
| 1 | `text_lengths_distribution_Africa.png` | Africa statement-length distribution |
| 2 | `sessions_distribution_Africa.png` | Africa participation across sessions |
| 3 | `countries_distribution_Africa.png` | speech counts by African country |
| 4 | `wordcloud_Africa.png` | overall Africa word cloud |
| 5 | `sentiment_distribution.png` | Africa VADER sentiment distribution |
| 6 | `sentiment_trends_over_time.png` | Africa sentiment over time |
| 7 | `positive_africa.png` | positive-sentiment word cloud |
| 8 | `negative_africa.png` | negative-sentiment word cloud |
| 9 | `LDA_topic_distribution.png` | LDA topic-share distribution |
| 10 | `topic_distribution_heatmap.png` | NMF document-topic heatmap |
| 11 | `topic_0.png` | NMF Topic 0 word cloud |
| 12 | `topic_1.png` | NMF Topic 1 word cloud |
| 13 | `topic_2.png` | NMF Topic 2 word cloud |
| 14 | `topic_3.png` | NMF Topic 3 word cloud |
| 15 | `topic_4.png` | NMF Topic 4 word cloud |
| 16 | `topic_5.png` | NMF Topic 5 word cloud |
| 17 | `topic_6.png` | NMF Topic 6 word cloud |
| 18 | `topic_7.png` | NMF Topic 7 word cloud |
| 19 | `topic_8.png` | NMF Topic 8 word cloud |
| 20 | `topic_9.png` | NMF Topic 9 word cloud |
| 21 | `network_plot.png` | directed country-mention network |

### BERTopic output

The final Graphs folder does **not** contain a separate static BERTopic PNG. BERTopic results are stored in the notebook output as topic-word lists / topic information and are summarized in the paper through the model-comparison discussion and coherence value. The GitHub documentation therefore explains BERTopic from the actual source output rather than inventing a missing source plot.

---

# Coursework-reported topic coherence

| Model | `c_v` coherence |
|---|---:|
| LDA | **0.3663** |
| NMF | **0.5464** |
| BERTopic | **0.7768** |

The submitted paper interprets BERTopic as the strongest model on these values. The professional methodology/QA notes explain why they should be treated as **coursework-reported diagnostics rather than a fully harmonized benchmark**: the three original model sections do not construct their coherence reference corpora identically.

For model mechanics, exact source topics and substantive interpretation, see [`../docs/models_and_interpretation.md`](../docs/models_and_interpretation.md).
