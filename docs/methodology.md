# Methodology and provenance

This note documents how the professional rebuild was reconciled with the original coursework files. It is intentionally explicit about what is reproduced, what is corrected, and what should not be interpreted as a validated substantive finding.

## Computational source of truth

The primary computational source is the final Google Colab notebook named **`Topic Modeling`** together with its processed Africa dataset. That notebook records:

- 7,507 speeches in the full corpus;
- coverage from 1970 through 2015;
- 2,159 speeches in the Africa subset;
- 54 African country codes;
- LDA estimated with 10 topics, 50 passes, and `random_state=0`;
- an original Africa LDA `c_v` coherence score of 0.3662893178.

A separate coursework PDF uses a different corpus snapshot and a pre/post-MDG framing. Because its observation count, date range, and evaluation setup do not match the final notebook, it is treated only as contextual documentation and is not used as the computational source for this repository.

## Changes made in the rebuild

### 1. Portable project structure

The original notebooks relied on Google Colab installation cells and absolute Google Drive paths. The rebuild uses relative paths and separates reusable code into `src/` modules.

### 2. Safe sample construction

The Africa sample is created with `.loc[...].copy()` rather than mutating a filtered DataFrame view. This removes the `SettingWithCopyWarning` present in the exploratory notebook and makes the transformation explicit.

### 3. Sentiment-analysis unit corrected

The original sentiment cell tokenized the speech first and subsequently applied sentence tokenization to each token. As a result, VADER was effectively scoring token-level units rather than complete sentences. The rebuild computes sentence-level VADER scores from the original speech text and aggregates them to the speech level. For this reason, the original sentiment plots are not presented as validated results in the public-facing README.

### 4. Comparable topic-model evaluation

The original LDA, NMF, and BERTopic sections did not use exactly the same reference texts and dictionaries for coherence evaluation. In the rebuild, model topic-word lists can be evaluated with a common `c_v` reference corpus. The recorded LDA coherence of 0.3663 is retained as an **original-coursework diagnostic**, not as a claim that LDA is superior or inferior to the other models.

### 5. BERTopic kept optional

BERTopic has a heavier dependency stack and may download a sentence-transformer model at first run. Its import is therefore lazy and the clean notebook makes the BERTopic step optional. LDA and NMF can be reproduced without loading those dependencies.

## Interpretation boundaries

This project is descriptive NLP. Topic prevalence and sentiment are measurements derived from text and do not identify causal effects. Changes in the number of speeches over time can also reflect UN membership, corpus availability, and country coverage rather than a behavioral change in diplomatic participation.

Topic labels should be assigned only after inspecting high-weight terms and representative speeches. The README therefore reports the original top words and prevalence rather than imposing strong substantive labels that were not validated in the coursework.

## Reproducibility

Raw and processed data are intentionally excluded from Git history. The public UN General Debate corpus should be downloaded locally and placed under `data/`. Generated outputs can be recreated from the notebook and functions in `src/`.
