from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Dict, List

PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT))

from lib.io_utils import load_yaml, write_json, write_text  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PIPELINE_ROOT / "config.yaml"


def _load_config() -> Dict:
    return load_yaml(CONFIG_PATH, default={}) or {}


def _collect_files(root: Path, exclude_dirs: List[str]) -> List[Path]:
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in exclude_dirs for part in path.parts):
            continue
        files.append(path)
    return files


def _detect_frameworks(repo_root: Path) -> List[str]:
    frameworks = []
    package_json = repo_root / "package.json"
    if package_json.exists():
        data = json.loads(package_json.read_text(encoding="utf-8"))
        deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
        if "next" in deps:
            frameworks.append("Next.js")
        if "react" in deps:
            frameworks.append("React")
        if "gatsby" in deps:
            frameworks.append("Gatsby")
        if "astro" in deps:
            frameworks.append("Astro")
        if "vue" in deps or "nuxt" in deps:
            frameworks.append("Vue")
        if "svelte" in deps or "sveltekit" in deps:
            frameworks.append("SvelteKit")
        if "@docusaurus/core" in deps:
            frameworks.append("Docusaurus")
    return frameworks


def _detect_content_types(files: List[Path]) -> List[str]:
    types = set()
    for path in files:
        suffix = path.suffix.lower()
        if suffix == ".html":
            types.add("HTML")
        if suffix == ".md":
            types.add("Markdown")
        if suffix == ".mdx":
            types.add("MDX")
    return sorted(types)


def _detect_source_roots(repo_root: Path) -> List[str]:
    candidates = [
        "app",
        "pages",
        "src/app",
        "src/pages",
        "content",
        "docs",
        "blog",
    ]
    roots = []
    for candidate in candidates:
        if (repo_root / candidate).exists():
            roots.append(candidate)
    return roots


def _detect_build_dirs(repo_root: Path) -> List[str]:
    candidates = [".next", "out", "dist", "build", "public"]
    return [c for c in candidates if (repo_root / c).exists()]


def _find_homepages(files: List[Path], repo_root: Path) -> List[str]:
    candidates = []
    for path in files:
        name = path.name.lower()
        if name in {"index.html", "index.md", "index.mdx", "page.tsx", "page.jsx"}:
            candidates.append(path.relative_to(repo_root).as_posix())
    return sorted(set(candidates))


def _find_nav_links(files: List[Path]) -> List[str]:
    links = set()
    href_re = re.compile(r"href=\"([^\"]+)\"")
    md_link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in files:
        if path.suffix.lower() not in {".html", ".md", ".mdx"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in href_re.findall(text):
            if match.startswith("/") and not match.startswith("//"):
                links.add(match)
        for match in md_link_re.findall(text):
            if match.startswith("/") and not match.startswith("//"):
                links.add(match)
    return sorted(links)


def _find_long_form_pages(files: List[Path], repo_root: Path) -> List[str]:
    long_pages = []
    for path in files:
        if path.suffix.lower() not in {".md", ".mdx", ".html"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        words = re.findall(r"\b\w+\b", text)
        if len(words) >= 1200:
            long_pages.append(path.relative_to(repo_root).as_posix())
    return sorted(long_pages)


def _image_conventions(files: List[Path], repo_root: Path) -> List[str]:
    image_dirs = set()
    for path in files:
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
            image_dirs.add(path.parent.relative_to(repo_root).as_posix())
    return sorted(image_dirs)


def _detect_locale(repo_root: Path, files: List[Path]) -> Dict[str, str]:
    locale = {"country": "", "locale": ""}
    next_config = repo_root / "next.config.js"
    if next_config.exists():
        text = next_config.read_text(encoding="utf-8", errors="ignore")
        match = re.search(r"locales\s*:\s*\[([^\]]+)\]", text)
        if match:
            locale_list = match.group(1)
            locale["locale"] = locale_list.split(",")[0].strip().strip("'\"")
    for path in files:
        if path.suffix.lower() != ".html":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        match = re.search(r"lang=\"([a-zA-Z-]+)\"", text)
        if match:
            locale["locale"] = match.group(1)
            break
    return locale


def main() -> None:
    config = _load_config()
    exclude_dirs = config.get("exclude_dirs", [])

    files = _collect_files(REPO_ROOT, exclude_dirs)

    profile = {
        "repo_root": str(REPO_ROOT),
        "frameworks": _detect_frameworks(REPO_ROOT),
        "content_types": _detect_content_types(files),
        "source_roots": _detect_source_roots(REPO_ROOT),
        "build_dirs": _detect_build_dirs(REPO_ROOT),
        "homepage_candidates": _find_homepages(files, REPO_ROOT),
        "nav_links": _find_nav_links(files),
        "long_form_pages": _find_long_form_pages(files, REPO_ROOT),
        "image_conventions": _image_conventions(files, REPO_ROOT),
        "market": _detect_locale(REPO_ROOT, files),
    }

    write_json(PIPELINE_ROOT / "repo_profile.json", profile)

    md = ["# Repo Profile", ""]
    for key, value in profile.items():
        md.append(f"## {key}")
        md.append("```")
        md.append(json.dumps(value, indent=2))
        md.append("```")
        md.append("")

    write_text(PIPELINE_ROOT / "REPO_PROFILE.md", "\n".join(md))


if __name__ == "__main__":
    main()
