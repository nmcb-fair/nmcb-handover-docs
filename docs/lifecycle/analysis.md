# Data analysis

This stage covers analytical work performed on NMCB data after it has been issued: statistical analysis, modelling, and exploratory work.

## What belongs in analysis

| Activity | Purpose |
|----------|---------|
| Statistical analysis | Hypothesis testing, descriptive statistics |
| Modelling | Regression, survival analysis, machine learning |
| Exploratory analysis | Data exploration, visualisation |
| Summary counts | Numbers for reports and publications |

## Relationship to the pipeline

Analysis typically uses data that has passed through:

- [Modelling](modelling.md) — Structured, analysis-ready datasets
- [Issuing](issuing.md) — Extracts prepared for specific projects

Analysis outputs may feed into [Publication](publication.md).

## Hand-over considerations

- Document where analysis code lives (scripts, notebooks, repositories).
- Note dependencies: which datasets, which scripts, which software versions.
- For recurring analyses (e.g. eligibility counts, summary tables), document the workflow so it can be reproduced.

## Scripts

See [Scripts and QC](../systems/scripts-and-qc.md) for scripts used to get numbers and summary counts.
