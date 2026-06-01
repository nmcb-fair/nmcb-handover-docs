# Device data transfer SOP

Standard protocol for exporting **Tanita**, **VU-AMS**, **Nellcor**, and **Omron** data after a visit and uploading files to NMCB storage. Two official Word versions exist: **Amsterdam UMC (v3)** and **multi-centre (v1)** — device steps are largely the same; **final upload** differs.

| Version | Scope | Date | Source in repo |
| ------- | ----- | ---- | -------------- |
| **v3 — AMC** | Amsterdam visit / AMC laptop workflow | 22 October 2025 | [device-data-transfer-sop-v3-amc.docx](../files/sop-data-transfer/device-data-transfer-sop-v3-amc.docx) |
| **v1 — Multi-centre (Nijmegen)** | **Nijmegen centre only** — template for other sites; device export steps are generic | 2 February 2026 | [multicentre-device-data-transfer-sop-v1-nijmegen.docx](../files/sop-data-transfer/multicentre-device-data-transfer-sop-v1-nijmegen.docx) |

Author (both): Shuxin Zhang. After export, data enters [Device data workflow](../workflows/device-data-workflow.md) QC on Research Drive under `organized/{device}/`.

!!! important "SURF upload links are centre-specific"
    The **Research Drive upload URLs** in v1 (§5.1–5.4) are issued for **Nijmegen (Radboud)** only. **Do not** reuse them for Leiden, Amsterdam multicentre visits, or any **new centre** — the data team will provide **separate links** per site. Update this page when a new centre goes live.

---

## Executive summary

1. Collect per-device exports locally using **Castor ID** in filenames or annotations.
2. Stage files in a local **NMCB Device Data Transfer** folder (OneDrive on AMC laptop, or equivalent at site).
3. Upload to **Research Drive** (and legacy paths below where the SOP still references them).
4. Data team marks weekly folders **newly uploaded** → **ready for QC** after the week closes.

