# Complete coursework figure index

This index separates the analytical outputs from the two original submissions. Decorative university/UN logos and stock photographs in the PDFs are intentionally excluded; every **analytical** figure is listed.

## Part I - AI course foundation: Africa vs Europe

1. Africa overall word cloud
2. Europe overall word cloud
3. Africa speech-length distribution
4. Europe speech-length distribution
5. TF-IDF cosine-similarity output (`0.2640`)
6. LDA topic-distribution comparison: Africa vs Europe
7. K-means elbow diagnostic
8. Continent-by-cluster heatmap
9. K-means cluster distribution
10. K-means cluster 0 word cloud
11. K-means cluster 1 word cloud
12. K-means cluster 2 word cloud
13. LSTM classification report / training output
14. LSTM confusion matrix
15. VADER sentiment trends: Africa vs Europe
16. Negative-sentiment word cloud: Africa
17. Negative-sentiment word cloud: Europe
18. Positive-sentiment word cloud: Africa
19. Positive-sentiment word cloud: Europe

These figures come from the final AI-course submission and its associated graph folder.

## Part II - Social Media & Web Analytics extension: Africa

1. Africa speech-length distribution
2. Africa participation across UN sessions
3. Africa overall word cloud
4. Positive-sentiment word cloud
5. Negative-sentiment word cloud
6. Average compound sentiment over time, 1970-2015
7. Directed African country-mention network

These seven figures are the complete set of analytical figures embedded in the submitted SMWA paper `898396.pdf`.

## Topic-model results in the SMWA paper

The topic-model comparison is reported primarily through text and a coherence table rather than an additional embedded chart:

| Model | Coursework-reported `c_v` coherence |
|---|---:|
| LDA | 0.3663 |
| NMF | 0.5464 |
| BERTopic | 0.7768 |

The submitted paper interprets BERTopic as the strongest model on these values; the professional methodology note explains why the numbers should be treated as source-reported diagnostics rather than a fully harmonized benchmark.
