4.5 Deep-Sea Exploration Runner
runner:
  name: "Deep-Sea Exploration"
  aliases: ["deepsea","auv","rov","hadal","subsea"]
  risk_tier: "R3"
  confidence_target: 0.975
  refusal_policy:
    - "Refuse concepts lacking legal permits or habitat protection plans."
    - "Refuse operations without pressure/safety margins and recovery plans."
  micro_gates:
    - {id: "Sea-Legal-ScopeOK", description: "Jurisdiction/EEZ/permits documented", evidence: "13_docs/COMMUNITY_ENGAGEMENT_AND_PERMITS.md"}
    - {id: "SOTA-DepthClassOK", description: "Depth-rated components credible for target class", evidence: "EVIDENCE_LEDGER.md"}
    - {id: "C7.Repro", description: "Bench sims and test tanks reproducible", evidence: "06_evidence/replication/*"}
  metrics:
    - {name: "structural_margin", target: "≥ safety factor target"}
    - {name: "mission_success_rate", target: "≥ 0.9 in trials"}
  artifacts_add: []
  kickoff:
    prompt_template: |
      attach runner deepsea
      Initiate GCP V49 for Spark: <subsea system/instrument>
      Mode: <Full-Run|Auto> • Risk: R3
      Deliverables: permits/ethics dossier, depth class evidence, recovery plan, signed release

(Aligns with your Deep-Sea micro-gates.)
