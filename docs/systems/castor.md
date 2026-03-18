# Castor EDC

Castor is the main data capture environment for study forms, survey logic, and participant-related study data.

## Current Castor-related task themes from the board

- review of calculations
- parallel eligibility calculation in Python/R versus Castor JavaScript logic
- screener reminders for participants with incomplete surveys
- dependencies and calculation logic for specific questionnaires
- connection between Castor and Snowflake-oriented workflows
- evaluation of a new Castor setup for uploading files

## Core hand-over points

### 1. Calculations and logic

Castor calculations should not be treated as self-evident. Where important calculations exist, document:

- variable dependencies
- formula or logic definition
- expected output values
- known edge cases
- whether the same logic exists in an external validation script

### 2. Eligibility scripts

The board indicates Python/R scripts exist to calculate eligibility in parallel with Castor automatic calculations. This is good practice because it provides an external check.

Document for each script:

- input export required from Castor
- exact fields used
- run command or notebook location
- expected output structure
- how discrepancies with Castor are resolved

### 3. Reminders for incomplete screeners

The board includes a task for reminding 89 participants who had not completed screening surveys. That should become a standard operational workflow rather than a one-off memory-based task.

Suggested workflow elements:

1. Define the query or filter used to identify incomplete cases.
2. Export or list the relevant participants.
3. Review exclusions before sending reminders.
4. Send reminders through the agreed channel.
5. Record reminder date and outcome.

### 4. File uploads in Castor

If Castor is being used for uploading files, document very clearly:

- allowed file types
- naming conventions
- maximum size or system limitations
- where uploaded files are later retrieved for QC or processing

## Risks

Main risks in Castor workflows include:

- hidden logic in form calculations
- inconsistent use of identifiers
- reminder processes that are not reproducible
- dependence on manual exports without versioning
