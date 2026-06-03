# Castor EDC

Castor is NMCB’s electronic data capture (EDC) platform: screening, cohort visits, GP surveys, file uploads, and in-form calculations. Exports feed [Snowflake](snowflake.md), [data-request](../tasks/data-request.md) packages, and operational checks.

---

## Castor studies

Studies are grouped by **status** in the Castor UI. Names below match production Castor exactly.

Some databases stay in **Live** or **Test** but are **read-only** (forms locked): data entry is closed, but the study remains open for viewing participant data (e.g. clinical review).

### Live


| Study                                  | Purpose                                                                                                                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **NMCB Bestanden**                     | Participant **file uploads** — documents attached in Castor, separate from the main clinical eCRF.                                                                                                |
| **NMCB Study**                         | **Main cohort eCRF** — screening survey, DSQ-2, full survey, and visit data entry.                                                                                                                |
| **NMCB GP Survey**                     | **GP survey** for general practitioners to record information about enrolled participants (not participant-facing forms).                                                                         |
| **NMCB Measurements & Questionnaires** | **Onsite visit** measurements and questionnaires (NASA Lean Test, handgrip, Beighton, protocol deviations, visit forms). Called “MeasQuest” in RDM documentation. **Read-only** — see note above. |


### Test


| Study                   | Purpose                                                                       |
| ----------------------- | ----------------------------------------------------------------------------- |
| **TEST NMCB Bestanden** | Sandbox for **file-upload** forms before changes go live in `NMCB Bestanden`. |
| **TEST_NMCB Study**     | Sandbox for the **main study eCRF** structure and logic.                      |
| **TEST_NMCB GP Survey** | Sandbox for **GP survey** invitations, fields, and calculations.              |
| **NMCB Screening**      | **Early screening** questionnaires. **Read-only** — see note above.           |


### Archived


| Study                                         | Purpose                                                                       |
| --------------------------------------------- | ----------------------------------------------------------------------------- |
| **Interested in participating in NMCB**       | **Registration portal** for initial interest before full screening enrolment. |
| **TEST_NMCB Screening (LDOT)**                | Screening forms used while **LDOT** was integrated with Castor.               |
| **NMCB Measurements & Questionnaires (LDOT)** | Deprecated **LDOT-linked** variant of MeasQuest.                              |
| **PRODUCTION_NMCB Screening PII**             | Former **production screening** database that included **PII** fields.        |
| **NMCB Screening PII**                        | **Test/sandbox** for `PRODUCTION_NMCB Screening PII` before go-live.          |


**Archived study data (exports):** participant data from the archived databases above is **not** only in Castor — locked/export copies are stored on **Google Drive (G-drive)** under:

```text
NMCB/O. Data management/2. Collection/rawData/Castor/Study Lock
```

Use this folder for historical screening and deprecated-study exports. G-drive is **not** reachable from [myDRE](mydre.md); copy to Research Drive or YoDa if needed for analysis platforms — see [Research Drive — G-drive](research-drive.md#research-drive-vs-yoda-irods).

---

## RDM quality control (2024)

Amsterdam UMC **Research Data Management (RDM)** ran formal Castor QC under **SOP RDM01**, using templates **F02** (validation & derivation plan), **F03** (user acceptance test), and **F08** (eCRF technical QC). Full artefacts are archived on Research Drive under:

`data infrastructure/Data Sources/Castor/Archive/`


| Archive folder    | Scope (Castor studies)                                                                        | Summary                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **nonWMO-RDM-QC** | Screening / **Screening PII** / **GP Survey (Screening)**                                     | **July 2024.** F02 plan completed 2 Jul 2024 (multivariate validations marked NA; calculation/validation CSV exports for Screening PII and GP Survey). F03 UAT 13 Jun–2 Jul 2024 (two testers besides eCRF builder). F08 non-WMO checklist — QC **Sjoerd Manger**, builder **Shuxin Zhang**.                                                                                                  |
| **WMO-RDM-QC**    | **NMCB Measurements & Questionnaires**, **NMCB GP Survey**, main **NMCB** eCRF / survey forms | **August 2024.** Per-study **F08** checklists (MeasQuest QC from 19 Aug; GP Survey QC from 15 Aug, resolved). **F03** WMO user acceptance tests (`F08_NMCB_WMO_UserTest` workbooks, including resolved/adjusted versions). Supporting docs: **WMO Translation.xlsx**, validation form, F02 WMO derivation plan. QC **Alden van Putten** on MeasQuest and GP Survey; builder **Shuxin Zhang**. |


RDM F08 checks **technical** eCRF setup (structure, automations, calculations documentation, data dictionary) — not protocol or scientific design. Findings were tracked in each checklist’s FINDINGS table until closed.

---

## Calculations (JavaScript)

In-form **calculations and eligibility logic** implemented in Castor (JavaScript) are maintained in the GitHub repository:

**[github.com/nmcb-fair/castor-eligibility](https://github.com/nmcb-fair/castor-eligibility)**

Repository layout (top level):


| Folder       | Typical content                     |
| ------------ | ----------------------------------- |
| `Screening/` | Screening-study calculation scripts |
| `GPSurvey/`  | GP Survey calculation scripts       |


Use this repo as the **source of truth** when reviewing or changing Castor calculations; deploy updated scripts into the matching **live** or **test** study after UAT. External validation (e.g. R/Python eligibility checks) should stay aligned with these definitions — see also [GitHub — castor-eligibility](github.md).

---

## Related

- [Snowflake](snowflake.md) — structured loads from Castor
- [LDOT](ldot.md) — registry / logistics (Castor ID linkage)
- [Data request](../tasks/data-request.md) — variable packages from Castor exports
- [Withdrawal SOP](../tasks/sop-withdrawal.md) — LDOT first, then Castor status/archive
- [Where data lives](../where-data-lives.md) — Castor exports on Research Drive / `data pool/`

