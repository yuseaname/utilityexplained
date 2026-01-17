from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict

PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT))

from lib.io_utils import load_json, load_yaml, write_csv, write_json  # noqa: E402
from lib.prompt_engine import PROMPT_VERSION, build_prompt, extract_topic, hash_prompt  # noqa: E402

CONFIG_PATH = PIPELINE_ROOT / "config.yaml"
PROFILE_PATH = PIPELINE_ROOT / "repo_profile.json"
PROMPTS_ROOT = PIPELINE_ROOT / "prompts" / "slots"


def _load_config() -> Dict:
    return load_yaml(CONFIG_PATH, default={}) or {}


def _load_profile() -> Dict:
    return load_json(PROFILE_PATH, default={}) or {}


def _market_injection(config: Dict, profile: Dict) -> Dict[str, str]:
    market = profile.get("market", {})
    if config.get("market", {}).get("mode") == "fixed":
        market = {
            "country": config.get("market", {}).get("country", ""),
            "locale": config.get("market", {}).get("locale", ""),
        }

    country = market.get("country") or ""
    locale = market.get("locale") or ""

    injection = ""
    if country and config.get("visual_localization", {}).get("enabled", True):
        rules = config.get("visual_localization", {}).get("rules_by_country", {}).get(country, {})
        injection = rules.get("injection", "")
    return {"country": country, "locale": locale, "injection": injection}


def main() -> None:
    config = _load_config()
    profile = _load_profile()
    slots_index = load_json(PROMPTS_ROOT / "index.json", default={})

    market = _market_injection(config, profile)

    slots = slots_index.get("slots", [])
    refined = []
    for slot in slots:
        slot_dir = PROMPTS_ROOT / slot["slot_id"]
        meta = load_json(slot_dir / "meta.json", default=slot) or slot
        topic = extract_topic(meta)
        prompt = build_prompt(topic, market_injection=market.get("injection"))
        prompt_hash = hash_prompt(prompt)

        meta.update(
            {
                "prompt": prompt,
                "prompt_hash": prompt_hash,
                "prompt_version": PROMPT_VERSION,
                "market": {"country": market.get("country", ""), "locale": market.get("locale", "")},
            }
        )

        write_json(slot_dir / "meta.json", meta)
        refined.append(meta)

    write_json(PROMPTS_ROOT / "index.json", {"generated": True, "slots": refined})

    write_csv(
        PROMPTS_ROOT / "index.csv",
        [
            "slot_id",
            "page_path",
            "anchor_text",
            "anchor_selector",
            "anchor_index",
            "insertion_mode",
            "slot_key",
            "priority_level",
            "risk_score",
            "prompt_hash",
        ],
        [
            [
                slot["slot_id"],
                slot.get("page_path", ""),
                slot.get("anchor_text", ""),
                slot.get("anchor_selector", ""),
                slot.get("anchor_index", 0),
                slot.get("insertion_mode", ""),
                slot.get("slot_key", ""),
                slot.get("priority_level", 3),
                slot.get("risk_score", 0.0),
                slot.get("prompt_hash", ""),
            ]
            for slot in refined
        ],
    )


if __name__ == "__main__":
    main()
