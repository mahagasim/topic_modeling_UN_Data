# Complete coursework figure index

This index separates the analytical outputs from the two original submissions and inventories the **individual source image files kept in the final project `Graphs` folders**. Decorative university/UN logos and stock photographs are excluded.

> **Source vs live display.** The original coursework contains **43 analytical source images: 22 from the AI Africa–Europe project and 21 from the SMWA Africa extension**. Some historical raster assets imported during the first GitHub rebuild did not decode reliably in GitHub. The portfolio therefore preserves the source filenames/provenance here while the README and visual galleries use **12 validated PNG figures under `figures/rendered/`**, generated from clean repository sources and verified by Pillow in GitHub Actions.

The submitted papers contain only a selected subset of the source figures; the final `Graphs` folders include additional diagnostics, sentiment outputs and topic visualizations.

---

# Part I — AI course foundation: Africa vs Europe

The final Africa–Europe `Graphs` folder contains **22 analytical PNG files**.

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
| 16 | `confusion_matrix_lstm.png` | LSTM Africa–Europe classification confusion matrix |
| 17 | `sentiment_distribution_comparison.png` | Africa–Europe VADER sentiment distribution |
| 18 | `sentiment_trends_over_time.png` | Africa–Europe sentiment trend by year |
| 19 | `positive_africa.png` | strongly positive sentence vocabulary — Africa |
| 20 | `negative_africa.png` | strongly negative sentence vocabulary — Africa |
| 21 | `positive_europe.png` | strongly positive sentence vocabulary — Europe |
| 22 | `negative_europe.png` | strongly negative sentence vocabulary — Europe |

The submitted AI PDF also reports the TF-IDF cosine output and LSTM classification metrics in text/table form. The `0.2640` cosine number is documented as `cosine_sim[0][0]` rather than a corpus-level mean.

The live AI gallery is [`ai_course/figures.md`](ai_course/figures.md). It uses validated PNGs for regional vocabulary, TF-IDF diagnostics, LDA, K-means, LSTM and sentiment interpretation while retaining this list as the source-level provenance record.

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

The final `Graphs` folder does **not** contain a separate static BERTopic PNG. BERTopic results are stored in notebook output as topic-word lists/topic information. The GitHub documentation therefore summarizes BERTopic from the executed source output rather than inventing a missing plot.

The live SMWA gallery is [`social_media_web_analytics/figures.md`](social_media_web_analytics/figures.md), with validated PNG summaries for LDA, NMF, coherence and the professional network reconstruction plus source-level interpretation of the word-cloud and sentiment outputs.

---

# Coursework-reported topic coherence

| Model | `c_v` coherence |
|---|---:|
| LDA | **0.3663** |
| NMF | **0.5464** |
| BERTopic | **0.7768** |

The submitted paper interprets BERTopic as strongest on these values. The professional methodology/QA notes explain why they should be treated as **coursework-reported diagnostics rather than a fully harmonized benchmark**: the three original model sections do not construct their coherence reference corpora identically.

For model mechanics, exact source topics and substantive interpretation, see [`../docs/models_and_interpretation.md`](../docs/models_and_interpretation.md).
