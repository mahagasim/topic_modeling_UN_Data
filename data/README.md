# Data

This project uses the **United Nations General Debate Corpus (UNGDC)**.

## Expected local file

Download the corpus and place the CSV in this directory as:

```text
data/un-general-debates.csv
```

The original coursework used a CSV with the variables:

- `country`
- `session`
- `year`
- `text`

The original files in Google Drive cover speeches from 1970 through 2015.

## Source

The dataset used in the coursework is publicly available through Kaggle:

`https://www.kaggle.com/datasets/unitednations/un-general-debates/data`

## Why the data are not committed

The raw CSV is approximately 135 MB and the processed spreadsheet versions are also large. They are intentionally excluded from Git history. The professional version of the project should regenerate processed data from the raw source using code rather than store duplicated transformed files.

## Original coursework artifacts

The Drive archive contains several versions of the raw and processed data. These are retained as historical coursework artifacts, but they are not treated as canonical inputs for the rebuilt repository.
