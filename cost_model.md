# Cost & Performance Model

| Scenario | Runs/Month | Cost/Run (USD) | Monthly Cost (USD) |
|---------|------------|----------------|--------------------|
| Low     | 300        | 0.01           | 3                  |
| Medium  | 3_000      | 0.01           | 30                 |
| High    | 30_000     | 0.009          | 270                |

## Optimization Plan

- **Hot path**: cache workflow run queries to cut API calls (≈15% cost drop).
- **Cold path**: batch report uploads to object storage (≈10% cost drop).

## Tuning Levers

- Adjust parallelism: ±20% cost impact.
- Enable incremental analysis: 25% runtime reduction with low risk.
