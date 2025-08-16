4.6 Spaceflight / Aerospace Runner
runner:
  name: "Spaceflight / Aerospace"
  aliases: ["space","aero","sat","avionics","g&c","adcs"]
  risk_tier: "R3"
  confidence_target: 0.975
  refusal_policy:
    - "Refuse concepts without launch/ops safety margins and RF/regulatory compliance."
  micro_gates:
    - {id: "TVAC-Vibe-EMC", description: "Thermal-vacuum, vibe, EMC plan/results (or justified analyses)", evidence: "06_evidence/stats/*"}
    - {id: "SEE-Resilience", description: "SEE latch-up/SEFI/SET analysis & safe-mode drills", evidence: "ADVERSARY_LEDGER.md"}
    - {id: "AIT-Flow", description: "AIT flow + flight rules defined", evidence: "11_product/ICD/*"}
    - {id: "C7.Repro", description: "Env lock & seeds", evidence: "06_evidence/replication/*"}
  metrics:
    - {name: "power_margin_EOL", target: "≥ target"}
    - {name: "unrecoverable_faults", target: "0 in flight rules sims"}
  artifacts_add: []
  kickoff:
    prompt_template: |
      attach runner space
      Initiate GCP V49 for Spark: <space system/payload>
      Mode: <Full-Run|Auto> • Risk: R3
      Deliverables: TVAC/vibe/EMC, SEE plan, AIT flow & flight rules, signed release

(From your space runner sections.)
