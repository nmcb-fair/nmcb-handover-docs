# Snowflake and structured data

**Status:** Ongoing

*Role: structured storage; modelling and eligibility outputs; extracts for requests and downstream use.*

The board includes several tasks related to SQL and Snowflake, including setup testing, connection fixes, and automated eligibility ideas.

## What Snowflake appears to be used for

Based on the task board, Snowflake is part of the effort to:

- structure study data more systematically
- reduce manual transformations
- support downstream extraction and reporting
- potentially move logic such as eligibility into a more controlled environment

## Current board themes

- test SQL setup
- fix connection with Snowflake
- SQL knowledge building
- automated eligibility in Snowflake
- improve extraction flow by combining patient-centric with source-centric views

## Hand-over expectations

Document the following as soon as possible:

### Access model

- who grants access
- which roles exist
- which environment is used for development versus production-like work

### Connection details

Do not store secrets here, but document:

- how credentials are provisioned
- required driver or package
- whether VPN or network rules apply
- a simple connection test procedure

### Data model

Document key tables or views relevant for NMCB workflows, especially where they are used for:

- participant-level extracts
- eligibility logic
- data request preparation
- QC summaries

### Failure handling

When connection problems occur, record:

- exact error message
- date/time
- whether issue was local, credential-based, or server-side
- whether a fallback workflow was used

## Architecture note

Moving logic into Snowflake can be beneficial, but only if business rules remain readable and versioned. Avoid replacing one opaque manual process with an opaque database process.
