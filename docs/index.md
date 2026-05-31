# NMCB hand-over documentation

Welcome to the working hand-over for the **Netherlands ME/CFS Cohort and Biobank (NMCB)** data management and data infrastructure role.

For folder paths see [Where data lives](where-data-lives.md). For step-by-step procedures see [Workflows](workflows/index.md).

---

## End-to-end data flow

The diagram below runs from **capture at the visit** through **Research Drive** stages to **Snowflake**, with delivery to requestors. **Click a box** in the diagram (desktop) or use the [step reference table](#step-reference-clickable-links) — every step links to the relevant workflow or system page.

**Versioning:** keep raw data under `organized/`; each cleaning or merge produces a **new** `processed/` (or `analyzed/`) output — do not overwrite the only raw copy ([Research Drive](systems/research-drive.md#data-journey-document-this-over-time)).

```mermaid
flowchart TB
  subgraph CAP["① Capture"]
    VISIT["Visit & operational logs"]
    CASTOR["Castor EDC"]
    DEVICES["Devices"]
    SETUP["Device setup for visit"]
  end

  subgraph LAB["Lab & sample files"]
    CDL["CDL / CRL exports"]
    RDL["RDL & RL files"]
  end

  subgraph ORG["② Research Drive — organized"]
    RDORG["organized/ dated folders"]
  end

  subgraph WRK["③ QC & workflows"]
    QC["Cleaning / QC scripts"]
    WCDL["CDL processing"]
    WRDL["RDL processing"]
  end

  subgraph DER["④ Research Drive — processed & analyzed"]
    RDPROC["processed/"]
    RDAN["analyzed/ alerts"]
  end

  subgraph STR["⑤ Structured analytics"]
    POOL["data pool/ exports"]
    SF["Snowflake"]
  end

  subgraph OUT["⑥ Delivery & use"]
    DREQ["Data request packages"]
    MYDRE["myDRE workspaces"]
  end

  subgraph SMP["Samples (parallel)"]
    OS["OpenSpecimen inventory"]
  end

  SETUP --> DEVICES
  VISIT --> CASTOR
  VISIT --> DEVICES
  VISIT --> CDL
  CASTOR --> RDORG
  DEVICES --> RDORG
  CDL --> RDORG
  RDL --> RDORG
  RDORG --> QC
  RDORG --> WCDL
  RDORG --> WRDL
  QC --> RDPROC
  WCDL --> RDPROC
  WCDL --> RDAN
  WRDL --> RDPROC
  WRDL --> RDAN
  RDPROC --> POOL
  RDPROC --> SF
  POOL --> SF
  SF --> DREQ
  SF --> MYDRE
  POOL --> DREQ
  RDPROC --> OS

  click VISIT "workflows/recurring-routines/" "Recurring study routines"
  click CASTOR "systems/castor/" "Castor EDC"
  click DEVICES "systems/devices/" "Devices"
  click SETUP "workflows/device-setup-for-visit/" "Device setup for visit"
  click CDL "workflows/cdl-alert-workflow/" "CDL alert workflow"
  click RDL "workflows/rdl-alert-workflow/" "RDL alert workflow"
  click RDORG "systems/research-drive/" "Research Drive — organized"
  click QC "systems/github/" "GitHub scripts"
  click WCDL "workflows/cdl-alert-workflow/" "CDL processing"
  click WRDL "workflows/rdl-alert-workflow/" "RDL processing"
  click RDPROC "where-data-lives/" "Where data lives — processed"
  click RDAN "where-data-lives/" "Where data lives — analyzed"
  click POOL "tasks/data-request/" "Data request — data pool"
  click SF "systems/snowflake/" "Snowflake"
  click DREQ "tasks/data-request/" "Data request task"
  click MYDRE "systems/mydre/" "myDRE"
  click OS "systems/openspecimen/" "OpenSpecimen"
```

### Step reference (clickable links)

| Step | What happens | Documentation |
| ---- | ------------ | ------------- |
| **① Visit & logs** | Scheduling, visit log, subject ID log, mailbox routines | [Recurring study routines](workflows/recurring-routines.md) · [Where data lives](where-data-lives.md) |
| **Castor EDC** | eCRF and surveys during / after visit | [Castor](systems/castor.md) |
| **Device setup** | iPad / laptop ready before measurements | [Device setup for visit](workflows/device-setup-for-visit.md) |
| **Devices** | VU-AMS, Omron, Nellcor, Tanita, ACS, … | [Devices](systems/devices.md) · [Device data workflow](workflows/device-data-workflow.md) |
| **CDL / CRL** | Central lab raw files → per-participant outputs & alerts | [CDL alert workflow](workflows/cdl-alert-workflow.md) |
| **RDL / RL** | Radboud lab + blood-tube / box files | [RDL alert workflow](workflows/rdl-alert-workflow.md) · [Multi-centre sample data workflow](workflows/multicentre-sample-data-workflow.md) |
| **② `organized/`** | Raw drops on Research Drive (`organized/CDL/`, `organized/{device}/`, …) | [Research Drive](systems/research-drive.md) · [Where data lives](where-data-lives.md) |
| **③ QC & scripts** | Python/R cleaning, validation, device conversion | [GitHub](systems/github.md) (`nmcb-fair` repos) |
| **④ `processed/` & `analyzed/`** | Analysis-ready tables; CDL/RDL alert folders for clinicians | [Where data lives](where-data-lives.md) |
| **⑤ `data pool/`** | Latest Castor + device exports for package builds | [Data request](tasks/data-request.md) |
| **⑤ Snowflake** | Structured cohort tables, eligibility, reporting | [Snowflake](systems/snowflake.md) |
| **⑥ Data request** | Approved CSV packages for researchers | [Data request](tasks/data-request.md) · [GDPR rules](#keep-in-mind-gdpr-and-data-sharing) |
| **⑥ myDRE** | Controlled analysis environment for approved subsets | [myDRE](systems/mydre.md) |
| **OpenSpecimen** | Physical sample metadata & release (from biobank path) | [Biobank](systems/biobank.md) · [OpenSpecimen](systems/openspecimen.md) |

---

## Overview

NMCB data currently spans:

- study capture in [Castor](systems/castor.md)
- operational logs — [Recurring study routines](workflows/recurring-routines.md)
- devices — [Devices](systems/devices.md), [Device data workflow](workflows/device-data-workflow.md)
- labs (CDL, RDL, RL) — [workflows](workflows/index.md)
- files on [Research Drive](systems/research-drive.md); sensitive data on YoDa when required
- analytics in [Snowflake](systems/snowflake.md)
- sharing via [Data request](tasks/data-request.md) and [myDRE](systems/mydre.md)
- samples in [OpenSpecimen](systems/openspecimen.md)

## Architecture principle

Identifiers and provenance should survive every transformation step. Every workflow should make it possible to answer: where did this record originate; which process changed it; which ID links it to the participant; is the dataset raw, intermediate, or analysis-ready?

---

## Keep in mind (GDPR and data sharing)

These rules apply to **every** export, list, myDRE delivery, or biobank hand-off. Source: Amsterdam UMC RDM (Paulo Heemskerk, myDRE / data-request discussions, Aug 2025).

### Minimize what you share

- Share **only variables and participants that the request actually needs** — no “nice to have” columns, no wider cohort than necessary.
- Prefer the **least identifying** form of a variable (e.g. share **age**, not **date of birth**, when age is enough for matching or analysis).
- Do **not** send screener or cohort **answers for all participants** so requestors can browse and pick subjects. Requestors must provide **selection criteria in advance**; you return data **only for participants who meet those criteria**.
- Sharing the **list of questions / data dictionary** (what was collected, not the answers) is fine; sharing multi-participant answer sets for pre-selection is **not**.

### Identifiers

- Use **participant / Castor study ID** in NMCB workflows — not **hospital patient ID** (highly sensitive). There is **no** default ethics/privacy approval to share patient IDs; do not include them unless explicitly approved for that request.
- When Jos or others say “patient ID”, they usually mean **Castor participant ID** — confirm before exporting.

### Before you send anything

1. Is each field **required** for the stated purpose?
2. Is the extract limited to **relevant participants** (documented selection criteria)?
3. Could any column be replaced by a **less sensitive** alternative (age vs DOB)?
4. Is delivery via an **approved channel** ([myDRE](systems/mydre.md), controlled folder, etc.)?

**RDM contact:** Paulo Heemskerk — [p.f.heemskerk@amsterdamumc.nl](mailto:p.f.heemskerk@amsterdamumc.nl). Operational tooling: [Data request](tasks/data-request.md).

---

## How this site is organised

| Section | Purpose |
| ------- | ------- |
| **Where data lives** | Paths on Research Drive, Castor, OpenSpecimen, … |
| **Workflows** | CDL/RDL alerts, multicentre samples, devices, recurring routines |
| **Systems** | Castor, devices, Snowflake, Research Drive, biobank, myDRE, [NMCB Core list](systems/distributed-list.md), GitHub |
| **Tasks** | Data request, sample request, DMP, ChatGPT, device QC, … |
| **FAIR** | Metadata, FIP, OMOP — [overview](fair/index.md) (handover context; no active follow-up) |

## How to use this documentation

Use the **diagram above**, then [Where data lives](where-data-lives.md) and the **workflow** or **system** page for the task at hand. **Tasks** hold runnable procedures (data packages, sample requests, tooling).

Each task page should answer: why it exists; when to do it; where; steps; what to check before done.

---

## FAIR and catalogue metadata (future)

Study-level metadata, Health-RI, and FAIR Data Point pilots are **not** in day-to-day operations. See [FAIR projects](fair/index.md). **Controlled vocabulary:** [Ontology harmonization](fair/ontology-harmonization.md), [OMOP mapping](fair/omop-mapping.md) in [nmcb-codebook](https://github.com/nmcb-fair/nmcb-codebook).
