# OpenSpecimen

**Status:** Ongoing

*Role: authoritative sample inventory for the Amsterdam UMC biobank; supports sample request and status reporting.*

OpenSpecimen tracks **where** each aliquot is stored and **what** it is. Broader biobank context—submission files, external-lab mappings, and data flow—is in [Biobank data](biobank.md).

## Purpose

- Sample inventory and storage location (container, box, position)
- Link specimens to participants and visits
- Feed [Sample request workflow](../workflows/sample-request-workflow.md) via CSV exports

## Access

OpenSpecimen access is granted by the biobank team. For new accounts or role changes, contact **Erik van Iperen** (see [Biobank contacts](biobank.md#contacts-amsterdam-umc-biobank)).

Document who on the data team has which role once access is stable.

## Key fields (exports and queries)

When you export or build a query, use these fields consistently:


| OpenSpecimen field              | Use in NMCB                             | Notes                                                         |
| ------------------------------- | --------------------------------------- | ------------------------------------------------------------- |
| `Participant.PPID`              | Participant / internal ID               | Use **PPID**, not a generic “Participant ID” label in exports |
| `Specimen.Barcode`              | Specimen identifier                     | Used in sample-request scripts and aliquot selection          |
| `Specimen.Type`                 | Sample type (with additive / container) | See [sample type mapping](#nmcb-sample-type-mapping) below    |
| `Specimen.Additive`             | Distinguishes plasma sub-types          | Required when `Specimen.Type` alone is ambiguous              |
| `Specimen.Collection.Container` | Tube / container label                  | Second discriminator for some types                           |
| Concentration fields            | e.g. PBMC Ficoll totals                 | Document exact column names in your saved query export        |


**Participant ID linkage:** `Participant.PPID` aligns with NMCB **Internal_ID** / Castor participant identifiers used in CRL Admin and sample-request pipelines.

## NMCB sample type mapping

NMCB standardises sample types in scripts (e.g. `track_biobank.Rmd`). In OpenSpecimen, the same material may appear under different `Specimen.Type`, `Specimen.Additive`, and container combinations. Use this table when defining queries or interpreting exports:


| NMCB sample type | `Specimen.Type` (contains)                         | `Specimen.Additive` (contains) | `Specimen.Collection.Container` (equals) |
| ---------------- | -------------------------------------------------- | ------------------------------ | ---------------------------------------- |
| DNA              | DNA                                                | —                              | —                                        |
| SERUM            | Serum                                              | —                              | —                                        |
| EDTA             | Plasma                                             | EDTA                           | —                                        |
| EDTA             | Plasma                                             | —                              | BD Vacutainer EDTA 10 mL                 |
| HEP              | Plasma                                             | Heparin                        | —                                        |
| HEP              | Plasma                                             | —                              | BD Vacutainer Heparin (gel) 3 mL         |
| CITRAAT          | Plasma                                             | Citrate                        | —                                        |
| CITRAAT          | Plasma                                             | —                              | BD Vacutainer Citrate 2.7 mL             |
| PAXGENE RNA      | Blood                                              | PAXgene RNA                    | —                                        |
| PAXGENE RNA      | Blood                                              | —                              | BD Vacutainer PAXgene RNA Tube 10 mL     |
| PBMC FICOLL      | Cells - PBMC (Peripheral Blood Mono Nuclear Cells) | Heparin                        | —                                        |
| PBMC FICOLL      | Cells - PBMC (Peripheral Blood Mono Nuclear Cells) | —                              | BD Vacutainer Heparin 9 mL               |
| PBMC CPT         | Cells - PBMC (Peripheral Blood Mono Nuclear Cells) | Na-Citrate (CPT)               | —                                        |
| PBMC CPT         | Cells - PBMC (Peripheral Blood Mono Nuclear Cells) | —                              | BD Vacutainer CPT 8 mL                   |


Source: [Understand OpenSpecimen](../files/biobank/Understnd%20OS.xlsx) (same rules as above; maintained in the biobank file set).

## Reference materials


| Resource                                                                                                  | Description                               |
| --------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| [Understand OpenSpecimen](../files/biobank/Understnd%20OS.xlsx)                                           | Field notes and sample-type mapping rules |
| [Quick Start on Using OpenSpecimen](../files/openspecimen/Quick%20Start%20on%20Using%20OpenSpecimen.pptx) | Introductory slides for new users         |


## Export for sample requests

The [Sample request workflow](../workflows/sample-request-workflow.md) expects a recent OpenSpecimen CSV export, typically:

```text
data/openspecimen/query_198_*.csv
```

**Suggested routine:**

1. Run or refresh the saved query that returns **all NMCB samples** (include PPID, barcode, type, additive, container, concentration, and mother-tube fields needed for requests).
2. Save the export with a dated filename under the sample-request project `data/openspecimen/` folder.
3. Run `track_biobank.Rmd` before generating a new request so specimen and participant status files use the latest inventory.

## Handover checklist

- Document the saved query name/ID for “all NMCB samples” and who may edit it
- Confirm export column list matches `track_biobank.Rmd` expectations
- Record access roles (view vs edit) for data team members
- After OpenSpecimen or container naming changes, update [Understand OpenSpecimen](../files/biobank/Understnd%20OS.xlsx) and this mapping table if rules change

## Related

- [Biobank data](biobank.md) — codebook, biobank flow, and Amsterdam UMC contacts
- [Sample request workflow](../workflows/sample-request-workflow.md) — `track_biobank.Rmd` and request generation
- [Multi-centre sample data workflow](../workflows/multicentre-sample-data-workflow.md) — data before specimens enter OpenSpecimen

