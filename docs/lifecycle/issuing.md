# Data issuing

This stage covers how data is shared with requesters: data requests, multicentre transfers, and internal extracts.

## Main issuing channels

| Channel | Purpose | Documentation |
|---------|---------|---------------|
| Data requests | External access | [Data requests](../governance/data-requests.md) |
| myDRE | Secure analysis environment for requestors | [myDRE](../systems/mydre.md) |
| Sample requests | Biobank sample release | [Data requests](../governance/data-requests.md), [OpenSpecimen](../systems/openspecimen.md) |
| Multicentre transfers | Nijmegen ↔ Amsterdam UMC | [Multicentre](../systems/multicentre.md) |
| Internal extracts | Analysis-ready datasets | [Snowflake](../systems/snowflake.md), [Scripts and QC](../systems/scripts-and-qc.md) |

## Data request workflow

1. Receive request form.
2. Check completeness.
3. Confirm scientific and governance fit.
4. Confirm requested data or sample scope.
5. Prepare extract or response.
6. Record what was shared and when.

Before release, confirm:

- the requested data exists
- the request is in scope
- identifiers and anonymisation level are appropriate
- the deliverable can be reproduced if asked again later

## Multicentre transfers

For data moving between Nijmegen and Amsterdam UMC or other sites, document:

- transfer trigger
- transfer frequency
- allowed transport mechanism
- file naming and structure
- expected confirmation back from receiver
- escalation if files are missing or inconsistent

## Operational risk

Biobank and multicentre workflows are especially vulnerable to confusion when naming conventions, sample identifiers, or template versions are not tightly controlled.
