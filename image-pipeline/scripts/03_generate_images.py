from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from dotenv import load_dotenv

PIPELINE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PIPELINE_ROOT))

# Load .env from repo root
load_dotenv(REPO_ROOT / ".env")

from lib.image_postprocess import write_png_and_webp  # noqa: E402
from lib.io_utils import load_json, load_yaml, write_json  # noqa: E402
from lib.openai_images import OpenAIImageError, generate_image  # noqa: E402

CONFIG_PATH = PIPELINE_ROOT / "config.yaml"
PROMPTS_ROOT = PIPELINE_ROOT / "prompts" / "slots"
GENERATED_ROOT = PIPELINE_ROOT / "generated"
LEDGER_ROOT = PIPELINE_ROOT / "ledger"


def _load_config() -> Dict:
    return load_yaml(CONFIG_PATH, default={}) or {}


def _load_slots() -> List[Dict]:
    return load_json(PROMPTS_ROOT / "index.json", default={}).get("slots", [])


def _load_locked() -> List[str]:
    return load_json(LEDGER_ROOT / "locked_slots.json", default={}).get("locked_slot_ids", [])


def _load_manifest() -> Dict:
    return load_json(GENERATED_ROOT / "manifest.json", default={"generated": False, "images": []})


def _slot_key(slot: Dict) -> tuple:
    return (-int(slot.get("priority_level", 3)), slot.get("slot_id", ""))


def _should_skip(slot: Dict, manifest: Dict, locked: List[str], force: bool) -> bool:
    if slot.get("slot_id") in locked:
        return True
    if force:
        return False
    for entry in manifest.get("images", []):
        if entry.get("slot_id") == slot.get("slot_id") and entry.get("prompt_hash") == slot.get("prompt_hash"):
            return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-slots", type=int, default=None)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--debug-api", action="store_true")
    args = parser.parse_args()

    config = _load_config()
    slots = _load_slots()
    locked = _load_locked()
    manifest = _load_manifest()

    model = config.get("openai", {}).get("default_model", "gpt-image-1")
    quality = config.get("openai", {}).get("default_quality", "medium")
    size = config.get("openai", {}).get("default_size", "1536x1024")

    slots_sorted = sorted(slots, key=_slot_key)
    top_n = config.get("pipeline", {}).get("top_n", 20)
    limit = args.max_slots if args.max_slots is not None else top_n

    selected = []
    for slot in slots_sorted:
        if _should_skip(slot, manifest, locked, args.force):
            continue
        selected.append(slot)
        if len(selected) >= limit:
            break

    if args.dry_run:
        print(f"[dry-run] would generate {len(selected)} image(s)")
        return

    logs_path = GENERATED_ROOT / "logs.jsonl"
    images_out = manifest.get("images", [])

    for slot in selected:
        slot_id = slot["slot_id"]
        prompt = slot.get("prompt")
        if not prompt:
            raise RuntimeError(f"Missing prompt for slot {slot_id}")

        try:
            result = generate_image(prompt=prompt, model=model, size=size, quality=quality)
        except OpenAIImageError as exc:
            raise SystemExit(str(exc)) from exc

        slot_dir = GENERATED_ROOT / "images" / "slots" / slot_id
        png_path = slot_dir / "image.png"
        webp_path = slot_dir / "image.webp"
        dims = write_png_and_webp(result["bytes"], png_path, webp_path)

        meta = {
            "slot_id": slot_id,
            "prompt_hash": slot.get("prompt_hash"),
            "model": model,
            "quality": quality,
            "size": size,
            "width": dims["width"],
            "height": dims["height"],
            "generated_at": datetime.utcnow().isoformat() + "Z",
        }

        write_json(slot_dir / "meta.generated.json", meta)

        images_out.append(
            {
                "slot_id": slot_id,
                "prompt_hash": slot.get("prompt_hash"),
                "image_path_png": png_path.relative_to(PIPELINE_ROOT).as_posix(),
                "image_path_webp": webp_path.relative_to(PIPELINE_ROOT).as_posix(),
                "generated_at": meta["generated_at"],
                "model": model,
                "quality": quality,
                "size": size,
                "width": dims["width"],
                "height": dims["height"],
            }
        )

        with logs_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"event": "generated", "slot_id": slot_id, "meta": meta}) + "\n")

    manifest["generated"] = True
    manifest["images"] = images_out
    write_json(GENERATED_ROOT / "manifest.json", manifest)


if __name__ == "__main__":
    main()
