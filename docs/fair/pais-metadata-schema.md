# PAIS metadata schema coordination

**Status:** Not started

*Cross-initiative alignment on **study-level metadata** for **Post-acute infection syndromes (PAIS)** in the **European Health Data Space (EHDS)**. Variable-level semantics (SNOMED CT, LOINC, NCIT) are covered separately under [Controlled vocabulary — Ontology harmonization](ontology-harmonization.md).*

**Source documents:**

- [Metadata Schema Coordination Meeting (PDF)](../files/fair/pais-metadata/metadata-schema-coordination-april-2026.pdf)
- [Editable DOCX](../files/fair/pais-metadata/metadata-schema-coordination-april-2026.docx) — add comments before meetings

---

## 1. Meeting goal

Explore how initiatives working on metadata schemas can **align** and optionally **coordinate development** for PAIS in the EHDS context.

**Aims:**

1. Share the **current status** of metadata schema development in each initiative  
2. **Identify overlaps and differences**  
3. Explore whether a **shared or aligned metadata framework** is feasible  
4. Agree **next steps for coordination**

---

## 2. Meeting information

| Item | Detail |
| ---- | ------ |
| **Scheduling** | [Doodle poll](https://doodle.com/group-poll/participate/aQKKPpld) |
| **Proposed window** | **10:00–11:00, 9 April 2026** |
| **Follow-up (core group)** | **29 April 2026** — Shuxin, Hajar, Margreet |
| **Organizer** | Shuxin Zhang |
| **Supporting organizer** | Margreet (ZonMw) |
| **Later scheduling** | Shuxin to send a new Doodle in **May 2026** |

---

## 3. Participants and perspectives

| Perspective | Initiative / organization | Representative |
| ----------- | ------------------------- | -------------- |
| **EHDS** (DCAT-AP) | [Health-RI](health-ri-metadata.md) | Hannah |
| **Post-COVID** | PCNN | Bianca, Hajar |
| **ME/CFS** | **NMCB** | Jos, Shuxin |
| **Biobank** | BBMRI.nl | Peggy |
| **Funder** | ZonMw | Margreet |

---

## 4. Current work by initiative

### EHDS / Health-RI

**Current activities:**

- HRI metadata schema aligned with EHDS (**HealthDCAT-AP**)
- Implement HRI metadata schema in the [national catalogue](https://catalogus.healthdata.nl/en)
- Onboard data holders (UMCs, domain nodes, individual organisations)
- **Framework:** HealthDCAT-AP; [Health-RI Metadata Model](https://github.com/Health-RI/health-ri-metadata) (general + health-related fields)
- **Harvesting:** metadata from **FDPs** at UMCs, central Health-RI FDP, or **push from Dataverse**

**Key challenges:**

- Consensus on **how** to fill the metadata schema
- Supporting data holders through **onboarding**
- HealthDCAT-AP is **quite general** — does not meet all data-holder needs

**Onboarding:** [onboarding@health-ri.nl](mailto:onboarding@health-ri.nl)

### PCNN

**Current metadata work:**

- Metadata collected for **32 (pre-PCNN) studies** — **variable level** (Shuxin)
- **Study-level**, human-readable format: [PCNN-Projects/Metadata-format](https://github.com/PCNN-Projects/Metadata-format) (EMIF-based)
- Health-RI reviewed overlap with PCNN format vs EHDS needs — **partial overlap, more differences**
- Exploring searchable catalogues: **YoDa**, **CKAN**, **MOLGENIS**
- **Ontologies in codebook (variable level):** SNOMED CT, LOINC, NCIT — see [Ontology harmonization](ontology-harmonization.md) and [IOS Press paper](https://ebooks.iospress.nl/doi/10.3233/SHTI260692)

**Key needs:**

- Align **metadata**, **codebook**, and **study management**
- Study-level metadata vs variable-level codebook — same artefact or separate? Ontologies for all study-level fields?
- Where should UMCs **collect** which metadata under EHDS obligations? Enough for PCNN without **double work** for researchers
- Will there be a **PAIS node** in Health-RI — and where?

**PCNN / catalogue (Bianca):**

- Make metadata easy for **researchers**; **FAIR Data Point alone is too complex** for many users
- PCNN network should align with **[Health-RI Data Catalogue](https://catalogus.healthdata.nl/en)** (not replace it with FDP-only workflows)
- A **PAIS node** in Health-RI is possible but **no funding yet**
- Inventory underway for **HORIZON** participation (Bianca)

### NMCB

**Current metadata work:**

- **[NMCB codebook](https://github.com/nmcb-fair/nmcb-codebook)** available (variable-level; LinkML in progress)
- **No** dedicated metadata schema yet
- Demand to **organise** metadata (study + variable layers)
- **Handover focus (Shuxin):** document work before role change; **NMCB onboarding** to Health-RI where applicable

**Rough link between Health-DCAT-AP-NL and codebook** (discussion draft):

- **Simple:** dataset uses PAIS/NMCB codebook via `dcat:uses` → link to codebook URI  
- **Advanced:** dataset `dcat:collect` per variable (e.g. fatigue, biological sex) with mappings to ontology URIs — see [mapping examples](#mapping-examples-pcnn--ontologies) below

### BBMRI.nl — metadata for biobanks

- **Metadata model:** which attributes describe data; mandatory vs recommended; human- and machine-readable; controlled vocabularies
- Uses **Health-RI metadata model** (general, EHDS-aligned) — **not biobank-specific** alone
- **Catalogue rule:** **one catalogue entry per biobank or collection** in the National Health Data Catalogue  
  - Single-centre: UMC **onboarding route**  
  - Multi-centre: via **coordinating center**
- Agreements needed on: available biosamples, population specifics, etc.
- **Standards:** [MIABIS](https://www.bbmri-eric.eu/howtomiabis/) and related biobank metadata
- **FAIR Data Point Amsterdam:** [https://fdp.healthdataspace.amsterdam](https://fdp.healthdataspace.amsterdam)  
  - Contacts: Erik van Iperen — [e.p.vaniperen@amsterdamumc.nl](mailto:e.p.vaniperen@amsterdamumc.nl); René Oostergo — [r.j.oostergo@umcg.nl](mailto:r.j.oostergo@umcg.nl)  
  - See also [FAIR Data Point](fair-data-point.md)

### ZonMw — funder perspective

**Expectations today:**

- Reuse existing data where possible  
- Use **domain-specific standards**  
- Engage a **data steward**  
- Budget for data stewardship activities  

**Under development:**

- **Machine-actionable DMP** and **PIDs**
- Minimal metadata to enrich datasets: participant counts, variables, etc.

**Interoperability priorities:**

- Controlled vocabulary for **generic health terms** (EHDS-compliant)
- Richer **disease/context** terms (to be developed)
- **PIDs:** ROR, ORCID, DOI

---

## 5. Existing resources

| Resource | Link | Comment |
| -------- | ---- | ------- |
| Health-RI metadata schema | [github.com/Health-RI/health-ri-metadata](https://github.com/Health-RI/health-ri-metadata) | SHACL Core; EHDS alignment |
| Health-RI Data Catalogue | [catalogus.healthdata.nl](https://catalogus.healthdata.nl/en) | National exposure target for PCNN/NMCB |
| PCNN metadata dictionary | [github.com/PCNN-Projects/Metadata-format](https://github.com/PCNN-Projects/Metadata-format) | Study-level; can act as researcher **input form** |
| NMCB variable list / codebook | [github.com/nmcb-fair/nmcb-codebook](https://github.com/nmcb-fair/nmcb-codebook) | Variable-level; LinkML + OMOP |
| BBMRI MIABIS | [bbmri-eric.eu/howtomiabis](https://www.bbmri-eric.eu/howtomiabis/) | Biobank collections |
| DCAT vocabulary | [W3C DCAT 3](https://www.w3.org/TR/vocab-dcat-3/#basic-example) | Base catalogue model |
| COVID-19 metadata schemes (2021–2025) | Project admin · project content · collection · dataset (DCAT); M4M — GO FAIR | Historical reference |
| ZonMw COVID-19 (BioPortal) | [ZonMw COVID-19 \| NCBO](https://bioportal.bioontology.org/ontologies) | Search “ZonMw” in BioPortal |
| Nanopublication templates | [nanodash](https://nanodash.app/) | Optional nanopublication route |
| FAIR Data Point Amsterdam | [fdp.healthdataspace.amsterdam](https://fdp.healthdataspace.amsterdam) | UMC FDP instance |

*Margreet / Renske:* track initiatives named in grant proposals (overview not public-linked yet).

---

## 6. Key questions for coordination

**Cross-PAIS:**

1. What **minimum metadata set** should exist across PAIS cohorts? *(Margreet: minimal common elements.)*  
2. How can PAIS cohorts **align with EHDS** requirements?  
3. Can we reuse **MIABIS** or other health metadata frameworks?  
4. **Shared schema** vs **mapping between schemas**?  
5. How does the schema become **tangible products** (catalogue, access workflow)?  

**Margreet — product vision:**

- Input **form** for researchers to supply metadata  
- **Catalogue** exposing metadata (complement to EHDS national catalogue)  
- Search → find → **request** procedure (HDAB-related concepts)  
- Data access + **terms of use**  
- Predefined **SPARQL** on metadata for knowledge generation / visualisations  

**PCNN / NMCB-specific (from §4):**

- One codebook for study + variable metadata, or separate systems?  
- Where is the line between EHDS reporting and PCNN/NMCB needs?  
- PAIS node in Health-RI — **if yes, where and who funds it?**

**Health-DCAT gap (Margreet):**

- Use **Health-DCAT-AP-NL** as much as possible; extra fields via **own schema** / `other metadata scheme`  
- Health-DCAT may lack explicit **“variables”** attribution — connect via **DCAT qualified attribution** (roles: funder, …) and **qualified relation** (e.g. link to codebook)  
- **PIDs:** grant-id, ORCID, ROR, DOI  

---

## 7. Expected outcomes

**Possible meeting outcomes:**

- Agreement on **shared metadata principles**  
- Identification of **common metadata domains**  
- **Planning** of metadata actions  

**Margreet — suggested actions:**

- Meet to fix **metadata elements** for rich **project content** description  
- Reuse terms / controlled vocabularies from **PCNN codebook** and **biobank metadata**  

**Renske — suggested actions:**

- Find similar **national and EU** initiatives to collaborate  
- Clarify **who participates** and **roles**  

**Scope constraints (29 April prep — Margreet / consortium):**

Set a **feasible scope** for ME/CFS / PCNN metadata development given:

| Factor | Notes |
| ------ | ----- |
| **Health-DCAT-AP-NL** | Default backbone |
| **Health-RI** | Support only for **their** responsibilities — ask explicitly |
| **ZonMw** | Identifies needs; **others execute** |
| **Consortium** | ZonMw, ME/CVS, PCNN, PAIS-funded projects |
| **Experts, time, budget** | Limit promises |

**Metadata system components (target architecture):**

| Layer | Examples |
| ----- | -------- |
| **Scheme** | Health-DCAT-AP-NL + optional “other scheme” (which standard?) |
| **Controlled vocabularies** | EHDS generic + richer disease/context terms |
| **Input** | HRI onboarding form · PCNN metadata dictionary XLS · [maDMP ZonMw](https://www.zonmw.nl/) (in development) · institute/FDP/nanopublication endpoints |
| **Exposure** | [National catalogue](https://catalogus.healthdata.nl/en) · data platform · project website |

**To-dos captured in doc:**

- Margreet → ask Mijke/Hannah how to work per above model  
- Shuxin/Hajar → explain codebook use case, PCNN XLS, onboarding  
- Align PCNN metadata dictionary XLS with Health-DCAT scheme (**with HRI/Mijke**)  
- **PAIS codebook** — extra fields to be added (Shuxin & Hajar; list TBD in DOCX)  

---

## 8. Draft agenda (April 2026 meeting)

| Time | Topic |
| ---- | ----- |
| 5 min | Introduction and meeting objective |
| — | Short updates: **PCNN + NMCB (PAIS)**, BBMRI, Health-RI |
| — | Discussion: overlaps and alignment |
| — | Discussion: EHDS relevance |
| — | Agreement on next steps |

---

## Mapping examples (PCNN ↔ ontologies)

Working notes from coordination doc — for [ontology harmonization](ontology-harmonization.md) and future **LinkML / RDF** exports.

**Prefixes (example):**

```text
PREFIX sct:  <http://snomed.info/id/>
PREFIX ncit: <http://purl.obolibrary.org/obo/NCIT_>
PREFIX pcnn: <https://pcnn.example/id/>   # replace with real namespace
```

**Relation types:**

| PCNN variable | Relation | Ontology term | Note |
| ------------- | -------- | ------------- | ---- |
| `pcnn:fatigue` | `skos:exactMatch` | `sct:fatigue` | Direct match |
| `pcnn:sleeping_tiredness_10_days` | `skos:narrowMatch` | `sct:sleeping_tiredness` | Do **not** invent SCT term for “10 days” |
| `pcnn:sleeping_tiredness_10_days` | `skos:exactMatch` | `sct:sleeping_tiredness_10_days` | When SCT creates a specific concept |

**FAIR variable naming (illustrative):** `sct_12345` → `http://snomed.info/id/12345`

**RDF mapping record (pattern):**

```turtle
pais:mapping01 a dcat:Mapping ;
  dcat:subject pcnn:fatigue ;
  dcat:predicate skos:narrowMatch ;
  dcat:object sct:fatigue_related ;
  dcat:author orcid:0000-0000-... ;   # e.g. Hajar
  dcat:status "wait for SNOMED CT new codes" .
```

---

## NMCB handover checklist

- [ ] Complete study-level metadata fields for PAIS codebook (with Hajar)  
- [ ] Document HRI **onboarding** steps taken or planned for NMCB  
- [ ] Meeting notes from **9 April** and **29 April 2026** appended to DOCX/PDF in `docs/files/fair/pais-metadata/`  
- [ ] Clarify PAIS node funding and Health-RI ownership with Margreet / Hannah  
- [ ] Align PCNN metadata XLS with Health-DCAT — meeting with HRI (Mijke/Hannah)  
- [ ] Keep [DMP](../tasks/data-management-plan.md) and catalogue (DataverseNL, ACH) consistent with agreed metadata set  

---

## Related

- [FAIR overview](index.md)
- [Health-RI metadata](health-ri-metadata.md)
- [FAIR Data Point](fair-data-point.md) · [FDP Amsterdam](https://fdp.healthdataspace.amsterdam)
- [Controlled vocabulary](controlled-vocabulary.md)
- [Ontology harmonization](ontology-harmonization.md)
- [Data management plan](../tasks/data-management-plan.md)
- [NMCB ChatGPT](../tasks/nmcb-chatgpt.md)
