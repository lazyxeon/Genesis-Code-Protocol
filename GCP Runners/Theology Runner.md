4.17 Religion & Theology Runner (with “Wisdom-Voice”)
runner:
  name: "Religion & Theology (Scholarly Synthesis)"
  aliases: ["religion","theology","comparative","textual-criticism"]
  risk_tier: "R2"
  confidence_target: 0.95
  refusal_policy:
    - "No proselytizing or demeaning; comparative, respectful synthesis only."
    - "No claims beyond sources; mark conjecture; avoid personal PII."
  micro_gates:
    - {id: "Source-Set", description: "Multi-tradition canonical set defined (e.g., KJV vs DSS; Qur’an Uthmanic; Vedas critical ed.)", evidence: "EVIDENCE_LEDGER.md"}
    - {id: "Textual-Criticism", description: "Variant analysis & dating with citations", evidence: "EVIDENCE_LEDGER.md"}
    - {id: "Tradition-Balance", description: "Balanced representation; no single school dominates", evidence: "ASSUMPTION_LEDGER.md"}
    - {id: "Wisdom-Voice", description: "Patterned, anonymized aggregation from vetted public forums; bias checks", evidence: "07_ledgers/ADVERSARY_LEDGER.md"}
  metrics:
    - {name: "source_diversity_index", target: "≥ threshold across traditions"}
    - {name: "bias_alerts", target: "0 critical"}
  standards_refs:
    - {name: "Leon Levy DSS Digital Library", url_or_citation: "Primary DSS images/transcriptions."}         # :contentReference[oaicite:37]{index=37}
    - {name: "KJV (1611) historical context", url_or_citation: "History of KJV translation."}               # :contentReference[oaicite:38]{index=38}
    - {name: "Uthmanic codex tradition", url_or_citation: "Scholarly overview."}                            # :contentReference[oaicite:39]{index=39}
    - {name: "Rigveda critical edition", url_or_citation: "Academic context."}                              # :contentReference[oaicite:40]{index=40}
  artifacts_add:
    - {path: "13_docs/SOURCE_CANON_MAP.md", purpose: "canon & editions list"}
    - {path: "06_evidence/stats/TEXTUAL_VARIANT_TABLE.csv", purpose: "variant grid"}
    - {path: "08_safety_privacy/WISDOM_VOICE_METHOD.md", purpose: "forum sampling, de-biasing, privacy"}
  kickoff:
    prompt_template: |
      attach runner religion
      Initiate GCP V49 for Spark: <theological synthesis or tool>
      Mode: <Full-Run|Auto> • Risk: R2
      Deliverables: canon map, textual variant table, balance checks, wisdom-voice analysis, signed release
