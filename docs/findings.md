# Consolidated findings from the original coursework

This document summarizes what the two submitted coursework projects actually report. It deliberately distinguishes **source-derived findings** from methodological comments added during the professional rebuild.

# Part I - AI course: Africa vs Europe

## Shared vocabulary, but substantial regional separation

The TF-IDF comparison reports a cosine similarity of **0.2640** between the African and European corpora. The submission interprets this as evidence of common diplomatic language alongside substantial differences in vocabulary and emphasis.

The regional word clouds reinforce that interpretation visually: both corpora contain the institutional vocabulary of international diplomacy, but their relative term prominence differs.

## Topic structure differs across regions

The joint 10-topic LDA model identifies a mixture of historical, geopolitical and development-related themes.

The submitted discussion associates European discourse more strongly with themes involving **Kosovo, terrorism, Bosnia/Yugoslavia, Cyprus and Cold War political language**, while African discourse gives more prominence to **post-colonialism/racism, African regional conflict and governance challenges**.

Development and human-welfare vocabulary also appears in the shared topic structure, including **food, health, education and MDGs**.

## Unsupervised clusters contain overlapping diplomatic vocabulary

K-means is estimated on TF-IDF features with three clusters selected after an elbow diagnostic. The top cluster terms remain dominated by broadly shared diplomatic concepts including `international`, `united`, `nations`, `development`, `peace`, `security`, `people`, `economic`, `africa`, and `human/right` language.

This means the clustering should not be interpreted as three clean substantive ideologies; instead, it demonstrates heterogeneous mixtures within a vocabulary that is strongly shaped by the UN diplomatic setting.

## Text predicts continent with meaningful accuracy

The submitted LSTM reports **85.1% test accuracy** on 766 held-out speeches.

- Europe: precision 0.86, recall 0.90, F1 0.88.
- Africa: precision 0.84, recall 0.78, F1 0.81.

The model therefore recovers substantial regional information from text, although the misclassification rate and lower recall for African speeches show that regional discourse overlaps considerably.

## Sentiment changes over time

The AI submission reports changing sentiment patterns across both continents and describes African statements as relatively more negative in parts of the 1970s through the mid-1980s. The four sentiment-specific word clouds provide qualitative context by separately visualizing strongly positive and negative sentences in Africa and Europe.

**Methodological note:** the professional rebuild preserves these as submitted results while using a cleaner sentence-level VADER implementation for future reproduction.

# Part II - Social Media & Web Analytics: Africa extension

## African participation is persistent across the corpus

The submitted paper describes relatively consistent participation across UN sessions and a right-skewed distribution of speech length. Its Africa word cloud prominently features institutional and development-related vocabulary such as **United Nations**, **international community**, **developing country**, and **Security Council**.

## Sentiment is volatile but trends upward in the submitted analysis

The SMWA paper reports substantial year-to-year variation in mean compound VADER sentiment from 1970 to 2015, alongside a **gradual upward trend in positivity**.

Its positive sentiment word cloud emphasizes words associated with **peace, justice, people, hope and cooperation**, while the negative word cloud emphasizes **war, conflict, terrorism, poverty and violence**.

## Topic models recover conflict, development and rights-related themes

The submitted interpretation of the three models is:

- **LDA:** regional conflicts, health issues and colonial history, including terms connected with countries such as Zambia and Sudan and with HIV/AIDS;
- **NMF:** apartheid, sustainable development, human rights and geopolitical/social issues;
- **BERTopic:** broader contextual topics with recurring language around nations, international affairs and development.

The paper reports `c_v` coherence values of **0.3663 (LDA), 0.5464 (NMF), and 0.7768 (BERTopic)** and concludes that BERTopic performs best on those values.

**Methodological note:** the professional audit does not treat that ranking as a fully controlled benchmark because the original coherence reference constructions differ across model sections.

## The country-mention network is regionally structured

The submitted network analysis represents African countries as nodes and mentions between countries as directed weighted edges.

The paper highlights:

- **Madagascar** as especially central;
- important positions for **Namibia** and **Comoros**;
- **Somalia** as a notable node in conflict/humanitarian discourse;
- **South Sudan** as comparatively isolated;
- regional clusters involving East African countries such as Kenya, Uganda, Tanzania and Rwanda, and West African countries such as Nigeria, Ghana and Senegal.

These are descriptive properties of the constructed mention network, not estimates of causal influence.

# Integrated interpretation

Taken together, the two courses show a natural analytical progression:

1. **Can regional diplomatic discourse be distinguished?**  
   The Africa-Europe comparison suggests yes: similarity is modest, topics differ in prevalence, and an LSTM classifies continent with about 85% test accuracy.

2. **What structures the African corpus internally?**  
   The extension shows a mix of conflict, development, health, rights and international-cooperation language; sentiment varies over time; and country mentions form non-random regional/network patterns.

3. **Why use multiple NLP methods?**  
   TF-IDF, LDA, NMF, BERTopic, clustering, deep learning, sentiment analysis and networks answer different measurement questions. Agreement across methods can strengthen an interpretation, while disagreement is itself informative about representation and model assumptions.

# What is not established

Neither submission identifies causal effects. The analyses do **not** establish that region causes rhetorical differences, that sentiment changes are caused by particular historical events, or that network centrality measures diplomatic power. Those would require separate identification strategies and validation exercises.
