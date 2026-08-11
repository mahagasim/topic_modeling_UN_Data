from __future__ import annotations

import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RASTER = {'.png', '.jpg', '.jpeg', '.webp'}


def is_valid(path: Path, data: bytes) -> bool:
    ext = path.suffix.lower()
    if ext == '.png':
        return data.startswith(b'\x89PNG\r\n\x1a\n')
    if ext in {'.jpg', '.jpeg'}:
        return data.startswith(b'\xff\xd8\xff')
    if ext == '.webp':
        return len(data) >= 12 and data[:4] == b'RIFF' and data[8:12] == b'WEBP'
    return False


def decode_layer(data: bytes) -> bytes | None:
    try:
        text = data.decode('ascii').strip()
    except UnicodeDecodeError:
        return None
    # tolerate wrappers accidentally written by debug/export code
    if (text.startswith("b'") and text.endswith("'")) or (text.startswith('b"') and text.endswith('"')):
        text = text[2:-1]
    try:
        return base64.b64decode(''.join(text.split()), validate=True)
    except Exception:
        return None


def main() -> int:
    repaired = 0
    invalid = 0
    for path in ROOT.rglob('*'):
        if not path.is_file() or path.suffix.lower() not in RASTER or '.git' in path.parts:
            continue
        original = path.read_bytes()
        if is_valid(path, original):
            continue
        candidate = original
        fixed = None
        for _ in range(3):
            candidate = decode_layer(candidate)
            if candidate is None:
                break
            if is_valid(path, candidate):
                fixed = candidate
                break
        if fixed is not None:
            path.write_bytes(fixed)
            repaired += 1
            print(f'REPAIRED {path.relative_to(ROOT)}: {len(original):,} -> {len(fixed):,} bytes')
        else:
            invalid += 1
            print(f'UNRESOLVED {path.relative_to(ROOT)}')
    print(f'Image repair complete: repaired={repaired}, unresolved={invalid}')
    return 1 if invalid else 0


if __name__ == '__main__':
    raise SystemExit(main())
