# Risks and improvement backlog

**Status:** Ongoing

This page turns scattered board items into a manageable improvement backlog.

## Current recurring risks

| Risk | Why it matters | Suggested mitigation |
|---|---|---|
| Tacit knowledge in operational tasks | Handover failure if one person leaves | Write task-based instructions and file maps |
| Inconsistent identifiers across systems | Broken merges and wrong linkage | Maintain subject ID source of truth and checks |
| Device-specific data quirks | QC errors and mismatched outputs | Standardise conversion docs and mapping tables |
| Hidden logic in Castor calculations | Hard-to-debug discrepancies | Mirror critical logic in documented scripts |
| Fragile data extraction flow | Manual work and inconsistent exports | Design patient-centric + source-centric extraction model |
| Limited documentation of SQL/Snowflake setup | Slow onboarding and troubleshooting | Document access, connection tests, and key tables |

## Good next improvements

### High priority

- complete the “where everything lives” page
- create a script inventory
- define source of truth for identifiers
- formalise device mapping tables and QC output expectations

### Medium priority

- add a current-state data pipeline diagram
- standardise request log and delivery logging
- create sample examples for common extracts

### Strategic priority

- move recurring manual transformations into versioned pipelines
- evaluate a formal analytical data model
- document OMOP considerations only after core operational flows are stable
