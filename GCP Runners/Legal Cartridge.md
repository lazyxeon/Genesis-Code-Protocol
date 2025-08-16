4.10 Legal Runner Cartridge
runner:
  name: "Legal (Advisory-Safe)"
  aliases: ["legal","law","compliance","policy-legal"]
  risk_tier: "R3"
  confidence_target: 0.975
  refusal_policy:
    - "Refuse jurisdiction-specific legal advice; require licensed review."
    - "No client-confidential data; confidentiality assured for any provided hypotheticals."
  micro_gates:
    - {id: "LegalCompetenceOK", description: "Cite primary sources; mark non-advice disclaimer", evidence: "Runners/Exotics/Cartridges/Legal/LEGAL_USE_POLICY.md"}
    - {id: "ConfidentialityProtectedOK", description: "PII/privileged data not ingested; controls in place", evidence: "08_safety_privacy/PRIVACY_DPIA.md"}
    - {id: "ConflictCheckOK", description: "Conflict ledger scanned (abstracted)", evidence: "Runners/Exotics/Cartridges/Legal/CONFLICT_LEDGER.md"}
    - {id: "ComplianceReferenceOK", description: "Model Rules/Bar guidance cited where used", evidence: "EVIDENCE_LEDGER.md"}
  metrics:
    - {name: "legal_review_required", target: "true for deliverables"}
    - {name: "data_breach_risk", target: "0 critical"}
  standards_refs:
    - {name: "ABA Model Rules (Competence/Confidentiality/Candor)", url_or_citation: "Use authoritative bar guidance."}  # (general ABA refs)
  artifacts_add:
    - {path: "Runners/Exotics/Cartridges/Legal/LEGAL_USE_POLICY.md", purpose: "non-advice policy"}
    - {path: "Runners/Exotics/Cartridges/Legal/SEVEN_CS_ASSESSMENT.md", purpose: "competence/confidentiality checks"}
    - {path: "Runners/Exotics/Cartridges/Legal/CONFLICT_LEDGER.md", purpose: "abstract conflicts"}
  kickoff:
    prompt_template: |
      attach runner legal
      Initiate GCP V49 for Spark: <compliance tooling/contract analyzer>
      Mode: <Full-Run|Auto> • Risk: R3
      Deliverables: Legal use policy, confidentiality DPIA, conflict ledger (abstract), signed release

(Structure per your cartridge.)
