# Models, measurement and interpretation

This note explains **what each model is doing, how it was implemented in the original coursework, what the reported results mean, and what they do not mean**. It should be read together with the source-figure galleries and `docs/qa.md`.

> **Provenance convention.** "Coursework-reported" values come from the final submitted notebooks/reports preserved in Google Drive. "Professional reconstruction" refers to code or diagnostics added during the GitHub rebuild. The two are not silently mixed.

---

## 1. Text preprocessing and sample construction

Both coursework projects start from the United Nations General Debate Corpus and use the core fields `session`, `year`, `country`, and `text`.

The Africa-Europe AI project maps country codes to continents and retains **2,159 African** and **1,667 European** statements in the saved computational snapshot, for **3,826 statements** in the comparative sample. The Africa-focused SMWA extension retains the same **2,159 African statements**.

The original preprocessing combines several standard NLP operations:

- removal of punctuation and non-visible/special characters;
- tokenization;
- removal of English stop words;
- lemmatization in the AI workflow and the earlier SMWA preprocessing;
- additional stemming and n-gram construction in the BERTopic section.

### Interpretation

Preprocessing determines what information the models can see. Removing common function words reduces noise for bag-of-words methods, but aggressive cleaning can also remove rhetorical or grammatical information. The professional rebuild therefore keeps the raw speech text available for analyses such as sentiment where sentence structure matters.

---

# Part I — Africa vs Europe

## 2. Regional word clouds

### What a word cloud measures

A word cloud is a **frequency visualization**: terms shown with larger visual weight occur more often in the selected corpus after the preprocessing used to construct the cloud. It is useful for orientation, not statistical inference.

### Source result

The original Africa and Europe word clouds both contain the institutional vocabulary of UN diplomacy, but their relative emphasis differs.

**Africa:** prominent terms include `United Nations`, `international community`, `General Assembly`, `Security Council`, `developing country`, `South Africa`, peace/security language, and development-related vocabulary.

**Europe:** prominent terms include `United Nations`, `international community`, `General Assembly`, `human rights`, `Security Council`, `Soviet Union`, `Member State`, peace/security language, and European/Middle East geopolitical vocabulary.

### Interpretation

The shared high-frequency vocabulary is expected because all documents come from the same institutional setting. Differences in relative prominence are more informative than the mere presence of a word. The clouds are therefore best used as a descriptive entry point before the formal topic, clustering and classification analyses.

---

## 3. TF-IDF and cosine similarity

### Model mechanics

**TF-IDF (term frequency-inverse document frequency)** converts each speech into a sparse vector. Terms receive more weight when they are frequent in a document but relatively uncommon across the whole collection. **Cosine similarity** then compares the angle between two vectors: higher values indicate more similar weighted vocabularies.

### Original implementation and QA correction

The final AI notebook constructs a full Europe-by-Africa cosine-similarity matrix and prints `cosine_sim[0][0] = 0.2640`.

That means the coursework-reported **0.2640** is the similarity of **one Europe-Africa speech pair**, not a corpus-level average. The professional audit therefore reports three different estimands separately:

| Similarity estimand | Value | Meaning |
|---|---:|---|
| Original first speech pair | **0.264** | Reproduces the submitted scalar |
| Sampled cross-region pairwise mean | **~0.188** | Mean similarity for a deterministic 300×300 cross-region speech sample |
| Regional TF-IDF centroid cosine | **~0.906** | Similarity between the mean Africa and Europe TF-IDF vectors |

### Interpretation

These values answer different questions. Individual speeches can be quite different while the two large regional corpora still share a strong common diplomatic vocabulary. The high centroid similarity is therefore not inconsistent with lower pairwise similarity.

---

## 4. Latent Dirichlet Allocation (LDA): Africa-Europe comparison

### Model mechanics

LDA is a **probabilistic mixed-membership topic model**. Each document is represented as a mixture of topics, and each topic is represented as a probability distribution over words. A speech can therefore contain several topics rather than being assigned to only one category.

### Original implementation

