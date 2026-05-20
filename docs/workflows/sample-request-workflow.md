# Sample Request Workflow

**Status:** Complete

This page documents the **Sample Request** project under `github.com/nmcb-fair/sample-request`. The project turns CRL Admin, OpenSpecimen, and screening exports into reproducible **participant-level** and **specimen-level** outputs for sample release requests.

The workflow has two layers:

1. **Base data preparation** in `track_biobank.Rmd`
2. **Request generation** using reusable and project-specific R Markdown files under `request/`

## Purpose

The project supports requests such as:

- select participants by `Patient type`
- require a minimum number of available aliquots for one or more sample types
- prioritize participants with more aliquots
- select one or more random aliquots per participant
- generate pseudonymized exports and `Samplegegevens` files for release

## Main Inputs

### Core inputs

- `data/crl_admin/CRL*admin*.xlsx`
- `data/openspecimen/query_198_*.csv`
- `data/screener/*.csv`

### Derived inputs used by request scripts

`track_biobank.Rmd` creates the derived files that downstream request scripts use:

- `exports/biosample_status/<date>/biosample_status_<date>.csv`
- `exports/biosample_status/<date>/participant_sample_status_<date>.xlsx`

The downstream request workflow should normally use these exports rather than re-reading CRL Admin directly.

## Supported Sample Types

The current `track_biobank.Rmd` sample-type mapping supports:

- `DNA`
- `SERUM`
- `EDTA`
- `HEP`
- `CITRAAT`
- `PAXGENE RNA`
- `PBMC FICOLL`
- `PBMC CPT`

In addition, `participant_sample_status_*.xlsx` can include derived participant-level fields such as:

- `pbmc_ficoll_conc_total`
- `age` / `sex`
- `Patient type`
- ME/CFS screening indicators such as `dsq_cdc`, `dsq_ccc`, `dsq_iom`, `calckps`

## Base Workflow: `track_biobank.Rmd`

`track_biobank.Rmd` is the foundational document for the sample request pipeline.

It performs the following steps:

1. Loads CRL Admin.
2. Loads the latest OpenSpecimen export.
3. Maps raw OpenSpecimen rows to standardized `sample_type` values.
4. Writes specimen-level export `biosample_status_<date>.csv`.
5. Aggregates per-participant counts per sample type.
6. Calculates `pbmc_ficoll_conc_total`.
7. Loads and merges screener data.
8. Writes participant-level export `participant_sample_status_<date>.xlsx`.

This means request-generation scripts can work from a stable, already-merged participant table and a stable specimen table.

## Request Generation Layer

### Generic reusable workflow

The main reusable request engine is:

- `request/stratified_sample_selection.Rmd`

This script supports parameterized requests with:

- `project_code`
- `sample_types`
- `min_aliquots_eligibility`
- `n_aliquots_pick`
- `n_per_group`
- `prioritize_by_aliquot_count`
- `group_definitions`
- `participant_status_xlsx`
- `random_seed`

`group_definitions` is the scalable grouping mechanism. Format:

```text
Group label=Patient type A;Patient type B|Other group=Other type
```

Example:

```text
Post-COVID=Post-COVID|Healthy Control=Gezonde Controle|Lyme=Lyme
```

Behavior:

- one request can define any number of patient groups
- each group receives the same `n_per_group`
- if `prioritize_by_aliquot_count = TRUE`, participants with more aliquots of the first requested sample type are selected first
- random aliquots are then picked from `biosample_status_*.csv`

### One-off / project-specific request scripts

There are also request-specific Rmds for special logic:

- `request/P006_20260324/P006_selection.Rmd`
  - EDTA request
  - PBMC Ficoll concentration threshold
  - project-specific exports
- `request/P004_Niels/P004_selection.Rmd`
  - DNA request
  - participant priority by higher DNA count
- `request/P002_Brent_20251217/P002_serum_postcovid_selection.Rmd`
  - one SERUM aliquot for Post-COVID participants
  - excludes participants with `SERUM <= 2`
  - can exclude previously mapped P002 participants
- `request/P001_Marjan_20251205/P001_Marjan_raaplijst_participant_link.Rmd`
  - older request-specific workflow for raaplijst / participant linking

These scripts are useful examples of custom logic when the generic runner is not enough.

## Pseudonymization

Pseudonyms are generated via:

- `generate_pseudonym_mapping.R`

This script maintains per-project mapping files:

- `mapping_table/NMCB_<project_code>_pseudonym_mapping.csv`

Behavior:

- keeps existing `Internal_ID -> External_ID` mappings stable
- adds new pseudonyms only for new internal IDs
- outputs `External_ID` values in the form `NMCB-<project_code>-<suffix>`

## Nontechnical Runner

To make routine requests executable by nontechnical colleagues, the project includes:

- `request/sample_request_template.xlsx`
- `request/sample_request_template.csv`
- `request/run_sample_request.R`
- `request/run_sample_request.command` for macOS
- `request/run_sample_request.bat` for Windows
- `request/README.md`

### Excel template

`sample_request_template.xlsx` is the preferred front-end for users.

It contains:

- `requests` sheet: fill-in form
- `guide` sheet: field explanations, examples, and supported sample types

### Runner script

`run_sample_request.R`:

- reads the request template
- validates the row(s)
- renders `request/stratified_sample_selection.Rmd`
- creates `request/<project_code>/`
- writes request snapshots and outputs

It supports both:

- `.xlsx`
- `.csv`

## End-User Steps

These are the current practical run steps from `request/README.md`:

1. Run `track_biobank.Rmd` first so the latest exports exist under `exports/biosample_status/`.
2. Open `request/sample_request_template.xlsx` in Excel.
3. Edit the row you want to run.
4. Set `enabled` to `TRUE`.
5. Run:
  - macOS: double-click `run_sample_request.command`
  - Windows: double-click `run_sample_request.bat`
6. Wait for the Terminal / Command Prompt window to finish.
7. Open `request/<project_code>/` for the HTML report and `exports/`.

## Template Fields

The current request template includes:

- `enabled`
- `project_code`
- `sample_types`
- `min_aliquots_eligibility`
- `n_aliquots_pick`
- `n_per_group`
- `prioritize_by_aliquot_count`
- `group_definitions`
- `participant_status_xlsx`
- `random_seed`
- `notes`

## Outputs

Typical outputs are:

- `request/<project_code>/<project_code>_selection_<date>.html`
- `request/<project_code>/exports/*`
- `Samplegegevens/Samplegegevens_<project_code>.xlsx`

Common export contents include:

- eligible participant pool
- selected aliquots
- participant key (`External_ID`, `Internal_ID`, age, sex, patient type)
- Samplegegevens export with `External_ID` plus specimen columns

## Platform / Dependency Notes

### Operating systems

The workflow is now prepared for both:

- macOS
- Windows

### Software requirements

The runner requires:

- R
- `rmarkdown`
- `openxlsx`
- `readxl`
- Pandoc

For nontechnical users, the easiest recommendation is:

- install **RStudio Desktop**, because it provides a straightforward R environment and includes Pandoc

The runner now stops early with a friendly message if Pandoc is missing.

## Current Limitations / Handover Notes

- `track_biobank.Rmd` still remains the required first step before request generation.
- Some older request folders use custom one-off logic rather than the generic runner.
- The generic runner is designed for standard stratified selection, but very specific request rules may still need a dedicated Rmd.
- Mapping files in `mapping_table/` are cumulative and should be treated as project records.

## Related

- [Data request workflow](data-request-workflow.md)
- [Multi-centre sample data workflow](multicentre-sample-data-workflow.md)

