# Cost and Performance Model

## Unit Economics
- Container runtime cost: $0.05 per minute
- Average run time: 2 minutes
- **Per run cost:** $0.10

### Monthly Scenarios
| Runs/month | Cost/month |
|------------|------------|
| 100        | $10        |
| 1,000      | $100       |
| 10,000     | $1,000     |

## Hot vs Cold Path
- Hot path: reuse prepared containers and cached dependency DB to save 30% run time.
- Cold path: full initialization without cache.

## Tuning Levers
- Increase fuzz parallelism: +20% cost, -30% latency.
- Adjust Trivy DB update cadence: -5% cost, +1% risk.
