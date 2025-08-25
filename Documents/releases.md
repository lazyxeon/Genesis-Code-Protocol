# Releases

We publish Git tags and GitHub Releases for major Genesis Code Protocol editions.  Tags follow semantic versioning: minor increments (e.g. `v46.5`) represent incremental improvements, while major increments (`v47`, `v48`, `v49`, `v50`) indicate significant changes such as new phases or operating modes.  The latest release, **V50**, is the flagship AI‑native edition.

## Tags

- `v50` — **Flagship AI‑Native Edition**.  Introduces Autonomous Spark Generation (Phase I‑1), unifies full/auto runs, extends the phase map through archival/export, and ships new supplemental documents (Operational Manual, Master Runners Codex, Cartridges Pack).
- `v49` — **Protocol‑First Edition**.  Adds a comprehensive gate decision card, optional runners (Code, Physical, Theory, OT, Mobility, LifeSci, AgMRV, FinTech), alias resolver and C7.Repro micro‑gate.
- `v48` — **Pre‑Execution Reasoning & Adversarial Rigor**.  Inserts pre‑execution analyses (TRIZ/ARIZ, C‑K drift), future exploration, adversarial red‑team phases and new ledgers.
- `v47.2` — **Dual‑Mode & Renumbered Flow**.  Enables full run vs auto mode and reorders the phase numbering from C‑0.5 to CE.
- `v47.1` — **Checkpoint‑Gate UX**.  Improves the gate interface with deterministic branching and explicit stop/summary options.
- `v47` — **Worth‑It Realism**.  Adds the Worth‑It sprint (Phase −1), minimal‑intervention principle and forecasting.
- `v46.5` — **Continuous Assurance Edition**.  Introduces continuous export, SPDX/SAST/DAST checks and compatibility constraints.
- `v46` — **Ironclad Field‑Test Edition**.

## Creating a Release (via GitHub CLI)

Use the GitHub CLI to tag and publish releases.  For example, to publish **V50** at the current commit:

```
# create and push an annotated tag
git tag -a v50 -m "GCP V50 — Flagship AI‑Native Edition"
git push origin v50

# create a GitHub release from the tag
gh release create v50 --title "GCP V50 — Flagship Edition" --notes "Autonomous spark generation, unified modes and extended phases.  See README and docs for details."
```

The `gh release create` command supports additional options (e.g. attaching assets); see the [GitHub CLI documentation](https://cli.github.com/manual/gh_release_create) for details.

---

## Docs Site Seed

If you enable GitHub Pages or host the docs externally, seed a minimal index page (e.g. `/docs/index.md`) that links to this folder.  For **V50** your index might look like this:

```
# Genesis Code Protocol — Docs

This site hosts versioned documentation for GCP.

## Editions
- **V50** — Flagship AI‑Native
- **V49** — Protocol‑First
- **V48** — Pre‑Execution & Adversarial
- **V47** — Worth‑It Realism
- **V46.5** — Continuous Assurance
- **V46** — Ironclad Field‑Test

See the README for quick links to supplemental docs, notebooks and CLI usage.
```
