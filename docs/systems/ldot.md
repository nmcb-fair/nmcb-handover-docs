# LDOT


*Role: participant registry and study logistics (screening, locations, postcodes) for NMCB; exports feed overview and eligibility pipelines.*

LDOT Manager is operated with support from **MEMIC** (Maastricht). For export paths used in recurring jobs, see [Recurring study routines — Get numbers](../workflows/recurring-routines.md#get-numbers) (`data/LDOT/`).

---

## Bulk update postcodes

Use this when many participants need a **postal code correction** at once (e.g. after migrating legacy participants and finding postcode misalignment).

**Template (from MEMIC):** [format-update-subject-information.xlsx](../files/ldot/format-update-subject-information.xlsx)  
Original filename from LDOT support: `format update subject information.xlsx`.

| Column | Meaning |
| ------ | ------- |
| `SUBJECT_ID` | **MEMIC UNIQUE ID** from LDOT (not NMCB study ID) |
| `SUBJECT_DETAIL_CONTACT.ZIPCODE` | Zipcode field in LDOT |
| `SUBJECT_DETAIL_CUSTOM.CUSTOM_VAR_01` | Postal code — **4 digits only** (custom var 01) |

Fill both zipcode columns consistently when correcting a participant.

### Step 1 — Retrieve `MEMIC UNIQUE ID`s

1. Open **LDOT Manager**.
2. **Study Management → Subject Handling → Export Subjects**.
3. Choose a **parent location**:
   - **NMCB** — if the participant is still before screener / under the main NMCB tree.
   - Otherwise use the **imported location** where the subject currently lives.
4. Select fields **Zipcode** and **Custom var 01** (postal code, 4 digits).
5. **Generate export**.
6. From the export, note the **MEMIC UNIQUE ID** for each participant whose postcode must change.

### Step 2 — Prepare the import file

1. Open [format-update-subject-information.xlsx](../files/ldot/format-update-subject-information.xlsx).
2. Paste each **MEMIC UNIQUE ID** into the **`SUBJECT_ID`** column.
3. Enter the **correct** values in `SUBJECT_DETAIL_CONTACT.ZIPCODE` and `SUBJECT_DETAIL_CUSTOM.CUSTOM_VAR_01` (4-digit postal code where applicable).

### Step 3 — Import updates

1. Open **LDOT Manager**.
2. **Study Management → Subject Handling → Update Subject Information**.
3. Upload the completed spreadsheet.

Verify a few updated subjects in LDOT after import before relying on downstream exports (overview Rmd, Snowflake, etc.).

---

## Context (Oct 2025)

After bulk migration of 1300+ legacy participants into LDOT, many postcodes were wrong due to field misalignment. MEMIC (David Moonen) provided the template and procedure above instead of a Study Group overwrite file.

---

## Support contacts

| Role | Contact |
| ---- | ------- |
| **LDOT / MEMIC application support** | [ldot-memic@maastrichtuniversity.nl](mailto:ldot-memic@maastrichtuniversity.nl) — David Moonen (Tue–Fri) |
| **LDOT** | [www.ldot.org](https://www.ldot.org) · [MEMIC](https://www.memicmaastricht.nl) |

---

## Handover priorities (still open)

### Access and roles

- Document who has LDOT Manager access at Amsterdam UMC and which locations exist (NMCB, imported sites).

### Other workflows

- Subject export for [Get numbers](../workflows/recurring-routines.md#get-numbers)
- Link between LDOT IDs, Castor, and Subject ID log

### Integration

- `data/LDOT/` exports → `ldot_overview.Rmd` → participant overview spreadsheets

---

## Related

- [Recurring study routines](../workflows/recurring-routines.md) — LDOT export cadence and overview
- [Castor](castor.md) — clinical capture (separate from LDOT logistics)
- [Where data lives](../where-data-lives.md) — record LDOT paths and owners when known
