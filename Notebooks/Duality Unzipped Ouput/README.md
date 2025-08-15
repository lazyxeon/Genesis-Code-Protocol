# Synthetic QoE Suite — DUALITY (Proto)

Generates packet arrival traces with jitter spikes and micro-outages, then evaluates:
- Baseline
- DUALITY Single-Path (buffer + thin parity)
- DUALITY Dual-Path (buffer + thin parity + LTE assist)

Run:
```
make bench
```
