# Where data lives


Map of **where NMCB data and related operational resources are stored**. For how data **moves** from capture to Snowflake (clickable diagram), see the [home page — End-to-end data flow](index.md#end-to-end-data-flow).

Paths below are relative to the NMCB **Research Drive project folder** unless another system is named. Site-specific trees use `Amsterdam/` and `Radboud/`; each site typically follows `organized` → `processed` → `analyzed` → `archive`. See [Research Drive](systems/research-drive.md) for the top-level layout and sensitivity rules.

---

## Research Drive lifecycle (reminder)


| Stage               | Meaning                                         | Examples                                                                                           |
| ------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **organized** (raw) | Incoming exports, not yet split per participant | `organized/CDL/{YYYYMMDD}/`, `organized/RDL/{YYYYMMDD}/`, device drops under `organized/{device}/` |
| **processed**       | Data-team outputs ready for analysis or upload  | Per-participant CDL CSVs, `processed/RDL/`, `Radboud/processed/Biobank/`                           |
| **analyzed**        | Clinical review, alerts, derived QC             | `analyzed/CDL/` (alert folders), `analyzed/RDL/RDL_alert/`                                         |
| **archive**         | Superseded inputs after successful processing   | Dated CDL/RDL folders moved after processing                                                       |


Do not overwrite the only copy of raw data; add dated folders or move to `Archive` / `archive` as described in each [workflow](workflows/index.md).

---

## Data by type

### Study capture and questionnaires


| What                                             | Where                                                                                                | Notes                                                                   |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Castor EDC** (live eCRF, surveys, study logic) | **Castor** (cloud) — [Castor EDC](systems/castor.md)                                                 | Source of truth for participant forms; export for checks and packages   |
| Castor exports used in coding / requests         | Research Drive and/or `data pool/` in [data-request](https://github.com/nmcb-fair/data-request) repo | Refreshed before package builds — [Data request](tasks/data-request.md) |


### Central lab — CDL (Amsterdam / CRL)


| What                                                 | Where                                                                             | Notes                                                                                    |
| ---------------------------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Raw CDL files + `CRL admin`                          | `organized/CDL/{YYYYMMDD}/`                                                       | Mailbox → Research Drive Mon/Thu — [CDL alert workflow](workflows/cdl-alert-workflow.md) |
| Processed lab result + alert files (per participant) | Under CDL **processed** tree (then inputs archived)                               | Produced by data team same day                                                           |
| **CDL alert files for clinical review**              | `analyzed/CDL/` — subfolders such as `**ALERT`**, `**Afwijkend**`, `**Archived**` | Nurse/physician review Fri/Tue; informed participants → `Archived`                       |


### Radboud lab — RDL and blood-tube (RL) files


| What                         | Where                                                                                 | Notes                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Raw RDL export               | `organized/RDL/` → dated `organized/RDL/{YYYYMMDD}/`                                  | With Radboud Visit Data Log — [RDL alert workflow](workflows/rdl-alert-workflow.md) |
| Processed RDL results        | `processed/RDL/{YYYYMMDD}/`                                                           | For Snowflake and downstream use                                                    |
| RDL alert outputs            | `analyzed/RDL/RDL_alert/`                                                             | Parallel to CDL alert pattern                                                       |
| Raw RL blood-tube file       | Agreed Radboud upload location (then `Radboud/organized/RL/archive` after processing) | [Multi-centre sample data workflow](workflows/multicentre-sample-data-workflow.md)  |
| Processed RL per participant | `Radboud/processed/RL/` (e.g. `processed_{participant_ID}_RL.csv`)                    |                                                                                     |


### Biobank and samples


| What                                                | Where                                                                                                         | Notes                                      |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Box data files** (boxing / hand-off spreadsheets) | Research Drive `**organized/`** and/or `**processed/**` **biobank** areas (e.g. `Radboud/processed/Biobank/`) | Rename per workflow before upload          |
| Submission / mapping working files                  | Research Drive biobank-related folders + [reference XLSX in repo](systems/biobank.md#reference-files)         | Variable and sample-type mappings          |
| **Final sample inventory, locations, requests**     | **OpenSpecimen** — [OpenSpecimen](systems/openspecimen.md)                                                    | Authoritative for “where is this aliquot?” |
| Physical samples                                    | Amsterdam UMC biobank (and partner sites per protocol)                                                        | Linked from OpenSpecimen records           |


### Devices (VU-AMS, Omron, Nellcor, Tanita, …)


| What                   | Where                                                           | Notes                                                                                                                 |
| ---------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Raw device exports     | Research Drive `organized/{device}/` (e.g. `organized/VU_AMS/`) | [Device data workflow](workflows/device-data-workflow.md), [Devices](systems/devices.md)                              |
| QC and cleaned outputs | Research Drive processed/QC paths per device                    | [Devices](systems/devices.md), [Device data workflow](workflows/device-data-workflow.md), [GitHub](systems/github.md) |


### Structured analytics and code


| What                                     | Where                                                                                                                               | Notes                                                                         |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Snowflake** (structured cohort tables) | Snowflake account / schemas (provisioned per project)                                                                               | Fed from processed Research Drive exports — [Snowflake](systems/snowflake.md) |
| Cleaning and ETL scripts                 | [GitHub `nmcb-fair](systems/github.md)` org + Research Drive `data infrastructure/`                                                 | Version scripts with outputs                                                  |
| Researcher **data packages**             | Built in [data-request](tasks/data-request.md) from `data pool/` → delivered via approved channel ([myDRE](systems/mydre.md), etc.) |                                                                               |


### Participant registry and operational logs


| What                                            | Where                                                                         | Notes                                                                 |
| ----------------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **LDOT** (registry / logistics)                 | LDOT Manager + exports under Research Drive `data/LDOT/`                      | [LDOT](systems/ldot.md)                                               |
| Visit log, subject ID log, mailbox-driven files | Research Drive operational folders — **confirm exact paths with coordinator** | Listed in [Recurring study routines](workflows/recurring-routines.md) |


### Sensitive data (exception path)


| What                                             | Where                            | Notes                                                                                                                              |
| ------------------------------------------------ | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| High-sensitivity files **not** on Research Drive | **YoDa / iRODS** (when approved) | Default remains Research Drive for agreed tiers — [Research Drive vs YoDa](systems/research-drive.md#research-drive-vs-yoda-irods) |


---

## Other useful locations (not raw study data)


| Resource                                       | Where                                                                                                | Notes                                                              |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **NMCB Core email list**                       | `>Research BV NMCB Core` / [resbv-nmcb-core@amsterdamumc.nl](mailto:resbv-nmcb-core@amsterdamumc.nl) | [NMCB Core distribution list](systems/distributed-list.md)         |
| **Data management plans, training**            | Research Drive `data management/` + [repo copies](files/data-management-plan/README.md)              | [Data management plan](tasks/data-management-plan.md)              |
| **Request metadata** (approvals, sharing docs) | Research Drive `request/`                                                                            | Sample and data access paperwork                                   |
| **SOPs, OMOP, technical docs**                 | Research Drive `data infrastructure/`                                                                | Models, pipelines, governance                                      |
| **NMCB codebook & mappings**                   | [GitHub nmcb-codebook](https://github.com/nmcb-fair/nmcb-codebook)                                   | Variable definitions; biobank/device mappings                      |
| **Hand-over documentation**                    | This site + [GitHub nmcb-handover-docs](https://github.com/nmcb-fair/nmcb-handover-docs)             |                                                                    |
| **FAIR / catalogue work**                      | Documented under [FAIR](fair/index.md); not day-to-day ops storage                                   | FIP, Health-RI, OMOP pilots                                        |
| **RDM contact (GDPR, myDRE)**                  | Paulo Heemskerk — [p.f.heemskerk@amsterdamumc.nl](mailto:p.f.heemskerk@amsterdamumc.nl)              | [Keep in mind (GDPR)](index.md#keep-in-mind-gdpr-and-data-sharing) |


---

## Quick lookup

```text
Castor (cloud)                    → live study data
Research Drive organized/         → raw CDL, RDL, devices, RL, …
Research Drive processed/         → cleaned tables, biobank box files
Research Drive analyzed/CDL/      → CDL alert clinical review
Research Drive analyzed/RDL/      → RDL alerts
OpenSpecimen                      → sample inventory & requests
Snowflake                         → structured analytics copy
GitHub nmcb-fair/*                → scripts, data-request, codebook
```

---

## Related

- [Research Drive](systems/research-drive.md) — project folder layout (`Amsterdam/`, `Radboud/`, `request/`, …)
- [Data flow (home)](index.md#end-to-end-data-flow) — end-to-end diagram
- [Workflows](workflows/index.md) — procedures that move data between folders
- [Where to update this page](#data-by-type) — when paths change, update this table and the relevant workflow page in the same PR

