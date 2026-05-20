# GitHub

**Status:** Complete

*Role: version control for study code and related analysis artefacts.*

GitHub is used for version control of scripts, code, and documentation.

## Purpose

- script and code versioning
- collaboration and review
- documentation publishing (including this hand-over site)

## Current organization setup

The `nmcb-fair` GitHub organization is now the central home for NMCB repositories.

Key repositories currently in use:

- `nmcb-overview`
- `nmcb-codebook`
- `nmcb-castor` (archived)
- `castor-eligibility`
- `acs-data-clean`
- `patient-resume`
- `sample-request`
- `data-request`
- `nmcb-handover-docs`
- `.github` (organization profile README)

Most repositories are private; selected repositories are public when needed for profile/docs visibility.

## What was completed in this migration period

### 1) Organization profile and explanation page

- Updated the organization profile repository: `nmcb-fair/.github`
- Rewrote `profile/README.md` so the org page clearly explains:
  - `nmcb-fair` is the umbrella community
  - repositories represent project-specific workstreams
- Set `.github` repository visibility to public so the org profile README is displayed

### 2) Repository consolidation

- Migrated and pushed `nmcb-codebook` updates, including `omop` content
- Migrated repository ownership/path for hand-over docs:
  - from `sxzhang1201/nmcb-handover-docs`
  - to `nmcb-fair/nmcb-handover-docs`
- Kept old source remote as `old-origin` locally for traceability

### 3) Archive decision

- `nmcb-castor` is private and archived
- `castor-eligibility` remains active (decision deferred)

### 4) Documentation cleanup

- Community docs were simplified to governance + inventory model
- migration-plan-specific artifacts were removed from local workspace docs
- repository inventory was updated with current project directories and status notes

### 5) Handover docs site deployment

- Enabled GitHub Actions Pages deploy for `nmcb-handover-docs`
- Resolved deployment blocker (private repo + Pages plan limitation) by switching repo to public
- Successfully deployed site:
  - https://nmcb-fair.github.io/nmcb-handover-docs/

## Operational notes for future maintainers

### Local workspace model

- `PycharmProjects/nmcb-fair` acts as a local umbrella folder containing multiple independent git repositories.
- The umbrella folder itself is not a git repository.
- For day-to-day development, open and work inside the specific project repository folder (for example `sample-request`), not the umbrella root.

### Commit and push workflow

For each project repo:

1. work inside that repo directory
2. run `git status` before changes
3. commit in that repo only
4. push to that repo's `origin`

This prevents accidental cross-repo edits and keeps history clean.

### Pages deployment troubleshooting

If `deploy-pages` fails with `404 Not Found` during deployment creation:

- check whether GitHub Pages is enabled for the repo
- verify repo visibility/plan supports Pages for that repository
- confirm workflow permissions include:
  - `pages: write`
  - `id-token: write`
- ensure Pages build type is configured for workflow deployment

## Handover checklist (GitHub)

- [ ] confirm repo inventory is up to date
- [ ] confirm repository visibility and archive status are intentional
- [ ] confirm maintainers/team permissions per repo
- [ ] confirm branch protections on active repos
- [ ] confirm Actions and Pages deployment status on documentation repos
- [ ] confirm organization profile README reflects current structure

## Related system

- [Research Drive](research-drive.md)
