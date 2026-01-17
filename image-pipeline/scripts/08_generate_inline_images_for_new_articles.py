from __future__ import annotations

import argparse
import hashlib
import json
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

PROMPTS_PATH = PIPELINE_ROOT / "prompts" / "articles" / "inline_prompts.json"
PROMPTS_CSV_PATH = PIPELINE_ROOT / "prompts" / "articles" / "inline_prompts.csv"
GENERATED_ROOT = PIPELINE_ROOT / "generated"
MANIFEST_PATH = GENERATED_ROOT / "inline-manifest.json"
LOGS_PATH = GENERATED_ROOT / "inline-logs.jsonl"
CONFIG_PATH = PIPELINE_ROOT / "config.yaml"

PROMPT_VERSION = "inline-v1"

INLINE_ITEMS = [
    {
        "slug": "why-did-my-utility-bill-go-up-this-month",
        "title": "Why Did My Utility Bill Go Up This Month? (Even Without Using More)",
        "category": "Budgeting",
        "source": "lib/generatedPosts/utilityBillsPillarBillUpThisMonthPosts_2026_01_15.tsx",
        "images": [
            {
                "image_key": "three-buckets-diagram",
                "placement": "after H2: The three buckets that change your total",
                "purpose": "Orient the reader to the bill structure",
                "image_type": "diagram",
                "alt_text": "Diagram showing a bill total built from usage, rate, and fixed fees",
                "prompt": (
                    "Minimal editorial vector diagram showing three stacked layers with simple icons "
                    "(usage, rate, fixed fees), clean white background, muted palette, no text, no logos, "
                    "horizontal framing."
                ),
            },
            {
                "image_key": "billing-days-chart",
                "placement": "after H2: The billing days trap (28 days vs 33 days)",
                "purpose": "Show how a longer billing period raises totals",
                "image_type": "chart",
                "alt_text": "Chart comparing a shorter and longer billing period",
                "prompt": (
                    "Minimal bar chart with two bars of different heights representing shorter and longer "
                    "billing periods, neutral colors, light gridlines, no text, no numbers, horizontal framing."
                ),
            },
            {
                "image_key": "estimated-correction-diagram",
                "placement": "after H2: Estimated reads and catch-up bills",
                "purpose": "Explain estimated then corrected bills",
                "image_type": "diagram",
                "alt_text": "Diagram showing an estimated bill followed by a correction bill",
                "prompt": (
                    "Simple vector diagram of two monthly bill stacks side by side with a dotted arrow from "
                    "the first to the second, subtle calendar icon, no text, no logos, horizontal framing."
                ),
            },
            {
                "image_key": "self-check-photo",
                "placement": "after H2: A quick self-check you can do in 5 minutes",
                "purpose": "Ground the checklist in a real-life scene",
                "image_type": "photo",
                "alt_text": "Person reviewing a utility bill with a highlighter",
                "prompt": (
                    "Photorealistic scene of a person at a kitchen table reviewing a utility bill with a "
                    "highlighter and calculator, warm natural light, no readable text, no logos, horizontal framing."
                ),
            },
        ],
    },
    {
        "slug": "why-electric-bill-changes-month-to-month",
        "title": "Why Your Electric Bill Changes Month to Month (Even With Similar Usage)",
        "category": "Electricity",
        "source": "lib/generatedPosts/electricityPillarBillChangesPosts_2026_01_15.tsx",
        "images": [
            {
                "image_key": "tou-tier-diagram",
                "placement": "after H2: Price changes hidden in plain sight",
                "purpose": "Show time windows and tiers",
                "image_type": "diagram",
                "alt_text": "Diagram showing time-based and tiered electricity pricing",
                "prompt": (
                    "Editorial vector diagram combining a clock icon with tiered blocks ascending in steps, "
                    "muted palette, clean white background, no text, no logos, horizontal framing."
                ),
            },
            {
                "image_key": "demand-peak-chart",
                "placement": "after H2: Demand charges: the spike you did not feel",
                "purpose": "Highlight a single peak driving the charge",
                "image_type": "chart",
                "alt_text": "Chart showing a single peak that drives a demand charge",
                "prompt": (
                    "Minimal line graph with one sharp peak highlighted in a contrasting color, subtle grid, "
                    "no text, no numbers, horizontal framing."
                ),
            },
            {
                "image_key": "delivery-supply-split",
                "placement": "after H2: Delivery vs supply: two moving parts",
                "purpose": "Split the bill into two parts",
                "image_type": "diagram",
                "alt_text": "Diagram splitting an electric bill into delivery and supply parts",
                "prompt": (
                    "Simple split-bill illustration with two shaded halves and generic utility icons, clean vector "
                    "style, no text, no logos, horizontal framing."
                ),
            },
            {
                "image_key": "billing-window-calendar",
                "placement": "after H2: Meter read timing and estimated reads",
                "purpose": "Show timing effect of read windows",
                "image_type": "diagram",
                "alt_text": "Illustration showing a billing window on a calendar",
                "prompt": (
                    "Clean vector illustration of a calendar page with a highlighted billing window and a bill icon, "
                    "no text, no logos, horizontal framing."
                ),
            },
        ],
    },
    {
        "slug": "how-utility-rates-fees-usage-work-together",
        "title": "How Utility Rates, Fees, and Usage Work Together on Your Bill",
        "category": "Budgeting",
        "source": "lib/generatedPosts/utilityBillsPillarRatesFeesUsageBridgePosts_2026_01_15.tsx",
        "images": [
            {
                "image_key": "layered-model-diagram",
                "placement": "after H2: Think in layers: usage times rate, plus fixed charges",
                "purpose": "Explain the layered model",
                "image_type": "diagram",
                "alt_text": "Layered model of usage, rate, and fixed charges",
                "prompt": (
                    "Layered stack diagram with three translucent sheets and small utility icons, clean editorial "
                    "vector style, no text, no logos, horizontal framing."
                ),
            },
            {
                "image_key": "rate-shapes-chart",
                "placement": "after H2: Rates: the price per unit (and why it changes)",
                "purpose": "Compare flat, tiered, and time-based shapes",
                "image_type": "chart",
                "alt_text": "Visual comparison of flat, tiered, and time-of-use rate shapes",
                "prompt": (
                    "Three small charts side by side showing a flat line, stepped tiers, and time-based waves, "
                    "minimal vector style, no text, no numbers, horizontal framing."
                ),
            },
            {
                "image_key": "fixed-vs-variable-diagram",
                "placement": "after H2: Fees: the parts that do not depend on usage",
                "purpose": "Contrast fixed and variable charges",
                "image_type": "diagram",
                "alt_text": "Diagram comparing fixed charges and usage-based charges",
                "prompt": (
                    "Two-column balance illustration with a fixed block on one side and a variable block on the other, "
                    "neutral colors, clean vector style, no text, no logos, horizontal framing."
                ),
            },
            {
                "image_key": "ripple-total-illustration",
                "placement": "after H2: How one change ripples through the total",
                "purpose": "Show a small change creating a larger total",
                "image_type": "diagram",
                "alt_text": "Illustration showing a small rate change causing a bigger total change",
                "prompt": (
                    "Minimal illustration of a small slider moving upward with a larger total bar rising, clean vector "
                    "style, no text, no logos, horizontal framing."
                ),
            },
        ],
    },
]


