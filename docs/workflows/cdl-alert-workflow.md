# CDL Alert Workflow

Central Diagnostic Laboratory (CDL) blood results and alerts for NMCB participants, from visit through clinical follow-up.

## Roles

- **Research nurses** — blood draw during visit; later review of Alert / Abnormal folders with physicians
- **Research assistants** — transfer of new CDL files and `CRL admin` from the NMCB data mailbox to Research Drive
- **Data team** — processing raw files into per-participant outputs; archiving processed inputs
- **Physicians** — review with nurses; participant contact by phone or email by severity

## Steps

1. When a participant completes the visit, blood tubes are drawn by **research nurses** during the visit and delivered to the CRL lab. Two tubes are used for lab results exported as CDL data files.
2. Every **Monday and Thursday**, new CDL data files together with the newest `CRL admin` file are transferred by **research assistants** from the NMCB data mailbox to Research Drive (target folder: `/organized/CDL/{YYYYMMDD}`). CDL data files are raw and not organised per participant; `**CRL admin`** links measurements to participants.
3. By the end of **Monday and Thursday**, these files are processed by the **data team**, producing two files per participant (see below). After processing, move processed files or folders to `**Archive`**.
  - **Lab result data file** — biomarker measures; CSV
  - **Lab alert file** — measures and reference ranges; indicates whether a participant is normal (`Normal`), abnormal (`Afwijkend`), or alert (`ALERT`)
4. Every **Friday and Tuesday**, files in `ALERT` and `Afwijkend` are reviewed by **research nurses** and **physicians**; participants are informed by phone or email depending on severity. After a participant is informed, move their CDL alert file to `**Archived`**.

## Related

- [Biobank data workflow](biobank-data-workflow.md) — other blood / lab–adjacent flows
- [Device data workflow](device-data-workflow.md) — device QC cadence (CDL alert file cleaning appears on the data-team schedule)
- [Systems: Biobank](../systems/biobank.md) — sample and metadata context

