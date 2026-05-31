# Device setup for visit


Install and configure study devices on the **iPad** (and laptop where noted) before a participant visit. For what happens after capture—storage, QC, and cleaning—see [Device data workflow](device-data-workflow.md).

## VU-AMS

**Product site:** [VU-AMS Core](https://vu-ams.nl/vu-ams-core/)

### Install


| Where                  | Software      | Link                                                                                   |
| ---------------------- | ------------- | -------------------------------------------------------------------------------------- |
| iPad                   | `coreControl` | [VU-AMS Core app ecosystem](https://vu-ams.nl/vu-ams-core-app-ecosystem/)              |
| Laptop (analysis only) | VU-AMS Core   | [Analysis software](https://vu-ams.nl/analysis-software-for-vu-ams-core-vu-dams-beta/) |
| Laptop (analysis only) | Java 21 SDK   | [Oracle Java 21 downloads](https://www.oracle.com/java/technologies/downloads/#java21) |


### Storage and file types

- Raw and derived VU-AMS files live under Research Drive: `organized/VU_AMS/`.
- The first time you open a `.7fs` file in **VU-AMS Core**, the software also creates a `.amsdatai` sidecar file. Keep it with the `.7fs` file; it speeds up reopening the recording.

### Example ECG trace

A normal recording should look similar to this:

Example VU-AMS ECG trace

*Figure: example VU-AMS ECG graph for QC reference.*

### Contact Person

Martin: [m.j.gevonden@vu.nl](mailto:m.j.gevonden@vu.nl)

Kor: [cjj.stoof@vu.nl](mailto:cjj.stoof@vu.nl)

---

## Omron

### Install

On the iPad, install **OMRON connect**.

### Login

Login is required. Credentials are stored on SharePoint:

`Core Team / Documents / Team Management / Login details / Omron.docx`

([SharePoint login details folder](https://amsterdamumc.sharepoint.com/sites/CoreTeam/Shared%20Documents/Team%20Management/Login%20details?csf=1&web=1&e=wMYiGW))

### Pairing and operational rules

Follow the in-app instructions when pairing OMRON connect to the physical device.

**Important:**

- On the device, **do not switch between User 1 and User 2**. Mixing users causes merged exports and manual cleanup.
- Give each physical device a distinct name in the app (e.g. `Omron 5`) so staff do not pair or connect to the wrong unit.

---

## Castor EDC

On the iPad, add a **Castor EDC** shortcut on the home screen so forms are easy to open during the visit.

Further Castor configuration is documented in [Castor EDC](../systems/castor.md).

---

## Nellcor

### 1. Install Nellcor Analytics Tool (NAT)

1. Open the [Nellcor Analytics Tool software page](https://www.medtronic.com/en-us/healthcare-professionals/products/patient-monitoring/pulse-oximetry/portable-patient-monitoring/nellcor-portable-spo2-patient-monitor/nellcor-analytics-tool-software.html).
2. Click **Download and install**.
3. Complete the survey (placeholder answers are fine).
4. Download and install the application when the download button appears.

### 2. Install Silicon Labs USB driver (Windows)

1. Download the [USB-to-UART bridge VCP drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers).
2. Under **Downloads**, choose **Universal Windows Driver** and unzip the package.
3. On the Windows laptop, open **Device Manager** → **Ports (COM & LPT)**.
4. Select the Nellcor-related port, choose **Update driver** → **Browse my computer for drivers**, and point to the unzipped folder.
5. After installation, Windows should recognise the Nellcor **COM port**.

Set the device date format to **DD/MM/YY** (not MM/DD/YY) before field use so exports match visit dates in downstream QC.

---

## Tanita

Follow the Tanita device manual for onsite and portable units.

The license is issued via **Tanita Service** (typically from `logistics@tanita.eu`). Field mapping differences between onsite Tanita Pro and portable home-visit units are noted in [Devices](../systems/devices.md).

---

## Related

- [Device data workflow](device-data-workflow.md) — export, QC cadence, and cleaning
- [Devices](../systems/devices.md) — per-device handover notes and risks
- [GitHub](../systems/github.md) — device conversion and QC scripts in `nmcb-fair` repos

