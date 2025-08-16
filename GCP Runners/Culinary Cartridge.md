4.9 Culinary & Food Systems Runner Cartridge
runner:
  name: "Culinary & Food Systems"
  aliases: ["culinary","food","kitchen","haccp","fsms"]
  risk_tier: "R3"
  confidence_target: 0.975
  refusal_policy:
    - "Refuse unsafe temps/practices; refuse allergen omission."
  micro_gates:
    - {id: "HACCPPlanOK", description: "CCPs identified; monitoring & corrective actions defined", evidence: "HACCP_PLAN_TEMPLATE.md"}
    - {id: "FoodCodeOK", description: "FDA Food Code alignment", evidence: "FOOD_CODE_CHECKLIST.csv"}
    - {id: "PublicHygieneOK", description: "WHO Five Keys summary posted", evidence: "WHO_5_KEYS_BRIEF.md"}
  metrics:
    - {name: "ccp_coverage", target: "100%"}
    - {name: "food_code_violations", target: "0"}
  standards_refs:
    - {name: "FDA Food Code (2022)", url_or_citation: "Food Code pdf"}                         # :contentReference[oaicite:23]{index=23}
    - {name: "Codex HACCP (CXC 1-1969) + ISO 22000:2018", url_or_citation: "HACCP/FSMS"}      # :contentReference[oaicite:24]{index=24}
    - {name: "WHO Five Keys to Safer Food", url_or_citation: "WHO guidance"}                  # :contentReference[oaicite:25]{index=25}
  artifacts_add:
    - {path: "Runners/Exotics/Cartridges/Culinary/HACCP_PLAN_TEMPLATE.md", purpose: "HACCP"}
    - {path: "Runners/Exotics/Cartridges/Culinary/FOOD_CODE_CHECKLIST.csv", purpose: "checklist"}
    - {path: "Runners/Exotics/Cartridges/Culinary/ALLERGEN_LEDGER.md", purpose: "allergen log"}
    - {path: "Runners/Exotics/Cartridges/Culinary/WHO_5_KEYS_BRIEF.md", purpose: "hygiene note"}
  kickoff:
    prompt_template: |
      attach runner culinary
      Initiate GCP V49 for Spark: <food system/recipe tool>
      Mode: <Full-Run|Auto> • Risk: R3
      Deliverables: HACCP plan, Food Code checklist, WHO 5 Keys brief, signed release

(Cartridge matches your file layout.)
