from __future__ import annotations

from pathlib import Path
from typing import Dict

from PIL import Image

from .io_utils import ensure_dir


def write_png_and_webp(image_bytes: bytes, png_path: Path, webp_path: Path) -> Dict[str, int]:
    ensure_dir(png_path.parent)
    png_path.write_bytes(image_bytes)

    with Image.open(png_path) as img:
        width, height = img.size
        ensure_dir(webp_path.parent)
        img.save(webp_path, format="WEBP", quality=90, method=6)

    return {"width": width, "height": height}
