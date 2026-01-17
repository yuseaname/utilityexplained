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
PROMPTS_PATH = PIPELINE_ROOT / "prompts" / "articles" / "featured_prompts.json"
GENERATED_ROOT = PIPELINE_ROOT / "generated"
MANIFEST_PATH = GENERATED_ROOT / "featured-manifest.json"
LOGS_PATH = GENERATED_ROOT / "featured-logs.jsonl"


def _load_config() -> Dict:
    return load_yaml(CONFIG_PATH, default={}) or {}


def _load_prompts() -> List[Dict]:
    data = load_json(PROMPTS_PATH, default={}) or {}
    return data.get("items", [])


def _load_manifest() -> Dict:
    return load_json(MANIFEST_PATH, default={"generated": False, "images": []})


def _should_skip(item: Dict, manifest: Dict, force: bool) -> bool:
    if force:
        return False
    for entry in manifest.get("images", []):
        if entry.get("slug") == item.get("slug") and entry.get("prompt_hash") == item.get("prompt_hash"):
            return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-items", type=int, default=None)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    config = _load_config()
    prompts = sorted(_load_prompts(), key=lambda item: item.get("slug", ""))
    manifest = _load_manifest()

    model = config.get("openai", {}).get("default_model", "gpt-image-1")
    quality = config.get("openai", {}).get("default_quality", "medium")
    size = config.get("openai", {}).get("default_size", "1536x1024")

    limit = args.max_items if args.max_items is not None else len(prompts)

    selected = []
    for item in prompts:
        if _should_skip(item, manifest, args.force):
            continue
        selected.append(item)
        if len(selected) >= limit:
            break

    if args.dry_run:
        print(f"[dry-run] would generate {len(selected)} featured image(s)")
        return

    images_out = manifest.get("images", [])

    for item in selected:
        slug = item["slug"]
        prompt = item.get("prompt")
        if not prompt:
            raise RuntimeError(f"Missing prompt for slug {slug}")

        try:
            result = generate_image(prompt=prompt, model=model, size=size, quality=quality)
        except OpenAIImageError as exc:
            raise SystemExit(str(exc)) from exc

        out_dir = GENERATED_ROOT / "articles" / slug
        png_path = out_dir / "image.png"
        webp_path = out_dir / "image.webp"
        dims = write_png_and_webp(result["bytes"], png_path, webp_path)

        meta = {
            "slug": slug,
            "prompt_hash": item.get("prompt_hash"),
            "model": model,
            "quality": quality,
            "size": size,
            "width": dims["width"],
            "height": dims["height"],
            "generated_at": datetime.utcnow().isoformat() + "Z",
        }

        write_json(out_dir / "meta.generated.json", meta)

        images_out.append(
            {
                "slug": slug,
                "title": item.get("title"),
                "category": item.get("category"),
                "prompt_hash": item.get("prompt_hash"),
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

        with LOGS_PATH.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"event": "featured_generated", "slug": slug, "meta": meta}) + "\n")

    manifest["generated"] = True
    manifest["images"] = images_out
    write_json(MANIFEST_PATH, manifest)


if __name__ == "__main__":
    main()
