# Site usage


Visitor statistics for this hand-over site. Counts are collected with [GoatCounter](https://www.goatcounter.com/) (privacy-friendly, no cookies) and refreshed on each deploy.

!!! important "Numbers do not update live"
    Browsing the docs **does not** update this page immediately. Visits are stored in GoatCounter; charts update only when **deploy-docs** runs (push to `main` or **Actions → Run workflow**). Check your [GoatCounter dashboard](https://www.goatcounter.com/) first — if it shows visits but this page is empty, run **deploy-docs** again.

!!! info "Status"
    Charts load from [pageviews-data.json](../javascripts/pageviews-data.json) after each deploy. If you see empty charts, open that JSON: `"configured": true` means data loaded; `"configured": false` shows the error in `"message"`.

---

## By section

<p id="pageviews-meta">Loading statistics…</p>

<canvas id="pageviews-by-section" height="100" aria-label="Bar chart of visitors per site section"></canvas>

---

## Top pages

<canvas id="pageviews-by-page" height="320" aria-label="Horizontal bar chart of visitors per page"></canvas>

<table>
  <thead>
    <tr>
      <th>Page</th>
      <th>Title</th>
      <th>Section</th>
      <th style="text-align:right">Visitors</th>
    </tr>
  </thead>
  <tbody id="pageviews-table-body"></tbody>
</table>

---

## Setup (maintainers)

To enable tracking and charts on GitHub Pages:

1. Create a free site at [goatcounter.com](https://www.goatcounter.com/) (e.g. `nmcb-handover.goatcounter.com`).
2. In GoatCounter: **Settings → Site settings** — allow counting on `nmcb-fair.github.io` (or your custom domain).
3. Create an **API token** ([GoatCounter API help](https://www.goatcounter.com/help/api)):
   - Top menu → your **username** → **API** → **Create token**
   - Enable **Read statistics** (required for charts). *Record pageviews* alone is not enough.
   - Ensure the token is allowed for your site (e.g. `sxzhang1201.goatcounter.com`).
4. In the GitHub repo **Settings → Secrets and variables → Actions**, add:

| Secret | Example |
| ------ | ------- |
| `GOATCOUNTER_API_HOST` | `https://sxzhang1201.goatcounter.com` — must include **`https://`** (host only, no `/count`) |
| `GOATCOUNTER_API_TOKEN` | token from step 3 |
| `GOATCOUNTER_COUNT_URL` | `https://sxzhang1201.goatcounter.com/count` (optional; `https://` required if you set this) |

!!! warning "Empty charts but page loads"
    Open [pageviews-data.json](../javascripts/pageviews-data.json). If `"configured": false` and the message contains **403 Forbidden**, create a **new** API token with **Read statistics** checked, replace `GOATCOUNTER_API_TOKEN`, then **Actions → deploy-docs → Run workflow**.

Common mistakes:

- Host without `https://` → API error “No scheme supplied”
- Token with only **Record pageviews** → **403 Forbidden** (current issue if charts stay empty)

!!! warning "If /site-usage/ shows 404"
    The page is only on GitHub Pages after a **successful** **deploy-docs** run. If the workflow failed on **Fetch pageview statistics**, fix the secrets above and re-run **Actions → deploy-docs → Run workflow**. A failed fetch no longer blocks deploy, but you must redeploy after the fix is on `main`.

5. Push to `main` / `master` (or run **deploy-docs** manually). The workflow runs `scripts/fetch_pageviews.py` before `mkdocs build` and updates `docs/javascripts/pageviews-data.json`.

**Local test:** with secrets in the environment:

```bash
export GOATCOUNTER_API_HOST=https://your-site.goatcounter.com
export GOATCOUNTER_API_TOKEN=your-token
pip install requests
python scripts/fetch_pageviews.py
mkdocs serve
```

Open [http://127.0.0.1:8000/nmcb-handover-docs/site-usage/](http://127.0.0.1:8000/nmcb-handover-docs/site-usage/) after a few real visits to your GoatCounter site.

!!! note "Privacy"
    GoatCounter is used without cookies. For Amsterdam UMC policy, confirm that lightweight page analytics on a public hand-over site is acceptable. Do not put participant-identifiable data in URLs or page titles.
