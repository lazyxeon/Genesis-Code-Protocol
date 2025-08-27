# Cost and Performance Model

| Scenario | Runs/Month | Cost per Run (USD) | Monthly Cost (USD) |
|----------|------------|--------------------|--------------------|
| Low      | 200        | 0.20               | 40                 |
| Medium   | 1000       | 0.18               | 180                |
| High     | 5000       | 0.15               | 750                |

Hot path optimization focuses on reducing container startup time using pre-built images.
Cold path optimization caches Python dependencies to cut setup time by ~30%.

Tuning levers:
- Parallelism: increasing runners raises throughput (~20% gain) but increases cost.
- Test sharding: reduces latency by ~15% with minimal risk.
- Dependency cache TTL: longer TTL lowers cold-start cost (~10%) but risks stale packages.
