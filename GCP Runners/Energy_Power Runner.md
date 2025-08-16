4.20 Energy & Power Systems Runner
runner:
  name: "Energy & Power Systems"
  aliases: ["energy","grid","storage","power","renewables"]
  risk_tier: "R2"
  confidence_target: 0.95
  refusal_policy:
    - "Refuse unsafe interconnect proposals; grid safety first."
  micro_gates:
    - {id: "Safety-Interconnect", description: "Protection/relay/inrush analyses", evidence: "EVIDENCE_LEDGER.md"}
    - {id: "Reliability", description: "N-1 and tail-risk checks", evidence: "BENCHMARK_LEDGER.md"}
  metrics:
    - {name: "saidi_saifi_delta", target: "non-negative"}
  artifacts_add: []
  kickoff:
    prompt_template: |
      attach runner energy
      Initiate GCP V49 for Spark: <power/grid/storage>
      Mode: <Full-Run|Auto> • Risk: R2
      Deliverables: interconnect safety, reliability analysis, signed release
