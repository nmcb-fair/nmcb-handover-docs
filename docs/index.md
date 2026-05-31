# NMCB hand-over documentation

**Status:** Ongoing

Welcome to the working hand-over for the **Netherlands ME/CFS Cohort and Biobank (NMCB)** data management and data infrastructure role.

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

This documentation is written to make the role:

- transferable
- reproducible
- easier to maintain
- less dependent on tacit knowledge

## How this site is organised

| Section | Purpose |
|---------|---------|
| **Where everything lives** | Paths, owners, and key locations (start here) |
| **Workflows** | CDL/RDL alerts, multicentre sample handling, devices, recurring routines |
| **Systems** | Castor, devices, scripts, Snowflake, Research Drive, biobank, myDRE, [NMCB Core list](systems/distributed-list.md), GitHub |
| **Tasks** | Step-by-step procedures (data request, sample request, ChatGPT, device QC, etc.) |

## Page status

- **Complete** — ready to use for hand-over; only routine maintenance expected.
- **Ongoing** — useful now, but details still need confirmation, extension, or regular updates.
- **Not started** — placeholder or draft page that still needs core content.

## How to use this documentation

Start with [Where everything lives](where-everything-lives.md), then open the **workflow** or **system** page for the task at hand. Use **Tasks** for runnable procedures (data packages, sample requests, tooling).

Each task page should answer:

1. Why does this task exist?
2. When should it be done?
3. Where is it done?
4. What are the steps?
5. What should be checked before the task is considered complete?
