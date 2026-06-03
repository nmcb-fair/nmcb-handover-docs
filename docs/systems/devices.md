# Devices

*Role: device outputs and visit-related measurements.*

For **setup before a visit**, see [Device setup for visit](../workflows/device-setup-for-visit.md). For the **flow** from capture to QC and scripts, see [Device data workflow](../workflows/device-data-workflow.md).

The task board shows several device-related workflows. Device data capture needs explicit documentation because it often contains tacit operational knowledge.

## General rule for device workflows

For each device, document:

1. setup before use
2. raw output format
3. naming convention
4. where output is stored for QC (see [Device data workflow](../workflows/device-data-workflow.md) and [Where data lives](../where-data-lives.md))

## Omron

Logi in is required for using the `OMRON connect` application, and login in detail can be found at: [https://amsterdamumc.sharepoint.com/sites/CoreTeam/Shared%20Documents/Team%20Management/Login%20details?csf=1&web=1&e=wMYiGW](https://amsterdamumc.sharepoint.com/sites/CoreTeam/Shared%20Documents/Team%20Management/Login%20details?csf=1&web=1&e=wMYiGW)

## Nellcor

### Current board signal

There is a setup task and a task specifically about changing the device date format from **MM/DD/YY** to **DD/MM/YY**.

### Handover note

Device settings matter because date formatting mistakes can break downstream matching to visits. Record:

- exact setup steps
- screenshot or instruction source
- verification step before field use

## Tanita

### Current board signal

The board notes a difference between onsite Tanita Pro and portable home-visit Tanita data, with missing mappings.

### Handover note

Document:

- what fields differ between device versions
- whether a field mapping table exists
- how outputs are standardised (conversion scripts in [GitHub](github.md) repos)

## VU-AMS

### Current board signal

The board notes abnormal reports. It also mentions that multiple or unexpectedly large files can be created rather than a single expected file.

### Processing setup: mount Research Drive (not a local myDRE path)

VU-AMS analysis code (e.g. Angela Koloi’s processing class) must read and write on **Research Drive**, not on a personal or workspace-local path inside myDRE. An early build used a **local myDRE path**; the intended production setup uses the **shared Research Drive tree** (e.g. `organized/VU_AMS/` — see [Improve VU-AMS](../tasks/improve-vu-ams.md)).

**RDM approach (Paulo Heemskerk, Jan–Feb 2026):**

1. **Mount Research Drive via WebDAV** on the machine where you run the class (myDRE VM or workstation), e.g. as drive `**R:*`*.
2. Run the processing class **as if working locally**, but with paths rooted on that mount (e.g. `R:\...` instead of `C:\...` or a myDRE-only folder).
3. Use a WebDAV client supported by Amsterdam UMC / SURF:
  - **[Cyberduck](https://cyberduck.io/)** — documented for Research Drive: [Access Research Drive via Cyberduck (SURF)](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/126222540/RD+Access+Research+Drive+via+Cyberduck)
  - **[Mountain Duck](https://mountainduck.io/)** — alternative client (same WebDAV mount idea)

After mounting, point the VU-AMS pipeline at the NMCB folder on Research Drive so outputs land in the shared layout. **Processed files** should be placed in the agreed shared folders on a **weekly** cadence (coordination with Anne Rolf / DM team).

**Contacts for mount / Research Drive access:** Paulo Heemskerk — [p.f.heemskerk@amsterdamumc.nl](mailto:p.f.heemskerk@amsterdamumc.nl) (RDM). Processing / class: Angela Koloi — [a.koloi@uva.nl](mailto:a.koloi@uva.nl).

### Abnormal file sizes and dates (VU-AMS support)

Typical `.7fs` exports are on the order of **~200 MB** per recording. Outliers need different handling depending on whether the file is **too large** or **too small** (see [Improve VU-AMS — Task 3](../tasks/improve-vu-ams.md#task-3-investigate-abnormal-vu-ams-file-sizes) for undersized files).

**Oversized file (~600 MB) — device crash (Martin Gevonden, VU-AMS):**

- The recording metadata may show **today’s date**, but the file is **not** a normal long visit.
- Cause: a **device crash** prevented the recording from being **closed and truncated** as usual, so the export grows far beyond the expected size.
- Treat as a **corrupted / incomplete close** export; confirm with VU-AMS support before using in analysis. Do not assume valid visit length from file size alone.

**Wrong recording date (e.g. 9 September 1919):**

- Another failure mode on **older device firmware**: timestamps can be wrong (e.g. year **1919**) even when the visit was recent.
- Always cross-check the **actual visit date** (visit log, Castor, Subject ID log) against the date inside the `.7fs` / export metadata.

**Firmware:**

- These issues were **rare** on the firmware version in use at the time; VU-AMS reported they are **fixed in current firmware**.
- Plan **firmware upgrades** on field devices with [Martin Gevonden](mailto:m.j.gevonden@vu.nl) / [VU-AMS Core](https://vu-ams.nl/vu-ams-core/) when anomalies appear or on a maintenance schedule.


| Symptom                                    | Likely cause                    | Action                                                                                                |
| ------------------------------------------ | ------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Very large** (~600 MB+), “today” in file | Crash; file not closed normally | Flag for VU-AMS; verify visit; see QC protocol                                                        |
| **Wrong year** in file metadata            | Old firmware date bug           | Compare to real visit date; upgrade firmware                                                          |
| **Much smaller** than ~200 MB              | Short visit or export problem   | See [Improve VU-AMS Task 3](../tasks/improve-vu-ams.md#task-3-investigate-abnormal-vu-ams-file-sizes) |


### Handover note

Active improvement work: [Improve VU-AMS](../tasks/improve-vu-ams.md) (QC protocol, Research Drive layout, abnormal file sizes).

Document:

- expected file pattern (~200 MB; flag outliers per table above)
- known abnormal export patterns
- whether all files should be preserved
- QC procedure (see [Device data workflow](../workflows/device-data-workflow.md))
- confirmed WebDAV mount letter and path prefix used in production (`R:\` or equivalent)

## Amsterdam Cognitive Scan

Document the setup, output format, and how output is linked back to the participant ID. QC cadence is in [Device data workflow](../workflows/device-data-workflow.md).

## iPads for home visits

Install Castor, Omron, VU-AMS, and other visit apps as described in [Device setup for visit](../workflows/device-setup-for-visit.md). If iPads are used for data collection or participant-facing workflows, also document:

- setup checklist
- installed apps
- account or login dependencies
- reset or handover procedure after use

