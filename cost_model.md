# Cost & Performance Model

| Scenario | Runs/Month | Cost/Run (USD) | Monthly Cost (USD) |
|---------|------------|----------------|--------------------|
| Low     | 100        | 0.05           | 5 |
| Medium  | 1_000      | 0.045          | 45 |
| High    | 10_000     | 0.04           | 400 |

## Optimization Plan

- **Hot path**: cache dependency data and markdown lint results to cut runtime ≈20%.
- **Cold path**: batch changelog and TOC updates nightly to reduce triggers ≈15%.

## Tuning Levers

- Adjust concurrency: ±25% cost impact.
- Toggle SBOM generation: 10% runtime trade-off with security risk.
