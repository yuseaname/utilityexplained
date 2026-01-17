from __future__ import annotations

import re
from typing import List, Tuple


def extract_headings(markdown: str) -> List[Tuple[str, int]]:
    headings = []
    for line in markdown.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+)$", line.strip())
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()
            headings.append((text, level))
    return headings


def estimate_word_count(markdown: str) -> int:
    return len(re.findall(r"\b\w+\b", markdown))
