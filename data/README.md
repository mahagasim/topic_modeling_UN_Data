# Data

This combined project uses the **United Nations General Debate Corpus (UNGDC)**.

## Expected local files

Download the corpus and place the CSV in this directory as:

```text
data/un-general-debates.csv
```

The core variables used by both coursework projects are:

- `country`
- `session`
- `year`
- `text`

For the Africa-Europe comparative notebook, also provide:

```text
data/country_continent.csv
```

with columns `country` (UN/ISO-style country code used by the corpus) and `Continent`. The original coursework created this mapping manually and reused it across both analyses.

## Analysis window

The final computational notebooks use speeches from **1970 through 2015**. One submitted document describes the source corpus as extending through 2016; this discrepancy is preserved in the provenance note rather than silently reconciled.

## Source

The dataset used in the coursework is publicly available through Kaggle:

`https://www.kaggle.com/datasets/unitednations/un-general-debates/data`

## Why the data are not committed

The raw CSV is approximately 135 MB and the processed spreadsheet versions are also large. They are intentionally excluded from Git history. The professional version regenerates processed variables from the raw source rather than storing duplicated intermediate copies.

## Original coursework artifacts

Google Drive contains multiple raw/processed snapshots created during the two courses. They remain historical coursework artifacts and are useful for auditing submitted outputs, but the professional workflow treats code + a single raw corpus as the preferred reproducibility path.
