from __future__ import annotations

from typing import Tuple

from bs4 import BeautifulSoup


def parse_html(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "lxml")


def find_heading(soup: BeautifulSoup, tag_name: str, index: int) -> Tuple[bool, object]:
    headings = soup.find_all(tag_name)
    if index < 0 or index >= len(headings):
        return False, None
    return True, headings[index]


def insert_after(element, new_element) -> None:
    if element and new_element:
        element.insert_after(new_element)


def render_img_tag(src: str, alt: str, width: int, height: int, slot_id: str, eager: bool) -> BeautifulSoup:
    attrs = {
        "src": src,
        "alt": alt,
        "width": str(width),
        "height": str(height),
        "data-slot-id": slot_id,
    }
    if eager:
        attrs["loading"] = "eager"
        attrs["fetchpriority"] = "high"
    else:
        attrs["loading"] = "lazy"
        attrs["decoding"] = "async"

    tag = BeautifulSoup("", "lxml").new_tag("img", **attrs)
    return tag
