# Cost Model

| Load Scenario | Runs/Month | Cost/Run (USD) | Monthly Cost (USD) |
|---------------|------------|----------------|--------------------|
| Low           | 100        | 0.01           | 1.00               |
| Medium        | 500        | 0.01           | 5.00               |
| High          | 1000       | 0.01           | 10.00              |

Hot path optimization: cache token lookup (~5% latency reduction).
Cold path: avoid unnecessary API calls.

Tuning levers: reduce retention days (low risk, -10% cost), adjust canary percentage (medium risk, -5% cost).
