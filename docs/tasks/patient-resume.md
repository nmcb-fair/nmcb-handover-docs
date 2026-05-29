# Patient resume

**Status:** Active

## Purpose

Generate one **Excel patient summary (resumé)** per participant from Castor EDC exports and supporting study files. The pipeline fills a fixed template (`Resumé` sheet plus illness, medication, NASA test, and laboratory sheets) for ME/CFS screening review, visit preparation, or data-request packages.

Canonical code repository: `[nmcb-fair/patient-resume](https://github.com/nmcb-fair/patient-resume)`

## When to run

- When a participant summary workbook is needed for screening or visit review
- After refreshing Castor exports or supporting inputs (visit, DSQ2, CRL admin, NASA lean, CDL alert)
- Before sharing summary files outside the study team — review `field_capture_report.csv` first

## Inputs

Place or update files under `input/` before running. The loader picks the **newest matching file** in each folder (by modification time).


| Folder / file                       | Contents                                                                                                   |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `input/screening/`                  | Latest `NMCB_Study_ME_CFS_Screener_*export_*.csv/.xlsx` — main screener (`df_me_cfs`)                      |
| `input/screening/`                  | Optional `NMCB_Screening_excel_export_*.xlsx` — `ME_CFS_Screener` sheet for gap-filling                    |
| `input/visit/`                      | Latest `NMCB_Study_*export_*.csv/.xlsx` — visit data; hand grip → D26, `visit_meds`* → medication          |
| `input/visit/` or `input/`          | Optional `NMCB_Measurements_Questionnaires_*export_*` — legacy fallback for older participants             |
| `input/dsq_2/`                      | Latest `NMCB_Study_Symptomen_frequentie_en_ernst_hiervan_*export_*` — Survey Progress → D30                |
| `input/vragenlijsten/`              | Optional `NMCB_Study_Vragenlijsten_*export_*` — supplemental Castor source when primary fields are missing |
| `input/CRL admin/CRL_Admin.xlsx`    | Patient type → D32                                                                                         |
| `input/Omron/NASA_LEAN_TEST.csv`    | NASA lean rows copied to **NASA test** sheet                                                               |
| `input/CDL_alert/` (and subfolders) | Lab CSVs whose filename contains the participant ID → **Laboratorium** sheet                               |
| `template/template.xlsx`            | Excel template (main sheet name: `Resumé`)                                                                 |


## How to run

From the project root in R:

```r
source("run_all.R")
```

### Configure participant IDs

Edit `run_all.R`:

- **Manual mode** (default): set `use_random_ids <- FALSE` and list IDs in `participant_ids_manual`
- **Random sample**: set `use_random_ids <- TRUE`, adjust `n_random_participants` and optional `random_seed`

Other settings in the same file: `template_path`, `output_dir` (`exports_resume`), `sheet_name` (`Resumé`).

### Run modules individually

```r
source("01_load_libraries.R")
source("02_load_data.R")
source("03_mapping.R")
source("04_helper_functions.R")
source("05_export_function.R")

export_participants_resume(
  df = df_me_cfs,
  ids = c("1000175", "0000005"),
  map = map_resume,
  template_path = "template/template.xlsx",
  sheet = "Resumé",
  out_dir = "exports_resume",
  df_visit = df_visit,
  df_dsq2 = df_dsq2,
  df_crl_admin = df_crl_admin,
  df_nasa_lean = df_nasa_lean,
  df_measurements = df_measurements,
  df_vragenlijsten = df_vragenlijsten,
  df_screening_bmi = df_screening_bmi,
  df_screening_excel_me_cfs = df_screening_excel_me_cfs,
  cdl_alert_dir = "input/CDL_alert"
)
```

### Requirements

- R with packages `**readr**` and `**openxlsx**`
- Install once if needed: `install.packages(c("readr", "openxlsx"))`

## What the pipeline does

1. `**01_load_libraries.R**` — loads `readr` and `openxlsx`
2. `**02_load_data.R**` — reads Castor exports and supporting files from `input/`
3. `**03_mapping.R**` — defines `map_resume` (variable → Excel cell or sheet behaviour)
4. `**04_helper_functions.R**` — cell parsing, value transforms (`ja`/`nee`, `vrouw`/`man`), diagnosis text helpers
5. `**05_export_function.R**` — `export_participants_resume()` builds one workbook per ID

For each participant, the exporter:

- Normalizes column names and fuzzy-matches mapped variables
- Matches IDs across datasets (with or without leading zeros)
- Writes direct mappings to the **Resumé** sheet
- Builds illness and medication lists on separate sheets
- Derives fields such as grip-strength average (D26), DSQ survey progress (D30), CRL patient type (D32), NASA/POTS-related summaries, and lab priority from CDL alert
- Copies NASA lean rows and matching CDL lab CSV content into dedicated sheets

Variable-to-cell rules live in `**03_mapping.R`** — change mappings there, not in the export function.

## Outputs


| Output                                    | Purpose                                                              |
| ----------------------------------------- | -------------------------------------------------------------------- |
| `exports_resume/Participant_<ID>.xlsx`    | One filled workbook per participant                                  |
| `exports_resume/field_capture_report.csv` | Audit log: field, target cell, status, value preview, source dataset |


Review `**field_capture_report.csv**` for missing mappings, skipped fields, or unexpected empty values before distributing files.

IDs not found in the ME/CFS screener export are skipped with a console warning.

## Quality checks

- Confirm the latest Castor exports are in the correct `input/` subfolders (check file dates)
- Ensure `CRL_Admin.xlsx` and `NASA_LEAN_TEST.csv` are current when D32 or NASA sheets matter
- Place CDL alert CSVs under `input/CDL_alert/` with participant ID in the filename
- Open a sample `Participant_<ID>.xlsx` against the template layout
- Scan `field_capture_report.csv` for `status` values that indicate gaps
- Do **not** commit or share real participant data in issues, screenshots, or git history

## Privacy

Do not upload real participant exports or generated resumes to GitHub issues, pull requests, commits, or public logs. Use synthetic or redacted examples when reporting bugs.

## Related

- [Castor EDC](../systems/castor.md) — source of screening and visit exports
- [CDL alert workflow](../workflows/cdl-alert-workflow.md) — laboratory alert files used for the **Laboratorium** sheet
- [Recurring study routines](../workflows/recurring-routines.md) — CRL admin and patient type maintenance
- [GitHub](../systems/github.md) — repository list including `patient-resume`
- Upstream repository README: [patient-resume](https://github.com/nmcb-fair/patient-resume)

## Notes

- Legacy workflow: `generate_patient_resume.Rmd` (reference only; use the modular `.R` scripts)
- Modules must be sourced in order (`01` → `05`)
- Mapping operations include direct writes, `ja_nee`, `vrouw_man`, `no_decimal`, `add_to_list`, `add_to_sheet`, and `add_text_to_sheet` — see `03_mapping.R` for the full table

