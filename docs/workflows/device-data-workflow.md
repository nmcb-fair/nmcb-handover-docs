# Device data workflow


How device outputs move from capture through QC and into cleaning scripts / structured storage. Install apps and devices before a visit in [Device setup for visit](device-setup-for-visit.md); per-device risks and notes stay in [Devices](../systems/devices.md). This page is the **flow** view.

## General rule

For each device, the handover should make explicit:

1. setup before use
2. raw output format
3. naming convention
4. where output is stored for QC (see [Devices](../systems/devices.md))

## Cadence (from current plan)

Operational cleaning load is uneven by device. Typical assignments include:

- **Weekly** cleaning: Omron, Nellcor, Tanita (onsite / field variants as applicable)
- **Twice weekly** cleaning: **CDL alert file** (see [CDL alert workflow](cdl-alert-workflow.md) for the full lab pipeline)
- **VU-AMS** — ongoing QC; watch for abnormal export patterns (see [Improve VU-AMS](../tasks/improve-vu-ams.md))

Document exact weekdays and owners in project SOPs as they stabilise.

## Flow

```text
Device use at visit or home
    -> raw export to agreed folder
    -> QC / format checks
    -> cleaning or mapping scripts
    -> structured or archive location (e.g. Snowflake-oriented handoff)
```

## Device topics to document (from board)

- portable Tanita vs onsite Tanita Pro — field mapping differences  
- VU-AMS abnormal reports and file patterns  
- Amsterdam Cognitive Scan — link outputs to participant ID  
- Nellcor date format (MM/DD/YY vs DD/MM/YY)  
- iPad setup for home visits

## Correction of data

When a mistake shows up in [Snowflake](../systems/snowflake.md) (SF), it usually means something went wrong earlier in the **organized → processed → Snowflake** chain. Trace the error back to the source files on [Research Drive](../systems/research-drive.md) before changing anything downstream.

### Example: wrong participant ID in a Nellcor (oximetry) file

Participant **1001234** had an oximetry file incorrectly named `1004321_Nellcor.xlsx`. The wrong ID propagated through the whole pipeline:

| Stage | File or table | ID used |
| ----- | ------------- | ------- |
| Raw | `1004321_Nellcor.xlsx` | `1004321` (filename and field values) |
| Processed | `1004321_Nellcor.csv` | `1004321` |
| Snowflake | Oximetry table | `1004321` as `PARTICIPANT_ID` |

### Step 1 — Back up and correct the raw file

Work in the dated `organized/{Device}/{YYYYMMDD}/` folder where the file lives (e.g. `organized/Nellcor/20260101/`).

**Raw (`organized/`)**

1. Create an **`archive`** subfolder in that dated folder.
2. Copy the incorrect raw file into `archive/` and rename it — e.g. `1004321_Nellcor_wrong.xlsx`. Use a `_wrong` suffix because a real participant **1004321** may appear later; keeping the bare ID in the archive name would cause confusion.
3. Edit the copy **outside** `archive/` (the file that stays in the dated folder) and correct the participant ID and any related fields.

**Processed (`processed/`)**

4. **Delete** the incorrect processed file (e.g. `1004321_Nellcor.csv` in `processed/Nellcor/20260101/`). Do not archive it with `_wrong` — a stray processed file is easy to reload by mistake. The raw `_wrong` copy in `organized/.../archive/` is enough audit trail.

!!! warning "How to edit raw files"
    Correct IDs in a **text editor** (e.g. Notepad) or with a **script** — not by editing directly on Research Drive or in Excel. Direct edits on the share or in Excel are not recommended (formatting, encoding, and sync issues).

### Step 2 — Fix downstream data

Choose **Option A** or **Option B** depending on the error and who uses the data. Contact **Aad** and **Gabriel** before any Snowflake delete, update, or reload — they can advise on the safest approach for the affected table(s).

!!! tip "Which option?"
    **Prefer Option A (reprocess)** when you can — it keeps `organized/`, `processed/`, and Snowflake aligned, and any future reload from processed files will not undo the fix.

    **Option B (Snowflake-only)** is reasonable for a **simple, isolated mistake** (e.g. wrong `PARTICIPANT_ID` only, no bad derived values) when reprocessing is slow or risky and you accept that `processed/` will stay empty for that participant until the next full run. Step 1 (correct raw + delete wrong processed) should still be done so Research Drive reflects the truth even if you skip reprocessing.

#### Option A — Reprocess and reload (default)

1. Run the usual cleaning pipeline on the corrected raw file (e.g. `1001234_Nellcor.xlsx` after rename/correction).
2. Place the corrected raw file in the **most recent processing folder** — under the current agreement, device raw files are processed every **Monday**, and folders are named for that Monday’s date. For example, if today is **5 June 2026**, use folder **`20260608`** (the upcoming Monday).
3. **Remove the wrong rows from Snowflake**, then load from the new processed output.

#### Option B — Update Snowflake only (exception)

1. **Do not** move the corrected raw file to the recent Monday folder and **do not** re-run the cleaning pipeline.
2. **Update the affected values in Snowflake** directly (e.g. set `PARTICIPANT_ID` from `1004321` to `1001234` for the affected rows). Coordinate with **Aad** and **Gabriel** on the exact `UPDATE` / delete-and-replace strategy and on whether linked tables need the same change.

!!! warning "Option B risks"
    Snowflake may be correct while `processed/` has no file for that participant (you deleted the wrong one in Step 1). That is usually fine if nothing reads `processed/` for this fix, but **data pool builds, audits, or a full Snowflake reload from processed files could diverge**. Document that Option B was used and schedule reprocessing if a full chain refresh is planned.

Document what was wrong, which raw `_wrong` file was archived, which processed file was deleted, which option you used, and who approved the Snowflake change in the team log or ticket for that correction.

## Related

- [Device setup for visit](device-setup-for-visit.md) — install and configure devices on iPad/laptop before capture  
- [Improve VU-AMS](../tasks/improve-vu-ams.md) — QC protocol, folder structure, abnormal file sizes  
- [Devices](../systems/devices.md) — Omron, Nellcor, Tanita, VU-AMS, ACS, iPads  
- [Research Drive](../systems/research-drive.md) — `organized/` and `processed/` device folders  
- [Snowflake](../systems/snowflake.md) — structured device tables after processing  
- [CDL alert workflow](cdl-alert-workflow.md) — lab alerts (not a “device” but same data team cadence)

