4.13 Education & Assessment Runner
runner:
  name: "Education & Assessment"
  aliases: ["education","assessment","lms","irt","curriculum"]
  risk_tier: "R2"
  confidence_target: 0.95
  refusal_policy:
    - "Refuse biased/opaque evaluation without fairness deltas."
  micro_gates:
    - {id: "Learning-Objectives", description: "Measurable objectives mapped to tasks", evidence: "USER_GUIDE.md"}
    - {id: "Assessment-Validity", description: "Validity/reliability plan, IRT where applicable", evidence: "EVIDENCE_LEDGER.md"}
    - {id: "Privacy-EEA", description: "Student data DPIA complete", evidence: "08_safety_privacy/PRIVACY_DPIA.md"}
  metrics:
    - {name: "fairness_delta", target: "<= 0.5%"}
  artifacts_add: []
  kickoff:
    prompt_template: |
      attach runner education
      Initiate GCP V49 for Spark: <learning tool/assessment>
      Mode: <Full-Run|Auto> • Risk: R2
      Deliverables: objectives map, validity plan, DPIA, signed release

