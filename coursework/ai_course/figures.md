# AI course — complete Africa-Europe visual gallery

This page makes the **original AI-course analytical outputs visible directly in GitHub** rather than requiring a reader to hunt through the submitted PDF. The source audit found **22 individual PNG files** in the final Africa-Europe `Graphs` folder; they are represented below in the five archival sheets created from the original coursework outputs.

For the exact source filenames, see [`../FIGURE_INDEX.md`](../FIGURE_INDEX.md). For model mechanics and detailed interpretation, see [`../../docs/models_and_interpretation.md`](../../docs/models_and_interpretation.md).

---

## 1. Corpus diagnostics and regional word clouds

![AI course: corpus diagnostics and Africa-Europe word clouds](figures/figure-sheet-01.jpg)

**Open at full resolution:** [`figure-sheet-01.jpg`](figures/figure-sheet-01.jpg)

This stage covers the Africa/Europe session distributions, country participation, speech-length diagnostics and the two **overall regional word clouds**.

### What the word clouds show

Both regions share the institutional vocabulary of UN diplomacy. The Africa cloud gives substantial visual prominence to language around **United Nations, international community, developing countries, Africa/South Africa, peace, security and development**. The Europe cloud similarly emphasizes **United Nations, international community, human rights, Security Council, peace/security and European/Cold-War-related vocabulary**.

The key interpretation is comparative: the same institutional language dominates both corpora, but the **relative prominence of development, colonial/regional and European geopolitical terms differs**.

---

## 2. TF-IDF and LDA topic comparison

![AI course: text similarity and LDA topic comparison](figures/figure-sheet-02.jpg)

**Open at full resolution:** [`figure-sheet-02.jpg`](figures/figure-sheet-02.jpg)

The LDA plot compares the prevalence of a joint **10-topic model** between Africa and Europe. Strong contrasts include:

- Africa-heavy topics involving **colonialism/racism**, Somalia-Liberia-Sierra Leone-Congo, Chad-Rwanda-Burundi and development/health/MDGs;
- Europe-heavy topics involving **Kosovo/terrorism**, Soviet/détente language and Bosnia-Herzegovina/Yugoslavia/Cyprus.

The TF-IDF QA note is important: the submitted `0.2640` scalar was one Europe-Africa speech-pair similarity (`cosine_sim[0][0]`), not a regional average. The professional README now reports that value separately from pairwise and centroid similarity estimands.

---

## 3. K-means diagnostics and cluster structure

![AI course: K-means elbow, cluster distribution and heatmap](figures/figure-sheet-03.jpg)

**Open at full resolution:** [`figure-sheet-03.jpg`](figures/figure-sheet-03.jpg)

The elbow diagnostic motivates **three clusters**. In the audited saved-data snapshot, African speeches dominate Cluster 0, European speeches dominate Cluster 1, and both regions have substantial representation in Cluster 2.

The cluster vocabularies all contain generic UN terms, so the clusters should be interpreted as **different mixtures of development/security, governance/rights and economic/international-relations language**, not as three clean political ideologies.

---

## 4. LSTM classification and sentiment distribution/trends

![AI course: LSTM classification and VADER sentiment comparison](figures/figure-sheet-04.jpg)

**Open at full resolution:** [`figure-sheet-04.jpg`](figures/figure-sheet-04.jpg)

This sheet includes the LSTM evaluation and the **Africa-Europe VADER sentiment distribution/trend graphs** that were difficult to find on the previous GitHub page.

### LSTM result

The coursework reports **85.1% held-out accuracy**. Europe has precision/recall/F1 of **0.86/0.90/0.88** and Africa **0.84/0.78/0.81**. The result shows that text contains substantial regional signal, although the training history also shows overfitting.

### Sentiment result

The source sentiment comparison shows both regional series fluctuating over 1970–2015. The submitted interpretation emphasizes relatively more negative African sentiment in parts of the **1970s through the mid-1980s**, followed by improvement and continued variation. The professional QA retains the original plot while separately documenting the sentiment unit-of-analysis issue in the source code.

---

## 5. Positive and negative sentiment word clouds

![AI course: Africa-Europe positive and negative sentiment word clouds](figures/figure-sheet-05.jpg)

**Open at full resolution:** [`figure-sheet-05.jpg`](figures/figure-sheet-05.jpg)

This sheet contains the four missing **sentiment-specific word clouds**:

### Positive — Africa

Prominent language includes **United Nations, peace, security, people, justice, freedom, hope, progress, organization, support and respect**.

### Negative — Africa

Prominent language includes **world war, conflict, terrorism, violence, poverty, destruction, crisis and weapons**.

### Positive — Europe

Prominent language includes **United Nations, freedom, peace, people, security, respect, support, cooperation, organization and justice**.

### Negative — Europe

Prominent language includes **war, terrorism, violence, weapons, conflict, mass destruction, crisis and human rights**.

### Interpretation

The clouds show a notable shared diplomatic sentiment vocabulary: positive passages emphasize **peace, cooperation, rights and institutional support**, while negative passages emphasize **war, violence, terrorism, conflict and weapons**. The differences are in relative emphasis rather than completely distinct vocabularies.

---

## Complete source inventory

The final Drive `Graphs` folder contains **22 individual AI-course plot files** covering:

- 8 EDA/regional-vocabulary plots;
- 1 LDA comparison plot;
- 6 K-means diagnostics/cluster plots;
- 1 LSTM confusion matrix;
- 2 sentiment distribution/trend plots;
- 4 positive/negative sentiment word clouds.

Every filename is listed in [`../FIGURE_INDEX.md`](../FIGURE_INDEX.md).

The professional reconstruction of the analytical pipeline is organized in [`../../notebooks/02_africa_europe_ml.ipynb`](../../notebooks/02_africa_europe_ml.ipynb), with reusable code in [`../../src/comparative_analysis.py`](../../src/comparative_analysis.py), [`../../src/sentiment.py`](../../src/sentiment.py) and [`../../src/visualization.py`](../../src/visualization.py).
