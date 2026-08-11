from __future__ import annotations

from pathlib import Path

from PIL import Image
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures" / "rendered"
OUT.mkdir(parents=True, exist_ok=True)

# Professional SVG figures used on the README/galleries.
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
    cairosvg.svg2png(url=str(src), write_to=str(dst), output_width=1400)

# Original coursework sheets: convert to PNG so the README does not depend
# on the older binary/JPEG rendering path.
for i in range(1, 6):
    src = ROOT / "coursework" / "ai_course" / "figures" / f"figure-sheet-{i:02d}.jpg"
    dst = OUT / f"ai_course_sheet_{i:02d}.png"
    if not src.exists():
        raise FileNotFoundError(src)
    with Image.open(src) as im:
        im.convert("RGB").save(dst, format="PNG", optimize=True)

src = ROOT / "coursework" / "social_media_web_analytics" / "figures" / "figure-sheet-01.jpg"
dst = OUT / "smwa_sheet_01.png"
if not src.exists():
    raise FileNotFoundError(src)
with Image.open(src) as im:
    im.convert("RGB").save(dst, format="PNG", optimize=True)

# Replace README/gallery references with the PNG fallbacks using standard
# Markdown-friendly relative paths.
replacements = {
    "README.md": {
        "figures/professional/": "figures/rendered/",
        ".svg\"": ".png\"",
        "coursework/ai_course/figures/figure-sheet-01.jpg": "figures/rendered/ai_course_sheet_01.png",
        "coursework/ai_course/figures/figure-sheet-02.jpg": "figures/rendered/ai_course_sheet_02.png",
        "coursework/ai_course/figures/figure-sheet-03.jpg": "figures/rendered/ai_course_sheet_03.png",
        "coursework/ai_course/figures/figure-sheet-04.jpg": "figures/rendered/ai_course_sheet_04.png",
        "coursework/ai_course/figures/figure-sheet-05.jpg": "figures/rendered/ai_course_sheet_05.png",
        "coursework/social_media_web_analytics/figures/figure-sheet-01.jpg": "figures/rendered/smwa_sheet_01.png",
    },
    "coursework/ai_course/figures.md": {
        "figures/figure-sheet-01.jpg": "../../figures/rendered/ai_course_sheet_01.png",
        "figures/figure-sheet-02.jpg": "../../figures/rendered/ai_course_sheet_02.png",
        "figures/figure-sheet-03.jpg": "../../figures/rendered/ai_course_sheet_03.png",
        "figures/figure-sheet-04.jpg": "../../figures/rendered/ai_course_sheet_04.png",
        "figures/figure-sheet-05.jpg": "../../figures/rendered/ai_course_sheet_05.png",
        "../../figures/professional/": "../../figures/rendered/",
        ".svg)": ".png)",
    },
    "coursework/social_media_web_analytics/figures.md": {
        "figures/figure-sheet-01.jpg": "../../figures/rendered/smwa_sheet_01.png",
        "../../figures/professional/": "../../figures/rendered/",
        ".svg)": ".png)",
    },
}

for rel, mapping in replacements.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    for old, new in mapping.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")

# Verify every rendered file is a valid PNG with non-trivial dimensions.
for path in sorted(OUT.glob("*.png")):
    with Image.open(path) as im:
        im.verify()
    with Image.open(path) as im:
        if im.width < 300 or im.height < 150:
            raise RuntimeError(f"Unexpectedly small rendered image: {path} {im.size}")

print(f"Generated and verified {len(list(OUT.glob('*.png')))} PNG fallbacks in {OUT}")