def _load_config() -> Dict:
    return load_yaml(CONFIG_PATH, default={}) or {}


def _load_prompts() -> Dict:
    return load_json(PROMPTS_PATH, default={"generated": False, "count": 0, "items": []})


def _load_manifest() -> Dict:
    return load_json(MANIFEST_PATH, default={"generated": False, "images": []})


def _hash_prompt(prompt: str) -> str:
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()


def _flatten_items() -> List[Dict]:
    flattened = []
    for entry in INLINE_ITEMS:
        for image in entry["images"]:
            prompt = image["prompt"]
            flattened.append(
                {
                    "slug": entry["slug"],
                    "title": entry["title"],
                    "category": entry["category"],
                    "source": entry["source"],
                    "image_key": image["image_key"],
                    "placement": image["placement"],
                    "purpose": image["purpose"],
                    "image_type": image["image_type"],
                    "alt_text": image["alt_text"],
                    "prompt": prompt,
                    "prompt_hash": _hash_prompt(prompt),
                    "prompt_version": PROMPT_VERSION,
                }
            )
    return flattened


def _merge_prompts(existing: Dict, new_items: List[Dict], update_existing: bool) -> Dict:
    items = existing.get("items", [])
    by_key = {(item.get("slug"), item.get("image_key")): item for item in items}
    added = 0

    for item in new_items:
        key = (item.get("slug"), item.get("image_key"))
        if key in by_key and not update_existing:
            continue
        if key in by_key:
            by_key[key].update(item)
        else:
            items.append(item)
            added += 1

    items_sorted = sorted(items, key=lambda entry: (entry.get("slug", ""), entry.get("image_key", "")))
    existing["items"] = items_sorted
    existing["count"] = len(items_sorted)
    existing["generated"] = True
    return {"data": existing, "added": added}


