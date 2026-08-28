#!/usr/bin/env python3
"""Inventory published Hugo guides for source-traceability and date-risk signals.

Normal mode always exits 0 so it can be used to establish a baseline.  Add
--strict to return 1 when any published guide has one or more flagged issues.
This is an editorial triage tool, not a substitute for source-by-source review.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

URL_PATTERN = re.compile(r"https?://[^\s)>\]]+", re.IGNORECASE)
QUANTITATIVE_PATTERN = re.compile(
    r"(?:\$\s?\d|\b\d+(?:\.\d+)?\s?(?:%|kwh|therms?|ccf|mcf|gallons?|mw|gw|¢|cents?))",
    re.IGNORECASE,
)
FUTURE_YEAR_PATTERN = re.compile(r"\b(20\d{2})\b")
MONTH_PATTERN = re.compile(
    r"\b(january|february|march|april|may|june|july|august|september|october|november|december)\s+(20\d{2})\b",
    re.IGNORECASE,
)
MONTH_NUMBERS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


@dataclass(frozen=True)
class AuditResult:
    path: Path
    title: str
    published: bool
    word_count: int
    source_urls: tuple[str, ...]
    issue_codes: tuple[str, ...]


def split_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    closing_match = re.search(r"^\s*---\s*$", text[4:], re.MULTILINE)
    if closing_match is None:
        return "", text
    closing_start = 4 + closing_match.start()
    closing_end = 4 + closing_match.end()
    return text[4:closing_start], text[closing_end:]


def front_matter_value(front_matter: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", front_matter, re.MULTILINE)
    return match.group(1).strip().strip("\"'") if match else ""


def front_matter_sources(front_matter: str) -> tuple[str, ...]:
    lines = front_matter.splitlines()
    urls: list[str] = []
    in_sources = False
    for raw_line in lines:
        line = raw_line.strip()
        if re.match(r"^sources:\s*$", line):
            in_sources = True
            continue
        if in_sources:
            if re.match(r"^[A-Za-z_][\w-]*:\s*", line):
                break
            match = re.match(r"^-\s*(https?://\S+)\s*$", line)
            if match:
                urls.append(match.group(1))
    return tuple(urls)


def has_future_claim(body: str, today: date) -> bool:
    for match in MONTH_PATTERN.finditer(body):
        month = MONTH_NUMBERS[match.group(1).lower()]
        claimed_date = date(int(match.group(2)), month, 1)
        if claimed_date > today:
            return True
    return any(int(year) > today.year for year in FUTURE_YEAR_PATTERN.findall(body))


def audit_file(path: Path, today: date | None = None) -> AuditResult:
    today = today or date.today()
    text = path.read_text(encoding="utf-8")
    front_matter, body = split_front_matter(text)
    published = front_matter_value(front_matter, "draft").lower() != "true"
    source_urls = front_matter_sources(front_matter)
    visible_source_urls = tuple(URL_PATTERN.findall(body))
    issues: list[str] = []

    if published and has_future_claim(body, today):
        issues.append("future_claim")
    if published and QUANTITATIVE_PATTERN.search(body) and not source_urls:
        issues.append("missing_sources")
    if published and source_urls and not visible_source_urls:
        issues.append("sources_not_visible")

    title = front_matter_value(front_matter, "title") or path.stem
    word_count = len(re.findall(r"\b[\w'-]+\b", body))
    return AuditResult(path, title, published, word_count, source_urls, tuple(issues))


def published_guides(content_root: Path) -> list[Path]:
    blog_root = content_root / "blog"
    return sorted(path for path in blog_root.glob("*.md") if path.name != "_index.md")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--content-root", default="content", type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)

    results = [audit_file(path) for path in published_guides(args.content_root)]
    flagged = [result for result in results if result.issue_codes]
    print(f"PUBLISHED_GUIDES {sum(result.published for result in results)}")
    print(f"FLAGGED_GUIDES {len(flagged)}")
    for result in flagged:
        print(
            f"{result.path} | {result.word_count} words | "
            f"{','.join(result.issue_codes)} | {result.title}"
        )
    return 1 if args.strict and flagged else 0


if __name__ == "__main__":
    sys.exit(main())
