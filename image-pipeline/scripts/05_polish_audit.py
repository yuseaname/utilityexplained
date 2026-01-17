from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT))

from lib.io_utils import load_json, write_text  # noqa: E402

PROMPTS_ROOT = PIPELINE_ROOT / "prompts" / "slots"
GENERATED_ROOT = PIPELINE_ROOT / "generated"
PROFILE_PATH = PIPELINE_ROOT / "repo_profile.json"


def _load_slots() -> List[Dict]:
    return load_json(PROMPTS_ROOT / "index.json", default={}).get("slots", [])


def _load_manifest() -> Dict:
    return load_json(GENERATED_ROOT / "manifest.json", default={"generated": False, "images": []})


def _load_profile() -> Dict:
    return load_json(PROFILE_PATH, default={})


def _audit_prompts(slots: List[Dict]) -> List[str]:
    findings = []
    for slot in slots:
        prompt = slot.get("prompt", "")
        if not prompt:
            findings.append(f"missing prompt: {slot.get('slot_id')}")
            continue
        if "No text" not in prompt and "No text" not in prompt.replace("-", ""):
            findings.append(f"prompt missing no-text rule: {slot.get('slot_id')}")
        if "logo" in prompt.lower() or "branding" in prompt.lower():
            findings.append(f"prompt mentions logo/branding: {slot.get('slot_id')}")
        if "screen" in prompt.lower() or "ui" in prompt.lower():
            findings.append(f"prompt mentions screen/ui: {slot.get('slot_id')}")
    return findings


def _audit_manifest(manifest: Dict) -> List[str]:
    findings = []
    for image in manifest.get("images", []):
        if not image.get("width") or not image.get("height"):
            findings.append(f"missing dimensions: {image.get('slot_id')}")
        if not image.get("image_path_webp"):
            findings.append(f"missing webp: {image.get('slot_id')}")
    return findings


def _audit_market(slots: List[Dict], profile: Dict) -> List[str]:
    findings = []
    market = profile.get("market", {})
    country = market.get("country")
    if country:
        for slot in slots:
            prompt = slot.get("prompt", "")
            if "Market realism rules" not in prompt:
                findings.append(f"market injection missing: {slot.get('slot_id')}")
    return findings


def main() -> None:
    slots = _load_slots()
    manifest = _load_manifest()
    profile = _load_profile()

    findings = []
    findings.extend(_audit_prompts(slots))
    findings.extend(_audit_manifest(manifest))
    findings.extend(_audit_market(slots, profile))

    lines = ["# Audit Report", ""]
    if not findings:
        lines.append("No issues found.")
    else:
        lines.append("Findings:")
        for item in findings:
            lines.append(f"- {item}")

    write_text(GENERATED_ROOT / "AUDIT_REPORT.md", "\n".join(lines))


if __name__ == "__main__":
    main()
