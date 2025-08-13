# Releases

We publish Git tags and GitHub Releases for major protocol editions.

## Tags
- `v46` — Ironclad Field-Test Edition
- `v46.5` — Ironclad+ Continuous Assurance Edition
- `v47` — Worth-It Realism Edition

## Creating a release (via GitHub CLI)

```bash
# create and push an annotated tag
git tag -a v47 -m "GCP V47 — Worth-It Realism Edition"
git push origin v47

# create a GitHub release from the tag
gh release create v47 --title "GCP V47 — Worth-It Realism" --notes "See README for highlights."



> The `gh release create` flow and options are per the GitHub CLI manual. :contentReference[oaicite:12]{index=12}

---

## 9) (Optional) Docs site seed
**Path:** `/docs/index.md` (if you enable GitHub Pages later)

```md
# Genesis Code Protocol — Docs

This site hosts versioned documentation for GCP.

## Editions
- **V46** — Ironclad Field-Test
- **V46.5** — Ironclad+ Continuous Assurance
- **V47** — Worth-It Realism

Start in the README for quick links to notebooks and CLI usage.
