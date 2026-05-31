# OMOP CDM mapping

**Status:** Not started

*Map NMCB variables to the **[OMOP Common Data Model](https://www.ohdsi.org/data-standardization/the-common-data-model/)** for interoperable analytics with OHDSI tools. Active work is in **`nmcb-codebook/omop/`**; older conceptual models are archived only.*

---

## Canonical implementation

**Repository:** [github.com/nmcb-fair/nmcb-codebook](https://github.com/nmcb-fair/nmcb-codebook) — folder `omop/`

| Path | Role |
| ---- | ---- |
| `omop/README.md` | Structure and cross-reference contract |
| `omop/metadata/omop_mappings.yaml` | Index of table mapping files |
| `omop/metadata/tables/person.yaml` | Example: `sex` / `dob` → `person.gender_concept_id`, `birth_datetime`, … |
| `omop/metadata/tables/measurement.yaml`, `observation.yaml`, `condition_occurrence.yaml` | Other CDM tables (extend as needed) |
| `omop/sql/omop_etl/` | SQL loaders (e.g. person gender, birth datetime, measurements) |

**Rule:** every `variable_id` in `omop/metadata/tables/*.yaml` must exist in `linkml/metadata/nmcb_codebook_metadata.yaml`. The export script merges OMOP mappings into the generated codebook Excel.

---

## Example: PERSON table

### Manual mapping workbook

Spreadsheet used to document **CDM fields**, **NMCB / Castor sources**, and **concept IDs**:

- **Hand-over copy:** [person-manual-map-v1.xlsx](../files/fair/omop/person-manual-map-v1.xlsx) (from `nmcb-codebook/omop/`)
- **Typical columns:** `OMOP_TABLE`, `CDM_FIELD`, `NMCB_SOURCE`, `NMCB_VARIABLE`, `CASTOR`, value / `CDM_CODE` / OMOP `concept_id` notes

Example mapping rows (conceptual):

| CDM field | NMCB source (examples) |
| --------- | ------------------------ |
| `gender_concept_id` | Castor `sex`, `sex_1`, `sex_2` → concepts 8507 (male), 8532 (female), 46273637 (intersex), … |
| `year_of_birth` / `month_of_birth` / `day_of_birth` | `dob`, `dob_1`, `dob_2` (partial dates) |
| `birth_datetime` | Combined DOB fields |
| `person_source_value` | Participant / device IDs (e.g. Omron, Tanita participant fields) |

### Example OMOP PERSON export (CSV)

Small example output shape: [person-export-example.csv](../files/fair/omop/person-export-example.csv) (columns: `person_id`, `gender_concept_id`, `year_of_birth`, `race_concept_id`, `ethnicity_concept_id`, `person_source_value`, …).

!!! note "ETL quality"
    Example CSV may contain placeholder or test values (e.g. unusual `year_of_birth`) — use only as a **column template**, not production data.

### YAML mapping (git)

Current `person.yaml` entries tie `variable_id` (e.g. `sex`, `dob`) to `omop_column` — see [person.yaml in codebook repo](https://github.com/nmcb-fair/nmcb-codebook/blob/master/omop/metadata/tables/person.yaml).

---

## Training materials (Rowdy — OHDSI / OMOP)

Store on Research Drive under **`NMCB/10. OMOP Data Model/`** (copy into `docs/files/fair/omop/` for git archive if desired):

| File | Purpose |
| ---- | ------- |
| `FAIR en OHDSI.pptx` | FAIR and OHDSI context |
| `Introductie OHDSI en OMOP - Mental health project.pptx` | Introduction to OHDSI / OMOP (mental health example) |

---

## Archive: Hamdi model (no longer used)

Earlier conceptual OMOP-related modelling by previous data manager **Hamdi** — **superseded** by the current `nmcb-codebook/omop/` YAML + ETL approach.

| File | Location |
| ---- | -------- |
| `Hamdi Model.pdf` | Research Drive: `10. OMOP Data Model/Archive/` → archive copy: `docs/files/fair/omop/hamdi-model-archive.pdf` (add when available) |

Keep for historical reference only; do not use for new ETL.

---

## Relation to ontology harmonization

| Layer | Project |
| ----- | ------- |
| **Ontology terms** (SNOMED, LOINC, NCIT) | [Ontology harmonization](ontology-harmonization.md) — semantic layer on variables |
| **OMOP concepts** | This page — CDM tables / `concept_id` for OHDSI analytics |

Both export through `linkml/scripts/export_excel.py` into the unified codebook workbook.

---

## Handover checklist

- [ ] Confirm OHDSI / OMOP target version (CDM v5.x) and vocabulary snapshots used for concept IDs
- [ ] Extend `omop/metadata/tables/*.yaml` for next domains (visits, conditions, labs)
- [ ] Run / document ETL scripts under `omop/sql/omop_etl/` against Snowflake or staging DB
- [ ] Copy Rowdy training decks and Hamdi PDF into `docs/files/fair/omop/` or link Research Drive path in [Where everything lives](../where-everything-lives.md)
- [ ] Align with board task “mapping NMCB data toward OMOP” in [Data architecture](../systems/data-architecture.md)

---

## Related

- [Controlled vocabulary overview](controlled-vocabulary.md)
- [Ontology harmonization](ontology-harmonization.md)
- [Snowflake](../systems/snowflake.md) — possible OMOP staging warehouse
- [GitHub](../systems/github.md) — `nmcb-codebook` migration notes
