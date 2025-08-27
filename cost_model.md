<<<<<< codex/analyze-failing-github-workflows
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
=======
<<<<<< codex/develop-fuzzing-and-vulnerability-scanning-workflow
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
=======
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
>>>>>> main
>>>>>> main
