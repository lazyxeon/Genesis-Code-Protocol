# Cost & Performance Model

| Scenario | Runs/Month | Cost/Run (USD) | Monthly Cost (USD) |
|---------|------------|----------------|--------------------|
| Low     | 100        | 0.04           | 4                  |
| Medium  | 1_000      | 0.035          | 35                 |
| High    | 10_000     | 0.03           | 300                |

## Optimization Plan

- **Hot path**: reuse scan artifacts across branches to reduce Fortify invocations (≈20% cost drop).
- **Cold path**: schedule Codacy scans nightly for infrequently changed modules (≈10% cost drop).

## Tuning Levers

- Adjust concurrency: ±25% cost impact.
- Enable incremental SAST scans: 30% runtime reduction with moderate risk.
