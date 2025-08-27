# Cost Model

| load | runs/month | cost/run (USD) | cost/month (USD) |
| --- | --- | --- | --- |
| low | 100 | 0.50 | 50 |
| medium | 1000 | 0.40 | 400 |
| high | 5000 | 0.35 | 1750 |

Hot path is build+push; cold path is ingest. Caching dependencies reduces build time by ~20% with minimal risk. Parallelizing tests could cut latency by 30% but increases infra cost ~10%.