The AI project estimates **10 topics** with vocabulary filtering (`no_above=0.30`, `no_below=10`), **50 passes**, and `random_state=0`. Topic prevalence is then compared between African and European statements.

### Results and interpretation

| Topic | High-weight terms | Africa prevalence | Europe prevalence | Source-based interpretation |
|---|---|---:|---:|---|
| 0 | Sudan, Morocco, Egypt, Mediterranean, Libya | 0.0578 | 0.0125 | North Africa / Mediterranean geopolitics |
| 1 | racist, aggression, colonial, peoples, Zimbabwe | **0.1771** | 0.0307 | colonialism, racism, apartheid-era politics |
| 2 | Kosovo, terrorist, prevention, Spain, Iraq | 0.0370 | **0.2589** | terrorism, Kosovo and international legal/security issues |
| 3 | Somalia, Liberia, Sierra Leone, Congo, Leone | **0.1667** | 0.0141 | African regional conflict and governance |
| 4 | Chad, Rwanda, Burundi, Niger, recovery | **0.2019** | 0.0405 | African conflict/recovery and country-specific concerns |
| 5 | Ireland, Africa, Ethiopia, Cyprus, sanction | 0.1473 | 0.1068 | mixed geopolitical / sanctions vocabulary |
| 6 | Soviet, détente, socialist, peoples, German | 0.0332 | **0.1788** | Cold War and European political language |
| 7 | Bosnia, Herzegovina, Yugoslavia, Cyprus, former | 0.0170 | **0.1820** | Balkan / European conflict and transition |
| 8 | food, goals, health, Malawi, Guinea | **0.1016** | 0.0389 | development, health, food and MDGs |
| 9 | France, culture, think, Italy, religion | 0.0578 | **0.1343** | European/cultural-political vocabulary |

The strongest contrasts occur in Topics 1, 2, 3, 4, 6, 7 and 8. The result supports the descriptive conclusion that the two regional corpora share an institutional language but differ markedly in **which substantive themes receive more weight**.

### Limitation

Topic numbers have no intrinsic meaning. The labels above are interpretations of high-weight words and should be validated by reading representative speeches. They are not causal effects of continent.

---

## 5. K-means clustering

### Model mechanics

K-means is a **hard clustering** algorithm. After TF-IDF vectorization, every speech is assigned to exactly one cluster by minimizing distance to cluster centroids. Unlike LDA, a speech does not receive a mixture of clusters.

### Original implementation

The AI notebook uses an elbow diagnostic and selects **k = 3**. The saved processed-data snapshot produces:

| Continent | Cluster 0 | Cluster 1 | Cluster 2 |
|---|---:|---:|---:|
| Africa | **1,194** | 51 | **914** |
| Europe | 8 | **1,140** | **519** |

The submitted PDF contains slightly different counts from a separate run (for example 1,202 African documents in Cluster 0 and 1,112 European documents in Cluster 1); both are preserved as provenance.

### Cluster vocabulary

- **Cluster 0:** `country`, `international`, `united`, `development`, `nations`, `peace`, `world`, `people`, `security`, `african`.
- **Cluster 1:** `united`, `nations`, `international`, `country`, `security`, `world`, `development`, `human`, `right`.
- **Cluster 2:** `country`, `international`, `united`, `people`, `world`, `nations`, `peace`, `economic`, `africa`, `states`.

### Interpretation

The continent-by-cluster distribution is strongly asymmetric: African speeches dominate Cluster 0, European speeches dominate Cluster 1, and both appear substantially in Cluster 2. However, all three clusters contain a great deal of generic UN vocabulary. The clusters are therefore better understood as **different mixtures of diplomatic, development, security and economic language** than as sharply separated ideologies.

---

## 6. LSTM continent classifier

### Model mechanics

A Long Short-Term Memory (LSTM) network is a recurrent neural-network architecture designed for sequential data. Here it learns patterns in word sequences that help classify a statement as **Africa or Europe**.

### Original architecture

- 80/20 train-test split with `random_state=42`;
- tokenizer vocabulary: 10,000 words;
- maximum sequence length: 100;
- embedding dimension: 100;
- LSTM layer: 128 units;
- softmax output layer;
- Adam optimizer, learning rate 0.001;
- batch size 20;
- 10 epochs.

