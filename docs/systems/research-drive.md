# NMCB Research Drive


## Overview

**NMCB choice:** **Research Drive** is the primary shared file store for cohort operations, device outputs, biobank hand-offs, scripts, and collaboration with the data management / IT team. **YoDa** (on **iRODS**) is **not** in routine use today but is the approved option when **sensitive** data cannot sit on Research Drive.

This Research Drive project folder contains the shared data, documentation, and infrastructure resources for the Netherlands ME/CFS Cohort and Biobank (NMCB).

!!! warning "Do not store sensitive data on Research Drive"
    Research Drive is **not** suitable for **sensitive** (high-protection) data. Use **YoDa / iRODS** for that class of data instead. Keep pseudonymized study files and operational datasets on Research Drive only when they match the agreed sensitivity tier (RDM: Paulo Heemskerk, Feb 2026).

The folder structure is organized to support:

- research data storage
- data access governance
- research data management
- technical data infrastructure
- reproducible data processing and analysis

Detailed documentation is available in folder-specific README files.

---

## Research Drive vs YoDa (iRODS)

| Store | NMCB use | Suitable for |
| ----- | -------- | -------------- |
| **Research Drive** (SURF) | **Current default** — raw/processed devices, biobank files, requests, SOPs, team folders | Shared project files, collaboration, non-sensitive or agreed-tier pseudonymized data |
| **YoDa** | **Future / selective** — when sensitivity or policy requires iRODS | **Sensitive** data; governed storage with strong access control |
| **Google Drive (G-drive)** | **Avoid for myDRE workflows** | Not reachable from myDRE; migrate or copy into Research Drive or YoDa if still needed |

**YoDa** is a web and tooling layer on top of **[iRODS](https://irods.org/)** (integrated Rule-Oriented Data System). Read more:

- [About YoDa (Utrecht University)](https://www.uu.nl/en/research/yoda/about-yoda)
- [YoDa documentation](https://utrechtuniversity.github.io/yoda/)

**myDRE note:** **G-drive is not (and will not be) accessible from myDRE.** Data used in myDRE must live on **Research Drive** (mounted via WebDAV) or **YoDa/iRODS**, or be copied into myDRE workspace storage — see [myDRE](mydre.md).

**RDM contact (storage policy):** Paulo Heemskerk — [p.f.heemskerk@amsterdamumc.nl](mailto:p.f.heemskerk@amsterdamumc.nl).

---

## Data journey (document this over time)

RDM asked the team to write out how data **travel** from capture to analysis — e.g. device → QC → Research Drive → Snowflake → requests / myDRE. The **clickable end-to-end diagram** (with links to every workflow) is on the [home page — End-to-end data flow](../index.md#end-to-end-data-flow).

**Versioning rule (RDM):**

- Keep **untouched raw** data in a dedicated location (do not overwrite in place).
- Every manipulation (cleaning, merge, export) should produce a **new version** or folder generation (e.g. date-stamped `organized/CDL/{YYYYMMDD}`), not silent replacement of the only copy.

---

## Folder for IT / data management team

Use Research Drive as the **hand-off surface** with central IT / data management: create a folder they can **read and write**, separate from participant-facing raw areas where possible. Document the path in [Where data lives](../where-data-lives.md) when finalized.

---

## Top-Level Folder Structure

```text
NMCB (Projectfolder)
├── Amsterdam/
├── Radboud/
├── request/
├── data management/
└── data infrastructure/
```

---

## Folder Overview

## Amsterdam/

Primary Amsterdam data environment supporting the full research data lifecycle.

Includes:

```text
organized → processed → analyzed → archive
```

Contains source data, processed datasets, analysis outputs, and archived data.

See:

```text
Amsterdam/README.md
```

---

## Radboud/

Data environment for project data managed under Radboud UMC.

See:

```text
Radboud/README.md
```

---

## request/

Contains metadata and documentation related to sample and data access requests.

Examples:

- project requests
- transfer requests
- approvals
- request metadata
- data sharing documentation

See:

```text
request/README.md
```

---

## data management/

Contains resources supporting:

- participant and sample tracking
- cohort monitoring
- **data management plans (DMPs)** — main PDF, sub-project templates, training materials ([DMP task](../tasks/data-management-plan.md))
- guidance for affiliated projects

See:

```text
data management/README.md
```

---

## data infrastructure/

Contains resources related to technical infrastructure, including:

- SOPs
- data models (e.g. OMOP)
- technical documentation

See:

```text
data infrastructure/README.md
```

---

## Principles

This structure supports:

- separation of data and governance documentation
- structured data lifecycle management
- traceability
- reproducibility
- FAIR data management practices
- **raw preservation** and **versioned** derivatives (see [Data journey](#data-journey-document-this-over-time))
- **sensitivity-appropriate** storage (Research Drive vs YoDa — see [Research Drive vs YoDa](#research-drive-vs-yoda-irods))

---

## Related

- [Data flow (home)](../index.md#end-to-end-data-flow) — end-to-end pipeline diagram
- [myDRE](mydre.md) — secure analysis and controlled issuing (folder access or copied subsets)
- [Data request](../tasks/data-request.md) — building deliverables from Research Drive sources
- [Devices](devices.md) — VU-AMS and other outputs under `organized/`

## Notes

- Detailed documentation is maintained in subfolder README files.
- Access permissions may differ across folders.
- Users should follow applicable governance and data handling procedures when modifying shared data.

---

Last updated: 2026-04-17