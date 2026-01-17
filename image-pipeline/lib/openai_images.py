from __future__ import annotations

import base64
import os
import time
from typing import Any, Dict

import requests

ALLOWED_MODEL = "gpt-image-1"


class OpenAIImageError(RuntimeError):
    pass


def _validate_model(model: str) -> None:
    if model != ALLOWED_MODEL:
        raise OpenAIImageError(f"Unsupported image model: {model}. Only {ALLOWED_MODEL} is allowed.")


def _request_with_retry(url: str, headers: Dict[str, str], payload: Dict[str, Any]) -> Dict[str, Any]:
    backoff = 1.5
    for attempt in range(6):
        resp = requests.post(url, headers=headers, json=payload, timeout=90)
        if resp.status_code < 400:
            return resp.json()
        if resp.status_code in (429, 500, 502, 503, 504):
            time.sleep(backoff)
            backoff *= 2
            continue
        raise OpenAIImageError(f"Image API error {resp.status_code}: {resp.text}")
    raise OpenAIImageError("Image API failed after retries.")


def generate_image(prompt: str, model: str, size: str, quality: str) -> Dict[str, Any]:
    _validate_model(model)
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise OpenAIImageError("OPENAI_API_KEY is not set.")

    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "n": 1,
    }

    data = _request_with_retry(url, headers, payload)
    if "data" not in data or not data["data"]:
        raise OpenAIImageError("Image API response missing data.")

    b64 = data["data"][0].get("b64_json")
    if not b64:
        raise OpenAIImageError("Image API response missing b64_json.")

    image_bytes = base64.b64decode(b64)
    return {
        "bytes": image_bytes,
        "model": model,
        "size": size,
        "quality": quality,
    }
