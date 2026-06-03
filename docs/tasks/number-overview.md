# NMCB numbers overview


Produce standard **NMCB recruitment and visit-progress counts** — participant-level overview tables, funnel summaries, and plots for board updates, operational reports, and ad hoc stakeholder questions.

Canonical repository: **[github.com/nmcb-fair/nmcb-overview](https://github.com/nmcb-fair/nmcb-overview)**

For routine reporting, use this pipeline rather than ad hoc Castor or Snowflake queries. Counts are built from **LDOT**, screener exports, and **CRL Admin**, merged into one overview dataset before summary tables and figures are generated.

Operator guide in the repo: [`USER_GUIDE.Rmd`](https://github.com/nmcb-fair/nmcb-overview/blob/main/USER_GUIDE.Rmd)

---

## Purpose

The pipeline:

1. Builds a **participant-level overview** from LDOT, screening, postcode, and CRL Admin inputs (`ldot_overview.Rmd`)
2. Generates **summary tables and plots** for reporting (`scripts/get_numbers.R`)

Typical questions it answers:

- How many participants are registered, screener sent/completed, waiting for call/video/visit, visit done, or lost — by **participant type** (`pt_type`)
- Geographic distribution (distance to Amsterdam UMC / Radboud UMC)
- Visit cohort breakdowns by sex and DSQ criteria (CDC / CCC / IOM)

Column definitions for the participant export: [`docs/participant_export_columns.md`](https://github.com/nmcb-fair/nmcb-overview/blob/main/docs/participant_export_columns.md) in the repo.

---

## When to run

- **Weekly or bi-weekly** during active recruitment (typical board rhythm)
- **On demand** when stakeholders ask for updated funnel or visit counts
- **After refreshing inputs** — always run with fresh LDOT and screener exports; stale files produce stale numbers even if the script succeeds

Also covered under [Recurring study routines — Get numbers](../workflows/recurring-routines.md#get-numbers).

---

## Inputs

Place the latest files under `data/` before running. The loader picks the **newest file by modification time** matching each prefix (see `func/data_loading.R`).

### `data/LDOT/`

| File prefix (start of filename) | Content |
| ------------------------------- | ------- |
| `NMCB consortium CHILDREN EXPORT FOR PARENT AMSTERDAM UMC_ Deelnemer` | LDOT participant export — Amsterdam UMC |
| `NMCB consortium CHILDREN EXPORT FOR PARENT NMCB_ Deelnemer` | LDOT participant export — NMCB |
| `NMCB consortium CHILDREN EXPORT FOR PARENT RADBOUD_ Deelnemer` | LDOT participant export — Radboud |
| `STUDY EXPORT STUDYID 460 EXPORTED` | LDOT event log / event detail (CSV or XLSX) |

Export LDOT from the registry before each run — see [LDOT](../systems/ldot.md).

### `data/Screening/`

| File prefix | Content |
| ----------- | ------- |
| `NMCB_Study_NMCB_Screener_export_` | ME/CFS screener (Castor) |
| `NMCB_Study_Post-COVID_Screener_export_` | Post-COVID screener |
| `NMCB_Study_Lyme_Screener` | Lyme screener |
| `NMCB_Screening_ME_CFS_Screener_export_` | Legacy Castor ME/CFS screener (if still needed) |

Screener CSVs use **semicolon** delimiters. Source forms live in [Castor EDC](../systems/castor.md).

### `data/postcode/`

Static reference files (update only when radius definitions change):

- `50km-pc4.csv`
- `65km radius NMCB participants.xlsx`
- `50km radius Nijmegen.txt`
- `65km radius Nijmegen.txt` (if used)

### `data/CRL Admin/`

| File | Content |
| ---- | ------- |
| `CRL_admin.xlsx` | Participant type, sex, age — used to align overview with CRL admin and deduplication |

Keep **one** CRL admin file in the folder; multiple matches cause the script to stop.

---

## How to run

### One-time setup

```r
install.packages("renv")
renv::restore()
```

Open **`Overview.Rproj`** in RStudio so paths resolve correctly.

### Standard run

1. Refresh all `data/` inputs listed above.
2. Open `run_all.R` and click **Source** (or run from the project root):

```r
source("run_all.R")
```

This runs:

- **Step 1:** `rmarkdown::render("ldot_overview.Rmd")` → participant overview Excel
- **Step 2:** `source("scripts/get_numbers.R")` → summary tables and plots

### Reporting date

By default the run date is **today** (`YYYYMMDD` in output filenames).

To re-run for a specific date:

```r
Sys.setenv(NMCB_RUN_DATE = "20260204")
source("run_all.R")
```

Or from the shell:

```bash
NMCB_RUN_DATE=20260204 Rscript run_all.R
```

### Run steps separately (optional)

```r
rmarkdown::render("ldot_overview.Rmd")
source("scripts/get_numbers.R")
```

---

## Outputs

| Path | Description |
| ---- | ----------- |
| `export/overview_participants/NMCB_Participants_LDOT__YYYYMMDD.xlsx` | Participant-level overview (one row per participant) |
| `export/numbers_and_figures/YYYYMMDD/overview_tables__YYYYMMDD.xlsx` | Summary tables (multi-sheet workbook) |
| `export/numbers_and_figures/YYYYMMDD/participant_flow_after_screener__YYYYMMDD.pdf` | Flow diagram after screener |
| `export/numbers_and_figures/YYYYMMDD/participant_funnel_pe_participant_type.pdf__YYYYMMDD.pdf` | Funnel by participant type |
| `export/numbers_and_figures/YYYYMMDD/geo_by_type_no_screener__YYYYMMDD.pdf` | Geography — registered, no screener yet |
| `export/numbers_and_figures/YYYYMMDD/visit_sex_by_type__YYYYMMDD.pdf` | Sex among visit-done participants |
| `export/numbers_and_figures/YYYYMMDD/visit_dsq_by_type__YYYYMMDD.pdf` | DSQ criteria among visit-done participants |

Share outputs in the format agreed with the study team (usually Excel + PDF for board slides). Record the run date and input file versions used.

### Which table answers which question

In `overview_tables__YYYYMMDD.xlsx`:

| Sheet | Use when asked about |
| ----- | -------------------- |
| `overview_table` | Overall funnel by `pt_type`: registered, screener sent/completed, waiting stages, visit done/scheduled, losses |
| `geo_by_type_no_screener` | Registered participants without screener yet, by distance to AMC/Radboud |
| `visit_sex_by_type` | Sex distribution among participants with visit done |
| `visit_dsq_by_type` | DSQ criteria counts (CDC/CCC/IOM) among participants with visit done |

---

## Quality checks

- Compare `overview_table` totals to the **previous run**; large unexpected jumps often mean export or deduplication issues.
- Confirm the requested date appears in output filenames.
- Spot-check known participants in `NMCB_Participants_LDOT__YYYYMMDD.xlsx` (`pt_id`, `pt_type`, `visit_status`, loss flags).
- Verify LDOT and screener files in `data/` were updated **before** the run (check file dates in Finder or `list.files()`).

---

## Troubleshooting

| Issue | What to check |
| ----- | ------------- |
| Path / connection errors | Run from project root — open `Overview.Rproj` first |
| `Missing required columns` | Re-export source file; column names may have changed |
| `No matching file found for prefix` | File name must **start with** the expected prefix and sit in the correct `data/` subfolder |
| Multiple CRL admin files | Keep only one `CRL_admin.xlsx` in `data/CRL Admin/` |
| Numbers look old | Inputs in `data/` were not refreshed before the run |

Full troubleshooting: [`USER_GUIDE.Rmd`](https://github.com/nmcb-fair/nmcb-overview/blob/main/USER_GUIDE.Rmd) in the repo.

---

## When not to use this pipeline

Use Snowflake, a direct Castor export, or a manual count only when:

- the metric is **not implemented** in `nmcb-overview`, or
- a one-off **historical slice** is needed outside current export files.

Document the alternative method in the report footnote. See [Snowflake](../systems/snowflake.md) for non-standard analytics.

---

## Repository layout

```text
nmcb-overview/
├── run_all.R                 ← main entry point
├── ldot_overview.Rmd         ← builds participant overview
├── scripts/get_numbers.R     ← summary tables and plots
├── func/                     ← data loading, criteria, plotting
├── data/                     ← inputs (LDOT, Screening, postcode, CRL Admin)
├── export/
│   ├── overview_participants/
│   └── numbers_and_figures/
├── task/                     ← one-off utilities (not part of routine run)
└── docs/participant_export_columns.md
```

**Requirements:** R packages managed via `renv` — `readr`, `readxl`, `dplyr`, `tidyr`, `stringr`, `lubridate`, `ggplot2`, `openxlsx`, `writexl`, `rmarkdown`.

---

## Related

- [Recurring study routines — Get numbers](../workflows/recurring-routines.md#get-numbers) — cadence and operational context
- [LDOT](../systems/ldot.md) — participant registry; primary overview input
- [Castor EDC](../systems/castor.md) — screener source exports
- [GitHub](../systems/github.md) — `nmcb-overview` repo access
- [Snowflake](../systems/snowflake.md) — use only for metrics outside this pipeline
