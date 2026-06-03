# Update NMCB codebook


Keep the **NMCB codebook** aligned with study changes — new or renamed Castor fields, value sets, questionnaires, device columns, OMOP mappings, or ontology terms.

Canonical repository: **[github.com/nmcb-fair/nmcb-codebook](https://github.com/nmcb-fair/nmcb-codebook)**

The codebook documents **what variables exist**, their labels, types, allowed values, and cross-study mappings. Downstream tools (data packages, ChatGPT discovery, OMOP ETL, biobank mappings) assume it stays current.

---

## When to update

Run this task after any change that affects variable meaning or structure:

- **Castor** — new/changed forms, fields, calculations, or response options ([Castor EDC](../systems/castor.md))
- **Devices** — new export columns or renamed fields ([Devices](../systems/devices.md))
- **Questionnaires / visits** — new instruments, sections, or scoring rules
- **Mappings** — biobank, OMOP, or ontology harmonization work ([OMOP mapping](../fair/omop-mapping.md), [Ontology harmonization](../fair/ontology-harmonization.md))
- **Researcher-facing exports** — before sharing an updated Excel codebook or refreshing [NMCB ChatGPT](nmcb-chatgpt.md) knowledge files

!!! tip "Rule of thumb"
    If a data steward or researcher would ask *“what does this column mean?”* or *“what are the allowed values?”*, the codebook should already reflect the answer.

---

## Source of truth

| Layer | Path in repo | Role |
| ----- | ------------ | ---- |
| **Variable metadata (primary)** | `linkml/metadata/nmcb_codebook_metadata.yaml` | Datasets, variables, value sets, labels, types |
| **Schema (structure)** | `linkml/schema/nmcb_codebook_schema.yaml` | Allowed object types and fields — change only when adding new metadata concepts |
| **Excel export (generated view)** | `linkml/exports/nmcb_codebook.xlsx` | Researcher-friendly workbook — **regenerate** after YAML changes |
| **Legacy Excel (reference)** | `linkml/exports/NMCB Codebook v6.0.xlsx` | Older baseline export; do not treat as authoritative |
| **OMOP mappings** | `omop/metadata/tables/*.yaml` | CDM table/column/concept links — must reference existing `variable_id` values |
| **Export layout** | `linkml/config/excel_categories.yaml`, `linkml/scripts/export_excel.py` | Sheet names, column order, display headers |

**Preferred workflow:** edit **LinkML YAML** (and OMOP YAML if applicable), then regenerate Excel.

**Excel-only edits** are acceptable for a quick fix or review pass, but you must **back-port changes into YAML** before committing — otherwise the next export will overwrite your Excel edits and git history will not reflect the true source.

---

## Repository layout

```text
nmcb-codebook/
├── linkml/
│   ├── metadata/
│   │   └── nmcb_codebook_metadata.yaml   ← variables, value sets (main edit target)
│   ├── schema/
│   │   └── nmcb_codebook_schema.yaml     ← LinkML class definitions
│   ├── config/
│   │   ├── excel_categories.yaml         ← sheet / section groupings for export
│   │   └── me_cfs_screener_translations.yaml
│   ├── scripts/
│   │   └── export_excel.py               ← YAML → Excel
│   └── exports/
│       └── nmcb_codebook.xlsx            ← generated output
└── omop/
    ├── metadata/tables/*.yaml            ← OMOP mappings by CDM table
    └── sql/omop_etl/                     ← example ETL scripts
```

See also [Controlled vocabulary](../fair/controlled-vocabulary.md) and [Where data lives](../where-data-lives.md) for how the codebook fits the wider data map.

---

## Workflow

### 1. Identify what changed

Compare the live source (Castor export, device file, form spec) with the current codebook:

- new, renamed, or removed **variable names**
- **label** or **description** changes
- **field type** corrections (numeric, date, categorical, …)
- **value set** changes (codes, labels, dependencies)
- new **dataset / section** (questionnaire, visit form, device)

Document the trigger (e.g. Castor form version, ticket, or study team request) in your commit message.

### 2. Update metadata (LinkML path — recommended)

Edit `linkml/metadata/nmcb_codebook_metadata.yaml`:

| Change type | What to edit |
| ----------- | ------------ |
| New variable | Add under `variables:` with stable `id`, `name`, `label`, `exported_field_type`, optional `value_set` |
| Value set | Add or update under `value_sets:` (`codes` with `code` + `label`) |
| New questionnaire / form block | Add `datasets:` entry and link variables via dataset/group fields |
| Label / type fix | Update the existing variable entry |

Detailed field guide: [linkml/metadata/README.md](https://github.com/nmcb-fair/nmcb-codebook/blob/master/linkml/metadata/README.md) in the repo.

If you add a **new kind of metadata field**, extend `linkml/schema/nmcb_codebook_schema.yaml` first, then populate instances in the metadata file.

### 3. Update OMOP mappings (if applicable)

When variables map to the OMOP CDM, edit the relevant file under `omop/metadata/tables/` (e.g. `person.yaml`, `measurement.yaml`).

**Contract:** every `variable_id` in OMOP YAML **must** exist in `nmcb_codebook_metadata.yaml`. The export script merges OMOP columns into the Excel workbook automatically.

See [OMOP mapping](../fair/omop-mapping.md) for examples and ETL context.

### 4. Regenerate Excel

From the repo root, with Python 3 and dependencies installed:

```bash
cd linkml/scripts
python export_excel.py
```

**Dependencies:** `pandas`, `openpyxl`, `pyyaml` (install via `pip` if needed).

Output: `linkml/exports/nmcb_codebook.xlsx`

To change **which sheets or columns** appear in Excel, edit `linkml/config/excel_categories.yaml` and/or column settings in `export_excel.py` — see [linkml/scripts/README.md](https://github.com/nmcb-fair/nmcb-codebook/blob/master/linkml/scripts/README.md).

### 5. Excel path (alternative)

If you start from Excel (e.g. reviewing with a study member):

1. Edit `linkml/exports/nmcb_codebook.xlsx` or the shared workbook copy on Research Drive.
2. **Transfer every change** back into `nmcb_codebook_metadata.yaml` (and OMOP YAML if OMOP columns changed).
3. Run `export_excel.py` and confirm the regenerated file matches your reviewed Excel.
4. Do **not** commit Excel-only changes without the matching YAML update.

### 6. Commit and communicate

```bash
git add linkml/metadata/nmcb_codebook_metadata.yaml
git add omop/metadata/tables/   # if changed
git add linkml/exports/nmcb_codebook.xlsx
git commit -m "codebook: <short description of what changed and why>"
git push
```

Tell downstream consumers when the update matters outside git:

- [NMCB ChatGPT](nmcb-chatgpt.md) — regenerate and re-upload enriched CSV knowledge files
- [Data request](data-request.md) — refresh `data pool/` Castor exports if block definitions depend on new fields
- Study team / RDM — share updated Excel or release note if researchers rely on a fixed workbook version

---

## Alignment checklist

Use this before closing a codebook update:

- [ ] Every changed Castor / device / form field has a matching variable (or deliberate deprecation note)
- [ ] Value sets match live export codes and labels (spot-check a few rows from a fresh Castor CSV)
- [ ] `export_excel.py` runs without error; `linkml/exports/nmcb_codebook.xlsx` is regenerated
- [ ] OMOP `variable_id` references still resolve (no orphan mappings)
- [ ] Schema changes (if any) are reflected in both `nmcb_codebook_schema.yaml` and metadata instances
- [ ] Git commit includes YAML **and** generated Excel (not Excel alone)
- [ ] Downstream artefacts updated if needed (ChatGPT CSVs, Research Drive copy, request block docs)

---

## Related

- [NMCB ChatGPT](nmcb-chatgpt.md) — variable discovery; refresh after codebook changes
- [Data request](data-request.md) — extraction blocks use codebook variable names
- [Castor EDC](../systems/castor.md) — primary eCRF source for most variables
- [OMOP mapping](../fair/omop-mapping.md) — CDM mappings in `omop/`
- [Ontology harmonization](../fair/ontology-harmonization.md) — SNOMED / LOINC / NCIT layer
- [GitHub](../systems/github.md) — `nmcb-codebook` repo access and migration notes
- [Where data lives](../where-data-lives.md) — codebook location in the data map