### Coursework-reported performance

**Held-out accuracy: 85.1%** on 766 speeches.

| Class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Europe | 0.86 | 0.90 | 0.88 | 452 |
| Africa | 0.84 | 0.78 | 0.81 | 314 |

### Interpretation

Text contains substantial information about geographic origin: the classifier correctly identifies most held-out speeches. The lower African recall (0.78) means African statements are more often misclassified as European than the reverse in the submitted test set.

The training history also shows **overfitting**. Training accuracy approaches 100%, while validation/test accuracy remains in the mid-80s. In addition, the original notebook uses the held-out test set as `validation_data` during training. The professional helper corrects that workflow by creating validation data from the training sample and reserving the test set for final evaluation.

The classifier demonstrates predictive separability; it does **not** imply that either continent has homogeneous political preferences.

---

## 7. VADER sentiment: Africa vs Europe

### Model mechanics

VADER is a **rule-based lexicon sentiment method**. It assigns negative, neutral and positive scores plus a normalized compound score. It does not learn sentiment from the UN corpus; it applies a pre-defined English sentiment lexicon and rules.

### Original analysis

The AI project compares sentiment distributions and annual sentiment trends for Africa and Europe and then creates four word clouds from strongly positive/negative sentences.

The submitted trend plot shows both regional series fluctuating through time. The project narrative particularly highlights more negative African sentiment in parts of the **1970s to mid-1980s**, followed by improvement and continued year-to-year variation.

### Sentiment-word-cloud interpretation

**Positive Africa:** prominent words/phrases include `United Nations`, `peace`, `security`, `people`, `justice`, `world`, `freedom`, `hope`, `progress`, `organization`, `support`, and `respect`.

**Negative Africa:** `world war`, `conflict`, `people`, `terrorism`, `state`, `violence`, `poverty`, `destruction`, `crisis`, and `weapon` are visually prominent.

**Positive Europe:** `United Nations`, `freedom`, `world`, `peace`, `people`, `security`, `respect`, `support`, `cooperation`, `organization`, `international`, and `justice` are prominent.

**Negative Europe:** `war`, `terrorism`, `people`, `violence`, `weapon`, `conflict`, `mass destruction`, `crisis`, `human rights`, and `world` are prominent.

### Interpretation

Positive language in both regions is strongly associated with institutional cooperation, peace, security, rights and support. Negative language in both regions is dominated by war, violence, terrorism, conflict and weapons. This suggests a **shared diplomatic sentiment vocabulary**, with historical variation in its prevalence.

### Important measurement caveat

The coursework contains more than one sentiment path. One works on heavily preprocessed text, while a later path returns to original speech text and extracts sentence-level positive/negative material for word clouds. The professional implementation therefore computes sentence-like VADER scores from the **original speech text** before aggregating to speeches. Original figures remain labeled as coursework outputs rather than being presented as newly validated estimates.

---

# Part II — Africa-focused SMWA extension

## 8. Africa-only descriptive analysis and word cloud

The SMWA project narrows the sample to the **2,159 African statements** and deepens the text analysis.

The submitted report describes a right-skewed speech-length distribution, relatively consistent participation across sessions, and a word cloud dominated by institutional/development vocabulary such as **United Nations, international community, developing country and Security Council**.

This section establishes the corpus structure before applying sentiment and topic models.

---

## 9. Africa sentiment over time

The SMWA analysis again uses VADER and reports substantial year-to-year fluctuation together with a **gradual upward trend in positivity over 1970–2015**.

The source positive word cloud emphasizes **United Nations, peace, organization, people, security, justice, freedom, development, hope and respect**. The negative word cloud emphasizes **war, people, terrorism, conflict, violence, destruction, state, poverty, weapon and crisis**.

### Interpretation

The sentiment results are consistent with the substantive role of UN General Debate speeches: positive language frequently concerns cooperation and institutional aspirations, while negative language concerns security threats, violence and hardship. Because VADER was developed for general English rather than long formal diplomatic speeches, the scores should be treated as a descriptive measurement rather than a direct measure of governments' latent preferences or welfare.

