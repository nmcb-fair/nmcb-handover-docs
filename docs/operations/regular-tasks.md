# Regular tasks

This page translates the recurring tasks from the board into executable hand-over instructions.

## Weekly NMCB mailbox

### Purpose

Monitor the shared mailbox and ensure time-sensitive operational items are not missed.

### Frequency

Weekly at minimum. Increase frequency during active recruitment or periods with many participant contacts.

### Inputs

- access to the shared mailbox
- current contact list
- current routing rules or responsibilities

### Steps

1. Review all unread or newly received messages.
2. Classify messages into one of the main categories:
   - participant communication
   - scheduling or visit follow-up
   - data issue
   - device issue
   - researcher request
   - administrative request
3. Forward or assign the message to the responsible person when it is outside your direct ownership.
4. Record any action needed in the relevant log or tracker.
5. Flag unresolved items that need follow-up.

### Output

- mailbox triaged
- urgent issues routed
- relevant operational actions logged

### Quality checks

- no urgent participant-facing email remains unassigned
- all data-related problems have an owner
- follow-up deadlines are visible somewhere outside the inbox

---

## Weekly visit log

### Purpose

Maintain an accurate overview of completed, pending, and problematic visits.

### Frequency

Weekly.

### Inputs

- current visit planning overview
- completed visit information from the team
- visit log source file

### Steps

1. Compare the planned visits with completed visits.
2. Update the visit log with visit date, visit type, and status.
3. Add notes on rescheduling, incomplete procedures, or data issues.
4. Flag visits where downstream actions are still pending, such as data upload or device return.

### Output

Updated visit log.

### Quality checks

- no completed visit is missing from the log
- incomplete visits are visibly flagged
- downstream data tasks can be derived from the log

---

## Bi-weekly subject ID log

### Purpose

Keep participant identifiers consistent across operational and analytical systems.

### Frequency

Bi-weekly, and additionally whenever new participants are added.

### Inputs

- current enrolment list
- subject ID log
- Castor identifiers or other operational IDs

### Steps

1. Identify all newly included participants.
2. Assign or verify the subject ID according to the agreed naming convention.
3. Check for duplicates or accidental reuse.
4. Confirm the same identifier is used consistently in all dependent systems.
5. Save the updated log in the agreed source location.

### Output

Updated subject ID master list.

### Quality checks

- no duplicate IDs
- no gaps caused by accidental deletion or overwriting
- mapping remains consistent across logs, Castor, and device outputs

---

## Bi-weekly send screeners to Linked2Trial

### Purpose

Ensure new participants receive the required general screeners within the expected time window.

### Context from current board

The current note indicates that Laurian provides a participant list regularly and that the general screeners should be sent within **48 hours**.

### Frequency

Bi-weekly routine check, but the operational expectation is driven by the 48-hour turnaround after receipt of the list.

### Inputs

- participant list from Linked2Trial or team contact
- agreed export or import format
- access to the receiving system and confirmation method

### Steps

1. Check whether a new participant list has been received.
2. Validate that the list has the required identifiers and contact fields.
3. Prepare the screener input file or upload package.
4. Send or upload the screener data according to the agreed workflow.
5. Confirm completion and record the date.
6. Flag participants who could not be processed.

### Output

Participants transferred into the screener workflow.

### Quality checks

- 48-hour target met where possible
- no participant appears twice
- any failed transfer is logged and visible

---

## Sample requests

### Purpose

Process requests for biological samples from the biobank. Ensure samples are released according to governance and that transfers are documented.

### Frequency or trigger

As requests are received. See [Data requests](../governance/data-requests.md) and [Sample request forms](../governance/data-requests.md#minimum-form-contents).

### Systems and locations

- [OpenSpecimen](../systems/openspecimen.md) — sample tracking
- [Biobank](../systems/biobank.md) — data flow and templates
- Sample request form and log

### Inputs

- approved sample request form
- access to OpenSpecimen and biobank systems

### Steps

1. Receive and validate the sample request.
2. Confirm request is approved and in scope.
3. Prepare sample list or extract according to template.
4. Coordinate with biobank for sample retrieval and transfer.
5. Record what was shared and when.

### Output

- samples released as per approval
- request logged

### Quality checks

- request has valid approval
- sample identifiers are correct
- transfer is documented

### Escalation

`TBD`

---

## Get numbers

### Purpose

Produce summary counts and numbers for reports, dashboards, or ad hoc requests (e.g. eligibility counts, recruitment status, visit completion).

### Frequency or trigger

As requested; may be weekly or monthly for routine reports.

### Systems and locations

- [Scripts and QC](../systems/scripts-and-qc.md) — scripts for summary counts
- [Snowflake](../systems/snowflake.md) — structured data queries
- [Castor](../systems/castor.md) — exports for counts

### Inputs

- access to relevant data sources
- script or query for the requested numbers

### Steps

1. Clarify what numbers are needed and for what period.
2. Identify the correct script, query, or export.
3. Run the script or query.
4. Validate the output (e.g. check against previous run).
5. Deliver the numbers in the agreed format.

### Output

- numbers delivered
- source and method documented for reproducibility

### Quality checks

- numbers are consistent with known totals where applicable
- method can be repeated if asked again

### Escalation

`TBD`

---

## Prepare checklist for data routine

### Purpose

Reduce dependence on memory and standardise recurring work.

### Frequency

Update monthly or whenever operational steps change.

### Steps

1. List recurring tasks by week, month, and ad hoc trigger.
2. Add owner, backup owner, and expected completion time.
3. Link each checklist item to the relevant documentation page.
4. Version the checklist so changes are traceable.

### Output

Operational checklist used for routine work and onboarding.
