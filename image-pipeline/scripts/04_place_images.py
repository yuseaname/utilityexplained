from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT))

from lib.html_tools import find_heading, insert_after, parse_html, render_img_tag  # noqa: E402
from lib.io_utils import load_json, load_yaml, write_json, write_text  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PIPELINE_ROOT / "config.yaml"
PROMPTS_ROOT = PIPELINE_ROOT / "prompts" / "slots"
GENERATED_ROOT = PIPELINE_ROOT / "generated"
BACKUPS_ROOT = PIPELINE_ROOT / "backups"


def _load_config() -> Dict:
    return load_yaml(CONFIG_PATH, default={}) or {}


def _load_slots() -> List[Dict]:
    return load_json(PROMPTS_ROOT / "index.json", default={}).get("slots", [])


def _load_manifest() -> Dict:
    return load_json(GENERATED_ROOT / "manifest.json", default={"generated": False, "images": []})


def _build_plan(slots: List[Dict], manifest: Dict) -> List[Dict]:
    images = {img["slot_id"]: img for img in manifest.get("images", [])}
    plan = []
    for slot in slots:
        image = images.get(slot["slot_id"])
        if not image:
            continue
        plan.append(
            {
                "slot_id": slot["slot_id"],
                "page_path": slot.get("page_path"),
                "insertion_mode": slot.get("insertion_mode"),
                "anchor_selector": slot.get("anchor_selector"),
                "anchor_index": slot.get("anchor_index"),
                "anchor_text": slot.get("anchor_text", ""),
                "image_path_webp": image.get("image_path_webp"),
                "width": image.get("width"),
                "height": image.get("height"),
            }
        )
    return plan


def _write_plan_md(plan: List[Dict]) -> None:
    lines = ["# Placement Plan", ""]
    lines.append(f"Total placements: {len(plan)}")
    lines.append("")
    for entry in plan:
        lines.append(f"- {entry['slot_id']} | {entry['page_path']} | {entry['insertion_mode']}")
    write_text(GENERATED_ROOT / "PLACEMENT_PLAN.md", "\n".join(lines))


def _safe_to_apply(path: Path, config: Dict) -> bool:
    if not config.get("placement", {}).get("html_apply_enabled", True):
        return False
    if path.suffix.lower() != ".html":
        return False
    return True


def _already_has_slot(html_text: str, slot_id: str) -> bool:
    return f"data-slot-id=\"{slot_id}\"" in html_text


def _apply_to_html(plan_entry: Dict, config: Dict) -> Dict:
    page_path = plan_entry["page_path"]
    file_path = REPO_ROOT / page_path
    if not file_path.exists():
        return {"slot_id": plan_entry["slot_id"], "status": "missing"}

    html_text = file_path.read_text(encoding="utf-8", errors="ignore")
    if _already_has_slot(html_text, plan_entry["slot_id"]):
        return {"slot_id": plan_entry["slot_id"], "status": "already_present"}

    soup = parse_html(html_text)
    tag_name = "h1" if plan_entry["insertion_mode"] == "HERO" else "h2"
    found, heading = find_heading(soup, tag_name, int(plan_entry["anchor_index"]))
    if not found:
        return {"slot_id": plan_entry["slot_id"], "status": "anchor_missing"}

    ad_markers = config.get("adsense_safety", {}).get("ad_marker_patterns", [])
    container_text = " ".join(
        filter(
            None,
            [
                getattr(heading.parent, "get", lambda *_: "")("id"),
                " ".join(getattr(heading.parent, "get", lambda *_: [])("class") or []),
            ],
        )
    ).lower()
    if any(marker in container_text for marker in ad_markers):
        return {"slot_id": plan_entry["slot_id"], "status": "skipped_ad_container"}

    img_tag = render_img_tag(
        src="/" + plan_entry["image_path_webp"],
        alt=plan_entry.get("anchor_text", ""),
        width=int(plan_entry.get("width") or 1536),
        height=int(plan_entry.get("height") or 1024),
        slot_id=plan_entry["slot_id"],
        eager=plan_entry["insertion_mode"] == "HERO",
    )

    insert_after(heading, img_tag)

    BACKUPS_ROOT.mkdir(parents=True, exist_ok=True)
    backup_path = BACKUPS_ROOT / page_path
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    if not backup_path.exists():
        backup_path.write_text(html_text, encoding="utf-8")

    file_path.write_text(str(soup), encoding="utf-8")
    return {"slot_id": plan_entry["slot_id"], "status": "applied"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    config = _load_config()
    slots = _load_slots()
    manifest = _load_manifest()

    plan = _build_plan(slots, manifest)
    _write_plan_md(plan)
    write_json(GENERATED_ROOT / "placement-report.json", {"generated": True, "placements": plan})

    if not args.apply:
        return

    results = []
    for entry in plan:
        path = REPO_ROOT / entry["page_path"]
        if not _safe_to_apply(path, config):
            results.append({"slot_id": entry["slot_id"], "status": "skipped"})
            continue
        results.append(_apply_to_html(entry, config))

    with (GENERATED_ROOT / "logs.jsonl").open("a", encoding="utf-8") as handle:
        for result in results:
            handle.write(json.dumps({"event": "placement", **result}) + "\n")


if __name__ == "__main__":
    main()
