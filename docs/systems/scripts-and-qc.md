# Scripts and QC

**Status:** Ongoing

*Role: conversion and QC scripts; eligibility-related logic; extracts and summary counts.*

The board indicates a substantial amount of scripting work in Python and R, including quality control of device outputs.

## Script themes visible in the board

- Python/R scripts for eligibility
- scripts for ME criteria
- scripts for inclusion criteria
- scripts for compiling M&L files and subsetting on request
- conversion documentation and code for Omron, Tanita, Nellcor, and M&L
- Python scripts for cleaning raw data and quality control
- getting numbers and summary counts

## Device QC

QC procedures for device outputs (see [Devices](devices.md)) are implemented in scripts. For each device, document:

- expected file pattern
- QC script or manual process
- pass/fail criteria
- cleaned output or conversion format

### Device-specific QC notes

- **Nellcor:** Date format change from MM/DD/YY to DD/MM/YY — device settings matter for downstream matching.

- **Tanita:** Difference between onsite Tanita Pro and portable home-visit Tanita data; document field mappings and how outputs are standardised.

- **VU-AMS:** Document expected file pattern, abnormal export patterns, QC script or manual process, and pass/fail criteria.

- **Amsterdam Cognitive Scan:** Document QC checks, completeness criteria, and how output links to participant ID.

## Recommended script inventory

Every script should be listed in a simple inventory table.

| Script | Purpose | Input | Output | Owner | Status |
|---|---|---|---|---|---|
| `TBD` | `TBD` | `TBD` | `TBD` | `TBD` | active / draft / deprecated |

## Minimum documentation per script

For each maintained script, capture:

- repository or folder location
- language and package dependencies
- how to run it
- required inputs
- produced outputs
- expected runtime or scale
- validation or QC rule

## Good practice for hand-over

Scripts should not be documented as only code references. The next person should be able to answer:

- when should this script be run?
- who relies on its output?
- what happens if it fails?
- does it overwrite data or create a new version?

## Automation opportunities reflected in the board

The board suggests repeated interest in reducing manual work, especially around:

- eligibility logic
- raw file cleaning and QC
- extraction flow design
- standardising conversion code

These are strong candidates for future formal pipelines rather than person-dependent scripts.
