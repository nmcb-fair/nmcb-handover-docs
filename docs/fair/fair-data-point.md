# FAIR Data Point (Amsterdam UMC)

**Status:** Not started

*A **FAIR Data Point (FDP)** publishes machine-readable metadata about datasets (catalogues, datasets, distributions) using RDF. Amsterdam UMC and Health-RI use FDPs in the **national health data catalogue** ecosystem.*

This page collects **links and deployment notes** from conversations with **Sjoerd Manger** (Amsterdam UMC) and the myDRE replication guide — not a production runbook for NMCB.

---

## Key links

| Resource | URL |
| -------- | --- |
| **FDP documentation (local deployment)** | [FAIR Data Point — Local deployment](https://fairdatapoint.readthedocs.io/en/latest/deployment/local-deployment.html) |
| **FDP documentation (home)** | [fairdatapoint.readthedocs.io](https://fairdatapoint.readthedocs.io/en/latest/) |
| **FAIR Data Point project** | [fairdatapoint.org](https://www.fairdatapoint.org/) · [GitHub FAIRDataTeam/FAIRDataPoint](https://github.com/FAIRDataTeam/FAIRDataPoint) |
| **Amsterdam UMC FDP (myDRE branch)** | [github.com/AmsterdamUMC/FDP_AMS (branch `myDRE`)](https://github.com/AmsterdamUMC/FDP_AMS/tree/myDRE) |
| **FAIR Data Point Amsterdam** | Production/catalogue instance — confirm current URL with Amsterdam UMC RDM / Health-RI (often referenced in Health-RI onboarding; may be listed on [Health-RI](https://www.health-ri.nl)) |
| **SeMPyRO (metadata → FDP)** | [Health-RI/SeMPyRO](https://github.com/Health-RI/SeMPyRO) · [FDP usage notebook](https://github.com/Health-RI/SeMPyRO/blob/main/docs/Usage_example_FDP.ipynb) |

---

## myDRE local FDP

To run or replicate FDP **inside myDRE** (private network, Docker on Ubuntu VM):

| Document | Location |
| -------- | -------- |
| **Replication guide (Oct 2024, v0.1)** | [PDF in repo](../files/fair/fdp/replicating-fdp-amsterdamumc-mydre-20241008.pdf) |

**Prerequisites mentioned in that guide and follow-up emails:**

- myDRE workspace with permission to install **Docker** on the VM  
  - [Installing Docker on Ubuntu 22 (myDRE KB)](https://support.mydre.org/portal/en/kb/articles/installing-docker-on-ubuntu-22#Docker_installation_steps)  
  - [Docker engine install (Ubuntu)](https://docs.docker.com/engine/install/ubuntu/)
- Follow [local deployment](https://fairdatapoint.readthedocs.io/en/latest/deployment/local-deployment.html) steps adapted for myDRE networking (whitelist outbound domains via myDRE ticket if needed — see [myDRE](../systems/mydre.md))

**Known integration notes (from PDF link targets):**

- [FAIRDataPoint issue #94](https://github.com/FAIRDataTeam/FAIRDataPoint/issues/94#issuecomment-726801943) — deployment quirks
- [health-ri-metadata issue #99](https://github.com/Health-RI/health-ri-metadata/issues/99#issuecomment-2176244905) — schema / FDP alignment

---

## Relation to Health-RI catalogue

Health-RI can **harvest metadata from FDPs** at UMCs (or a central FDP). NMCB study metadata would not automatically appear in a catalogue until:

1. Study-level metadata is defined (see [PAIS metadata schema](pais-metadata-schema.md)), and  
2. An FDP resource is created and kept in sync (often via SeMPyRO + [Health-RI SHACL/TTL](health-ri-metadata.md)).

---

## Handover checklist

- [ ] Confirm whether Amsterdam UMC FDP is still the intended publication path for NMCB
- [ ] Identify workspace owner for any myDRE FDP pilot
- [ ] List RDF/TTL resource definitions in use (from `FDP_AMS` or Health-RI Core)
- [ ] Document public catalogue URL once datasets are registered

---

## Related

- [FAIR overview](index.md)
- [Health-RI metadata](health-ri-metadata.md)
- [myDRE](../systems/mydre.md)
- [Research Drive](../systems/research-drive.md) — sensitive data stays off public FDP; metadata only in catalogue
