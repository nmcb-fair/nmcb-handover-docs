# PAIS metadata schema coordination

**Status:** Not started

*Cross-initiative alignment on **study-level metadata** for Post-acute infection syndromes (PAIS) in the **European Health Data Space (EHDS)** context.*

---

## Goal

Explore how metadata schema efforts (Health-RI, PCNN, NMCB, BBMRI.nl, ZonMw) can **align** or share a framework, without duplicating variable-level work already done in project codebooks.

**Source documents (April 2026):**

- [Metadata Schema Coordination Meeting (PDF)](../files/fair/pais-metadata/metadata-schema-coordination-april-2026.pdf)
- [Same content (DOCX)](../files/fair/pais-metadata/metadata-schema-coordination-april-2026.docx) — editable for comments before meetings

---

## Meeting logistics (from coordination doc)

| Item | Detail |
| ---- | ------ |
| **Proposed slot** | 10:00–11:00, **9 April 2026** |
| **Scheduling** | [Doodle poll](https://doodle.com/group-poll/participate/aQKKPpld) |
| **Follow-up** | Shuxin & Hajar — **29 April 2026** |
| **Organizer** | Shuxin Zhang; supporting organizer Margreet (ZonMw) |

### Participants (perspectives)

| Perspective | Initiative | Representative |
| ----------- | ---------- | -------------- |
| EHDS / DCAT-AP | Health-RI | Hannah |
| Post-COVID | PCNN | Bianca, Hajar |
| ME/CFS | **NMCB** | Jos, Shuxin |
| Biobank | BBMRI.nl | Peggy |
| Funder | ZonMw | Margreet |

---

## Initiative snapshots (April 2026)

### Health-RI / EHDS

- Health-RI metadata schema aligned with **HealthDCAT-AP**
- Implementation in national catalogue; onboarding UMCs and domain nodes
- Challenges: consensus on filling schema; HealthDCAT-AP is general; harvesting from **FDPs** at UMCs or central Health-RI FDP, or push from Dataverse
- Onboarding: [onboarding@health-ri.nl](mailto:onboarding@health-ri.nl)

### PCNN

- Metadata for 32 pre-PCNN studies (variable level); study-level human-readable format (EMIF-based) in PCNN-Projects
- Overlap with Health-RI schema — partial overlap, many differences
- Exploring catalogues: YoDa, CKAN, MOLGENIS
- Ontologies in codebook: SNOMED CT, LOINC, NCIT — see [Ontology harmonization](ontology-harmonization.md) and [IOS Press paper](https://ebooks.iospress.nl/doi/10.3233/SHTI260692)
- Open questions: align metadata vs codebook vs study management; PAIS node scope; avoid double work for researchers under EHDS reporting obligations

### NMCB

- **[NMCB codebook](https://github.com/nmcb-fair/nmcb-codebook)** available
- **No** standalone metadata schema yet
- Demand to better **organise** study-level metadata (link to [NMCB ChatGPT](../tasks/nmcb-chatgpt.md) for variable discovery)

### BBMRI.nl

- Biobank metadata model: mandatory/recommended attributes, human- and machine-readable formats, controlled vocabularies (see coordination doc for full bullets)

---

## Open coordination questions

1. Can PAIS initiatives share one **study-level** metadata profile (EHDS + domain needs)?
2. Where is the line between **variable-level** (codebook) and **study-level** (catalogue / DMP)?
3. Will there be a dedicated **PAIS node** in Health-RI — and what would NMCB report into it?
4. How to avoid researchers maintaining the same facts in Castor, DMP, codebook, and catalogue?

---

## Suggested next steps (if work resumes)

- [ ] Add NMCB study-level metadata draft (minimal fields) referencing [main DMP](../tasks/data-management-plan.md)
- [ ] Map codebook domains to Health-RI Core classes (see [Health-RI metadata](health-ri-metadata.md))
- [ ] Attend or document outcomes of April 2026 coordination meetings
- [ ] Store living notes on Research Drive next to DMP folder

---

## Related

- [FAIR overview](index.md)
- [Health-RI metadata](health-ri-metadata.md)
- [FAIR Data Point](fair-data-point.md) — catalogue harvest target
