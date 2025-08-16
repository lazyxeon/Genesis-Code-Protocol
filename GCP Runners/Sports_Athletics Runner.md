4.8 Sports & Athletics Runner
runner:
  name: "Sports & Athletics"
  aliases: ["sports","athlete","coaching","sport-science"]
  risk_tier: "R3"
  confidence_target: 0.975
  refusal_policy:
    - "Refuse medical guidance; defer to licensed clinician."
    - "Refuse doping circumvention; enforce WADA rules."
  micro_gates:
    - {id: "ConcussionProtocolOK", description: "Use latest consensus return-to-play model", evidence: "EVIDENCE_LEDGER.md"}   # IOC/Amsterdam 2022 consensus
    - {id: "HydrationHeatOK", description: "Heat acclimatization & hydration plan", evidence: "Runners/Exotics/Cartridges/Sports/artifacts/SPORTS_USE_POLICY.md"}
    - {id: "AntiDopingOK", description: "WADA Prohibited List screening", evidence: "Runners/Exotics/Cartridges/Sports/artifacts/WADA_SCREEN.csv"}
    - {id: "LoadMgmtOK", description: "Acute:Chronic load checks", evidence: "Runners/Exotics/Cartridges/Sports/artifacts/LOAD_MONITOR.csv"}
  metrics:
    - {name: "medical_deferral_compliance", target: "1.0"}
    - {name: "wada_conflict_hits", target: "0"}
    - {name: "load_spike_index", target: "within threshold policy"}
  standards_refs:
    - {name: "6th Int’l Concussion in Sport Consensus (Amsterdam 2022; BJSM 2023)", url_or_citation: "Return-to-sport framework."} # :contentReference[oaicite:19]{index=19}
    - {name: "WADA 2025 Prohibited List", url_or_citation: "List in force 1 Jan 2025 + Q&A."}                                     # :contentReference[oaicite:20]{index=20}
    - {name: "ACSM/NFHS heat hydration & acclimatization", url_or_citation: "Position/consensus resources."}                      # :contentReference[oaicite:21]{index=21}
  artifacts_add:
    - {path: "Runners/Exotics/Cartridges/Sports/standards_map.md", purpose: "norms"}
    - {path: "Runners/Exotics/Cartridges/Sports/micro_gates.md", purpose: "micro-gates"}
    - {path: "Runners/Exotics/Cartridges/Sports/metrics.md", purpose: "metrics"}
    - {path: "Runners/Exotics/Cartridges/Sports/artifacts/SPORTS_USE_POLICY.md", purpose: "use limits"}
    - {path: "Runners/Exotics/Cartridges/Sports/artifacts/WADA_SCREEN.csv", purpose: "screen matrix"}
    - {path: "Runners/Exotics/Cartridges/Sports/artifacts/LOAD_MONITOR.csv", purpose: "load tracking"}
  kickoff:
    prompt_template: |
      attach runner sports
      Initiate GCP V49 for Spark: <athlete performance tool>
      Mode: <Full-Run|Auto> • Risk: R3
      Deliverables: Concussion/heat policies, WADA screen, load plan, signed release

(Your sports cartridge structure + standards.)
