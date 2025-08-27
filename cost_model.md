# Cost Model

## Unit Economics
| Scenario | Runs/Month | Cost/Run (USD) | Monthly Cost (USD) |
|----------|-----------:|---------------:|-------------------:|
| Low      | 100        | 0.10           | 10                 |
| Medium   | 1000       | 0.08           | 80                 |
| High     | 5000       | 0.06           | 300                |

## Optimization Plan
- **Hot Path**: cache manifest parsing (expected 5% latency reduction, low risk)
- **Cold Path**: batch log downloads (expected 20% cost reduction, medium risk)

## Tuning Levers
- Adjust container CPU limits (-10% cost, low risk)
- Enable result caching (-15% cost, medium risk)