def _write_csv(items: List[Dict]) -> None:
    write_csv(
        PROMPTS_CSV_PATH,
        [
            "slug",
            "image_key",
            "title",
            "category",
            "placement",
            "purpose",
            "image_type",
            "alt_text",
            "prompt_hash",
            "prompt_version",
            "source",
            "prompt",
        ],
        [
            [
                item.get("slug"),
                item.get("image_key"),
                item.get("title"),
                item.get("category"),
                item.get("placement"),
                item.get("purpose"),
                item.get("image_type"),
                item.get("alt_text"),
                item.get("prompt_hash"),
                item.get("prompt_version"),
                item.get("source"),
                item.get("prompt"),
            ]
            for item in items
        ],
    )


def _should_skip(item: Dict, manifest: Dict, force: bool) -> bool:
    if force:
        return False
    for entry in manifest.get("images", []):
        if (
            entry.get("slug") == item.get("slug")
            and entry.get("image_key") == item.get("image_key")
            and entry.get("prompt_hash") == item.get("prompt_hash")
        ):
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
        print(f"[dry-run] would generate {len(selected)} inline image(s)")
        return len(selected)

    images_out = manifest.get("images", [])

    for item in selected:
        slug = item["slug"]
        image_key = item["image_key"]
        prompt = item.get("prompt")
        if not prompt:
            raise RuntimeError(f"Missing prompt for slug {slug} image {image_key}")

        try:
            result = generate_image(prompt=prompt, model=model, size=size, quality=quality)
        except OpenAIImageError as exc:
            raise SystemExit(str(exc)) from exc

        out_dir = GENERATED_ROOT / "articles" / slug / "inline" / image_key
        png_path = out_dir / "image.png"
        webp_path = out_dir / "image.webp"
        dims = write_png_and_webp(result["bytes"], png_path, webp_path)

        meta = {
            "slug": slug,
            "image_key": image_key,
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
                "image_key": image_key,
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
            handle.write(
                json.dumps(
                    {
                        "event": "inline_generated",
                        "slug": slug,
                        "image_key": image_key,
                        "meta": meta,
                    }
                )
                + "\n"
            )

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

    new_items = _flatten_items()
    if not new_items:
        raise SystemExit("No inline image items defined")

    prompts = _load_prompts()
    merge_result = _merge_prompts(prompts, new_items, args.update_existing)
    merged = merge_result["data"]
    write_json(PROMPTS_PATH, merged)
    _write_csv(merged["items"])

    if args.skip_generate:
        print(f"Updated inline prompts ({merge_result['added']} new). Generation skipped.")
        return

    count = _generate_images(new_items, args.force, args.dry_run)
    print(f"Generated {count} inline image(s).")


if __name__ == "__main__":
    main()
