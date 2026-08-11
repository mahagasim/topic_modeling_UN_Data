# Social Media & Web Analytics — complete visual analysis

This page documents the **Africa-focused SMWA extension** using the figures embedded in the submitted paper and the richer final source `Graphs` folder found during the Google Drive audit.

The source folder contains **21 analytical image files** — substantially more than the seven figures embedded in the submitted paper. The filename-level inventory is in [`../FIGURE_INDEX.md`](../FIGURE_INDEX.md), and detailed model explanations are in [`../../docs/models_and_interpretation.md`](../../docs/models_and_interpretation.md).

---

## 1. Submitted-paper visual overview

![SMWA analytical figure sheet](figures/figure-sheet-01.jpg)

**Open at full resolution:** [`figure-sheet-01.jpg`](figures/figure-sheet-01.jpg)

The submitted-paper visual set contains:

- Africa statement-length distribution;
- Africa participation across UN sessions;
- overall Africa word cloud;
- positive-sentiment word cloud;
- negative-sentiment word cloud;
- sentiment trend over time;
- directed African country-mention network.

**[Open/download the seven-figure submitted-paper archive](SMWA_all_figures.pdf)**

---

## 2. Africa overall word cloud

The final source graph folder contains `wordcloud_Africa.png` separately from the paper sheet. The most visible vocabulary is institutional and development-oriented, including **United Nations, international community, developing country, Security Council, peace, development and cooperation-related language**.

### Interpretation

The cloud confirms that the African corpus is strongly structured by the shared language of multilateral diplomacy. Because a frequency cloud does not adjust for document length, time or country composition, it is exploratory evidence rather than a formal comparison of priorities.

---

## 3. Sentiment distribution and sentiment over time

The final source folder contains both `sentiment_distribution.png` and `sentiment_trends_over_time.png`, as well as positive/negative Africa word clouds.

The submitted analysis reports noticeable year-to-year variation together with a **gradual upward trend in average positivity over 1970–2015**.

| Sentiment subset | Prominent source vocabulary | Interpretation |
|---|---|---|
| Positive Africa | United Nations, peace, organization, people, security, justice, freedom, development, hope, respect | cooperation, peace and institutional aspiration |
| Negative Africa | war, terrorism, conflict, violence, destruction, poverty, weapon, crisis | security threats, conflict and hardship |

VADER is a rule-based lexicon measurement rather than a learned model of diplomatic preferences. The professional implementation also corrects a source unit-of-analysis issue by scoring sentence-like units from raw speech text before aggregation.

---

## 4. LDA topic distribution

The final source folder contains `LDA_topic_distribution.png`. The executed source notebook reports **LDA `c_v` coherence = 0.3663**.

The largest fitted topic shares in the source output are:

| Topic | Source terms / interpretation | Mean share |
|---|---|---:|
| Topic 4 | racist, colonial, Pretoria, Zimbabwe, colonialism | **~30.3%** |
| Topic 3 | connection, recovery, Senegal, drought, structural | **~28.8%** |
| Topic 7 | goals, MDGs, Niger, Côte d'Ivoire-related language | **~12.8%** |
| Topic 2 | Congo, Togo, terrorism, Burundi, Guinea-Bissau | **~6.7%** |
| Topic 9 | Somalia, Sierra Leone, Liberia, Burundi | **~6.3%** |

### Interpretation

Under this specification, colonial/apartheid-related discourse and development/recovery language account for a large part of the fitted topic mass, while conflict, MDGs and country/region-specific issues form additional components.

Full source output: [`../../results/smwa_lda_topics.csv`](../../results/smwa_lda_topics.csv).

---

## 5. NMF topic heatmap and ten topic word clouds

The final Drive graph folder contains `topic_distribution_heatmap.png` plus **`topic_0.png` through `topic_9.png`**. The executed notebook reports **NMF `c_v` coherence = 0.5464**.

