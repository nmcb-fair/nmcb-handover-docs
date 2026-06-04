# Site usage


Visitor statistics for this hand-over site. Counts are collected with [GoatCounter](https://www.goatcounter.com/) (privacy-friendly, no cookies) and refreshed on each deploy.

---

## By section

<p id="pageviews-meta"></p>

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
3. Create an **API token** with read access (**Settings → API tokens**).
4. In the GitHub repo **Settings → Secrets and variables → Actions**, add:

| Secret | Example |
| ------ | ------- |
| `GOATCOUNTER_API_HOST` | `https://nmcb-handover.goatcounter.com` |
| `GOATCOUNTER_API_TOKEN` | token from step 3 |
| `GOATCOUNTER_COUNT_URL` | `https://nmcb-handover.goatcounter.com/count` (optional; defaults to `{API_HOST}/count`) |

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
