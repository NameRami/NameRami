#!/usr/bin/env python3
"""Generate a self-hosted GitHub profile badge for stars received by public, original repos."""

import json
import os
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from xml.sax.saxutils import escape

USERNAME = "NameRami"
OUTPUT = Path(__file__).resolve().parent.parent / "assets" / "stars-earned.svg"


def total_public_stars(username: str) -> int:
    """Sum stargazers_count across *owned, non-fork, public* repositories."""
    token = os.environ.get("GITHUB_TOKEN")
    total = 0
    page = 1
    while True:
        query = urlencode({"type": "owner", "per_page": 100, "page": page})
        url = f"https://api.github.com/users/{username}/repos?{query}"
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "github-profile-star-badge",
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        request = Request(url, headers=headers)
        with urlopen(request, timeout=30) as response:
            repositories = json.load(response)
        if not isinstance(repositories, list):
            raise ValueError("GitHub API returned an unexpected response")
        for repository in repositories:
            if not repository.get("fork", False) and not repository.get("private", False):
                total += int(repository["stargazers_count"])
        if len(repositories) < 100:
            return total
        page += 1


def svg_badge(value: int | str) -> str:
    """Build a standalone SVG: no third-party badge-image server required."""
    label_width = 112
    value_text = f"{value:,}" if isinstance(value, int) else str(value)
    value_width = max(35, 14 + 8 * len(value_text))
    width = label_width + value_width
    accessible_name = escape(f"Stars earned: {value_text}")
    safe_value = escape(value_text)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="20" viewBox="0 0 {width} 20" role="img" aria-label="{accessible_name}">
  <title>{accessible_name}</title>
  <clipPath id="rounded"><rect width="{width}" height="20" rx="4"/></clipPath>
  <g clip-path="url(#rounded)">
    <rect width="{label_width}" height="20" fill="#111827"/>
    <rect x="{label_width}" width="{value_width}" height="20" fill="#0F766E"/>
  </g>
  <path d="M12 3.2l1.6 3.4 3.8.5-2.7 2.7.7 3.8-3.4-1.8-3.4 1.8.7-3.8-2.7-2.7 3.8-.5z" fill="#FBBF24"/>
  <g font-family="DejaVu Sans,Verdana,Arial,sans-serif" font-size="10.5" fill="#FFFFFF">
    <text x="22" y="13.7">Stars earned</text>
    <text x="{label_width + value_width / 2}" y="13.7" text-anchor="middle" font-weight="bold">{safe_value}</text>
  </g>
</svg>
"""


def main() -> None:
    stars = total_public_stars(USERNAME)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(svg_badge(stars), encoding="utf-8")
    print(f"Wrote {OUTPUT} with {stars} stars")


if __name__ == "__main__":
    main()
