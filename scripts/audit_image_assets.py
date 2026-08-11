from __future__ import annotations

import base64
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = [
    ROOT / "README.md",
    ROOT / "coursework/ai_course/figures.md",
    ROOT / "coursework/social_media_web_analytics/figures.md",
    ROOT / "figures/professional/README.md",
]

IMAGE_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+\.(?:png|jpe?g|webp|svg))\)|<img[^>]+src=[\"']([^\"']+\.(?:png|jpe?g|webp|svg))[\"']", re.I)


def valid_bytes(path: Path, data: bytes) -> bool:
    ext = path.suffix.lower()
    if ext == ".png":
        return data.startswith(b"\x89PNG\r\n\x1a\n")
    if ext in {".jpg", ".jpeg"}:
        return data.startswith(b"\xff\xd8\xff")
    if ext == ".webp":
        return len(data) >= 12 and data[:4] == b"RIFF" and data[8:12] == b"WEBP"
    if ext == ".svg":
        text = data[:4096].decode("utf-8", errors="ignore").lower()
        return "<svg" in text
    return False


def base64_image(path: Path, data: bytes) -> bool:
    try:
        stripped = b"".join(data.split())
        decoded = base64.b64decode(stripped, validate=True)
    except Exception:
        return False
    return valid_bytes(path, decoded)


def refs_from(doc: Path) -> list[str]:
    if not doc.exists():
        return []
    text = doc.read_text(encoding="utf-8")
    refs: list[str] = []
    for m in IMAGE_RE.finditer(text):
        ref = m.group(1) or m.group(2)
        if ref and not re.match(r"^[a-z]+://", ref, re.I):
            refs.append(ref.split("#", 1)[0])
    return refs


def main() -> int:
    failures = 0
    seen: set[Path] = set()
    for doc in DOCS:
        for ref in refs_from(doc):
            target = (doc.parent / ref).resolve()
            if target in seen:
                continue
            seen.add(target)
            rel = target.relative_to(ROOT) if ROOT in target.parents else target
            if not target.exists():
                print(f"MISSING  {rel}")
                failures += 1
                continue
            data = target.read_bytes()
            if valid_bytes(target, data):
                print(f"OK       {rel} ({len(data):,} bytes)")
            elif base64_image(target, data):
                print(f"BASE64   {rel} ({len(data):,} bytes) — image bytes were stored as text")
                failures += 1
            else:
                print(f"INVALID  {rel} ({len(data):,} bytes)")
                failures += 1
    print(f"\nAudited {len(seen)} referenced image assets; failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
