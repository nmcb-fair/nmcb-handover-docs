# Where everything lives

**Status:** Not started

This page should be completed and kept current. It is often the most useful part of a hand-over.

## Recommended structure

Use this page as a map of systems, folders, owners, and permissions.

| Resource | Purpose | Current location | Owner | Notes |
|---|---|---|---|---|
| Shared mailbox | Operational follow-up | `TBD` | `TBD` | Add mailbox name and delegate setup |
| NMCB Core distribution list | Core team email | [resbv-nmcb-core@amsterdamumc.nl](mailto:resbv-nmcb-core@amsterdamumc.nl) | List owner | GAL name: `>Research BV NMCB Core` — [Distributed list](systems/distributed-list.md) |
| Visit log | Visit tracking | `TBD` | `TBD` | Define source of truth |
| Subject ID log | Participant ID mapping | `TBD` | `TBD` | Critical for joins across systems |
| Castor project | Data capture | `TBD` | `TBD` | Add project URL and role names |
| Linked2Trial input/output | Recruitment screener exchange | `TBD` | `TBD` | Note timing expectation |
| Research Drive | Primary file storage (non-sensitive) | NMCB project folder | `TBD` | Not for sensitive data — see [YoDa on Research Drive page](systems/research-drive.md#research-drive-vs-yoda-irods) |
| YoDa / iRODS | Sensitive storage (if needed) | `TBD` | UU / RDM | Future option; not NMCB default today |
| Device raw data | Raw exports | `TBD` | `TBD` | Organise by device and date |
| Device QC outputs | QC reports and cleaned outputs | `TBD` | `TBD` | Prefer versioned folders |
| Scripts | Python/R code | `TBD` | `TBD` | GitHub or Research Drive |
| Snowflake / SQL setup | Structured data | `TBD` | `TBD` | Record how access is provisioned |
| OpenSpecimen | Sample tracking | `TBD` | `TBD` | Biobank system |
| myDRE | Secure analysis environment | `TBD` | `TBD` | Data issuing for requestors |
| LDOT | Participant registry / logistics | LDOT Manager + `data/LDOT/` exports | MEMIC support | Bulk postcode updates: [LDOT](systems/ldot.md) |
| SOPs | Governance and procedures | `TBD` | `TBD` | Keep links stable |
| Data request forms | External access workflow | `TBD` | `TBD` | Add published version |
| Sample request forms | Sample release workflow | `TBD` | `TBD` | Add published version |

## Folder design principle

A good storage structure should separate:

- raw data
- processed data
- scripts
- logs
- documentation
- outgoing deliverables

## Minimum expectation

Every critical workflow documented on this site should point back to an actual folder, system, or repository here. Procedure pages live under [Workflows](workflows/index.md).
