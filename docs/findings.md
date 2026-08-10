# Consolidated findings

This note distinguishes **submitted/coursework findings** from **professional QA reconstructions**. The former reproduce what the two course submissions reported; the latter are explicitly labeled when the measurement definition changes.

## Part I — AI course foundation: Africa vs Europe

### Sample

The AI-course comparison uses 3,826 speeches in the saved processed snapshot: 2,159 from Africa and 1,667 from Europe, drawn from the 7,507-speech UNGD corpus covering 1970-2015 in the computational data.

### Regional vocabulary and EDA

The submitted project compares session distributions, country coverage, speech lengths and word clouds for Africa and Europe. The analysis emphasizes substantial common diplomatic vocabulary but meaningful differences in relative thematic prominence.

### TF-IDF / cosine similarity

The submission reports **0.2640**. QA of the original code shows that this value is `cosine_sim[0][0]`, i.e. one Europe-Africa speech pair. It should not be interpreted as a single summary of the two full regional corpora.

For transparency, the saved processed snapshot gives approximately:

- first-pair cosine (coursework implementation): **0.264**;
- deterministic sampled cross-region pairwise mean: **0.188**;
- regional TF-IDF centroid cosine: **0.906**.

The large difference is not a contradiction: these are different estimands.

### Joint LDA

The submitted joint LDA uses 10 topics, `no_above=0.30`, `no_below=10`, 50 passes and `random_state=0`. Source topic terms include:

- **Topic 0:** Sudan, Morocco, Egypt, Mediterranean, Libya, Malta, Tunisia;
- **Topic 1:** racist, aggression, colonial, Zimbabwe, domination, colonialism, occupation, Pretoria;
- **Topic 2:** Kosovo, terrorist, prevention, Iraq, court, globalization, partnership;
- **Topic 3:** Somalia, Liberia, Sierra Leone, Congo, Uganda, Sudan, governance;
- **Topic 4:** Chad, Rwanda, Burundi, Niger, Mali;
- **Topic 6:** Soviet, détente, socialist, Germany, armament, Cyprus;
- **Topic 7:** Bosnia, Herzegovina, Yugoslavia, Cyprus, Croatia, Greece, Ukraine;
- **Topic 8:** food, goals, health, education, water, MDGs.

The source prevalence table shows large Africa-Europe differences. For example, Topics 1, 3 and 4 are much more prevalent in African statements, while Topics 2, 6 and 7 are much more prevalent in European statements. These are descriptive topic-model patterns.

### K-means

The source workflow uses TF-IDF, an elbow diagnostic and `k=3`. Source top terms are:

- **Cluster 0:** country, international, united, development, nations, peace, world, people, security, African;
- **Cluster 1:** united, nations, international, country, security, world, must, development, human, right;
- **Cluster 2:** country, international, united, people, world, nations, peace, economic, Africa, states.

The saved processed snapshot assigns Africa mainly to Clusters 0 and 2 and Europe mainly to Clusters 1 and 2. The source narrative interprets these as security/development, governance/human-rights, and economic/international-relations emphases.

### LSTM classification

The submitted model uses an 80/20 split, vocabulary 10,000, max sequence length 100, embedding dimension 100, LSTM(128), Adam learning rate 0.001, batch size 20 and 10 epochs.

Submitted held-out results:

- accuracy: **85.1%**;
- Europe: precision 0.86, recall 0.90, F1 0.88 (n=452);
- Africa: precision 0.84, recall 0.78, F1 0.81 (n=314);
- confusion matrix: `[[406, 46], [68, 246]]`.

The training logs also show near-perfect training accuracy by later epochs but materially lower validation accuracy, indicating overfitting. The professional notebook therefore presents the classifier as a useful demonstration of regional text signal, not as a fully optimized predictive model.

### Sentiment

The submitted AI report describes more negative African sentiment in parts of the 1970s through the mid-1980s and shared negative vocabulary around terrorism, war, violence and conflict. Because the coursework contains multiple sentiment implementations, these are preserved as source-reported findings. The professional code uses corrected sentence-level VADER measurement for future reruns.

## Part II — SMWA extension: Africa deep dive

### Descriptive analysis

The submitted paper reports:

- right-skewed statement lengths, with many speeches around 5,000-20,000 characters and a peak around 10,000;
- relatively consistent engagement across sessions;
- frequent word-cloud terms including *United Nations*, *international community*, *developing country* and *Security Council*.

### Sentiment

The SMWA paper reports a gradual upward trend in average compound sentiment from 1970 to 2015 despite substantial year-to-year fluctuations.

Source interpretations of sentiment-specific word clouds:

- **positive:** United Nations, peace, justice, people, hope, cooperation/stability;
- **negative:** war, conflict, terrorism, poverty, violence, hardship/insecurity.

### LDA, NMF and BERTopic

The submitted paper reports the following `c_v` coherence values:

| Model | Coursework-reported coherence |
|---|---:|
| LDA | 0.3663 |
| NMF | 0.5464 |
| BERTopic | 0.7768 |

The paper interprets:

- LDA topics around regional conflict, health and colonial history;
- NMF topics around apartheid, sustainable development and human rights;
- BERTopic as recovering broader contextual themes around nations, international affairs and development.

The original paper ranks BERTopic highest. The QA note qualifies this because coherence inputs were not fully harmonized across the three model sections.

### Country-mention network

The submitted paper reports:

- Madagascar as particularly central;
- Namibia and Comoros as prominent;
- Somalia as a notable focus;
- South Sudan as comparatively isolated;
- Eritrea, Guinea-Bissau and Tunisia on the periphery;
- an East African grouping involving Kenya, Uganda, Tanzania and Rwanda;
- a West African grouping involving Nigeria, Ghana and Senegal.

These are source-reported patterns from the original network construction. The professional name/alias-based reconstruction produces a different ranking and is presented separately because the measurement rule is different.

## Interpretation boundary

All results are descriptive measurements from text. Topic prevalence, sentiment, cosine similarity, cluster membership, classifier accuracy and mention-network centrality do not identify causal effects and should not be read as evidence of homogeneous regional political preferences.
