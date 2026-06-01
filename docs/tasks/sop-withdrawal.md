# Withdrawal SOP

Procedure for handling participant **withdrawal** from the NMCB study: mark loss of follow-up (LOF) in LDOT, update Castor, and archive when required. Ensures GDPR-aligned handling with an auditable record while respecting the right to withdraw at any time.

**Canonical SOP (PDF):** [NMCB Withdrawal SOP v3 (Amsterdam UMC SharePoint)](https://amsterdamumc.sharepoint.com/sites/CoreTeam/Shared%20Documents/Participants%20and%20Visits/SOP/NMCB%20Withdrawal%20SOP%20v3.pdf?csf=1&web=1&e=Dh5lBx)  
**Protocol date on PDF:** 24 November 2025 (v3 includes LDOT **before** Castor; early “step 1” from older drafts was removed).

Keep a **backup copy** of the PDF (and any related Excel) in this repo or on Research Drive for **Clinical Monitoring Center (CMC)** checks — see [Backup copies](#backup-copies).

---

## Executive summary

When a participant withdraws:

1. **Identify** the participant (usually via cancellation email → search in **LDOT**).
2. **Register study loss** in LDOT (`SET LOF` → **Withdrawal**); note the **Castor ID** shown in LDOT.
3. **Update Castor** — status **Withdrawal**; **archive** the participant only if they explicitly request **data deletion**.
4. **Document** the case (withdrawal overview in LDOT; optional legacy files on Research Drive — see [Historical notes](#historical-notes)).

Performed by **research nurses** or the **data team** (central study team and multicentre sites use the same LDOT and Castor instances).

---

## When to use this SOP

- Participant sends a withdrawal / cancellation email (or equivalent contact).
- Core team or monitoring asks to reconcile archived Castor records vs withdrawal intent.
- Before CMC: confirm backup SOP PDF and withdrawal documentation are in the agreed folder.

---

## Step 1 — Register subject loss in LDOT

LDOT must be done **first** so you obtain the **Castor ID** for step 2.

1. Open **LDOT Manager** → **Subject Details** → **Search subject**.
2. Open the **Other** tab → select **Email address**.
3. Enter the email address from the participant’s cancellation message → search. The subject should appear in the list on the right.
4. If no match on email, try **first and/or last name** (from the email signature or address).
5. Click the subject entry.
6. Open the drop-down next to **Section** → select **Logistics**.
7. Scroll down → click **SET LOF**.
8. In the pop-up, select **Withdrawal** → **SAVE REASON(S)**.
9. Note the **Castor ID** next to the **Subject** header (required for Castor).

Further LDOT context: [LDOT](../systems/ldot.md). MEMIC added **Withdrawal** to LOF/PreLOF reason lists (Aug 2025).

---

## Step 2 — Archive participant in Castor

1. Log in to **Castor** → **Participant** menu.
2. In **Search**, enter the **Castor ID** from step 1.
3. Click the **three-dot** menu next to the participant → **Update Status**.
4. Set status to **Withdrawal** → enter reason → **Save Changes**.

### If the participant requests data deletion

Only when they **explicitly** ask for data to be deleted:

1. **Three-dot** menu again → **Archive**.
2. Confirm → **Archive Participant**.

If they withdraw but **do not** request deletion, use status **Withdrawal** only — **do not** archive (screening/data may need to remain for audit; see [Unarchive screening cases](#unarchive-screening-only-withdrawals) below).

Castor background: [Castor EDC](../systems/castor.md).

---

## Checklist (end of process)

| Check | Done |
| ----- | ---- |
| LOF set to **Withdrawal** in LDOT with reason saved | ☐ |
| Castor ID recorded matches LDOT and Castor | ☐ |
| Castor status = **Withdrawal** with reason | ☐ |
| **Archive** in Castor only if explicit **data deletion** requested | ☐ |
| If archived in error (withdrawal only): screening unarchive reviewed — see below | ☐ |
| Backup SOP PDF available for CMC folder when required | ☐ |

---

## Unarchive screening-only withdrawals

Some participants were **archived in Castor** after withdrawal but **did not** request data deletion. For those cases, **unarchive** the screening survey in the legacy **NMCB Screening** database if applicable.

**Historical lookup (obsolete list):** Research Drive `O.Data Management/5.Withdrawal/Participants not contacted further.xlsx` — Dutch communication notes. **This list is from an early process (pre-LDOT) and is no longer maintained**; use LDOT + Castor as source of truth.

Example Castor IDs discussed for unarchive (withdrawal only, no deletion request): 263243, 321255, 336619, 506421, 702794 — confirm current status with study lead before changing records.

**Permissions:** Castor unarchive may require elevated rights (study lead / PI); request access if needed.

---

## Backup copies

For **CMC** and handover continuity:

| Item | Location |
| ---- | -------- |
| **Official PDF** | [SharePoint — NMCB Withdrawal SOP v3](https://amsterdamumc.sharepoint.com/sites/CoreTeam/Shared%20Documents/Participants%20and%20Visits/SOP/NMCB%20Withdrawal%20SOP%20v3.pdf?csf=1&web=1&e=Dh5lBx) |
| **Recommended mirror** | Research Drive — Core Team / Participants and Visits / `SOP/` (same tree as SharePoint) |
| **This repo** | Add `docs/files/sop-withdrawal/` when copying PDF + Excel for offline backup (not yet in git) |

---

## Historical notes

| Topic | Status |
| ----- | ------ |
| **Withdrawal list / Excel update** | Superseded by LDOT LOF reasons; separate “update withdrawal list” step removed from active SOP |
| **`Participants not contacted further.xlsx`** | Early-stage document; **no longer in use** |
| **SOP v2 → v3** | v3: LDOT before Castor; removed obsolete opening step (Sep–Nov 2025, Teun Rijswijk / core team) |
| **LDOT checklist actions** | MEMIC suggested post–study-loss actions: archive Castor, update withdrawal list — list maintenance now in LDOT |

---

## Roles and contacts

| Role | Contact |
| ---- | ------- |
| SOP author / updates | Teun Rijswijk — [t.w.a.rijswijk@amsterdamumc.nl](mailto:t.w.a.rijswijk@amsterdamumc.nl) |
| Data management | Shuxin Zhang — [s.x.zhang@amsterdamumc.nl](mailto:s.x.zhang@amsterdamumc.nl); Kate Mudie |
| LDOT / LOF configuration | MEMIC — [ldot-memic@maastrichtuniversity.nl](mailto:ldot-memic@maastrichtuniversity.nl) (David Moonen) |
| RDM / GDPR | Paulo Heemskerk — [p.f.heemskerk@amsterdamumc.nl](mailto:p.f.heemskerk@amsterdamumc.nl) — see [Keep in mind (GDPR)](../index.md#keep-in-mind-gdpr-and-data-sharing) |

---

## Related

- [LDOT](../systems/ldot.md)
- [Castor EDC](../systems/castor.md)
- [Where data lives](../where-data-lives.md) — Research Drive `data management/` / withdrawal folders
- [Data management plan](data-management-plan.md) — Amsterdam UMC SOP 001 RDM
- [Recurring study routines](../workflows/recurring-routines.md) — operational cadence
- [Data flow (home)](../index.md#end-to-end-data-flow)
