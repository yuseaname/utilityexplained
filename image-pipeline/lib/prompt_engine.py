from __future__ import annotations

import hashlib
from typing import Any, Dict


PROMPT_VERSION = "v1"


def build_prompt(topic: str, market_injection: str | None = None) -> str:
    base = (
        "Photorealistic scene in a real environment, grounded in the topic:\n"
        f"{topic}\n\n"
        "Composition and realism rules:\n"
        "- Natural lighting, realistic perspective, and credible materials.\n"
        "- No text or typography in the scene.\n"
        "- No screens, UI, logos, or branding.\n"
        "- No ad-like or misleading button visuals.\n"
        "- Avoid centered symmetry; use organic framing.\n"
        "- Avoid repeated compositions across slots.\n\n"
        "Camera:\n"
        "- 35mm lens equivalent, shallow-to-moderate depth of field.\n"
        "- Horizontal framing unless the slot is explicitly vertical.\n"
    )
    if market_injection:
        return f"{base}\nMarket realism rules:\n{market_injection.strip()}\n"
    return base


def hash_prompt(prompt: str) -> str:
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()


def extract_topic(slot: Dict[str, Any]) -> str:
    anchor_text = slot.get("anchor_text", "").strip()
    page_path = slot.get("page_path", "")
    slot_key = slot.get("slot_key", "")
    parts = [p for p in [anchor_text, slot_key, page_path] if p]
    return " | ".join(parts)
