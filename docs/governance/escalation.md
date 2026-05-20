# Issue log and escalation

**Status:** Complete

A hand-over is incomplete without a simple rule for what to do when a task fails.

## Escalation model


| Issue type                 | Example                            | First action                                       | Escalate to                  |
| -------------------------- | ---------------------------------- | -------------------------------------------------- | ---------------------------- |
| Access issue               | Cannot open Castor or shared drive | Verify own permissions and recent changes          | System owner / IT            |
| Data integrity issue       | Duplicate subject IDs              | Pause downstream merging                           | Data manager                 |
| Participant workflow issue | Screener not sent in time          | Record impacted participant(s) and fix if possible | Study coordinator            |
| Device issue               | Corrupt or missing VU-AMS export   | Preserve raw files and document issue              | Device owner / research team |
| Warehouse issue            | Snowflake connection failure       | Capture error and test access assumptions          | Data engineer / IT           |


## Minimum issue log fields

When tracking recurring issues, capture at least:

- date
- workflow
- summary of problem
- impact
- action taken
- owner
- status

## Principle

Do not silently work around structural issues. If a workaround becomes repeated behaviour, it should either be documented as the new process or escalated as a design problem.