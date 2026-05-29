# Devices

**Status:** Complete

*Role: device outputs and visit-related measurements.*

For **setup before a visit**, see [Device setup for visit](../workflows/device-setup-for-visit.md). For the **flow** from capture to QC and scripts, see [Device data workflow](../workflows/device-data-workflow.md).

The task board shows several device-related workflows. Device data capture needs explicit documentation because it often contains tacit operational knowledge.

## Device topics visible in the board

- portable Tanita data and mapping differences
- VU-AMS abnormal report
- Amsterdam Cognitive Scan
- changing Nellcor date format from MM/DD/YY to DD/MM/YY
- iPad setup for home visits
- requisites for using Nellcor
- Tanita for home visit

## General rule for device workflows

For each device, document:

1. setup before use
2. raw output format
3. naming convention
4. where output is stored for QC (see [Scripts and QC](scripts-and-qc.md))

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
- how outputs are standardised (see [Scripts and QC](scripts-and-qc.md))

## VU-AMS

### Current board signal

The board notes abnormal reports. It also mentions that multiple or unexpectedly large files can be created rather than a single expected file.

### Handover note

Active improvement work: [Improve VU-AMS](../tasks/improve-vu-ams.md) (QC protocol, Research Drive layout, abnormal file sizes).

Document:

- expected file pattern
- known abnormal export patterns
- whether all files should be preserved
- QC procedure (see [Scripts and QC](scripts-and-qc.md))

## Amsterdam Cognitive Scan

Document the setup, output format, and how output is linked back to the participant ID. QC checks are in [Scripts and QC](scripts-and-qc.md).

## iPads for home visits

Install Castor, Omron, VU-AMS, and other visit apps as described in [Device setup for visit](../workflows/device-setup-for-visit.md). If iPads are used for data collection or participant-facing workflows, also document:

- setup checklist
- installed apps
- account or login dependencies
- reset or handover procedure after use

