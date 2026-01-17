from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path
from typing import Dict

PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT))

from lib.io_utils import load_json, write_csv, write_json, write_text  # noqa: E402

GENERATED_ROOT = PIPELINE_ROOT / "generated"
LEDGER_ROOT = PIPELINE_ROOT / "ledger"


def _load_manifest() -> Dict:
    return load_json(GENERATED_ROOT / "manifest.json", default={"generated": False, "images": []})


def main() -> None:
    manifest = _load_manifest()
    entries = []
    for image in manifest.get("images", []):
        entries.append(
            {
                "slot_id": image.get("slot_id"),
                "prompt_hash": image.get("prompt_hash"),
                "image_path_png": image.get("image_path_png"),
                "image_path_webp": image.get("image_path_webp"),
                "generated_at": image.get("generated_at"),
                "model": image.get("model"),
                "quality": image.get("quality"),
                "size": image.get("size"),
                "width": image.get("width"),
                "height": image.get("height"),
            }
        )

    write_json(LEDGER_ROOT / "ledger.json", {"generated": True, "entries": entries})

    write_csv(
        LEDGER_ROOT / "ledger.csv",
        [
            "slot_id",
            "prompt_hash",
            "image_path_png",
            "image_path_webp",
            "generated_at",
            "model",
            "quality",
            "size",
            "width",
            "height",
        ],
        [
            [
                entry.get("slot_id"),
                entry.get("prompt_hash"),
                entry.get("image_path_png"),
                entry.get("image_path_webp"),
                entry.get("generated_at"),
                entry.get("model"),
                entry.get("quality"),
                entry.get("size"),
                entry.get("width"),
                entry.get("height"),
            ]
            for entry in entries
        ],
    )

    summary = {
        "generated": True,
        "total_entries": len(entries),
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    write_json(LEDGER_ROOT / "summary.json", summary)

    lines = ["# Image Ledger", "", f"Total entries: {len(entries)}"]
    write_text(LEDGER_ROOT / "LEDGER.md", "\n".join(lines))


if __name__ == "__main__":
    main()
