# Data modelling

This stage covers how data is structured for analysis: Snowflake structures, eligibility logic, and OMOP mapping.

## Main modelling activities

| Activity | Purpose | System |
|----------|---------|--------|
| Snowflake structures | Tables, views, analytical queries | [Snowflake](../systems/snowflake.md) |
| Eligibility logic | Inclusion criteria, ME criteria | [Castor](../systems/castor.md), [Scripts and QC](../systems/scripts-and-qc.md) |
| OMOP mapping | Standardised data model | In progress |

## Eligibility scripts

Python/R scripts exist to calculate eligibility in parallel with Castor automatic calculations. This provides an external check.

Document for each script:

- input export required from Castor
- exact fields used
- run command or notebook location
- expected output structure
- how discrepancies with Castor are resolved

## Snowflake

Snowflake is used to potentially move logic such as eligibility into a more controlled environment.

Current board themes:

- automated eligibility in Snowflake
- improve extraction flow by combining patient-centric with source-centric views

## Architecture note

Moving logic into Snowflake can be beneficial, but only if business rules remain readable and versioned. Avoid replacing one opaque manual process with an opaque database process.

## OMOP

Mapping NMCB data toward OMOP is on the roadmap. Document OMOP considerations only after core operational flows are stable.

## Next stage

Structured data feeds into [Issuing](issuing.md) (extracts, data requests) and [Analysis](analysis.md).
