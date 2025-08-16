4.11 Entertainment & Gaming Runner Cartridge
runner:
  name: "Entertainment & Gaming"
  aliases: ["entertainment","gaming","game","media"]
  risk_tier: "R2"
  confidence_target: 0.95
  refusal_policy:
    - "Refuse non-consensual content or exploitative monetization."
    - "Refuse designs lacking ratings/age gating where required."
  micro_gates:
    - {id: "EthicsCodeOK", description: "IGDA ethics, inclusion, crediting mapped", evidence: "ETHICS_CHECK.csv"}
    - {id: "RatingComplianceOK", description: "ESRB/IARC mapping completed", evidence: "RATINGS_MAP.csv"}
    - {id: "ResponsibleGamblingOK", description: "If applicable, RG standards mapped", evidence: "GAMING_USE_POLICY.md"}
  metrics:
    - {name: "ethics_violations", target: "0"}
    - {name: "rating_conflicts", target: "0"}
  standards_refs:
    - {name: "IGDA Code of Ethics", url_or_citation: "IGDA Ethics/crediting."}                          # :contentReference[oaicite:28]{index=28}
    - {name: "ESRB Ratings", url_or_citation: "Official ESRB system."}                                   # :contentReference[oaicite:29]{index=29}
    - {name: "IARC", url_or_citation: "Global rating coalition."}                                        # :contentReference[oaicite:30]{index=30}
    - {name: "NCPG Internet Responsible Gambling Standards (2023)", url_or_citation: "RG baseline."}     # :contentReference[oaicite:31]{index=31}
  artifacts_add:
    - {path: "Runners/Exotics/Cartridges/Entertainment/GAMING_USE_POLICY.md", purpose: "content/monetization guardrails"}
    - {path: "Runners/Exotics/Cartridges/Entertainment/RATINGS_MAP.csv", purpose: "ratings mapping"}
    - {path: "Runners/Exotics/Cartridges/Entertainment/ETHICS_CHECK.csv", purpose: "ethics checklist"}
  kickoff:
    prompt_template: |
      attach runner entertainment
      Initiate GCP V49 for Spark: <game/media innovation>
      Mode: <Full-Run|Auto> • Risk: R2
      Deliverables: Ethics map, ESRB/IARC mapping, RG policy, signed release

(Per your cartridge list.)
