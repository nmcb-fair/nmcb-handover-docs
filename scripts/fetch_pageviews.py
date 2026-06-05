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
ENV_JS_FILE = JS_DIR / "goatcounter-env.js"
HITS_PAGE_LIMIT = 100  # GoatCounter API max per request

SITE_PREFIX = os.environ.get("SITE_PATH_PREFIX", "/nmcb-handover-docs").rstrip("/")
LOOKBACK_DAYS = int(os.environ.get("PAGEVIEW_LOOKBACK_DAYS", "365"))
MAX_LOOKBACK_DAYS = 366  # GoatCounter API limit


def normalize_host(host: str) -> str:
    host = host.strip().rstrip("/")
    if not host:
        return ""
    if not host.startswith(("http://", "https://")):
        host = "https://" + host
    for suffix in ("/count", "/api", "/api/v0"):
        if host.endswith(suffix):
            host = host[: -len(suffix)]
    return host.rstrip("/")


def normalize_count_url(count_url: str, host: str) -> str:
    url = count_url.strip() if count_url else ""
    if not url:
        return f"{host}/count" if host else ""
    if not url.startswith(("http://", "https://")):
        url = "https://" + url.lstrip("/")
    base = normalize_host(url)
    return f"{base}/count"

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


def _api_get(host: str, token: str, path: str, params: dict) -> dict:
    url = f"{host.rstrip('/')}{path}"
    resp = requests.get(
        url,
        params=params,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        timeout=90,
    )
    if not resp.ok:
        detail = resp.text[:300]
        raise requests.HTTPError(
            f"{resp.status_code} {resp.reason} for {path}: {detail}",
            response=resp,
        )
    return resp.json()


def api_error_hint(exc: requests.RequestException, host: str) -> str:
    """Short, actionable message for deploy logs and pageviews-data.json."""
    text = str(exc)
    if "403" in text:
        return (
            "GoatCounter returned 403 Forbidden: the API token cannot read statistics. "
            "In GoatCounter open your username (top menu) → API → create a NEW token and enable "
            "**Read statistics** (not only Record pageviews). Assign the token to site "
            f"{host}. Update GitHub secret GOATCOUNTER_API_TOKEN and run deploy-docs again. "
            "See https://www.goatcounter.com/help/api"
        )
    if "401" in text:
        return (
            "GoatCounter returned 401 Unauthorized: wrong or expired GOATCOUNTER_API_TOKEN. "
            "Create a new token and update the GitHub secret."
        )
    if "No scheme supplied" in text:
        return (
            "GOATCOUNTER_API_HOST must start with https:// "
            f"(e.g. https://yourcode.goatcounter.com). Got: {host!r}"
        )
    return f"API fetch failed: {exc}"


def fetch_hits(host: str, token: str, start: str, end: str) -> list[dict]:
    hits: list[dict] = []
    exclude: list[str] = []
    while True:
        params: dict = {
            "start": start,
            "end": end,
            "limit": HITS_PAGE_LIMIT,
        }
        if exclude:
            params["exclude_paths"] = exclude
        payload = _api_get(host, token, "/api/v0/stats/hits", params)
        batch = payload.get("hits") or []
        hits.extend(batch)
        if not payload.get("more") or not batch:
            break
        exclude.extend(str(hit.get("path_id")) for hit in batch if hit.get("path_id") is not None)
    return hits


def fetch_total_visitors(host: str, token: str, start: str, end: str) -> int | None:
    payload = _api_get(
        host,
        token,
        "/api/v0/stats/total",
        {"start": start, "end": end},
    )
    if payload.get("total") is not None:
        return int(payload["total"])
    stats = payload.get("stats") or []
    if not stats:
        return None
    return sum(int(row.get("daily") or 0) for row in stats)


def fetch_stats(host: str, token: str, lookback_days: int) -> tuple[list[dict], int | None, str, str]:
    """Return hits, total visitors, start, end (inclusive date range)."""
    days = min(lookback_days, MAX_LOOKBACK_DAYS)
    end = date.today()
    start = end - timedelta(days=days)
    start_s, end_s = start.isoformat(), end.isoformat()
    try:
        hits = fetch_hits(host, token, start_s, end_s)
        total = fetch_total_visitors(host, token, start_s, end_s)
        return hits, total, start_s, end_s
    except requests.HTTPError as exc:
        if exc.response is not None and exc.response.status_code == 400:
            end = date.today() - timedelta(days=1)
            start = end - timedelta(days=days)
            start_s, end_s = start.isoformat(), end.isoformat()
            hits = fetch_hits(host, token, start_s, end_s)
            total = fetch_total_visitors(host, token, start_s, end_s)
            return hits, total, start_s, end_s
        raise


def build_output(hits: list[dict], updated: str, total_visitors: int | None) -> dict:
    pages: list[dict] = []
    by_section: dict[str, int] = defaultdict(int)
    path_sum = 0

    for hit in hits:
        path = hit.get("path") or ""
        if hit.get("event") is True:
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
        "note": (
            "Counts refresh on each deploy, not live. "
            "If empty, open your GoatCounter dashboard — if that is also empty, "
            "tracking is not recording (check allowed domain nmcb-fair.github.io)."
        ),
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


def write_goatcounter_env(count_url: str | None) -> None:
    url = count_url or ""
    ENV_JS_FILE.write_text(
        "/* Generated by scripts/fetch_pageviews.py — do not edit by hand. */\n"
        f'window.NMCB_GC_COUNT_URL = {json.dumps(url)};\n',
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

    host = normalize_host(os.environ.get("GOATCOUNTER_API_HOST", ""))
    token = os.environ.get("GOATCOUNTER_API_TOKEN", "").strip()
    count_url = normalize_count_url(
        os.environ.get("GOATCOUNTER_COUNT_URL", "").strip(), host
    )

    active_count_url = count_url if host and token else None
    write_analytics_config(active_count_url)
    write_goatcounter_env(active_count_url)

    if not host or not token:
        DATA_FILE.write_text(
            json.dumps(placeholder("Set GOATCOUNTER_API_HOST and GOATCOUNTER_API_TOKEN in GitHub Actions secrets."), indent=2)
            + "\n",
            encoding="utf-8",
        )
        print("Wrote placeholder pageviews-data.json (GoatCounter secrets not set).")
        return 0

    updated = date.today().isoformat()

    try:
        try:
            hits, total_visitors, _, _ = fetch_stats(host, token, LOOKBACK_DAYS)
        except requests.RequestException:
            print("Retrying GoatCounter API with 90-day window...", file=sys.stderr)
            hits, total_visitors, _, _ = fetch_stats(host, token, 90)

        data = build_output(hits, updated, total_visitors)
        DATA_FILE.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {DATA_FILE} — {data['totalVisitors']} visitors across {len(data['pages'])} paths.")
    except requests.RequestException as exc:
        print(f"GoatCounter API error (deploy continues): {exc}", file=sys.stderr)
        DATA_FILE.write_text(
            json.dumps(placeholder(api_error_hint(exc, host)), indent=2) + "\n",
            encoding="utf-8",
        )
        # Do not fail the docs deploy — site-usage page must still be published.
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
