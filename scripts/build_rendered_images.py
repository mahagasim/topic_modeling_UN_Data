from __future__ import annotations

from pathlib import Path

from PIL import Image
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "rendered"
OUT.mkdir(parents=True, exist_ok=True)

# Portfolio-facing figures are generated only from valid SVG sources.
# The historical coursework JPEG sheets are retained as provenance but are
# deliberately excluded from the live rendering path because they are not
# reliably decodable by standard image libraries.
SVG_FILES = [
    "sample_composition",
    "ai_similarity_diagnostics",
    "ai_lda_topic_prevalence",
    "ai_kmeans_by_continent",
    "ai_lstm_confusion_matrix",
    "ai_lstm_training_history",
    "smwa_topic_coherence",
    "smwa_network_top_mentions",
    "ai_regional_vocabulary_summary",
    "ai_sentiment_vocabulary_summary",
    "smwa_lda_topic_shares",
    "smwa_nmf_topic_map",
]

for stem in SVG_FILES:
    src = ROOT / "figures" / "professional" / f"{stem}.svg"
    dst = OUT / f"{stem}.png"
    if not src.exists():
        raise FileNotFoundError(src)
    cairosvg.svg2png(url=str(src), write_to=str(dst), output_width=1600)

# Rewrite the portfolio-facing Markdown so it never relies on the historical
# JPEG sheets or inline SVG rendering.
replacements = {
    "README.md": {
        "coursework/ai_course/figures/figure-sheet-01.jpg": "figures/rendered/ai_regional_vocabulary_summary.png",
        "coursework/ai_course/figures/figure-sheet-02.jpg": "figures/rendered/ai_lda_topic_prevalence.png",
        "coursework/ai_course/figures/figure-sheet-03.jpg": "figures/rendered/ai_kmeans_by_continent.png",
        "coursework/ai_course/figures/figure-sheet-04.jpg": "figures/rendered/ai_lstm_confusion_matrix.png",
        "coursework/ai_course/figures/figure-sheet-05.jpg": "figures/rendered/ai_sentiment_vocabulary_summary.png",
        "coursework/social_media_web_analytics/figures/figure-sheet-01.jpg": "figures/rendered/smwa_lda_topic_shares.png",
    },
    "coursework/ai_course/figures.md": {
        "figures/figure-sheet-01.jpg": "../../figures/rendered/ai_regional_vocabulary_summary.png",
        "figures/figure-sheet-02.jpg": "../../figures/rendered/ai_lda_topic_prevalence.png",
        "figures/figure-sheet-03.jpg": "../../figures/rendered/ai_kmeans_by_continent.png",
        "figures/figure-sheet-04.jpg": "../../figures/rendered/ai_lstm_confusion_matrix.png",
        "figures/figure-sheet-05.jpg": "../../figures/rendered/ai_sentiment_vocabulary_summary.png",
    },
    "coursework/social_media_web_analytics/figures.md": {
        "figures/figure-sheet-01.jpg": "../../figures/rendered/smwa_lda_topic_shares.png",
    },
}

for rel, mapping in replacements.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    for old, new in mapping.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")

# Verify every rendered file is a genuine PNG with useful dimensions.
paths = sorted(OUT.glob("*.png"))
if len(paths) != len(SVG_FILES):
    raise RuntimeError(f"Expected {len(SVG_FILES)} PNGs, found {len(paths)}")

for path in paths:
    with Image.open(path) as im:
        im.verify()
    with Image.open(path) as im:
        if im.width < 600 or im.height < 250:
            raise RuntimeError(f"Unexpectedly small rendered image: {path} {im.size}")

print(f"Generated and verified {len(paths)} PNG figures in {OUT}")
