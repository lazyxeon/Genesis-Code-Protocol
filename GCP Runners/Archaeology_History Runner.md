4.16 Archaeology & Experimental History Runner
runner:
  name: "Archaeology & Experimental History"
  aliases: ["archaeology","experimental","megalithic","ancient","replica"]
  risk_tier: "R2"
  confidence_target: 0.95
  refusal_policy:
    - "Refuse destructive proposals; prioritize stewardship & consent."
  micro_gates:
    - {id: "Stewardship", description: "Site/people stewardship & permits", evidence: "13_docs/COMMUNITY_ENGAGEMENT_AND_PERMITS.md"}
    - {id: "Plausibility-Physics", description: "Materials/FEA & route/slope analyses", evidence: "06_evidence/stats/*"}
    - {id: "NonDestructive-Priority", description: "NDT first; reversible trials", evidence: "SAFETY_CASE.md"}
  metrics:
    - {name: "community_acceptance", target: "documented"}
  artifacts_add:
    - {path: "02_data/input_specs/CULTURE_TECH_PROFILE.yml", purpose: "context"}
    - {path: "06_evidence/stats/MATERIALS_PROP_TABLE.csv", purpose: "properties"}
    - {path: "07_ledgers/STEWARDSHIP_LEDGER.md", purpose: "stewardship"}
  kickoff:
    prompt_template: |
      attach runner archaeology
      Initiate GCP V49 for Spark: <ancient-tech reconstruction>
      Mode: <Full-Run|Auto> • Risk: R2
      Deliverables: stewardship dossier, physics/FEA, replica test SOP, signed release

(Directly mirrors your archaeology section.)
