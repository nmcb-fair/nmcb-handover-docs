# Data architecture

## Overview

NMCB data currently spans several operational and analytical domains:

- study capture and study logic in Castor
- participant and visit tracking in operational logs
- recruitment-related handoffs such as Linked2Trial
- device outputs requiring cleaning or quality control
- structured data and downstream transformation work in SQL or Snowflake-oriented workflows
- biobank and multicentre data transfer processes

## Conceptual flow

```text
Participant contact / visit
    -> operational tracking
    -> Castor data capture
    -> device outputs
    -> cleaning / QC / transformation
    -> structured storage and extract preparation
    -> internal review or external data request delivery
```

## Architecture principle

The most important technical rule is that identifiers and provenance should survive every transformation step.

That means every workflow should make it possible to answer:

- where did this record originate?
- which script or process changed it?
- which identifier links it back to the participant or visit?
- is the current dataset raw, intermediate, or analysis-ready?

## Current infrastructure topics reflected in the board

The task board shows active work on:

- building a diagram of the data pipeline
- designing file structures in the research drive
- testing SQL setup and Snowflake connectivity
- standardising conversion code for device-derived data
- improving extraction flow by combining patient-centric and source-centric approaches
- exploring automated eligibility logic in Snowflake
- mapping NMCB data toward OMOP

This suggests the infrastructure is still evolving and should be documented as a living system rather than a finished platform.
