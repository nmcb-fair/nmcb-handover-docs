# RDL Alert Workflow


**Radboud Diagnostic Lab (RDL)** blood results and alerts for NMCB participants at the Radboud site. The flow parallels the [CDL alert workflow](cdl-alert-workflow.md): raw export, linkage via a visit log, processing into structured data and alert outputs, then clinical follow-up on abnormal results.

## Roles

- **Radboud UMC team** — uploads raw RDL exports to Research Drive
- **Data steward** — adds the latest visit log and organises files into dated folders
- **Data scientist** — processes inputs into structured and alert exports
- **Physicians and research nurses** — review alert outputs and inform participants when results are abnormal

## Steps

1. The **Radboud UMC team** uploads a raw RDL export (`{YYYYMMDD}_RDL.xlsx`) to the organised RDL area on Research Drive (`organized/RDL/`).
2. The **data steward** uploads the most recent `Radboud Visit Data Log`, then moves that file and the new RDL export into a dated subfolder (`organized/RDL/{YYYYMMDD}/`).
3. The **data scientist** processes both inputs and produces two exports:
  - **Processed RDL data file** — structured lab results for downstream use (including Snowflake) and stored in `processed/RDL/{YYYYMMDD}/`
  - **RDL alert file** — results with reference ranges for clinical review; used by physicians and nurses to inform participants of abnormal findings; stored in `analyzed/RDL/RDL_alert/`
    ```markdown
    normal (`Normal`), abnormal (`Afwijkend`), or alert (`ALERT`)
    ```

## Reference files


| File                                                                                                                       | Purpose                                          |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| [RDL vs CDL mapping](../files/rdl-alert-workflow/RDL%20vs%20CDL%20mapping%20JD.xlsx)                                       | Crosswalk between RDL and CDL variables;         |
| [Example RDL export (2026-05-18)](../files/rdl-alert-workflow/20260518_RDL.xlsx)                                           | Sample raw RDL                                   |
| [AMC and Radboud lab value comparison](../files/rdl-alert-workflow/lab%20waarden%20AMC%20en%20Radboud%20vergelijking.docx) | Comparison of lab values between AMC and Radboud |


## Related

- [CDL alert workflow](cdl-alert-workflow.md) — Amsterdam CRL / CDL reference pattern
- [Multi-centre sample data workflow](multicentre-sample-data-workflow.md) — Radboud **RL** blood-tube file (separate from RDL diagnostic-lab alert exports)

