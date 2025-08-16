4.15 Infrastructure & Civil Runner
runner:
  name: "Infrastructure & Civil"
  aliases: ["infrastructure","civil","bridge","building","highway","water","levee","transit","smart-city"]
  risk_tier: "R3"
  confidence_target: 0.975
  refusal_policy:
    - "Refuse designs lacking code compliance or safety factors."
  micro_gates:
    - {id: "Code-Compliance", description: "Applicable codes mapped & satisfied", evidence: "COMPLIANCE_LEDGER.md"}
    - {id: "Structural-Safety", description: "Load cases & margins justified", evidence: "EVIDENCE_LEDGER.md"}
  metrics:
    - {name: "safety_margin_min", target: "≥ code"}
  artifacts_add: []
  kickoff:
    prompt_template: |
      attach runner infrastructure
      Initiate GCP V49 for Spark: <civil infrastructure>
      Mode: <Full-Run|Auto> • Risk: R3
      Deliverables: code map, load cases, safety margins, signed release
