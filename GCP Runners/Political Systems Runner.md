4.18 Political Systems Innovation (Governance-Safe) Runner
runner:
  name: "Political Systems Innovation (Governance-Safe)"
  aliases: ["politics","governance","electoral-systems","public-choice"]
  risk_tier: "R3"
  confidence_target: 0.975
  refusal_policy:
    - "Refuse partisan persuasion, campaign strategy, demographic targeting."
    - "Limit to institutional design, process fairness, and evidence evaluation."
  micro_gates:
    - {id: "Social-Choice-Disclosure", description: "Limits per Arrow/Gibbard-Satterthwaite declared", evidence: "APPENDIX_HUMAN_STUDY.md"}  # Arrow/G-S limits
    - {id: "Deliberative-Design", description: "Citizen assembly/deliberation plan", evidence: "OPERATIONAL_README.md"}                     # CDD/OECD
    - {id: "Impact-Equity", description: "Distributional/fairness deltas and constraints", evidence: "FAIRNESS_LEDGER.md"}
  metrics:
    - {name: "manipulation_risk_score", target: "≤ low"}
    - {name: "brier_score", target: "<= 0.15"}
  standards_refs:
    - {name: "Arrow’s Impossibility Theorem (SEP)", url_or_citation: "normative limits."}                 # :contentReference[oaicite:41]{index=41}
    - {name: "Gibbard-Satterthwaite (SEP)", url_or_citation: "limits on strategy-proofness."}             # :contentReference[oaicite:42]{index=42}
    - {name: "Deliberative Polling (CDD) & OECD principles", url_or_citation: "process design."}          # :contentReference[oaicite:43]{index=43}
  artifacts_add:
    - {path: "13_docs/NEUTRALITY_AND_CONFLICTS.md", purpose: "bias & conflicts policy"}
  kickoff:
    prompt_template: |
      attach runner governance
      Initiate GCP V49 for Spark: <governance system innovation>
      Mode: <Full-Run|Auto> • Risk: R3
      Deliverables: social-choice disclosure, deliberation plan, equity analysis, signed release


4.19 Cybersecurity & Secure Systems Runner
runner:
  name: "Cybersecurity & Secure Systems"
  aliases: ["security","cyber","infosec","appsec","cloudsec"]
  risk_tier: "R3"
  confidence_target: 0.975
  refusal_policy:
    - "Refuse offensive tooling or exploitation instructions."
  micro_gates:
    - {id: "ThreatModel", description: "STRIDE/LINDDUN completed & mitigations", evidence: "RISK_SAFETY_LEDGER.md"}
    - {id: "SAST-DAST-Secrets", description: "Scans green; exceptions dual-signed", evidence: "09_security_provenance/ATTESTATIONS/*"}
    - {id: "SBOM-Signing", description: "SBOM + provenance + signatures present", evidence: "09_security_provenance/*"}
  metrics:
    - {name: "critical_findings", target: "0 open"}
  artifacts_add: []
  kickoff:
    prompt_template: |
      attach runner security
      Initiate GCP V49 for Spark: <secure system/tool>
      Mode: <Full-Run|Auto> • Risk: R3
      Deliverables: threat model, scans, SBOM/attestations/signatures, signed release
