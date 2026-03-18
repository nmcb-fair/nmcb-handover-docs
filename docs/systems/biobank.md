# Biobank data

*Lifecycle stages: [Storage](../lifecycle/storage.md) (sample metadata); [Issuing](../lifecycle/issuing.md) (sample preparation)*

The board shows work around biobank data flow and sample management.

## Related system

Sample tracking is done in [OpenSpecimen](openspecimen.md), the biobank system used for tracking samples.

## Board themes

- biobank data flow
- fecal sample data template
- biosample data template except fecal sample
- prepare input file for biobank
- clean dirty ML data
- script and protocol for biobank data flow

## Handover priorities

### 1. Data flow clarity

Document the full biobank flow from source to destination:

1. where sample metadata originates
2. how it is cleaned or transformed
3. what template is used
4. who receives the prepared file
5. how completion is confirmed

### 2. Template governance

If multiple templates exist, define:

- which template is current
- version number or date
- owner of the template
- mandatory columns
- validation rules before sending

## Operational risk

Biobank workflows are vulnerable to confusion when naming conventions, sample identifiers, or template versions are not tightly controlled.
