# Biobank data

**Status:** Complete

*Role in NMCB: sample metadata, storage location, and hand-off between labs, Research Drive, OpenSpecimen, and sample requests.*

For each aliquot, biobank-related data should answer:

1. **Where** is it stored? (container, box, row, column)
2. **What** is it? (sample type, concentration, and related metadata)

Inventory and release requests are tracked in [OpenSpecimen](openspecimen.md). Operational steps for Radboud processing, box files, and submission are in [Multi-centre sample data workflow](../workflows/multicentre-sample-data-workflow.md).

## Systems and storage


| System / location                                   | Use                                                                                                |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| [OpenSpecimen](openspecimen.md)                     | Authoritative sample inventory and request tracking                                                |
| Amsterdam UMC biobank                               | Physical storage; receives validated submission files                                              |
| Research Drive (`Radboud/processed/Biobank/`, etc.) | Box data files, submission files, and processing outputs — see [Research Drive](research-drive.md) |


## Data sources

### Amsterdam UMC (internal lab)

Samples are processed by the internal lab and delivered to the biobank. Records are created from that in-house process.

### Radboud and multi-centre (external lab)

Samples are tracked in the template `Data lab NMCB  - Blood tubes file.xlsm`. Field names and values differ from the biobank database, so NMCB maintains explicit **variable** and **sample type** mappings before submission.

Use the codebook and mapping figures below when building or validating biobank submission files.

## Reference files


| File                                                                              | Description                                     |
| --------------------------------------------------------------------------------- | ----------------------------------------------- |
| [NMCB biobank Mappings v1](../files/biobank/nmcb-biobank-mappings-variables.xlsx) | Variable definitions and mapping rules          |
| [Understand OpenSpecimen](../files/biobank/Understnd%20OS.xlsx)                   | OpenSpecimen fields and how they relate to NMCB |


## External lab → biobank mappings

### Variables

Map fields from the external-lab template to biobank variables:

Variable mappings: external lab to biobank

*Figure: variable mappings (external lab → biobank).*

### Sample types

Map external-lab sample type labels to biobank sample types:

Sample type mappings: external lab to biobank

*Figure: sample type mappings (external lab → biobank).*

## Biobank data flow

End-to-end path from collection through storage and requests (internal and external):

Biobank data flow: internal and external paths

*Figure: biobank data flow.*


| File                                                                             | Description                  |
| -------------------------------------------------------------------------------- | ---------------------------- |
| [Biobank data flow drawio (editable)](../files/biobank/biobank data flow.drawio) | Source file for the workflow |


**Radboud / multi-centre detail:** RL file processing, [box file naming](../workflows/multicentre-sample-data-workflow.md#how-to-rename-box-data-files), expansion into a **Biobank Submission File**, validation, and FileSender delivery — see [Multi-centre sample data workflow](../workflows/multicentre-sample-data-workflow.md).

**Sample requests:** selection and pseudonymized exports — see [Sample request workflow](../workflows/sample-request-workflow.md).

## Contacts (Amsterdam UMC biobank)


| Role            | Contact                                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------- |
| General         | [biobank@amsterdamumc.nl](mailto:biobank@amsterdamumc.nl)                                                 |
| Maureen         | [m.e.s.vanderarend@amsterdamumc.nl](mailto:m.e.s.vanderarend@amsterdamumc.nl)                             |
| Erik van Iperen | [e.p.vaniperen@amsterdamumc.nl](mailto:e.p.vaniperen@amsterdamumc.nl) — can grant **OpenSpecimen** access |


## Additional Information

The index of blood tubes and their label.

*Figure: NMCB Blood Label.*

## Related

- [OpenSpecimen](openspecimen.md) — sample tracking system
- [Multi-centre sample data workflow](../workflows/multicentre-sample-data-workflow.md) — RL file, boxing, submission
- [Sample request workflow](../workflows/sample-request-workflow.md) — requesting samples from the biobank
- [Research Drive](research-drive.md) — shared storage layout