---

## 10. LDA in the Africa extension

The Africa-only LDA also uses **10 topics**. The executed coursework copy reports `c_v = 0.3663`.

| Topic | Leading terms | Mean topic share | Interpretation |
|---|---|---:|---|
| 0 | Zambia, Zimbabwe, Botswana, colonial | 0.0154 | Southern Africa / colonial transition |
| 1 | Sudan, Ethiopia, Chad, Eritrea, Libya | 0.0440 | Horn/Northeast African geopolitics |
| 2 | Congo, Togo, terrorist, Burundi, Guinea-Bissau | 0.0671 | conflict/security and country-specific crises |
| 3 | connection, recovery, Senegal, drought, structural | **0.2876** | development/recovery and structural challenges |
| 4 | racist, colonial, Pretoria, Zimbabwe, colonialism | **0.3032** | apartheid, colonialism and liberation politics |
| 5 | Morocco, Tunisia, Algeria, Cameroon, kingdom | 0.0297 | North Africa / monarchy and regional politics |
| 6 | Mauritius, Nigeria, Cape Verde, Malawi | 0.0270 | country-specific regional discourse |
| 7 | goals, d'Ivoire, MDGs, Niger, kingdom | 0.1279 | MDGs/development goals |
| 8 | Guinea, Egypt, Comoros, Equatorial, island | 0.0316 | country/island and regional vocabulary |
| 9 | Somalia, Sierra Leone, Liberia, Burundi | 0.0632 | conflict and post-conflict states |

Topics 3 and 4 dominate the fitted topic shares in the source output, placing development/recovery and colonial/apartheid-related language at the center of this particular LDA specification.

---

## 11. Non-negative Matrix Factorization (NMF)

### Model mechanics

NMF factorizes a **non-negative document-term matrix** into document-topic and topic-term matrices. In this project the input is TF-IDF, so the method finds additive latent factors built from terms with positive weights.

### Source topics

The executed coursework copy reports `c_v = 0.5464` and produces the following top-term structures:

| Topic | Leading terms | Interpretation |
|---|---|---|
| 0 | south, namibia, apartheid, regime, resolution | apartheid / Southern Africa |
| 1 | global, sustainable, challenge, 2015, goal, millennium, poverty | global development / MDGs-SDG transition |
| 2 | guinea, equatorial, bissau, government, republic, human, right | Guinea/Equatorial Guinea and rights/governance |
| 3 | morocco, tunisia, arab, egypt, palestinian, maghreb, mediterranean | North Africa / Arab-Maghreb politics |
| 4 | swaziland, kingdom, majesty, swazi, king, taiwan, china | Eswatini/Swaziland monarchy and diplomatic relations |
| 5 | ethiopia, somalia, eritrea, sudan, ethiopian, eritrean, IGAD, kenya | Horn of Africa conflict and regional cooperation |
| 6 | power, problem, independence, struggle, right, regime, territory | independence / political struggle |
| 7 | malawi, government, HIV, food, malawian, AIDS, Mozambique | health, food and Malawi-specific development |
| 8 | chad, libya, chadian, libyan, sudan, darfur | Chad-Libya-Sudan/Darfur security |
| 9 | burundi, rwanda, congo, conflict, democratic, political, niger | Great Lakes conflict / governance |

### Interpretation

Compared with the LDA output, NMF produces several factors that are easier to label from their highest-weighted terms. Many topics are geographically anchored, which is substantively useful but also shows that country names can dominate unsupervised topic discovery.

---

## 12. BERTopic

### Model mechanics

BERTopic is an **embedding-based topic-modeling pipeline**. In broad terms, it represents documents using transformer embeddings, reduces the representation, clusters semantically similar documents, and uses class-based TF-IDF to describe the resulting clusters.

### Original implementation and result

The source notebook applies bigram/trigram preprocessing, stemming and `BERTopic(n_gram_range=(1,5))`. The executed coursework copy reports **`c_v = 0.7768`**, higher than the reported NMF and LDA coherence values.