Always use **participant Castor ID** (usually six digits), not hospital patient ID — see [Keep in mind (GDPR)](../index.md#keep-in-mind-gdpr-and-data-sharing).

---

## When to use this SOP

- After each participant visit where devices were used.
- When onboarding a new site or research nurse to device export.
- Before changing upload links or folder naming on Research Drive (coordinate with data team).

---

## First-time setup

Create a local staging folder **`NMCB Device Data Transfer`** with subfolders:

- `Nellcor`
- `Omron`
- `Tanita`
- `VU_AMS` (or `VU AMS`)

### Software (one-time per laptop)

| Tool | Install |
| ---- | ------- |
| **Nellcor Analytics Tool (NAT)** | [Silicon Labs USB-UART driver](http://silabs.com/developers/usb-to-uart-bridge-vcp-drivers) + [Nellcor Analytics Tool request](https://www.medtronic.com/covidien/en-us/products/pulse-oximetry/nellcor-analytics-tool-request.html) |
| **VU-AMS Core** (laptop analysis) | [Java 21 SDK](https://www.oracle.com/java/technologies/downloads/#java21) + [VU-AMS Core](https://vu-ams.nl/vu-ams-core/) |

Visit-day iPad setup: [Device setup for visit](../workflows/device-setup-for-visit.md). Device notes: [Devices](../systems/devices.md).

---

## 1. Tanita

1. Power on Tanita → launch **Tanita Pro** on Windows laptop → connect cable.
2. **Add client:** `+` → Gender, Age; First name **NMCB**; Last name = **Castor ID** → Save → double-click to select.
3. Menu **≡** → **TANITA** tab → **Collect data** → complete measurement.
4. **Share** → **Download Excel** (optional **Send Email** if participant wants report).
5. Save to `NMCB Device Data Transfer/Tanita` → rename **`{CastorID}_Tanita.xlsx`**.

Repeat for each participant.

---

## 2. VU-AMS

1. Power on VU-AMS → **AmSapp** on iPad → connect → **Recording Information**.
2. Enter **PP_ID** = Castor ID, **Elec.Dist**, **Session** = 1, **Study_ID** = NMCB.
3. **Start Recording** → live ECG view.
4. **Markers (first-time):** Recording Information → **Markers** — configure visit markers (urine, NASA lean, handgrip, Beighton, Tanita, blood draw, sit/stand, etc.).
5. **Insert markers** during recording (device confirms with vibration).
6. **Stop Recording** on Recording Information page.
7. **Export:** power off device → remove SD card → card reader → **Do not encrypt** → move participant folder to `NMCB Device Data Transfer/VU_AMS` → rename **`{CastorID}_VU_AMS`**.

**Important:** Power off before removing the SD card; device must not appear in the app when off.

Raw path on Research Drive: `organized/VU_AMS/` — see [Devices — VU-AMS](../systems/devices.md).

---

## 3. Nellcor

1. Connect oximeter to laptop (mini-USB) → open **Nellcor Analytics Tool (NAT)**.
2. On device: **Service menu** → code **6290** → **Communication settings** → **SPDout, 115200**.
3. NAT: **Tools** → **Import Data From Oximeter** — Protocol SPDout, baud **115200**, COM port (often **COM3**) → **Test Connection** → **Download**.
4. **Patient Information:** ID = Castor ID → **Save Patient info**.
5. **Tools** → **Export** → **To Files** + **To Excel File** → filename **`{CastorID}_Oximeter.xlsx`** (e.g. `382718_Oximeter.xlsx`).
6. **Monitoring History** → **Clear Monitoring History** (before next participant).

---

## 4. Omron

### Annotate

1. **History** → **Blood Pressure**.
2. First measurement of participant → **Add Note** → enter **Castor ID** → Save.
3. Repeat for all that participant’s measurements.

### Export and store

1. **Share** (top right) → set date range → format **CSV** → **Show report** → **Share report** → **Mail**:

| Field | AMC v3 | Multi-centre (e.g. Nijmegen) |
| ----- | ------ | ---------------------------- |
| **To** | `nmcb.data@amsterdamumc.nl` | **Your own email** (then download attachment) |
| **Subject** | `Omron` | `Omron` |

2. Download from mailbox — keep default report name `Report(date–date)`; if two uploads same day use `_1`, `_2` suffixes.
3. Store locally until weekly upload.

**Nijmegen / multi-centre v1:** Start date = visit date of participants not yet uploaded; end date = export date.

---

## 5. Final data transfer

### 5.1 Devices — Tanita, Omron, Nellcor (both versions)

**Amsterdam v3 — Research Drive folder rhythm**

- Each **Monday**, a dated folder is created under `Data/organized/{Device}/` (Nellcor, Tanita, or Omron) named with the **date of the upcoming Monday** (e.g. `20251027`).
- The **previous** week’s folder is labelled **`ready for QC`**.
- Mark the **current** week’s folder **`newly uploaded`** when adding files.
- Upload all files collected that week into **that Monday’s folder** (example: upload on 22 Oct 2025 → folder `20251027` created Monday 20 Oct 2025, label **Newly uploaded**).

**Multi-centre v1 — SURF upload links (Nijmegen centre only)**

By **next Monday**, upload via the site-specific links below. These URLs are **only valid for Nijmegen**; other centres get their own links from the data team.

| Device | Upload link (**Nijmegen only**) |
| ------ | ------------------------------- |
| Nellcor | https://amsterdamumc.data.surf.nl/s/ptNJZyKM9A6rRNW |
| Omron | https://amsterdamumc.data.surf.nl/s/5KZaJAc5zC3QkxK |
| Tanita | https://amsterdamumc.data.surf.nl/s/J7gWKT9c8cftAjq |
| VU-AMS | https://amsterdamumc.data.surf.nl/s/x7cd3n5fzirr4EW |

| Centre | Upload links documented here |
| ------ | ---------------------------- |
| **Nijmegen (Radboud)** | Yes — table above |
| **Other / future centres** | Not yet — request links from data management before first upload |

### 5.2 VU-AMS — Amsterdam v3 only (legacy path)

v3 also describes moving the full **`{CastorID}_VU_AMS`** folder to:

`G:\divjk\mp_oz\NMCB\O. Data management\2. Collection\rawData\VU_AMS`

**Current practice:** prefer **Research Drive** `organized/VU_AMS/` (Nijmegen: SURF link in table above if applicable). **G-drive is not reachable from myDRE** — see [Research Drive](../systems/research-drive.md#research-drive-vs-yoda-irods). Align new uploads with the data team before relying on G-drive only.

### 5.3 Lab data — Nijmegen only (v1 §5.2)

When lab data are collected at **Nijmegen / Radboud**:

| Data type | Upload link (**Nijmegen only**) |
| --------- | ------------------------------- |
| Blood test results | https://amsterdamumc.data.surf.nl/s/KRrd2wJKPQ9bRfQ |
| Biological sample processing data | https://amsterdamumc.data.surf.nl/s/iKFNnDZtEBeog9T |

See also [RDL alert workflow](../workflows/rdl-alert-workflow.md) and [Multi-centre sample data workflow](../workflows/multicentre-sample-data-workflow.md).

### 5.4 Biobank box data — Nijmegen only (v1 §5.3)

When a sample box is full and ready to send to Amsterdam UMC (**Nijmegen workflow**):

| Data type | Upload link (**Nijmegen only**) |
| --------- | ------------------------------- |
| Box scan / box data | https://amsterdamumc.data.surf.nl/s/s8GQcFYxfc3fpLz |

Follow box naming in [Multi-centre sample data workflow](../workflows/multicentre-sample-data-workflow.md).

---

## Checklist (per visit / upload batch)

| Step | Done |
| ---- | ---- |
| All exports named or annotated with **Castor ID** | ☐ |
| Tanita → `{ID}_Tanita.xlsx` | ☐ |
| VU-AMS → `{ID}_VU_AMS` folder (SD export, device powered off) | ☐ |
| Nellcor → `{ID}_Oximeter.xlsx`; device history cleared | ☐ |
| Omron CSV exported and annotated | ☐ |
| Files in correct **Monday** folder (AMC) or **centre-specific** SURF link (not another site’s URL) | ☐ |
| Folder labelled **newly uploaded** (AMC rhythm) | ☐ |

---

## Differences at a glance (AMC v3 vs multi-centre v1)

| Topic | AMC v3 | Multi-centre v1 (Nijmegen) |
| ----- | ------ | -------------------------- |
| Omron email recipient | `nmcb.data@amsterdamumc.nl` | Site user’s own email |
| VU-AMS final path | G-drive path + (implicit RD) | Nijmegen SURF link only |
| Lab / biobank upload | Not in v3 | Nijmegen SURF links only |
| Weekly folders | `organized/{Device}/{YYYYMMDD}` labels | Per-centre SURF links (new centres ≠ same URLs) |

---

## Related

- [Device setup for visit](../workflows/device-setup-for-visit.md)
- [Device data workflow](../workflows/device-data-workflow.md)
- [Devices](../systems/devices.md)
- [Improve VU-AMS](../tasks/improve-vu-ams.md)
- [Where data lives](../where-data-lives.md) — `organized/{device}/`
- [Research Drive](../systems/research-drive.md)
- [Data flow (home)](../index.md#end-to-end-data-flow)
