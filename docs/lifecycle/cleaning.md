# Data cleaning

This stage covers quality control and transformation of raw data before it is used for analysis.

## Main cleaning activities

| Activity | Purpose | System |
|----------|---------|--------|
| Device QC | Validate and clean device outputs | [Scripts and QC](../systems/scripts-and-qc.md) |
| Conversion scripts | Standardise formats (Omron, Tanita, Nellcor, M&L) | [Scripts and QC](../systems/scripts-and-qc.md) |
| Python/R cleaning | Clean raw data, quality control | [Scripts and QC](../systems/scripts-and-qc.md) |

## Device QC and conversion

See [Scripts and QC](../systems/scripts-and-qc.md) for QC procedures and conversion scripts. For each device, document:

1. setup before use (see [Devices](../systems/devices.md))
2. raw output format
3. naming convention
4. quality control procedure
5. cleaned output or conversion format

## Scripts

Scripts for cleaning and conversion should be documented with:

- repository or folder location
- language and package dependencies
- how to run
- required inputs
- produced outputs
- validation or QC rule

## Automation opportunities

The board suggests repeated interest in reducing manual work around:

- raw file cleaning and QC
- standardising conversion code

These are strong candidates for future formal pipelines rather than person-dependent scripts.
