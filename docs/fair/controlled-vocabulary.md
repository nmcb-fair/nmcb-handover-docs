# Controlled vocabulary (FAIR)


*Semantic interoperability for NMCB / PCNN: **ontology-backed variable mappings** and **OMOP CDM** alignment. No active follow-up currently; documented for handover. Supports the **Interoperable** and **Reusable** FAIR principles alongside study-level metadata ([FAIR overview](index.md)).*

---

## Two project streams

| Stream | Page | Output |
| ------ | ---- | ------ |
| **1. Ontology harmonization** (SNOMED CT, LOINC, NCIT, …) | [Ontology harmonization](ontology-harmonization.md) | Machine-readable variable ↔ term pairs; PCNN codebook integration; expert review workflow |
| **2. OMOP CDM mapping** | [OMOP CDM mapping](omop-mapping.md) | Table-level mappings (e.g. `PERSON`); YAML + ETL in `nmcb-codebook`; training from OHDSI |

Both build on the canonical **[nmcb-codebook](https://github.com/nmcb-fair/nmcb-codebook)** repository (`linkml/` + `omop/`).

---

## Canonical code repository

| Path in `nmcb-codebook` | Role |
| ----------------------- | ---- |
| `linkml/metadata/nmcb_codebook_metadata.yaml` | Variable definitions, value sets |
| `linkml/schema/nmcb_codebook_schema.yaml` | **LinkML** schema (next-step formalization) |
| `linkml/scripts/export_excel.py` | Excel export merging metadata + OMOP mappings |
| `omop/metadata/tables/*.yaml` | OMOP mappings by CDM table |
| `omop/sql/omop_etl/` | Example load scripts |

---

## Attachments in this hand-over repo

| Subfolder | Files |
| --------- | ----- |
| `docs/files/fair/ontology/` | [Mapping review workflow (PNG)](../files/fair/ontology/mapping-review-workflow.png) |
| `docs/files/fair/omop/` | [person-manual-map v1 (XLSX)](../files/fair/omop/person-manual-map-v1.xlsx), [person export example (CSV)](../files/fair/omop/person-export-example.csv) |

**Copy to repo when available** (from Downloads / Research Drive):

- `codebook_curated_pcnn_subset_MIE_2026.xlsx` → `docs/files/fair/ontology/codebook-curated-pcnn-subset-MIE-2026.xlsx`
- OMOP training: `FAIR en OHDSI.pptx`, `Introductie OHDSI en OMOP - Mental health project.pptx`, `Archive/Hamdi Model.pdf` → `docs/files/fair/omop/`

Live copies may also sit under Research Drive `data management/` or `10. OMOP Data Model/`.

---

## Related

- [PAIS metadata schema](pais-metadata-schema.md) — study-level vs variable-level metadata
- [NMCB ChatGPT](../tasks/nmcb-chatgpt.md) — variable discovery on exported codebook CSVs
- [Data flow (home)](../index.md#end-to-end-data-flow)
