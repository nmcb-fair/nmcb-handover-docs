# ACS data clean

**Status:** Complete

## Purpose

Clean raw **Amsterdam Cognitive Scan (ACS)** CSV exports into headered, column-aligned files ready for QC and downstream use. Raw ACS files have **no headers**; this task applies the matching NMCB template, corrects common row shifts, filters test tokens, and writes audit logs.

Canonical code repository: `[nmcb-fair/acs-data-clean](https://github.com/nmcb-fair/acs-data-clean)`

## When to run

- Biweekly
- Before merging ACS outputs with participant IDs or uploading to structured storage

## Inputs

Place files in the repository before running:


| Folder    | Contents                                                                                |
| --------- | --------------------------------------------------------------------------------------- |
| `raw/`    | Raw ACS CSV files **without headers**, e.g. `acs-nmcb-1.csv` … `acs-nmcb-6.csv`         |
| `header/` | Matching one-row template files, e.g. `nmcb-acs-header-1.csv` … `nmcb-acs-header-6.csv` |


**Naming rule (batch mode):** the number must match between raw and header:

- `raw/acs-nmcb-4.csv` → `header/nmcb-acs-header-4.csv`

Extra copies such as `acs-nmcb-2 copy.csv` are ignored by the standard batch command.

## How to run

### Standard batch (files 1–6)

From the project root:

```bash
Rscript process_acs.R
```

This processes `raw/acs-nmcb-1.csv` through `acs-nmcb-6.csv` with their matching headers.

### Single file

```bash
Rscript process_acs.R --raw raw/acs-nmcb-2.csv --header header/nmcb-acs-header-2.csv
```

Optional explicit output path:

```bash
Rscript process_acs.R --raw raw/acs-nmcb-2.csv --header header/nmcb-acs-header-2.csv --out export/YYYYMMDD/acs-nmcb-2.csv
```

### Token filtering (NMCB default)

By default, only rows where `O_token` starts with `**nmcb**` are kept (test rows such as `marysetest` are excluded).

- Keep all rows (other studies): `Rscript process_acs.R --token-prefix all`
- Custom prefix: `Rscript process_acs.R --token-prefix studyabc`

### Requirements

- R with package `**data.table**`
- Install once if needed: `install.packages("data.table")`

## What the cleaning does

1. Reads the header/template row.
2. Reads each raw data row.
3. Expands packed questionnaire values like `1|Question text|0` into separate columns.
4. Places values under the correct template columns.
5. Uses checkpoint words (`message`, `video`, `questionnaire`, `mousetype`, etc.) to detect and correct shifts.
6. Writes cleaned CSVs and log files.
7. Excludes non-`nmcb` test rows unless token filtering is disabled.

Reusable functions live in `R/acs_cleaning.R`; most users run `process_acs.R` only.

## Outputs

Cleaned files are written to a **dated folder** under `export/`, e.g. `export/20260526/`:


| File                                    | Purpose                                                  |
| --------------------------------------- | -------------------------------------------------------- |
| `acs-nmcb-*.csv`                        | Cleaned data with headers                                |
| `deleted_cells_log.csv`                 | Values removed during checkpoint correction (batch mode) |
| `generalized_rule_misalignment_log.csv` | Remaining alignment warnings (batch mode)                |
| `README.md`                             | Run summary: row counts, completeness, incomplete tokens |


For single-file runs, logs are named after the output stem, e.g. `acs-nmcb-2_deleted_cells_log.csv`.

Each dated export folder also includes a generated **README** with:

- exported / complete / incomplete row counts
- per-battery-file breakdown
- list of incomplete participant tokens
- short description of the cleaning steps applied

## Completeness rule (NMCB)

A participant row is treated as **complete** when both are non-empty:

- `O_34_time_t`
- `O_34_type`

These belong to the mouse-type task near the end of the battery. Missing either value → row counts as **incomplete**, even if earlier tasks contain data. Do not treat incomplete rows as finished sessions.

Each battery file is exported separately; a participant appears in **only one** of the six files.

## Quality checks

- Confirm raw and header file numbers match before batch run.
- Review `deleted_cells_log.csv` for unexpected checkpoint deletions.
- Review `generalized_rule_misalignment_log.csv` for alignment warnings.
- Check export `README.md` incomplete-token list against visit log / Castor status.
- Compare row counts to previous export run; large jumps may indicate wrong raw drop or template mismatch.
- Do **not** commit or share real participant tokens in issues, screenshots, or git history.

## Privacy

Do not upload real ACS participant data to GitHub issues, pull requests, commits, or public logs. Use synthetic examples from `examples/` when reporting bugs.

## Related

- [Device data workflow](../workflows/device-data-workflow.md) — where ACS fits in the device pipeline
- [Devices](../systems/devices.md) — Amsterdam Cognitive Scan setup and output notes
- [Recurring study routines](../workflows/recurring-routines.md) — visit data log tracks whether ACS raw files were collected
- Upstream repository README: [acs-data-clean](https://github.com/nmcb-fair/acs-data-clean)

## Releases and citation

For stable reuse, prefer a [GitHub release](https://github.com/nmcb-fair/acs-data-clean/releases) tag rather than an arbitrary branch snapshot. Citation metadata is in `CITATION.cff` in the code repository.