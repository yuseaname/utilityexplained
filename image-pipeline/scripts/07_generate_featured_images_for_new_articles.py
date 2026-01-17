from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
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
from lib.io_utils import load_json, load_yaml, write_csv, write_json  # noqa: E402
from lib.openai_images import OpenAIImageError, generate_image  # noqa: E402

PROMPTS_PATH = PIPELINE_ROOT / "prompts" / "articles" / "featured_prompts.json"
PROMPTS_CSV_PATH = PIPELINE_ROOT / "prompts" / "articles" / "featured_prompts.csv"
GENERATED_ROOT = PIPELINE_ROOT / "generated"
MANIFEST_PATH = GENERATED_ROOT / "featured-manifest.json"
LOGS_PATH = GENERATED_ROOT / "featured-logs.jsonl"
CONFIG_PATH = PIPELINE_ROOT / "config.yaml"

NEW_SOURCE_FILES = [
    REPO_ROOT / "lib" / "generatedPosts" / "utilityBillsPillarBillUpThisMonthPosts_2026_01_15.tsx",
    REPO_ROOT / "lib" / "generatedPosts" / "electricityPillarBillChangesPosts_2026_01_15.tsx",
    REPO_ROOT / "lib" / "generatedPosts" / "utilityBillsPillarRatesFeesUsageBridgePosts_2026_01_15.tsx",
]

PROMPT_VERSION = "featured-v1"


def _load_config() -> Dict:
    return load_yaml(CONFIG_PATH, default={}) or {}


def _load_prompts() -> Dict:
    return load_json(PROMPTS_PATH, default={"generated": False, "count": 0, "items": []})


def _load_manifest() -> Dict:
    return load_json(MANIFEST_PATH, default={"generated": False, "images": []})


def _hash_prompt(prompt: str) -> str:
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()


def _build_prompt(title: str, description: str) -> str:
    return (
        "Photorealistic scene in a real environment that represents the article topic:\n"
        f"{title} - {description}\n\n"
        "Composition and realism rules:\n"
        "- Natural lighting, realistic perspective, and credible materials.\n"
        "- No text or typography in the scene.\n"
        "- No screens, UI, logos, or branding.\n"
        "- No ad-like or misleading button visuals.\n"
        "- Avoid centered symmetry; use organic framing.\n"
        "- Avoid repeated compositions across articles.\n\n"
        "Camera:\n"
        "- 35mm lens equivalent, shallow-to-moderate depth of field.\n"
        "- Horizontal framing.\n"
    )


def _parse_posts(path: Path) -> List[Dict]:
    text = path.read_text(encoding="utf-8")
    post_re = re.compile(
        r"slug:\s*\"([^\"]+)\"[\s\S]*?"
        r"title:\s*\"((?:[^\"\\]|\\.)*)\"[\s\S]*?"
        r"description:\s*\"((?:[^\"\\]|\\.)*)\"[\s\S]*?"
        r"category:\s*\"([^\"]+)\"",
        re.MULTILINE,
    )

    def _unescape(value: str) -> str:
        try:
            return json.loads(f"\"{value}\"")
        except json.JSONDecodeError:
            return value

    posts = []
    for match in post_re.finditer(text):
        posts.append(
            {
                "slug": match.group(1),
                "title": _unescape(match.group(2)),
                "description": _unescape(match.group(3)),
                "category": match.group(4),
                "source": path.relative_to(REPO_ROOT).as_posix(),
            }
        )
    return posts


def _merge_prompts(existing: Dict, new_items: List[Dict], update_existing: bool) -> Dict:
    items = existing.get("items", [])
    by_slug = {item.get("slug"): item for item in items}
    added = 0

    for item in new_items:
        slug = item["slug"]
        prompt = _build_prompt(item["title"], item["description"])
        prompt_hash = _hash_prompt(prompt)
        payload = {
            "slug": slug,
            "title": item["title"],
            "description": item["description"],
            "category": item["category"],
            "prompt": prompt,
            "prompt_hash": prompt_hash,
            "prompt_version": PROMPT_VERSION,
            "source": item["source"],
        }
        if slug in by_slug and not update_existing:
            continue
        if slug in by_slug:
            by_slug[slug].update(payload)
        else:
            items.append(payload)
            added += 1

    items_sorted = sorted(items, key=lambda entry: entry.get("slug", ""))
    existing["items"] = items_sorted
    existing["count"] = len(items_sorted)
    existing["generated"] = True
    return {"data": existing, "added": added}


def _write_csv(items: List[Dict]) -> None:
    write_csv(
        PROMPTS_CSV_PATH,
        [
            "slug",
            "title",
            "category",
            "prompt_hash",
            "prompt_version",
            "source",
            "description",
            "prompt",
        ],
        [
            [
                item.get("slug"),
                item.get("title"),
                item.get("category"),
                item.get("prompt_hash"),
                item.get("prompt_version"),
                item.get("source"),
                item.get("description"),
                item.get("prompt"),
            ]
            for item in items
        ],
    )


def _should_skip(item: Dict, manifest: Dict, force: bool) -> bool:
    if force:
        return False
    for entry in manifest.get("images", []):
        if entry.get("slug") == item.get("slug") and entry.get("prompt_hash") == item.get("prompt_hash"):
            return True
    return False


def _generate_images(items: List[Dict], force: bool, dry_run: bool) -> int:
    config = _load_config()
    model = config.get("openai", {}).get("default_model", "gpt-image-1")
    quality = config.get("openai", {}).get("default_quality", "medium")
    size = config.get("openai", {}).get("default_size", "1536x1024")

    manifest = _load_manifest()
    selected = [item for item in items if not _should_skip(item, manifest, force)]

    if dry_run:
        print(f"[dry-run] would generate {len(selected)} featured image(s)")
        return len(selected)

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
    return len(selected)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--update-existing", action="store_true")
    parser.add_argument("--skip-generate", action="store_true")
    args = parser.parse_args()

    new_items = []
    for source in NEW_SOURCE_FILES:
        if not source.exists():
            raise SystemExit(f"Missing source file: {source}")
        new_items.extend(_parse_posts(source))

    if not new_items:
        raise SystemExit("No posts found in NEW_SOURCE_FILES")

    prompts = _load_prompts()
    merge_result = _merge_prompts(prompts, new_items, args.update_existing)
    merged = merge_result["data"]
    write_json(PROMPTS_PATH, merged)
    _write_csv(merged["items"])

    if args.skip_generate:
        print(f"Updated featured prompts ({merge_result['added']} new). Generation skipped.")
        return

    count = _generate_images(merged["items"], args.force, args.dry_run)
    print(f"Generated {count} featured image(s).")


if __name__ == "__main__":
    main()
