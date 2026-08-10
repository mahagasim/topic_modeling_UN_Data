# Social Media & Web Analytics — complete visual analysis

This page documents the **Africa-focused SMWA extension** using both the figures embedded in the submitted paper and the richer final source `Graphs` folder found during the second Google Drive audit.

The source folder contains **21 analytical PNG files** — substantially more than the seven figures embedded in the submitted paper. The full filename-level inventory is in [`../FIGURE_INDEX.md`](../FIGURE_INDEX.md), and detailed model explanations are in [`../../docs/models_and_interpretation.md`](../../docs/models_and_interpretation.md).

---

## 1. Submitted-paper visual overview

![SMWA analytical figure sheet](figures/figure-sheet-01.jpg)

**Open at full resolution:** [`figure-sheet-01.jpg`](figures/figure-sheet-01.jpg)

The paper-level visual set contains:

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

The final source graph folder contains `wordcloud_Africa.png` separately from the paper sheet.

The most visible vocabulary is institutional and development-oriented, including **United Nations, international community, developing country, Security Council, peace, development and cooperation-related language**.

### Interpretation

The cloud confirms that the African corpus is strongly structured by the common language of multilateral diplomacy. Because a frequency cloud does not account for document length, time or country composition, it is used as exploratory evidence rather than as a formal comparison of priorities.

---

## 3. Sentiment distribution and sentiment over time

The source `Graphs` folder contains both:

- `sentiment_distribution.png`;
- `sentiment_trends_over_time.png`.

The submitted analysis reports noticeable year-to-year variation together with a **gradual upward trend in average positivity over 1970–2015**.

### Positive sentiment word cloud

The source `positive_africa.png` prominently features **United Nations, peace, organization, people, security, justice, freedom, development, hope and respect**.

### Negative sentiment word cloud

The source `negative_africa.png` emphasizes **war, people, terrorism, conflict, violence, destruction, state, poverty, weapon and crisis**.

### Interpretation

Positive passages are dominated by the aspirational/institutional vocabulary of cooperation and peace; negative passages are dominated by security threats, violence and hardship. The result is substantively plausible for diplomatic speeches, but VADER is still a lexicon-based measurement and should not be interpreted as a direct measure of government welfare, ideology or latent preference.

The professional code also corrects a unit-of-analysis issue in the original sentiment workflow by scoring sentence-like units from raw speech text before aggregation.

---

## 4. LDA topic distribution

The source folder contains `LDA_topic_distribution.png` in addition to the paper's textual topic-model discussion.

The executed source notebook reports **LDA `c_v` coherence = 0.3663**. The largest fitted topic shares in the source output are:

- Topic 4 — racist / colonial / Pretoria / Zimbabwe / colonialism: **~30.3%**;
- Topic 3 — connection / recovery / Senegal / drought / structural: **~28.8%**;
- Topic 7 — goals / MDGs / Niger / Côte d'Ivoire-related language: **~12.8%**;
- Topic 2 — Congo / Togo / terrorism / Burundi / Guinea-Bissau: **~6.7%**;
- Topic 9 — Somalia / Sierra Leone / Liberia / Burundi: **~6.3%**.

### Interpretation

Under this specification, colonial/apartheid-related discourse and development/recovery language account for a large fraction of the fitted topic mass, while conflict, MDGs and region/country-specific issues form additional components.

---

## 5. NMF topic heatmap and ten topic word clouds

These were missing from the previous GitHub explanation even though the final Drive `Graphs` folder contains them.

The source files are:

- `topic_distribution_heatmap.png`;
- `topic_0.png` through `topic_9.png`.

The executed notebook reports **NMF `c_v` coherence = 0.5464**.

### Source-derived topic interpretation

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

### Interpretation

NMF produces several topics that are relatively easy to label from their highest-weighted terms. At the same time, country names are often dominant. This is useful for mapping geographically concentrated discourse but also warns that an unsupervised model can separate documents by country-specific vocabulary rather than only by abstract policy domain.

---

## 6. BERTopic output

The final Drive `Graphs` folder does **not** contain a separate static BERTopic PNG. The source notebook stores BERTopic results as topic information and topic-word outputs.

The executed coursework copy reports **BERTopic `c_v` coherence = 0.7768**, the highest of the three source-reported values. Topics range from broad institutional language around nations, development, international affairs and peace to narrower country-specific clusters involving Liberia, Somalia, Angola, Madagascar and others; one source topic also clearly contains climate-change language.

### Interpretation

The submitted paper interprets BERTopic as producing the most semantically coherent topics. The professional audit preserves that conclusion as a coursework finding but adds two qualifications:

1. coherence was not calculated against an identical reference construction for all three models;
2. BERTopic generated many more/narrower topics, including generic and country-specific clusters, so a higher coherence score does not by itself establish that it is substantively superior.

---

## 7. Model comparison

| Model | Representation | Coursework `c_v` | What it contributes here |
|---|---|---:|---|
| LDA | probabilistic bag-of-words | **0.3663** | mixed topic prevalence and broad thematic structure |
| NMF | TF-IDF matrix factorization | **0.5464** | clear additive term factors and geographic themes |
| BERTopic | transformer embeddings + clustering | **0.7768** | contextual semantic clusters with finer granularity |

The agreement across methods around **conflict, development, rights, colonial history, health and regional geopolitics** is more substantively informative than treating coherence alone as a winner-takes-all score.

---

## 8. Country-mention network

The source folder contains `network_plot.png`. The submitted paper highlights **Madagascar, Namibia, Comoros and Somalia**, while South Sudan appears comparatively isolated and East/West African groupings are discussed.

The original network code searches speech text for ISO3 country codes, which is fragile. The professional reconstruction uses country names and historical/orthographic aliases instead, so the reconstructed ranking is intentionally kept separate from the submitted network.

The network is descriptive: mention strength is **not** causal diplomatic influence or formal alliance strength.

---

## Complete source-graph accounting

The final SMWA `Graphs` folder contains:

- 4 EDA/overall-word-cloud plots;
- 4 sentiment plots/word clouds;
- 1 LDA distribution plot;
- 1 NMF topic-distribution heatmap;
- 10 NMF topic word clouds;
- 1 network plot.

That is **21 analytical image files in total**. BERTopic is represented through notebook topic outputs rather than an additional static PNG.

For the exact filename list, see [`../FIGURE_INDEX.md`](../FIGURE_INDEX.md). The professional reconstruction is organized in [`../../notebooks/01_africa_ungd_nlp.ipynb`](../../notebooks/01_africa_ungd_nlp.ipynb), [`../../notebooks/03_africa_network_extension.ipynb`](../../notebooks/03_africa_network_extension.ipynb), and the reusable modules under [`../../src/`](../../src/).
