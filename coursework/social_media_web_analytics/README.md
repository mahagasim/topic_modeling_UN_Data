# Social Media & Web Analytics submission — Africa extension

This folder documents the original Africa-focused **Social Media & Web Analytics** submission and its analytical outputs.

## Role in the combined project

This is presented as an **extension of the AI-course analysis**. Using the same UN General Debate corpus, it narrows the substantive focus to African speeches and deepens the analysis with:

- descriptive analysis of speech length and session participation;
- an Africa word cloud;
- VADER sentiment analysis over 1970–2015;
- positive and negative sentiment word clouds;
- LDA, NMF, and BERTopic topic modeling;
- coherence-score comparison reported in the submission (LDA 0.3663, NMF 0.5464, BERTopic 0.7768);
- a country-mention network analysis.

The submission reports recurring themes around regional conflict, health, colonial history, sustainable development, human rights and international cooperation; it also reports a gradual upward sentiment trend and discusses regional structure in the country-mention network.

## Provenance

The authoritative submitted paper is **`898396.pdf`**. The source code is distributed across the final **`Topic Modeling`** and **`Network Analysis`** notebooks in the coursework Google Drive archive. They were read directly when reconstructing this repository.

The GitHub project records their methods and findings in:

- [`../../docs/methodology.md`](../../docs/methodology.md)
- [`../../docs/findings.md`](../../docs/findings.md)
- [`../FIGURE_INDEX.md`](../FIGURE_INDEX.md)
- [`../../notebooks/01_africa_ungd_nlp.ipynb`](../../notebooks/01_africa_ungd_nlp.ipynb)
- [`../../notebooks/03_africa_network_extension.ipynb`](../../notebooks/03_africa_network_extension.ipynb)

The figure index lists the complete set of analytical figures embedded in the submitted paper.
