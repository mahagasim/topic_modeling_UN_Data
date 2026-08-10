# Analytical result tables

This directory contains compact, machine-readable outputs extracted from the audited coursework artifacts or produced by the professional reconstruction. Files are labeled by provenance rather than mixing source and reconstructed results.

## AI course — Africa vs Europe

| File | Contents |
|---|---|
| `sample_counts.csv` | audited full/Africa/Europe sample sizes |
| `ai_similarity_audit.csv` | corrected definitions for first-pair, sampled pairwise and regional-centroid cosine similarity |
| `ai_lda_topics_and_prevalence.csv` | all 10 AI LDA topics, source terms and Africa/Europe mean prevalence |
| `ai_kmeans_cluster_counts.csv` | audited K-means cluster counts by continent |
| `ai_kmeans_top_terms.csv` | source top terms for the three K-means clusters |
| `ai_lstm_confusion_matrix.csv` | submitted LSTM confusion matrix |
| `ai_lstm_training_history.csv` | submitted 10-epoch training/validation history |

## SMWA extension — Africa

| File | Contents |
|---|---|
| `smwa_lda_topics.csv` | all 10 source LDA topics, mean topic shares and interpretation |
| `smwa_nmf_topics.csv` | all 10 source NMF topics and top ten terms |
| `smwa_bertopic_topics.csv` | **all 53 BERTopic topic-word outputs (Topics 0–52)** from the executed coursework notebook |
| `smwa_topic_coherence_coursework.csv` | coursework-reported LDA/NMF/BERTopic coherence scores |
| `professional_network_top_mentions.csv` | top incoming mentions under the professional country-name/alias reconstruction |

## Provenance rule

`smwa_lda_topics.csv`, `smwa_nmf_topics.csv`, `smwa_bertopic_topics.csv`, the AI LDA/K-means/LSTM source tables and the coherence table reproduce **executed coursework outputs**. The similarity audit and professional network table are explicitly labeled professional reconstructions/corrections.

For model explanation and substantive interpretation, see [`../docs/models_and_interpretation.md`](../docs/models_and_interpretation.md). For the complete original visual inventory, see [`../coursework/FIGURE_INDEX.md`](../coursework/FIGURE_INDEX.md).
