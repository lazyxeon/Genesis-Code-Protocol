4.14 Policy Design & Public Programs Runner
runner:
  name: "Policy Design & Public Programs"
  aliases: ["policy","program","governance","public-sector"]
  risk_tier: "R3"
  confidence_target: 0.975
  refusal_policy:
    - "Refuse partisan persuasion; only institutional design & evidence evaluation."
  micro_gates:
    - {id: "Causal-Validity", description: "Counterfactual logic + confounders addressed", evidence: "EVIDENCE_LEDGER.md"}
    - {id: "Deliberation-Plan", description: "Citizen assembly / deliberative process plan", evidence: "OPERATIONAL_README.md"}   # CDD/OECD
    - {id: "Equity-Impact", description: "Distributional effects analyzed", evidence: "FAIRNESS_LEDGER.md"}
  metrics:
    - {name: "brier_score", target: "<= 0.15"}
    - {name: "replication_ok", target: "true"}
  standards_refs:
    - {name: "Deliberative Polling (Stanford CDD)", url_or_citation: "official CDD resources"}   # :contentReference[oaicite:34]{index=34}
    - {name: "OECD Deliberative Principles", url_or_citation: "OECD guidance on public deliberation"} # :contentReference[oaicite:35]{index=35}
  kickoff:
    prompt_template: |
      attach runner policy
      Initiate GCP V49 for Spark: <governance system or public program>
      Mode: <Full-Run|Auto> • Risk: R3
      Deliverables: causal/equity analysis, deliberation plan, signed release
