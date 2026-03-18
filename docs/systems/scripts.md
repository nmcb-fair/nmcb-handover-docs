# Scripts and automation

The board indicates a substantial amount of scripting work in Python and R.

## Script themes visible in the board

- Python/R scripts for eligibility
- scripts for ME criteria
- scripts for inclusion criteria
- scripts for compiling M&L files and subsetting on request
- conversion documentation and code for Omron, Tanita, Nellcor, and M&L
- Python scripts for cleaning raw data and quality control
- getting numbers and summary counts

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
