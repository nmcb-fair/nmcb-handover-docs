# Devices and QC

The task board shows several device-related workflows. These need explicit documentation because device data often contains the highest amount of tacit operational knowledge.

## Device topics visible in the board

- portable Tanita data and mapping differences
- VU-AMS abnormal report
- VU-AMS quality control protocol
- changing Nellcor date format from MM/DD/YY to DD/MM/YY
- Amsterdam Cognitive Scan QC
- iPad setup for home visits
- requisites for using Nellcor
- Tanita for home visit

## General rule for device workflows

For each device, document five things:

1. setup before use
2. raw output format
3. naming convention
4. quality control procedure
5. cleaned output or conversion format

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

This is both a QC and data model issue. The next person should know:

- what fields differ between device versions
- whether a field mapping table exists
- how outputs are standardised before analysis use

## VU-AMS

### Current board signal

The board notes abnormal reports and a QC protocol. It also mentions that multiple or unexpectedly large files can be created rather than a single expected file.

### Handover note

Document:

- expected file pattern
- known abnormal export patterns
- whether all files should be preserved
- which script or manual process is used for QC
- what constitutes a pass/fail QC result

## Amsterdam Cognitive Scan

Document the QC checks performed, what is considered complete, and how output is linked back to the participant ID.

## iPads for home visits

If iPads are used for data collection or participant-facing workflows, document:

- setup checklist
- installed apps
- account or login dependencies
- reset or handover procedure after use
