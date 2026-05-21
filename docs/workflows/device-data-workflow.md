# Device data workflow

**Status:** Ongoing

How device outputs move from capture through QC and into cleaning scripts / structured storage. Install apps and devices before a visit in [Device setup for visit](device-setup-for-visit.md); per-device risks and notes stay in [Devices](../systems/devices.md). This page is the **flow** view.

## General rule

For each device, the handover should make explicit:

1. setup before use
2. raw output format
3. naming convention
4. where output is stored for QC (see [Scripts and QC](../systems/scripts-and-qc.md))

## Cadence (from current plan)

Operational cleaning load is uneven by device. Typical assignments include:

- **Weekly** cleaning: Omron, Nellcor, Tanita (onsite / field variants as applicable)
- **Twice weekly** cleaning: **CDL alert file** (see [CDL alert workflow](cdl-alert-workflow.md) for the full lab pipeline)
- **VU-AMS** — ongoing QC; watch for abnormal export patterns (multiple or oversized files)

Document exact weekdays and owners in project SOPs as they stabilise.

## Flow

```text
Device use at visit or home
    -> raw export to agreed folder
    -> QC / format checks (see Scripts and QC)
    -> cleaning or mapping scripts
    -> structured or archive location (e.g. Snowflake-oriented handoff)
```

## Device topics to document (from board)

- portable Tanita vs onsite Tanita Pro — field mapping differences  
- VU-AMS abnormal reports and file patterns  
- Amsterdam Cognitive Scan — link outputs to participant ID  
- Nellcor date format (MM/DD/YY vs DD/MM/YY)  
- iPad setup for home visits

## Related

- [Device setup for visit](device-setup-for-visit.md) — install and configure devices on iPad/laptop before capture  
- [Devices](../systems/devices.md) — Omron, Nellcor, Tanita, VU-AMS, ACS, iPads  
- [CDL alert workflow](cdl-alert-workflow.md) — lab alerts (not a “device” but same data team cadence)

