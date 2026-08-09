# AI course submission - Africa vs Europe

This folder documents the original **Data Analytics and Artificial Intelligence (2023/24)** submission and its analytical outputs.

## Role in the combined project

This is the **foundation analysis**. It compares African and European UN General Debate speeches using:

- exploratory text analysis and regional word clouds;
- TF-IDF and cosine similarity;
- 10-topic LDA and topic prevalence comparison;
- K-means clustering with elbow selection and cluster interpretation;
- an LSTM classifier for Africa vs Europe;
- VADER sentiment distributions and trends;
- positive and negative sentiment word clouds by continent.

The original submission reports a TF-IDF cosine similarity of **0.2640** and an LSTM test accuracy of **85.1%** (766 test speeches; Europe precision/recall/F1 = 0.86/0.90/0.88, Africa = 0.84/0.78/0.81).

## Visual archive

**[Open the complete AI course visual gallery](figures.md)** - five figure sheets collecting the original analytical outputs from the Africa-Europe project.

## Provenance

The authoritative submitted PDF is **`AI Project_ Africa - Europe Project`** and the final source notebook is **`AI project_Africa - Europe.ipynb`** in the coursework Google Drive archive. They were read directly when reconstructing this repository.

The GitHub project records their methods and findings in:

- [`../../docs/methodology.md`](../../docs/methodology.md)
- [`../../docs/findings.md`](../../docs/findings.md)
- [`../FIGURE_INDEX.md`](../FIGURE_INDEX.md)
- [`../../notebooks/02_africa_europe_ml.ipynb`](../../notebooks/02_africa_europe_ml.ipynb)
- [`figures.md`](figures.md)

The visual gallery is preserved as coursework provenance; the root-level notebook and source modules are the professionalized, portable reconstruction.