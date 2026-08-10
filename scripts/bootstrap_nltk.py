"""Download the small NLTK resources required by the preprocessing pipeline."""

import nltk

for resource in ("stopwords", "wordnet", "omw-1.4"):
    print(f"Downloading NLTK resource: {resource}")
    nltk.download(resource, quiet=False)