| NMF topic | Dominant terms | Interpretation |
|---|---|---|
| 0 | south, namibia, apartheid, regime, resolution | apartheid / Southern Africa |
| 1 | global, sustainable, 2015, goal, millennium, poverty | sustainable development / MDGs-SDG transition |
| 2 | guinea, equatorial, bissau, republic, human, right | Guinea-region governance and rights |
| 3 | morocco, tunisia, arab, egypt, palestinian, maghreb | North Africa / Arab-Maghreb politics |
| 4 | swaziland, kingdom, majesty, swazi, taiwan, china | Swaziland/Eswatini monarchy and diplomacy |
| 5 | ethiopia, somalia, eritrea, sudan, IGAD, kenya | Horn of Africa conflict/regional cooperation |
| 6 | power, independence, struggle, right, regime, territory | independence and political struggle |
| 7 | malawi, HIV, food, AIDS, Mozambique | health, food and Malawi development |
| 8 | chad, libya, sudan, darfur | Chad-Libya-Sudan / Darfur security |
| 9 | burundi, rwanda, congo, conflict, democratic | Great Lakes conflict and governance |

NMF yields several relatively interpretable factors, but country names are often dominant. That helps map geographically concentrated discourse while also warning that unsupervised models may separate documents by country-specific vocabulary rather than only by abstract policy domain.

Full source output: [`../../results/smwa_nmf_topics.csv`](../../results/smwa_nmf_topics.csv).

---

## 6. BERTopic output

The final Drive `Graphs` folder does **not** contain a separate static BERTopic figure. The executed source notebook stores BERTopic results as topic information and topic-word outputs.

The coursework reports **BERTopic `c_v` coherence = 0.7768**, the highest of the three source-reported diagnostics. The notebook contains **53 BERTopic topics (0–52)** ranging from broad institutional/development language to narrower country-specific clusters such as Liberia, Somalia, Angola, Madagascar and others, including a climate-change topic.

All source topic-word outputs are preserved in [`../../results/smwa_bertopic_topics.csv`](../../results/smwa_bertopic_topics.csv).

### Interpretation caveat

The submitted paper interprets BERTopic as producing the most semantically coherent topics, but the professional audit retains two qualifications: the coherence reference construction is not identical across the three model sections, and BERTopic generates many more/narrower topics. Therefore the higher number is retained as a coursework diagnostic rather than treated as conclusive model superiority.

---

## 7. Model comparison

| Model | Representation | Coursework `c_v` | Contribution |
|---|---|---:|---|
| LDA | probabilistic bag-of-words | **0.3663** | mixed topic prevalence and broad thematic structure |
| NMF | TF-IDF matrix factorization | **0.5464** | clear additive term factors and geographic themes |
| BERTopic | transformer embeddings + clustering | **0.7768** | contextual semantic clusters with finer granularity |

The recurring themes across methods — **conflict, development, rights, colonial history, health and regional geopolitics** — are more substantively useful than interpreting coherence as a winner-takes-all score.

---

## 8. Country-mention network

The final source folder contains `network_plot.png`. The submitted paper highlights **Madagascar, Namibia, Comoros and Somalia**, while South Sudan appears comparatively isolated and East/West African groupings are discussed.

The original network code searches text for ISO3 country codes, which is fragile. The professional reconstruction uses country names and historical/orthographic aliases instead, so reconstructed rankings are intentionally kept separate from the submitted network. Mention strength is descriptive and should not be read as causal diplomatic influence or formal alliance strength.

---

## Complete SMWA source-graph accounting

The final SMWA `Graphs` folder contains **21 analytical image files**:

- 4 EDA/overall-word-cloud plots;
- 4 sentiment plots/word clouds;
- 1 LDA distribution plot;
- 1 NMF topic-distribution heatmap;
- 10 NMF topic word clouds;
- 1 network plot.

BERTopic is represented through notebook topic outputs rather than an additional static figure.

For the exact filename list, see [`../FIGURE_INDEX.md`](../FIGURE_INDEX.md). The professional reconstruction is organized in [`../../notebooks/01_africa_ungd_nlp.ipynb`](../../notebooks/01_africa_ungd_nlp.ipynb), [`../../notebooks/03_africa_network_extension.ipynb`](../../notebooks/03_africa_network_extension.ipynb), and the reusable modules under [`../../src/`](../../src/).
