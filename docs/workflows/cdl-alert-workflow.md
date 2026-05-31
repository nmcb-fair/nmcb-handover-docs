# CDL Alert Workflow

Central Diagnostic Laboratory (CDL) blood results and alerts for NMCB participants, from visit through clinical follow-up.


## Roles

- **Research nurses** — blood draw during visit; later review of Alert / Abnormal folders with physicians
- **Research assistants** — transfer of new CDL files and `CRL admin` from the NMCB data mailbox to Research Drive
- **Data team** — processing raw files into per-participant outputs; archiving processed inputs
- **Physicians** — review with nurses; participant contact by phone or email by severity

## Steps

1. When a participant completes the visit, blood tubes are drawn by **research nurses** during the visit and delivered to the CRL lab. Two tubes are used for lab results exported as CDL data files.
2. Every **Monday and Thursday**, new CDL data files together with the newest `CRL admin` file are transferred by **research assistants** from the NMCB data mailbox to Research Drive (target folder: `/organized/CDL/{YYYYMMDD}`). CDL data files are raw and not organised per participant; `CRL admin` links measurements to participants.
3. By the end of **Monday and Thursday**, these files are processed by the **data team**, producing two files per participant (see below). After processing, move processed files or folders to `Archive`.
  - **Lab result data file** — biomarker measures; CSV
  - **Lab alert file** — measures and reference ranges; indicates whether a participant is normal (`Normal`), abnormal (`Afwijkend`), or alert (`ALERT`)
4. Every **Friday and Tuesday**, files in `ALERT` and `Afwijkend` are reviewed by **research nurses** and **physicians**; participants are informed by phone or email depending on severity. After a participant is informed, move their CDL alert file to `Archived`.

## Mappings: by-hand versus by-machine

When the analyser is temporarily unreliable, the lab runs selected tests **by hand** (e.g., **180070**) instead of **by machine** (e.g.,) **1003885**). Processing scripts must map hand codes to machine codes so results stay comparable in the CDL pipeline.

Full comparison (including examples and CRL comments): [Mappings between by-hand and by-machine](../files/cdl-alert-workflow/Mappings%20between%20by-hand%20and%20by-machine.xlsx).

### Exact matching (same BEPCODE and name)

These analytes use the same code whether measured by hand or by machine:


| Hand / machine BEPCODE | BEPNAAM (label) |
| ---------------------- | --------------- |
| RKRE                   | Kreatinine      |
| RNAT                   | Natrium         |
| RKAL                   | Kalium          |
| RCAL                   | Calcium         |
| ALBU                   | Albumine        |
| RFOS                   | Fosfaat         |
| RCPK                   | CPK             |
| CRPR                   | CRP             |
| EFER                   | Ferritine       |
| TSHR                   | TSH             |
| EFT4                   | Free T4         |
| RGGT                   | Gamma-GT        |
| RPT                    | ALAT(SGPT)      |
| EB12                   | Vitamine B12    |
| H1CI                   | Hb-A1-c IFCC    |
| CKDEPI                 | eGFR (CKD-EPI)  |
| HHB                    | Hemoglobine     |
| HHT                    | Hematocriet     |
| HMCV                   | MCV             |
| HLEU                   | Leukocyten      |
| DIFA                   | Leukodiff       |


### Differential counts: by-hand only vs machine aggregate

For white-cell differentials, the machine often reports **one** population where by-hand reports **several** lines. Use the decision rules below when cleaning or validating CDL exports.


| Decision        | By-hand                                                                       | By-machine                    | Notes                                                                                                          |
| --------------- | ----------------------------------------------------------------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Exact matching  | HLYM# — Lymfocyten#                                                           | HLYA — #Lymfocyten            | Match absolute count                                                                                           |
| Ignore          | HLYM — Lymfocyten (%)                                                         | —                             | Machine does not use separate % line                                                                           |
| Ignore          | HATY — Atypische lymfocyten                                                   | —                             | Machine groups with lymphocytes                                                                                |
| —               | *(CRL: hand lines above = one “lymfocyten” population on machine)*            |                               |                                                                                                                |
| Exact matching  | HEOS# — Eosinofielen#                                                         | HEOA — #Eosinofielen          |                                                                                                                |
| Ignore          | HEOS — Eosinofielen (%)                                                       | —                             |                                                                                                                |
| Exact matching  | HBAS# — Basofielen#                                                           | HBAA — #Basofielen            |                                                                                                                |
| Ignore          | HBAS — Basofielen (%)                                                         | —                             |                                                                                                                |
| Exact matching  | HMON# — Monocyten#                                                            | HMOA — #Monocyten             |                                                                                                                |
| Ignore          | HMON — Monocyten (%)                                                          | —                             |                                                                                                                |
| Sum matches     | HSEG# + HSTA# — Segmenten# + Staven#                                          | HNEA — #Neutrofielen          | Sum of hand # lines equals machine neutrophil count                                                            |
| Ignore          | HSEG, HSTA — Segmenten / Staven (%)                                           | —                             |                                                                                                                |
| —               | *(CRL: hand segment + stab = one “neutrofielen” population on machine)*       |                               |                                                                                                                |
| Different logic | HMEM, HMYE, HPRM — Metamyelocyten, Myelocyten, Promyelocyten                  | HIGA — #Immature Granulocyten | By-hand: abnormal if value between 0 and 2; alarm if value ≥ 2. Machine uses single immature-granulocyte count |
| —               | *(CRL: three hand lines = one “Immature granulocyten” population on machine)* |                               |                                                                                                                |
| Ignore          | HTOX — Toxische korreling                                                     | —                             | Not reported by machine                                                                                        |


## Related

- [RDL alert workflow](rdl-alert-workflow.md) — Radboud lab pattern (includes CDL vs RDL mapping reference)
- [Device data workflow](device-data-workflow.md) — device QC cadence (CDL alert file cleaning appears on the data-team schedule)
- [Systems: Biobank](../systems/biobank.md) — sample and metadata context

