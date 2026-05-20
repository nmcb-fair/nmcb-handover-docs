# To-do

**Status:** Ongoing

- SOPs
  - box data renaming 
  - visit data log 
  - subject id log
- Systems guidance:
  - Openspecimen
    - Query - get all NMCB samples
    - Field - PPID, Barcode, etc. 
    - Columns - concentration, mother tube
  - Castor 
    - **Detail** for Castor database going to Live 
    - Castor UAT and RDM QC workflow
    - change management 
    - Calculations (see GitHub)
    - Suggestion for future: 
      - 1. create data access matrix (who access what)
      - 1. whenever there is update on Castor, inform data steward to update the codebook - otherwise, data requestor get confused by the new values (e.g., Stijn request)
  - LDOT
    - Data download specifications
    - Do not add sensitive (personal identifiable) information on comments
- ## Tasks
- Just document for future:
  - VU-AMS QC document
  - myDRE setup  
  - ECG data mount

# Task template

Use this template for every operational or technical task that needs to be handed over.

## Template

```markdown
## Task name

### Purpose
Why this task exists.

### Frequency or trigger
When the task should be done.

### Systems and locations
Where the task is performed and where inputs/outputs live.

### Inputs
What is needed before starting.

### Steps
1. Step one
2. Step two
3. Step three

### Output
What should exist when the task is complete.

### Quality checks
How to verify the task was done correctly.

### Common issues
Typical errors or bottlenecks.

### Escalation
Who to contact when the task cannot be completed.
```

## Writing guidance

For hand-over quality, write task descriptions so that they are:

- action-based rather than narrative
- explicit about inputs and outputs
- linked to real systems and folders
- clear about owner and escalation path

## Best practice

Avoid descriptions like:

> Check data and fix issues.

Prefer descriptions like:

> Compare the latest Castor export with the previous export, review missing values in required fields, flag records with invalid visit status, and save the issue list in the QC folder.

