# NMCB hand-over documentation

Welcome to the working hand-over for the **Netherlands ME/CFS Cohort and Biobank (NMCB)** data management and data infrastructure role.

This documentation is written to make the role:

- transferable
- reproducible
- easier to maintain
- less dependent on tacit knowledge

## What this site covers

This hand-over focuses on the part of the role that sits between **study operations**, **data management**, and **data engineering**.

The current responsibility set includes work around:

- regular operational follow-up, such as mailbox review, visit tracking, and subject ID tracking
- Castor EDC workflows and eligibility logic
- device data handling and quality control
- scripts for cleaning, transforming, and extracting data
- Snowflake and structured data workflows
- biobank and multicentre data flows
- data request procedures and supporting documentation

## Main responsibility domains

| Domain | Examples |
|---|---|
| Operations | Weekly mailbox, visit log, subject ID log, Linked2Trial screening flow |
| Data capture | Castor forms, calculations, reminders, file uploads |
| Data infrastructure | File structure, data pipeline design, SQL/Snowflake, OMOP thinking |
| Devices | Nellcor, Tanita, VU-AMS, Amsterdam Cognitive Scan, iPad setup |
| Scripts | Eligibility, inclusion criteria, ME criteria, compilation scripts |
| Governance | Data request process, SOPs, sample and data request forms |

## How to use this documentation

Start with:

1. [Scope of this hand-over](getting-started.md)
2. [First 30 days](first-30-days.md)
3. [Where everything lives](where-everything-lives.md)

Then use the section navigation for the relevant workflow.

## Important note

This hand-over is intentionally written in a practical format. Each task should answer five questions:

1. Why does this task exist?
2. When should it be done?
3. Where is it done?
4. What are the steps?
5. What should be checked before the task is considered complete?
