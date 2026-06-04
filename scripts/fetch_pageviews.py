#!/usr/bin/env python3
"""Fetch GoatCounter path statistics and write JSON for the Site usage page."""

from __future__ import annotations

import json
import os
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
try:
    import requests
except ImportError:
    print("Install requests: pip install requests", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
JS_DIR = ROOT / "docs" / "javascripts"
DATA_FILE = JS_DIR / "pageviews-data.json"
CONFIG_FILE = JS_DIR / "analytics-config.json"

SITE_PREFIX = os.environ.get("SITE_PATH_PREFIX", "/nmcb-handover-docs").rstrip("/")
LOOKBACK_DAYS = int(os.environ.get("PAGEVIEW_LOOKBACK_DAYS", "365"))

SECTION_LABELS = {
    "": "Home",
    "workflows": "Workflows",
    "systems": "Systems",
    "fair": "FAIR",
    "tasks": "Tasks",
    "files": "Files (attachments)",
    "where-data-lives": "Where data lives",
    "site-usage": "Site usage",
}


def section_key(path: str) -> str:
    p = path.strip("/")
    if SITE_PREFIX and (p == SITE_PREFIX.lstrip("/") or p.startswith(SITE_PREFIX.lstrip("/") + "/")):
        p = p[len(SITE_PREFIX.lstrip("/")) :].lstrip("/")
    if not p:
        return ""
    return p.split("/")[0]


def friendly_page(path: str) -> str:
    p = path.strip("/")
    if SITE_PREFIX and p.startswith(SITE_PREFIX.lstrip("/")):
        p = p[len(SITE_PREFIX) :].lstrip("/")
    if not p or p.endswith("/index.html"):
        p = p.replace("/index.html", "").rstrip("/") or "home"
    return "/" + p if p else "/"


def fetch_hits(host: str, token: str, start: str, end: str) -> list[dict]:
    url = f"{host.rstrip('/')}/api/v0/stats/hits"
    resp = requests.get(
        url,
        params={"start": start, "end": end},
        headers={"Authorization": f"Bearer {token}"},
        timeout=90,
    )
    resp.raise_for_status()
    payload = resp.json()
    return payload.get("hits") or []


def fetch_total_visitors(host: str, token: str, start: str, end: str) -> int | None:
    url = f"{host.rstrip('/')}/api/v0/stats/total"
    resp = requests.get(
        url,
        params={"start": start, "end": end},
        headers={"Authorization": f"Bearer {token}"},
        timeout=90,
    )
    resp.raise_for_status()
    payload = resp.json()
    stats = payload.get("stats") or []
    return sum(int(row.get("count") or 0) for row in stats) if stats else None


def build_output(hits: list[dict], updated: str, total_visitors: int | None) -> dict:
    pages: list[dict] = []
    by_section: dict[str, int] = defaultdict(int)
    path_sum = 0

    for hit in hits:
        path = hit.get("path") or ""
        if hit.get("event"):
            continue
        if any(path.endswith(ext) for ext in (".js", ".json", ".css", ".png", ".ico", ".xml")):
            continue
        count = int(hit.get("count") or 0)
        if count <= 0:
            continue

        key = section_key(path)
        by_section[key] += count
        path_sum += count
        pages.append(
            {
                "path": friendly_page(path),
                "title": (hit.get("title") or "").strip() or None,
                "visitors": count,
                "section": SECTION_LABELS.get(key, key or "Other"),
            }
        )

    pages.sort(key=lambda x: (-x["visitors"], x["path"]))
    sections = [
        {
            "id": k,
            "label": SECTION_LABELS.get(k, k or "Other"),
            "visitors": v,
        }
        for k, v in sorted(by_section.items(), key=lambda x: -x[1])
    ]

    return {
        "configured": True,
        "updated": updated,
        "periodDays": LOOKBACK_DAYS,
        "totalVisitors": total_visitors if total_visitors is not None else path_sum,
        "sections": sections,
        "pages": pages[:80],
    }


def write_analytics_config(count_url: str | None) -> None:
    enabled = bool(count_url)
    CONFIG_FILE.write_text(
        json.dumps(
            {
                "enabled": enabled,
                "countUrl": count_url or "",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def placeholder(reason: str) -> dict:
    return {
        "configured": False,
        "updated": None,
        "message": reason,
        "periodDays": LOOKBACK_DAYS,
        "totalVisitors": 0,
        "sections": [],
        "pages": [],
    }


def main() -> int:
    JS_DIR.mkdir(parents=True, exist_ok=True)

    host = os.environ.get("GOATCOUNTER_API_HOST", "").strip()
    token = os.environ.get("GOATCOUNTER_API_TOKEN", "").strip()
    count_url = os.environ.get("GOATCOUNTER_COUNT_URL", "").strip()
    if not count_url and host:
        count_url = f"{host.rstrip('/')}/count"

    write_analytics_config(count_url if host and token else None)

    if not host or not token:
        DATA_FILE.write_text(
            json.dumps(placeholder("Set GOATCOUNTER_API_HOST and GOATCOUNTER_API_TOKEN in GitHub Actions secrets."), indent=2)
            + "\n",
            encoding="utf-8",
        )
        print("Wrote placeholder pageviews-data.json (GoatCounter secrets not set).")
        return 0

    end = date.today()
    start = end - timedelta(days=LOOKBACK_DAYS)
    updated = end.isoformat()

    try:
        start_s, end_s = start.isoformat(), end.isoformat()
        hits = fetch_hits(host, token, start_s, end_s)
        total_visitors = fetch_total_visitors(host, token, start_s, end_s)
        data = build_output(hits, updated, total_visitors)
        DATA_FILE.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {DATA_FILE} — {data['totalVisitors']} visitors across {len(data['pages'])} paths.")
    except requests.RequestException as exc:
        print(f"GoatCounter API error: {exc}", file=sys.stderr)
        DATA_FILE.write_text(
            json.dumps(placeholder(f"API fetch failed: {exc}"), indent=2) + "\n",
            encoding="utf-8",
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
