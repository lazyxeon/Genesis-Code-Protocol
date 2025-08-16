4.7 Disaster Relief & Humanitarian Ops Runner Cartridge
runner:
  name: "Disaster Relief & Humanitarian"
  aliases: ["disaster","humanitarian","emergency","ics","nims","sphere"]
  risk_tier: "R3"
  confidence_target: 0.975
  refusal_policy:
    - "Refuse bypass of ICS/NIMS; refuse PII data sharing without AAP/DPIA."
    - "Refuse plans that violate Sphere minimum standards."
  micro_gates:
    - {id: "ICS-Structure", description: "Incident Command System structure defined", evidence: "Runners/Exotics/Cartridges/Disaster/artifacts/ICS_STRUCTURE.md"}
    - {id: "Sphere-Matrix", description: "Response mapped to Sphere minimums", evidence: "Runners/Exotics/Cartridges/Disaster/artifacts/SPHERE_MATRIX.csv"}
    - {id: "Data-Responsibility", description: "Data responsibility assessment (IASC/OCHA) complete", evidence: "Runners/Exotics/Cartridges/Disaster/artifacts/DATA_RESP_ASSESSMENT.md"}
    - {id: "TTX", description: "Tabletop exercise pass & after-action items closed", evidence: "Runners/Exotics/Cartridges/Disaster/artifacts/ICS_TTX.md"}
  metrics:
    - {name: "lives_livelihoods_at_risk", target: "document reduction logic; no harm introduced"}
    - {name: "aap_compliance", target: "100%"}
  standards_refs:
    - {name: "Sphere Handbook", url_or_citation: "Sphere minimum standards in humanitarian response."}  # :contentReference[oaicite:15]{index=15}
    - {name: "FEMA ICS/NIMS", url_or_citation: "IS-700 NIMS; IS-200 ICS initial response."}             # :contentReference[oaicite:16]{index=16}
    - {name: "IASC/OCHA Data Responsibility", url_or_citation: "Operational Guidance (2021) / OCHA Guidelines (2021)."} # :contentReference[oaicite:17]{index=17}
  artifacts_add:
    - {path: "Runners/Exotics/Cartridges/Disaster/standards_map.md", purpose: "normative mapping"}
    - {path: "Runners/Exotics/Cartridges/Disaster/micro_gates.md", purpose: "micro-gate detail"}
    - {path: "Runners/Exotics/Cartridges/Disaster/metrics.md", purpose: "metrics table"}
    - {path: "Runners/Exotics/Cartridges/Disaster/artifacts/ICS_STRUCTURE.md", purpose: "ICS chart"}
    - {path: "Runners/Exotics/Cartridges/Disaster/artifacts/SPHERE_MATRIX.csv", purpose: "Sphere coverage"}
    - {path: "Runners/Exotics/Cartridges/Disaster/artifacts/DATA_RESP_ASSESSMENT.md", purpose: "AAP/data checks"}
    - {path: "Runners/Exotics/Cartridges/Disaster/artifacts/ICS_TTX.md", purpose: "TTX/AAR"}
  kickoff:
    prompt_template: |
      attach runner disaster
      Initiate GCP V49 for Spark: <response tool/plan>
      Mode: <Full-Run|Auto> • Risk: R3
      Deliverables: ICS/NIMS structure, Sphere mapping, Data Responsibility note, TTX + AAR, signed release

(Artifacts and refusal note align to your Exotics cartridge.)
