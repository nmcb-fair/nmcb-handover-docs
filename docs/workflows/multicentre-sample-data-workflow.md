# Multi-centre sample data workflow


## Multi-centre sample processing

1. After blood tubes are drawn, **research nurses** open `Data lab NMCB  - Blood tubes file.xlsm`, use the 2nd column `lab_sample_id`, scan barcodes of all blood tubes, and add Participant ID in the 1st column `participant_ID`. Rename the file to `Data lab NMCB  - Blood tubes file - {participant_id}.xlsm` and send it to the lab that processes samples at the Radboud site.
2. The Radboud lab (**RL**) completes the remainder of the file (e.g. `datetime_collection`, `start_datetime_processing`, `finish_datetime_processing`, `datetime_freezer`, `aliquot_nr`, …). Upload the raw **RL** file to the agreed location on Research Drive.
  **Example raw RL export:**
   Example raw RL export
3. **Data scientist** processes the raw RL file with the agreed Python pipeline. Move the raw file to `Radboud/organized/RL/archive` and upload the output to `Radboud/processed/RL/` as `Radboud/processed_{participant_ID}_RL.csv`.

---

## Sample boxing

1. When a sample box is full and delivered to Amsterdam UMC biobank, upload the **Box Data File** to NMCB Research Drive (`Radboud/processed/Biobank/`). Rename the file and fill in the box ID as described in [How to rename box data files](#how-to-rename-box-data-files) before upload.
2. **Data team** expands the Box Data File by adding columns from existing RL files—linking each sample row to the source participant and processing metadata. The result is the **Biobank Submission File**.
3. Another **data team** member validates (spot-check or scripts). Send the validated file to the biobank via FileSender. Current contacts: Erik and Maureen.

### How to rename box data files

One box data file represents **one physical box**. Each box must have its **own unique ID**; the ID must **not be empty**.

The box ID in the **filename** must match the value in the **designated column** inside that file.

#### DNA, PBMC, and PAXGene (Radboud)

These sample types use a shared naming pattern at Radboud UMC:

```text
NMCB_{SAMPLETYPE}_R{nn}_{YYYYMMDD}.xlsx
```

- `**R**` — Radboud UMC  
- `**{nn}**` — box sequence number (`01` = first box, `02` = second, …)  
- `**{YYYYMMDD}**` — date the file is prepared or submitted

Enter the box ID (without the date suffix) into the column shown below:


| Sample type | Example filename                 | Column for box ID | Enter this value   |
| ----------- | -------------------------------- | ----------------- | ------------------ |
| DNA         | `NMCB_DNA_R01_20260318.xlsx`     | `Container Id`    | `NMCB_DNA_R01`     |
| PBMC        | `NMCB_PBMC_R01_20260318.xlsx`    | `Doos`            | `NMCB_PBMC_R01`    |
| PAXGene     | `NMCB_PAXGENE_R01_20260318.xlsx` | `Doos`            | `NMCB_PAXGENE_R01` |


**PAXGene:** use the pattern above (e.g. `NMCB_PAXGENE_R01`), not the older style such as `NMCB_PAXgene_box013`. Continuing the old numbering risks mixing samples across boxes. If `NMCB_PAXgene_box013` was already used, start the new sequence at `NMCB_PAXGENE_R01` (or the next free `R{nn}`) and keep it consistent from then on.

#### Serum, EDTA, plasma, and similar types

Box IDs for types such as **Serum**, **EDTA**, and **Plasma** are **generated automatically when samples are scanned**. Do not invent or assign box IDs manually for these files.

DNA, PBMC, and PAXGene boxes are separate from Serum / EDTA / Plasma boxes; follow the rules for the sample type you are handling.

## Related

- [Sample request](../tasks/sample-request.md)
- [Systems: Biobank](../systems/biobank.md) — short system pointer

