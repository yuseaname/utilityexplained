from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Iterable, List


def normalize_path(path: Path, repo_root: Path) -> str:
    rel = path.relative_to(repo_root).as_posix()
    return rel.lower().strip()


def normalize_selector(selector: str) -> str:
    return re.sub(r"\s+", " ", selector.strip().lower())


def compute_slot_id(
    page_path: str,
    anchor_selector: str,
    anchor_index: int,
    insertion_mode: str,
    slot_key: str,
) -> str:
    raw = "|".join(
        [
            page_path.lower().strip(),
            normalize_selector(anchor_selector),
            str(anchor_index),
            insertion_mode.upper().strip(),
            slot_key.lower().strip(),
        ]
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:24]


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    return re.sub(r"\s+", "-", cleaned)[:64] or "slot"


def chunked(iterable: Iterable, size: int) -> Iterable[List]:
    batch: List = []
    for item in iterable:
        batch.append(item)
        if len(batch) >= size:
            yield batch
            batch = []
    if batch:
        yield batch
