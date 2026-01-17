from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, List

from bs4 import BeautifulSoup

PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT))

from lib.io_utils import load_json, load_yaml, write_csv, write_json  # noqa: E402
from lib.markdown_tools import estimate_word_count, extract_headings  # noqa: E402
from lib.slot_discovery import compute_slot_id, normalize_path, slugify  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PIPELINE_ROOT / "config.yaml"
PROFILE_PATH = PIPELINE_ROOT / "repo_profile.json"
PROMPTS_ROOT = PIPELINE_ROOT / "prompts" / "slots"


def _load_config() -> Dict:
    return load_yaml(CONFIG_PATH, default={}) or {}


def _load_profile() -> Dict:
    return load_json(PROFILE_PATH, default={}) or {}


def _collect_pages(content_roots: List[str], exclude_dirs: List[str]) -> List[Path]:
    pages = []
    roots = [REPO_ROOT / root for root in content_roots] if content_roots else [REPO_ROOT]
    for root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            if any(part in exclude_dirs for part in path.parts):
                continue
            if path.suffix.lower() in {".md", ".mdx", ".html", ".tsx", ".jsx"}:
                pages.append(path)
    return pages


def _is_excluded(path_str: str, exclusions: Dict) -> bool:
    patterns = exclusions.get("exclude_page_path_patterns", [])
    for pattern in patterns:
        if pattern.lower() in path_str.lower():
            return True
    return False


def _heading_excluded(text: str, exclusions: Dict) -> bool:
    patterns = exclusions.get("exclude_page_heading_patterns", [])
    for pattern in patterns:
        if pattern.lower() in text.lower():
            return True
    return False


def _risk_score(text: str, ad_markers: List[str]) -> Dict[str, List[str] | float]:
    factors = []
    lower = text.lower()
    for marker in ad_markers:
        if marker in lower:
            factors.append(f"ad_marker:{marker}")
    score = min(1.0, 0.2 * len(factors))
    return {"score": score, "factors": factors}


def _extract_html_headings(html: str) -> List[str]:
    soup = BeautifulSoup(html, "lxml")
    headings = []
    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if text:
            headings.append(text)
    return headings


def _extract_jsx_headings(tsx_content: str) -> List[str]:
    """Extract heading text from JSX/TSX <h1>, <h2>, <h3> tags."""
    import re
    headings = []
    # Match <h1...>content</h1>, <h2...>content</h2>, <h3...>content</h3>
    pattern = r'<h[123][^>]*>([^<]+)</h[123]>'
    matches = re.findall(pattern, tsx_content, re.DOTALL)
    for match in matches:
        # Clean up the text: strip whitespace and remove {}
        text = match.strip()
        # Remove JSX interpolations like {variable}
        text = re.sub(r'\{[^}]+\}', '', text).strip()
        if text:
            headings.append(text)
    return headings


def _build_slots_for_page(path: Path, config: Dict) -> List[Dict]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    ext = path.suffix.lower()
    headings: List[str] = []
    word_count = 0
    if ext in {".md", ".mdx"}:
        extracted = extract_headings(text)
        headings = [h[0] for h in extracted]
        word_count = estimate_word_count(text)
    elif ext in {".tsx", ".jsx"}:
        headings = _extract_jsx_headings(text)
        word_count = len(text.split())
    else:
        headings = _extract_html_headings(text)
        word_count = len(text.split())

    max_inline = max(
        1,
        int(word_count / 1200) * config.get("pipeline", {}).get("max_inline_images_per_1200_words", 3),
    )

    slots = []
    for index, heading in enumerate(headings):
        if _heading_excluded(heading, config.get("exclusions", {})):
            continue
        insertion_mode = "HERO" if index == 0 else "INLINE"
        if insertion_mode == "INLINE" and len([s for s in slots if s["insertion_mode"] == "INLINE"]) >= max_inline:
            continue

        if ext in {".md", ".mdx"}:
            anchor_selector = "md:h1" if index == 0 else "md:h2"
        elif ext in {".tsx", ".jsx"}:
            anchor_selector = "jsx:h1" if index == 0 else "jsx:h2"
        else:
            anchor_selector = "h1" if index == 0 else "h2"
        slot_key = "hero" if index == 0 else slugify(heading)
        rel_path = normalize_path(path, REPO_ROOT)
        slot_id = compute_slot_id(rel_path, anchor_selector, index, insertion_mode, slot_key)
        risk = _risk_score(heading, config.get("adsense_safety", {}).get("ad_marker_patterns", []))

        slots.append(
            {
                "slot_id": slot_id,
                "page_path": rel_path,
                "anchor_text": heading,
                "anchor_selector": anchor_selector,
                "anchor_index": index,
                "insertion_mode": insertion_mode,
                "slot_key": slot_key,
                "priority_level": 5 if insertion_mode == "HERO" else 3,
                "risk_score": risk["score"],
                "risk_factors": risk["factors"],
            }
        )
    return slots


def main() -> None:
    config = _load_config()
    profile = _load_profile()

    content_roots = config.get("content_roots") or profile.get("source_roots") or []
    exclude_dirs = config.get("exclude_dirs", [])
    pages = _collect_pages(content_roots, exclude_dirs)

    slots = []
    for path in pages:
        rel_path = normalize_path(path, REPO_ROOT)
        if _is_excluded(rel_path, config.get("exclusions", {})):
            continue
        slots.extend(_build_slots_for_page(path, config))

    slots_sorted = sorted(slots, key=lambda s: (s["page_path"], s["anchor_index"], s["slot_id"]))

    for slot in slots_sorted:
        slot_dir = PROMPTS_ROOT / slot["slot_id"]
        slot_dir.mkdir(parents=True, exist_ok=True)
        write_json(slot_dir / "meta.json", slot)

    write_json(PROMPTS_ROOT / "index.json", {"generated": True, "slots": slots_sorted})

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
                slot["page_path"],
                slot["anchor_text"],
                slot["anchor_selector"],
                slot["anchor_index"],
                slot["insertion_mode"],
                slot["slot_key"],
                slot["priority_level"],
                slot["risk_score"],
                slot.get("prompt_hash", ""),
            ]
            for slot in slots_sorted
        ],
    )


if __name__ == "__main__":
    main()
