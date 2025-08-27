# Cost & Performance Model

| Scenario | Runs/Month | Cost/Run (USD) | Monthly Cost (USD) |
|---------|------------|----------------|--------------------|
| Low     | 100        | 0.50           | 50                 |
| Medium  | 1000       | 0.45           | 450                |
| High    | 5000       | 0.40           | 2000               |

## Optimization Plan
- **Hot path**: cache scorecard results to reduce API calls (est. 20% cost drop).
- **Cold path**: batch remediation PR creation (est. 10% cost drop).

## Tuning Levers
- Adjust concurrency: +-15% cost impact.
- Enable delta scanning: 25% runtime reduction with moderate risk.