The resulting topics include broad institutional language as well as many country-specific clusters. Examples in the source output include general `nation/country/development/international/peace` language, Liberia-specific material, climate-change language, Somalia, Angola and Madagascar-related clusters.

### Interpretation and caveat

The submitted paper concludes that BERTopic gives the most coherent topics. The professional audit preserves that coursework conclusion but does **not** treat the three coherence numbers as a fully controlled model tournament because the LDA, NMF and BERTopic sections construct their coherence reference texts/dictionaries differently.

BERTopic also creates substantially more and narrower clusters than the fixed 10-topic LDA/NMF specifications. That can reveal fine-grained themes, but it can also fragment long UN speeches into country-specific or generic institutional topics. Coherence alone is therefore insufficient; topic diversity, stability, representative speeches and substantive usefulness should also be inspected.

---

## 13. Comparing the three topic models

| Model | Representation | Topic assignment | Coursework `c_v` | Main strength in this project | Main caution |
|---|---|---|---:|---|---|
| LDA | word counts / bag of words | mixed membership | 0.3663 | probabilistic, interpretable prevalence | lower reported coherence; sensitive to preprocessing/K |
| NMF | TF-IDF | additive factors | 0.5464 | clear high-weight term factors | often strongly country-driven |
| BERTopic | transformer embeddings + clustering | cluster-based | 0.7768 | contextual semantic representation | many/narrow topics; coherence setup not harmonized |

The three methods answer related but non-identical measurement questions. Agreement across them strengthens confidence that conflict, development, health, rights and regional geopolitics are recurring dimensions of the African UNGD corpus; differences show how representation and model assumptions shape the discovered structure.

---

## 14. Country-mention network

### Model mechanics

A directed mention network treats the **speaker country as the source node** and another African country mentioned in its speech as the **target node**. Edge weight records how frequently that directed mention occurs.

### Submitted result

The SMWA paper highlights **Madagascar, Namibia and Comoros** as central/prominent, **Somalia** as notable, **South Sudan** as comparatively isolated, and clusters involving East and West African countries.

### Professional reconstruction

The original source code searches speech text for ISO3 codes, which is a fragile measurement rule because speeches usually mention country names rather than codes. The GitHub reconstruction therefore matches country names and common historical/orthographic aliases and counts a target at most once per speech.

The reconstructed network consequently produces different rankings. This is intentional: the repository shows how a change in **measurement definition** changes the network result rather than pretending the two implementations are identical.

### Interpretation boundary

Degree/strength in this network measures textual mentions under a specified matching rule. It is not a causal measure of diplomatic influence, formal alliance strength or political importance.

---

# Overall substantive interpretation

Across the two coursework projects, several patterns recur:

1. **Strong shared institutional vocabulary.** Africa and Europe both speak in the language of the UN: peace, security, development, rights, cooperation and international institutions.
2. **Regional thematic differentiation.** LDA and K-means show substantial differences in the prevalence of colonial/apartheid, African regional-conflict, Balkan/Cold War, development/MDG and terrorism/security themes.
3. **Predictive regional signal.** The LSTM's 85.1% held-out accuracy shows that regional information is recoverable from text, although the model overfits and does not imply homogeneous discourse.
4. **Shared positive/negative diplomatic lexicons.** Positive language emphasizes peace, security, justice, cooperation and institutional support; negative language emphasizes war, terrorism, violence, conflict, weapons, poverty and crisis.
5. **Multiple topic models recover overlapping dimensions.** LDA, NMF and BERTopic repeatedly surface conflict, development, health, rights, colonial history and region-specific geopolitics, but with different granularity.
6. **Measurement choices matter.** The cosine-similarity scalar, sentiment unit of analysis, coherence construction and country-mention rule all materially affect interpretation. The professional rebuild makes those choices explicit.

## What the project does not establish

This is a **descriptive NLP and machine-learning analysis**, not a causal study. It does not establish that geographic region causes rhetorical differences, that particular historical events cause changes in sentiment, or that mention-network centrality measures political power. Those questions would require separate identification and validation strategies.
