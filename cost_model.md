# Cost Model

## Unit Economics
- Runner cost: $0.008/min.
- Average job time: 5 min.
- Cost per run: $0.04.

## Monthly Scenarios
| Runs/Month | Cost |
|-----------:|-----:|
| 100        | $4   |
| 1,000      | $40  |
| 10,000     | $400 |

## Optimization Plan
- **Hot path**: optimize tests to run in parallel — expected 30% time reduction, low risk.
- **Cold path**: cache dependencies — expected 20% cost reduction, low risk.

## Tuning Levers
- Reduce Python versions in matrix (risk: medium).
- Skip lint on documentation-only changes (risk: low).
