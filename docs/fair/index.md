# FAIR-related projects 

**Status:** Not started

*These initiatives are **not** part of day-to-day NMCB operations and currently have **no dedicated follow-up** in the team. They remain documented here for **hand-over** so work can resume (catalogues, PAIS metadata, ontology mapping, OMOP, FDP) without losing context.*

Metadata is a **core component** of FAIR (Findable, Accessible, Interoperable, Reusable). NMCB’s operational metadata today lives mainly in the [codebook](../tasks/nmcb-chatgpt.md), Castor, and [DMP](../tasks/data-management-plan.md); the projects below target **cohort-wide / national / EHDS** layers.

---

## Projects in this folder


| Project                               | Page                                              | Status                                                              |
| ------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------- |
| **FAIR Implementation Profile (FIP)** | [FIP — NMCB FER selections](fair-implementation-profile.md) | Wizard project + Sep 2024 overview (Survey vs Biobank)              |
| **PAIS metadata schema coordination** | [PAIS metadata schema](pais-metadata-schema.md)   | Coordination meeting April 2026; alignment across PAIS initiatives  |
| **FAIR Data Point (Amsterdam UMC)**   | [FAIR Data Point](fair-data-point.md)             | Local / myDRE deployment explored; links to Amsterdam UMC FDP       |
| **Health-RI core metadata schema**    | [Health-RI metadata](health-ri-metadata.md)       | National catalogue / EHDS (HealthDCAT-AP); SHACL + TTL              |
| **Controlled vocabulary**             | [Controlled vocabulary](controlled-vocabulary.md) | Ontology mapping (SNOMED / LOINC / NCIT) + OMOP CDM — see sub-pages |


### Controlled vocabulary (detail)


| Stream                                    | Page                                                |
| ----------------------------------------- | --------------------------------------------------- |
| Ontology harmonization + PCNN publication | [Ontology harmonization](ontology-harmonization.md) |
| OMOP CDM (`PERSON`, YAML, ETL)            | [OMOP CDM mapping](omop-mapping.md)                 |


---

## How this relates to NMCB


| NMCB asset                                                  | FAIR layer                                                                                             |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [NMCB codebook](https://github.com/nmcb-fair/nmcb-codebook) | Variable-level documentation; **LinkML** + **OMOP** + ontology mappings; input to study-level metadata |
| [Data management plan](../tasks/data-management-plan.md)    | Phase 4–5 catalogues (DataverseNL, ACH) named in DMP                                                   |
| [Research Drive](../systems/research-drive.md)              | Storage; not a public metadata catalogue                                                               |
| [myDRE](../systems/mydre.md)                                | Possible host for a **local FDP** instance (see FDP page)                                              |


---

## Attachments in this repo

All binaries live under `docs/files/fair/` (not rendered as site pages; download from git or Research Drive mirror).


| Subfolder        | Files                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `fip/`           | [NMCB FIP overview (XLSX)](../files/fair/fip/nmcb-fip-overview.xlsx), [mini-questionnaire (XLSX)](../files/fair/fip/fip-mini-questionnaire-nmcb.xlsx), [intro notes (DOCX)](../files/fair/fip/fip-documentation.docx) |
| `pais-metadata/` | [PDF](../files/fair/pais-metadata/metadata-schema-coordination-april-2026.pdf), [DOCX](../files/fair/pais-metadata/metadata-schema-coordination-april-2026.docx)                            |
| `fdp/`           | [Replicating FDP in myDRE (PDF)](../files/fair/fdp/replicating-fdp-amsterdamumc-mydre-20241008.pdf)                                                                                         |
| `ontology/`      | [Mapping review workflow (PNG)](../files/fair/ontology/mapping-review-workflow.png); PCNN subset XLSX (add when copied)                                                                     |
| `omop/`          | [person-manual-map v1 (XLSX)](../files/fair/omop/person-manual-map-v1.xlsx), [person CSV example](../files/fair/omop/person-export-example.csv); training PPTX / Hamdi PDF (Research Drive) |


---

## Contacts (from correspondence)


| Topic                                | Contact                                                                                                                                  |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| PAIS coordination / NMCB perspective | Shuxin Zhang — [s.x.zhang@amsterdamumc.nl](mailto:s.x.zhang@amsterdamumc.nl); Jos A. Bosch — [j.a.bosch@uva.nl](mailto:j.a.bosch@uva.nl) |
| Health-RI / EHDS onboarding          | [onboarding@health-ri.nl](mailto:onboarding@health-ri.nl)                                                                                |
| FDP Amsterdam UMC / myDRE            | Sjoerd Manger (Amsterdam UMC — follow up via internal directory)                                                                         |
| DMP / RDM                            | Meriem Manaï — [m.manai@amsterdamumc.nl](mailto:m.manai@amsterdamumc.nl)                                                                 |


---

## Related operational docs

- [Keep in mind (GDPR)](../index.md#keep-in-mind-gdpr-and-data-sharing)
- [Data architecture](../systems/data-architecture.md)
- [GitHub](../systems/github.md) — `nmcb-fair` org for code; FAIR tooling may live in separate repos (e.g. `AmsterdamUMC/FDP_AMS`)

