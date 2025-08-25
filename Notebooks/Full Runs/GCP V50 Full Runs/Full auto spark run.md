You said:
Cartridges_Pack_V50__WITH_INIT_DECL (1).md
File
Master_Runners_Codex_V50__WITH_INIT_HOOK (1).md
File
GCP V50.docx
Document
Init GCP — use attached core docs (Master_Runners_Codex_V50, Cartridges_Pack_V50, Refinement PDF if present). Read attachments, assemble run_context, then render **INIT GATE — v50** and strict **INIT_CONTRACT (JSON)**. STOP after the gate; do not execute steps until I reply with **Accept gate**, **Revise: {...}**, or **Select Spark: #**.
Thought for 1m 12s
ChatGPT said:
Acknowledged. I’ve read the attached Codex + Cartridges Pack (+ your V50 doc) and assembled the run_context per the INIT_HOOK TRIGGER/ON_ATTACH rules (read, assemble run_context; early sequence; infer fields with defaults; then render the gate) . Cartridge defaults and domain mapping hints were applied from the Cartridges Pack (DEFAULT_PACKS; DOMAIN_MAP_HINTS; keep ≤7) . Operation mode follows the V50 bootstrap conventions (auto/full/manual; autonomous vs spark_provided) .
INIT GATE — v50
Spark, Mode, Risk
Spark: missing → proposing three candidate sparks (choose #):


Issue First Responder — an autonomous triage bot for OSS repos that labels, requests repro steps, and assigns owners; target: time_to_first_triage ↓40%, revert_rate ≤3%.


PR Mentor — inline code-review suggester that generates tests and perf notes; target: PR_cycle_time ↓25%, revert_rate ≤3%.


Dependency Steward — batches low-risk updates + auto-SBOM/ML-BOM + provenance; target: update lead time ↓50%, revert_rate ≤3%.


Mode: auto (default)


Risk: r2 (default)


Cartridges
Selected (≤7): Core, Research, Code, Security, Governance, Delivery (defaults + code/dev/OSS map adds)


Budget Tier/Cap; Max Tokens
Tier S, max_cost_usd: 3, max_tokens: 450000


Orchestration
cost_guard: on, telemetry: std


Privacy
pii: forbid, data_rights_ack: true


Repos
[]


Languages
Python, TypeScript (defaults)


Acceptance Metrics
time_to_first_triage ↓, PR_cycle_time ↓, revert_rate ≤3%, $ per run ≤ budget


INIT_CONTRACT (JSON)
{
  "spark": "",
  "mode": "auto",
  "risk": "r2",
  "cartridges": ["Core","Research","Code","Security","Governance","Delivery"],
  "budget": {"tier":"S","max_cost_usd":3,"max_tokens":450000},
  "orchestration": {"cost_guard":"on","telemetry":"std"},
  "privacy": {"pii":"forbid","data_rights_ack": true},
  "repos": [],
  "languages": ["Python","TypeScript"],
  "acceptance_metrics": ["time_to_first_triage↓","PR_cycle_time↓","revert_rate≤3%","$ per run≤budget"],
  "gate_status": "pending_user_approval"
}

(Contract shape per INIT_HOOK)
STOP: Awaiting one of: Accept gate, Revise: {...}, or Select Spark: # .
Sources
You said:
Spark 2. proceed
ChatGPT said:
Thought for 1m 17s
Locked in: Spark #2 — PR Mentor. Executing per V50 run rules. Below is a minimal-but-ready plan + drop-in scaffolding to get value on Day 1 without committing you to paid APIs. LLM suggestions are optional and budget-guarded; static analyzers + policy bots do the bulk.
Phase 1 — Charter → Architecture → Scaffold
Objectives (measurable): cut PR cycle time ~25%; nudge test coverage up on changed code; keep revert rate ≤3%; stay ≤ your budget guard by default (LLM step off unless env key provided). Benchmarks come from repo insights + workflow telemetry (we’ll add later).
Approach (no-API baseline, API-optional):
Static analyzers to inline: Ruff (py), ESLint (js/ts), Bandit (py-sec), Semgrep (lightweight SAST). These post annotations / PR review comments via Actions. Astral DocsJestSemgrep+1


Policy bot: Danger JS to enforce PR hygiene & nudge tests/perf notes; emits a single summary comment. Danger Systems+1


Comment/annotation plumbing: GitHub Actions on pull_request with pull-requests: write perms, posting reviews/comments through native annotations, Reviewdog, or the REST endpoints (for custom scripts). GitHub Docs+1


What “good” looks like: encode review focus from Google’s eng-practices (design, tests, complexity, naming, docs) into Danger rules/messages. Google GitHub+1



Files to add (scaffold v0)
1) .github/workflows/pr-mentor.yml
A single job that (a) runs linters, (b) posts inline findings, (c) leaves a Danger summary comment, (d) adds a “missing tests” nudge.
name: pr-mentor
on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

permissions:
  contents: read
  pull-requests: write

jobs:
  pr-mentor:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # ---- Python toolchain
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - name: Install Python tools
        run: pip install -U ruff bandit semgrep

      # Ruff: fast py lint with GitHub-friendly output annotations
      - name: Ruff (lint)
        if: ${{ hashFiles('**/*.py') != '' }}
        run: ruff check --output-format=github .

      # Bandit: Python security checks → Reviewdog PR comments
      - uses: reviewdog/action-setup@v1
      - name: Bandit → reviewdog
        if: ${{ hashFiles('**/*.py') != '' }}
        run: bandit -q -r . -f txt | reviewdog -efm="%f:%l: %m" -name=bandit -reporter=github-pr-review -filter-mode=diff_context -fail-on-error=false

      # ---- Node toolchain
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - name: Install JS/TS tools
        if: ${{ hashFiles('**/*.{js,jsx,ts,tsx}') != '' }}
        run: npm i -D eslint

      # ESLint → Reviewdog PR comments (checkstyle is supported)
      - name: ESLint → reviewdog
        if: ${{ hashFiles('**/*.{js,jsx,ts,tsx}') != '' }}
        run: npx eslint . -f checkstyle | reviewdog -f=checkstyle -name=eslint -reporter=github-pr-review -filter-mode=diff_context -fail-on-error=false

      # ---- Semgrep (SAST lite). Native CI invocation.
      - name: Semgrep CI
        run: semgrep ci --error --disable-version-check || true

      # ---- Danger summary (hygiene/tests/perf)
      - name: Danger
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          npm i -D danger @actions/core
          npx danger ci

      # ---- Test nudge (if no tests changed)
      - name: Missing tests nudge
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python .github/scripts/test_guard.py

Why this works:
pull_request event + pull-requests: write lets the job annotate diffs and leave review-style comments where supported. GitHub Docs


Reviewdog converts linter output (e.g. ESLint checkstyle, Bandit text with errorformat) into inline PR comments. GitHub


Semgrep’s native CI path is current best practice (their old wrapper action is deprecated). SemgrepGitHub


Ruff’s --output-format=github yields GitHub annotations out-of-the-box for fast feedback. Sonar Community



2) Dangerfile.ts
Encodes Google-style review prompts into a human-readable summary (no paid LLM needed).
// Dangerfile.ts
import { danger, warn, markdown, fail } from "danger";

const modified = danger.github.pr.changed_files;
const pr = danger.github.pr;

const desc = (pr.body || "").toLowerCase();
const requiresSections = ["summary", "risk", "testing"];
const missing = requiresSections.filter(s => !desc.includes(`${s}:`));
if (missing.length) {
  warn(`PR description is missing sections: ${missing.map(s => `\`${s}:\``).join(", ")}`);
}

// Nudge for tests: if code changed but no *_test files touched.
const files = danger.git.modified_files.concat(danger.git.created_files);
const codeTouched = files.some(f => /\.(py|ts|tsx|js|jsx)$/.test(f));
const testsTouched = files.some(f => /(test|spec)\.(py|ts|tsx|js|jsx)$/.test(f) || /tests?\//.test(f));
if (codeTouched && !testsTouched) {
  warn("No tests changed. Consider adding/adjusting tests for modified code.");
}

// Big file guard
const bigAdded = files.filter(f => danger.git.linesOfCodeForFile(f)?.added > 800);
if (bigAdded.length) {
  warn(`Large additions detected: ${bigAdded.join(", ")}. Consider splitting or adding rationale.`);
}

markdown(`### PR Mentor Summary
- Review focus: design, functionality, complexity, tests, naming, docs.
- If you add code without tests, please justify under **Testing** in the PR body.
`);

Backed by the Danger JS DSL and Google’s public review guidance. Danger SystemsGoogle GitHub

3) .github/scripts/test_guard.py
Tiny helper to leave a nudge comment when code changes lack tests.
# .github/scripts/test_guard.py
import json, os, re, requests, sys, pathlib

event_path = os.getenv("GITHUB_EVENT_PATH")
token = os.getenv("GITHUB_TOKEN")
if not (event_path and token): sys.exit(0)

ev = json.load(open(event_path))
repo = ev["repository"]["full_name"]
pr_number = ev["pull_request"]["number"]
files_url = ev["pull_request"]["url"] + "/files"

headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
files = []
page = 1
while True:
  r = requests.get(files_url, headers=headers, params={"per_page": 100, "page": page})
  chunk = r.json()
  if not chunk or r.status_code != 200: break
  files += chunk
  if len(chunk) < 100: break
  page += 1

code = any(re.search(r'\.(py|js|jsx|ts|tsx)$', f["filename"]) for f in files)
tests = any(re.search(r'(tests?/|(\btest|\bspec)\.(py|js|jsx|ts|tsx)$)', f["filename"]) for f in files)

if code and not tests:
  body = {"body": "🧪 Heads-up: code changed but no tests were modified. Consider adding/adjusting tests or note rationale in PR body."}
  requests.post(f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments",
                headers=headers, json=body)

Uses the GitHub REST API “issue comment” on the PR thread; for line/inline you can use review comments endpoints later. GitHub Docs

4) PULL_REQUEST_TEMPLATE.md
## Summary:
## Risk:
## Testing:
- [ ] New/updated unit tests included
- [ ] Manual steps documented (if applicable)
## Performance notes:
- Hot paths touched? If yes, rationale/benchmarks here.


5) Optional: quickstarts for tests (links)
Python: pytest quickstart for basic scaffolds. pytest


JS/TS: Jest getting started. Jest



Run Context (updated)
{
  "spark": "PR Mentor — inline code-review suggestions that also generate test/perf nudges",
  "mode": "auto",
  "risk": "r2",
  "cartridges": ["Core","Research","Code","Security","Governance","Delivery"],
  "budget": {"tier":"S","max_cost_usd":3,"max_tokens":450000},
  "orchestration": {"cost_guard":"on","telemetry":"std"},
  "privacy": {"pii":"forbid","data_rights_ack": true},
  "repos": [],
  "languages": ["Python","TypeScript"],
  "acceptance_metrics": [
    "PR_cycle_time↓ ~25%",
    "revert_rate≤3%",
    "time_to_first_review↓",
    "$ per run≤budget"
  ]
}


Your move
If you want me to wire in an optional LLM reviewer (budget-guarded; only runs when LLM_API_KEY is present) that summarizes risky diffs and suggests tests, say “Add LLM step” and I’ll attach a drop-in Action step that calls a model and posts a single PR review (kept under your $3 cap). Otherwise, I can proceed to Phase 2 (repo-ready pack): I’ll emit the files above exactly, tuned for your repos.
You said:
add LLM step please
ChatGPT said:
Thought for 1m 19s
got it — here’s a drop-in LLM Reviewer step that runs only when you add an API key. it summarizes risky diffs and proposes tests, then posts a single PR review (not just an issue comment) via the GitHub REST API. GitHub Docs

1) Update your workflow (.github/workflows/pr-mentor.yml)
Add requests to your Python tools line and append the LLM Reviewer step below. It will auto-skip when LLM_API_KEY or LLM_PROVIDER is missing.
# ... keep everything above as-is ...

jobs:
  pr-mentor:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # ---- Python toolchain
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - name: Install Python tools
        run: pip install -U ruff bandit semgrep requests

      # (ruff/bandit/semgrep/reviewdog/eslint/danger steps unchanged)

      # ---- LLM Reviewer (summary) — optional, budget-guarded
      - name: LLM Reviewer (summary)
        if: ${{ vars.LLM_PROVIDER != '' && secrets.LLM_API_KEY != '' }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          LLM_PROVIDER: ${{ vars.LLM_PROVIDER }}     # openai | openrouter | deepseek
          LLM_API_KEY: ${{ secrets.LLM_API_KEY }}
          LLM_MODEL: ${{ vars.LLM_MODEL }}           # e.g., gpt-4o-mini | openai/gpt-4o-mini | deepseek-chat
          MAX_TOKENS: "900"                          # hard guard on cost/size
        run: python .github/scripts/llm_reviewer.py

Why pull-requests: write + review endpoint? Because we want a single consolidated review with event: "COMMENT" tied to the PR’s head commit. That uses GitHub’s Create a review for a pull request endpoint. GitHub Docs

2) Add the script: .github/scripts/llm_reviewer.py
This script:
Gathers changed files + patches from the PR files API (includes unified diffs). GitHub Docs


Truncates context to keep token usage under the guard.


Calls your chosen provider (OpenAI, OpenRouter, or DeepSeek) with a compact prompt. (DeepSeek’s endpoint shown in their docs; OpenRouter follows OpenAI-style chat completions; OpenAI reference linked.) DeepSeek API DocsOpenRouterOpenAI Platform


Posts a PR review with the LLM’s summary using the Reviews API. GitHub Docs


# .github/scripts/llm_reviewer.py
import json, os, re, textwrap, requests

EVENT_PATH = os.getenv("GITHUB_EVENT_PATH")
TOKEN = os.getenv("GITHUB_TOKEN")
if not (EVENT_PATH and TOKEN):
    raise SystemExit(0)

with open(EVENT_PATH, "r", encoding="utf-8") as f:
    ev = json.load(f)

repo_full = ev["repository"]["full_name"]           # owner/repo
pr_number = ev["pull_request"]["number"]
head_sha  = ev["pull_request"]["head"]["sha"]
files_url = ev["pull_request"]["url"] + "/files"    # includes 'patch' fields
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

# --- collect changed files & patches (paginate)
files, page = [], 1
while True:
    r = requests.get(files_url, headers=headers, params={"per_page": 100, "page": page})
    if r.status_code != 200: break
    chunk = r.json()
    files.extend(chunk)
    if len(chunk) < 100: break
    page += 1

def clamp(s: str, n: int) -> str:
    return s if len(s) <= n else (s[:n] + "\n...[truncated]")

MAX_PER_PATCH = 2000
diff_blocks = []
for f in files:
    name = f.get("filename","")
    patch = f.get("patch","")
    if not patch:
        continue
    diff_blocks.append(f"### {name}\n```\n{clamp(patch, MAX_PER_PATCH)}\n```")
diff_text = "\n\n".join(diff_blocks)
if not diff_text:
    diff_text = "_No textual diffs (binary or too large to render)._"

# --- compose compact prompt
user_prompt = f"""
You are **PR Mentor**. Summarize the pull request diff and propose concrete tests.

Return markdown with these sections only:
1) **Review Summary** — 3-7 bullets, crisp.
2) **Risky Changes** — bullets with file:path and reason.
3) **Suggested Tests** — unit/integration bullets with filenames or test names.
4) **Performance Notes** — only if hot paths are likely.

Scope: Base your analysis strictly on the provided diff hunks. Avoid speculation.
Diff hunks follow:

{diff_text}
"""

# --- choose provider
provider = (os.getenv("LLM_PROVIDER") or "").lower()
model    = os.getenv("LLM_MODEL") or (
    "deepseek-chat" if provider=="deepseek"
    else ("openai/gpt-4o-mini" if provider=="openrouter" else "gpt-4o-mini")
)
max_tokens = int(os.getenv("MAX_TOKENS", "900"))

if provider == "deepseek":
    # DeepSeek Chat Completions (OpenAI-compatible)
    # Docs: https://api.deepseek.com/chat/completions
    # Ref: DeepSeek API docs (OpenAI-compatible base) 
    url = "https://api.deepseek.com/chat/completions"   #   
- We create a **review** via `POST /repos/{owner}/{repo}/pulls/{pull_number}/reviews` with `event: "COMMENT"` so it shows up as a single threaded review on the PR. :contentReference[oaicite:7]{index=7}  
- Provider endpoints: **DeepSeek** chat completions (`https://api.deepseek.com/chat/completions`), **OpenRouter** OpenAI-style chat completions, **OpenAI** API reference. :contentReference[oaicite:8]{index=8}

---

# 3) Minimal configuration

- **Secrets** → add `LLM_API_KEY`.  
- **Repository variables** → add `LLM_PROVIDER` (`openai`, `openrouter`, or `deepseek`) and `LLM_MODEL` (e.g., `gpt-4o-mini`, `openai/gpt-4o-mini`, or `deepseek-chat`).  
- Token guard: tweak `MAX_TOKENS` in the step env.  
- If you want this to **hard-fail** on API error, set the workflow step to `continue-on-error: false`.

---

Want me to emit the **final, repo-ready files** (updated workflow + script) as your **Phase 2 (repo pack)** now? Or tweak defaults (provider/model/tokens) first?
::contentReference[oaicite:9]{index=9}

You said:
phase 2 please
ChatGPT said:
Thought for 1m 8s
Phase 2 — repo-ready pack is below. Copy each file to the indicated path and commit. I’ve pinned sensible defaults and added guards so nothing fails if you don’t set an LLM key. Key APIs and tools referenced are linked inline. GitHub Docs+3GitHub Docs+3GitHub Docs+3SemgrepGitHub+1

.github/workflows/pr-mentor.yml
name: pr-mentor
on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]

permissions:
  contents: read
  pull-requests: write  # needed to create PR reviews/comments

jobs:
  pr-mentor:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # -------- Python toolchain
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - name: Install Python tools
        run: pip install -U ruff bandit semgrep requests

      # Ruff: fast Python lint with native GitHub annotations
      - name: Ruff (lint)
        if: ${{ hashFiles('**/*.py') != '' }}
        run: ruff check --output-format=github .  # surfaces annotations in PR UI

      # Install reviewdog (CLI; used to convert linter output into PR review comments)
      - uses: reviewdog/action-setup@v1

      # Bandit: Python security → PR review comments via reviewdog
      - name: Bandit → reviewdog
        if: ${{ hashFiles('**/*.py') != '' }}
        run: bandit -q -r . -f txt | reviewdog -efm="%f:%l: %m" -name=bandit -reporter=github-pr-review -filter-mode=diff_context -fail-on-error=false

      # -------- Node/JS/TS toolchain
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - name: Install JS/TS tools
        if: ${{ hashFiles('**/*.{js,jsx,ts,tsx}') != '' }}
        run: |
          npm i -D eslint eslint-formatter-checkstyle typescript typescript-eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin danger ts-node @actions/core

      # ESLint → PR review comments via reviewdog (checkstyle format)
      - name: ESLint → reviewdog
        if: ${{ hashFiles('**/*.{js,jsx,ts,tsx}') != '' }}
        run: npx eslint . -f checkstyle | reviewdog -f=checkstyle -name=eslint -reporter=github-pr-review -filter-mode=diff_context -fail-on-error=false

      # Semgrep (SAST-lite). Keep non-blocking for now.
      - name: Semgrep CI
        run: semgrep ci --error --disable-version-check || true

      # Danger summary (PR hygiene/tests/perf prompts)
      - name: Danger (summary)
        if: ${{ hashFiles('.github/Dangerfile.*') != '' }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: npx danger ci

      # Nudge if code changed but no tests touched
      - name: Missing tests nudge
        env: { GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }} }
        run: python .github/scripts/test_guard.py

      # -------- Optional LLM Reviewer (single consolidated PR review)
      - name: LLM Reviewer (summary)
        if: ${{ vars.LLM_PROVIDER != '' && secrets.LLM_API_KEY != '' }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          LLM_PROVIDER: ${{ vars.LLM_PROVIDER }}     # openai | openrouter | deepseek
          LLM_API_KEY: ${{ secrets.LLM_API_KEY }}
          LLM_MODEL: ${{ vars.LLM_MODEL }}           # e.g., gpt-4o-mini | openai/gpt-4o-mini | deepseek-chat
          MAX_TOKENS: "900"
        run: python .github/scripts/llm_reviewer.py

“PR files” API provides unified diffs (patch) the LLM step consumes. GitHub Docs


We create a single PR review (event: COMMENT) tied to the head commit. GitHub Docs


If a review can’t be created, the script falls back to an issue comment on the PR thread. GitHub Docs


The workflow needs pull-requests: write and you may need to allow review creation under Actions → General → Workflow permissions. GitHub Docs+1


Semgrep’s CI entrypoint is semgrep ci. Semgrep+1


Danger JS automates PR conventions/hygiene. GitHub



.github/scripts/test_guard.py
# .github/scripts/test_guard.py
import json, os, re, requests, sys

event_path = os.getenv("GITHUB_EVENT_PATH")
token = os.getenv("GITHUB_TOKEN")
if not (event_path and token):
  sys.exit(0)

with open(event_path, "r", encoding="utf-8") as f:
  ev = json.load(f)

repo = ev["repository"]["full_name"]
pr_number = ev["pull_request"]["number"]
files_url = ev["pull_request"]["url"] + "/files"

headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}

files = []
page = 1
while True:
  r = requests.get(files_url, headers=headers, params={"per_page": 100, "page": page})
  if r.status_code != 200:
    break
  chunk = r.json()
  files += chunk
  if len(chunk) < 100:
    break
  page += 1

code = any(re.search(r'\.(py|js|jsx|ts|tsx)$', f.get("filename","")) for f in files)
tests = any(re.search(r'(tests?/|(\btest|\bspec)\.(py|js|jsx|ts|tsx)$)', f.get("filename","")) for f in files)

if code and not tests:
  body = {"body": "🧪 Heads-up: code changed but no tests were modified. Consider adding/adjusting tests or explain in PR body."}
  requests.post(f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments",
                headers=headers, json=body)

Uses PR files + issue comments REST endpoints. GitHub Docs+1

.github/scripts/llm_reviewer.py
# .github/scripts/llm_reviewer.py
import json, os, requests

EVENT_PATH = os.getenv("GITHUB_EVENT_PATH")
TOKEN = os.getenv("GITHUB_TOKEN")
if not (EVENT_PATH and TOKEN):
    raise SystemExit(0)

with open(EVENT_PATH, "r", encoding="utf-8") as f:
    ev = json.load(f)

repo_full = ev["repository"]["full_name"]
pr_number = ev["pull_request"]["number"]
head_sha  = ev["pull_request"]["head"]["sha"]
files_url = ev["pull_request"]["url"] + "/files"
headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}

# ---- collect changed files & patches (paginate)
files, page = [], 1
while True:
    r = requests.get(files_url, headers=headers, params={"per_page": 100, "page": page})
    if r.status_code != 200:
        break
    chunk = r.json()
    files.extend(chunk)
    if len(chunk) < 100:
        break
    page += 1

def clamp(text: str, limit: int = 2000) -> str:
    return text if len(text) <= limit else (text[:limit] + "\n...[truncated]")

blocks = []
for f in files:
    name = f.get("filename","")
    patch = f.get("patch","")
    if not patch:
        continue
    blocks.append(f"### {name}\n```\n{clamp(patch)}\n```")

diff_text = "\n\n".join(blocks) or "_No textual diffs (binary or too large to render)._"

user_prompt = f"""
You are **PR Mentor**. Summarize the pull request diff and propose concrete tests.

Return markdown with these sections only:
1) **Review Summary** — 3-7 bullets.
2) **Risky Changes** — bullets with file:path and reason.
3) **Suggested Tests** — unit/integration bullets with filenames or test names.
4) **Performance Notes** — only if hot paths are likely.

Scope: Base strictly on the provided diff hunks.
Diff hunks follow:

{diff_text}
"""

provider = (os.getenv("LLM_PROVIDER") or "").lower()
model    = os.getenv("LLM_MODEL") or ("deepseek-chat" if provider=="deepseek" else ("openai/gpt-4o-mini" if provider=="openrouter" else "gpt-4o-mini"))
max_tokens = int(os.getenv("MAX_TOKENS", "900"))
api_key = os.getenv("LLM_API_KEY")

if not (provider and api_key):
    raise SystemExit(0)

if provider == "deepseek":
    url = "https://api.deepseek.com/chat/completions"
elif provider == "openrouter":
    url = "https://openrouter.ai/api/v1/chat/completions"
else:
    url = "https://api.openai.com/v1/chat/completions"

payload = {
    "model": model,
    "messages": [
        {"role":"system","content":"You are a terse, high-signal code reviewer."},
        {"role":"user","content": user_prompt}
    ],
    "max_tokens": max_tokens,
    "temperature": 0.2,
}
resp = requests.post(url, headers={"Authorization": f"Bearer {api_key}", "Content-Type":"application/json"}, json=payload, timeout=120)

review_text = ""
try:
    j = resp.json()
    review_text = j["choices"][0]["message"]["content"].strip()
except Exception:
    review_text = f"LLM call failed ({resp.status_code}). Raw body:\n```\n{resp.text[:1200]}\n```"

# Post as a PR review (single consolidated thread)
review_url = f"https://api.github.com/repos/{repo_full}/pulls/{pr_number}/reviews"
review_payload = { "commit_id": head_sha, "event": "COMMENT", "body": review_text[:65000] }
gh = requests.post(review_url, headers=headers, json=review_payload, timeout=60)
if gh.status_code not in (200,201):
    # Fallback to issue comment on failure
    ic_url = f"https://api.github.com/repos/{repo_full}/issues/{pr_number}/comments"
    requests.post(ic_url, headers=headers, json={"body": review_text[:65000]}, timeout=60)

Pull-files response includes patch hunks. GitHub Docs


Creates a PR review via Reviews API; falls back to issue comment if needed. GitHub Docs+1



Dangerfile.ts
// Dangerfile.ts
import { danger, warn, markdown } from "danger";

const desc = (danger.github.pr.body || "").toLowerCase();
const requires = ["summary", "risk", "testing"];
const missing = requires.filter(s => !desc.includes(`${s}:`));
if (missing.length) {
  warn(`PR description is missing sections: ${missing.map(s => `\`${s}:\``).join(", ")}`);
}

const changed = danger.git.modified_files.concat(danger.git.created_files);
const codeTouched = changed.some(f => /\.(py|ts|tsx|js|jsx)$/.test(f));
const testsTouched = changed.some(f => /(tests?\/|(\btest|\bspec)\.(py|ts|tsx|js|jsx)$)/.test(f));

if (codeTouched && !testsTouched) {
  warn("No tests changed. Consider adding/adjusting tests for modified code.");
}

const bigAdded = changed.filter(f => (danger.git.linesOfCodeForFile(f)?.added || 0) > 800);
if (bigAdded.length) {
  warn(`Large additions detected: ${bigAdded.join(", ")}. Consider splitting or adding rationale.`);
}

markdown(`### PR Mentor Summary
- Review focus: design, functionality, complexity, tests, naming, docs.
- If you add code without tests, justify under **Testing** in the PR body.
`);

Runs with npx danger ci; Danger codifies PR rules/hygiene. GitHub+1

eslint.config.mjs (flat config for JS/TS)
// eslint.config.mjs
import js from "@eslint/js";
import tseslint from "typescript-eslint";

export default [
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    rules: {
      "no-unused-vars": ["warn", { argsIgnorePattern: "^_" }],
      "no-console": "off"
    }
  }
];

Use with npx eslint . -f checkstyle; we install eslint-formatter-checkstyle for reviewdog. ESLintnpm

.ruff.toml (optional but helpful)
line-length = 120

[lint]
select = ["E", "F", "W", "I"]  # errors, pyflakes, warnings, import sort
ignore = []

Ruff config surface per docs; ruff check --output-format=github yields GH annotations. Astral DocsGitHub

PULL_REQUEST_TEMPLATE.md
## Summary:
## Risk:
## Testing:
- [ ] New/updated unit tests included
- [ ] Manual steps documented (if applicable)

## Performance notes:
- Hot paths touched? If yes, add brief benchmarks/rationale here.


Final wiring checklist
Secrets & Variables


Secrets → LLM_API_KEY (only if you want the LLM review).


Repository Variables → LLM_PROVIDER (openai | openrouter | deepseek), LLM_MODEL (e.g., gpt-4o-mini, openai/gpt-4o-mini, or deepseek-chat).


Ensure Actions → General → Workflow permissions allow PR write/reviews if needed. GitHub Docs+1


What you’ll see on each PR


Inline lints from Ruff/Bandit/ESLint via reviewdog. GitHub+1


A Danger summary with hygiene nudges. GitHub


A tests-missing nudge if code changed but tests didn’t.


If an API key is set, a single LLM review summarizing risk & proposed tests using the PR’s diff hunks. GitHub Docs+1


If you want me to also generate a minimal commit message set and a README snippet for the PR Mentor system, say “Add docs” and I’ll append them.
You said:
add docs
ChatGPT said:
Thought for 17s
awesome — here are clean, drop-in docs + commit messages. they reference the exact APIs/tools we’re using and include links for setup & troubleshooting.

README snippet (paste anywhere in your repo README)
## PR Mentor — CI Assistant for Pull Requests

**What it does**
- Inline lint + security comments via **Ruff**, **ESLint**, **Bandit**, **Semgrep**, posted through **reviewdog**.  
- A **Danger** summary comment that enforces PR hygiene (tests, risk notes, big changes).  
- Optional **LLM Reviewer** that summarizes risky diffs and proposes concrete tests, posted as a single PR **review**.

**How it works (high level)**
- Runs on the `pull_request` event with `pull-requests: write` to create review comments.  
- The LLM step assembles unified diffs from the **PR Files** endpoint and posts one **Pull Request Review** via the Reviews API.  
- Actions permissions are least-privilege; toggle workflow permissions in repo settings if reviews aren’t posting.

**Enable the optional LLM Reviewer**
1) Add **Secret**: `LLM_API_KEY`.  
2) Add **Repository Variables**:  
   - `LLM_PROVIDER` = `openai` | `openrouter` | `deepseek`  
   - `LLM_MODEL` = e.g., `gpt-4o-mini`, `openai/gpt-4o-mini`, or `deepseek-chat`  
3) Commit the provided workflow + scripts.

**Key references**
- GitHub Reviews API (create a PR review). :contentReference[oaicite:0]{index=0}  
- PR Files API (diff `patch` field). :contentReference[oaicite:1]{index=1}  
- Actions permissions (`pull-requests: write`) + Workflow permissions settings. :contentReference[oaicite:2]{index=2}  
- Danger JS, reviewdog, Ruff, Semgrep, ESLint formatter docs. :contentReference[oaicite:3]{index=3}


docs/pr-mentor.md (new file)
# PR Mentor — Design & Setup

PR Mentor speeds up reviews with automated comments and a concise review summary.

## Features
- **Inline findings**: Ruff (Python), ESLint (JS/TS), Bandit (Python security), Semgrep (policy/SAST). Posted with reviewdog.  
- **Hygiene summary**: Danger JS enforces PR description sections and nudges for tests on code-only changes.  
- **Optional LLM Review**: One consolidated **Pull Request Review** with risks + suggested tests.

## How it works
1. Trigger: `pull_request` on open/sync/reopen/ready.  
2. Permissions: `pull-requests: write` so the job can create **reviews/comments**. Configure workflow permissions under repo **Settings → Actions → General** if needed. :contentReference[oaicite:4]{index=4}  
3. Linters:  
   - **Ruff** emits GitHub-native annotations with `--output-format=github`. :contentReference[oaicite:5]{index=5}  
   - **ESLint** outputs **checkstyle**; reviewdog converts to inline comments. (Built-in & custom formatters supported.) :contentReference[oaicite:6]{index=6}  
   - **Bandit** and **Semgrep** run in CI; `semgrep ci` is the recommended entrypoint. :contentReference[oaicite:7]{index=7}  
   - **reviewdog** posts only findings that touch the diff. :contentReference[oaicite:8]{index=8}
4. LLM Reviewer (optional):  
   - Collects unified diffs from the **PR Files** endpoint (provides `patch` hunks). :contentReference[oaicite:9]{index=9}  
   - Calls your chosen provider (OpenAI/OpenRouter/DeepSeek).  
   - Posts a single **PR review** via the Reviews API. :contentReference[oaicite:10]{index=10}

## Install
- Copy:
  - `.github/workflows/pr-mentor.yml`
  - `.github/scripts/test_guard.py`
  - `.github/scripts/llm_reviewer.py`
  - `Dangerfile.ts`, `.ruff.toml`, `eslint.config.mjs`, `PULL_REQUEST_TEMPLATE.md`
- (Optional) Add secrets/variables for the LLM step:
  - **Secret**: `LLM_API_KEY`
  - **Repo Vars**: `LLM_PROVIDER`, `LLM_MODEL` (examples in the workflow)

## Usage
Open a PR. You’ll see:
- Inline comments from linters via reviewdog. :contentReference[oaicite:11]{index=11}  
- A **Danger** summary comment with hygiene/test nudges. :contentReference[oaicite:12]{index=12}  
- If configured, a single **LLM review** summarizing risk and test ideas.

## Security & Permissions
- The workflow requests only `contents: read`, `pull-requests: write`. Keep tokens least-privilege. :contentReference[oaicite:13]{index=13}  
- For orgs that restrict review creation by Actions, enable “Allow GitHub Actions to create and approve pull requests.” :contentReference[oaicite:14]{index=14}

## References
- GitHub REST: PR **Reviews** and **PR Files**. :contentReference[oaicite:15]{index=15}  
- **Danger JS** docs. :contentReference[oaicite:16]{index=16}  
- **reviewdog** action & tool. :contentReference[oaicite:17]{index=17}  
- **Ruff** integrations. :contentReference[oaicite:18]{index=18}  
- **Semgrep** CI. :contentReference[oaicite:19]{index=19}  
- **ESLint** formatters. :contentReference[oaicite:20]{index=20}


docs/llm-reviewer.md (new file)
# LLM Reviewer — Configuration & Behavior

The LLM Reviewer posts a single PR **review** (not just an issue comment) with:
- Concise review summary (3–7 bullets)
- Risky changes (file:path + reason)
- Suggested tests (unit/integration)
- Performance notes when hot paths are detected

## Enable
- Add **Secret**: `LLM_API_KEY`
- Add **Repo Variables**:
  - `LLM_PROVIDER` = `openai` | `openrouter` | `deepseek`
  - `LLM_MODEL` = e.g., `gpt-4o-mini`, `openai/gpt-4o-mini`, `deepseek-chat`
- Optional guard: `MAX_TOKENS` (env in the workflow; default 900)

## Data flow
1. Fetch PR file list + `patch` hunks from **PR Files** endpoint (paginated). :contentReference[oaicite:21]{index=21}  
2. Build a compact prompt strictly from the hunks.  
3. Call provider API (chat completions).  
4. Create a **Pull Request Review** with `event: "COMMENT"` tied to the head commit. :contentReference[oaicite:22]{index=22}

## Cost/Privacy
- Hard token cap via `MAX_TOKENS`.  
- No code leaves GitHub unless you enable the LLM step with a key.

## Troubleshooting
- **“Resource not accessible by integration”** → Ensure `pull-requests: write` in the workflow **and** that repo **Workflow permissions** allow review creation. :contentReference[oaicite:23]{index=23}  
- **No `patch` in API response** → Very large/binary files may omit diff hunks; reviewer emits a safe fallback. See PR Files docs. :contentReference[oaicite:24]{index=24}


docs/troubleshooting.md (new file)
# Troubleshooting

### Reviews not appearing
- Check the job has `pull-requests: write` and that repo **Workflow permissions** allow creating PR reviews. :contentReference[oaicite:25]{index=25}

### reviewdog posts nothing
- reviewdog only comments on lines within the diff. If a linter error is outside the PR hunk, it’s ignored by design. :contentReference[oaicite:26]{index=26}

### Semgrep fails build
- We run `semgrep ci --error || true` to keep it non-blocking initially. See CLI docs to change severity/exit behavior. :contentReference[oaicite:27]{index=27}

### ESLint formatter confusion
- ESLint has built-in formatters; `-f checkstyle` works without extra packages. You *can* use a standalone formatter module if you prefer. :contentReference[oaicite:28]{index=28}


Suggested commit messages (copy any/all)
chore(ci): add PR Mentor workflow (Ruff, Bandit, ESLint, Semgrep, reviewdog, Danger)

chore(ci): add optional LLM Reviewer step (summary review from PR diffs)

docs(pr-mentor): add overview + setup guides with references

docs: add llm-reviewer + troubleshooting pages

chore: add PR template, Dangerfile, eslint flat config, ruff config

ci: set workflow permissions (pull-requests: write) and note repo setting for review creation

Want me to also generate a tiny badges block (e.g., “PR Mentor: enabled” + links to Actions runs) or a demo PR description template with checkboxes for teams?
You said:
generate both please
ChatGPT said:
Thought for 36s
sweet — here are both.

📛 Badges block (drop-in)
Generic (replace OWNER/REPO once):
<!-- PR Mentor badges -->
[![PR Mentor](https://github.com/OWNER/REPO/actions/workflows/pr-mentor.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/pr-mentor.yml)
[![LLM Reviewer: optional](https://img.shields.io/badge/LLM%20Reviewer-optional-lightgrey)](docs/llm-reviewer.md)
[![Danger JS](https://img.shields.io/badge/Danger%20JS-enabled-blue?logo=npm)](https://danger.systems/js/)
[![reviewdog](https://img.shields.io/badge/reviewdog-enabled-blue)](https://github.com/reviewdog/reviewdog)
[![Semgrep CI](https://img.shields.io/badge/Semgrep-ci--ready-blue)](https://semgrep.dev/docs/deployment/add-semgrep-to-ci)
[![Ruff](https://img.shields.io/badge/Ruff-linting-blue)](https://docs.astral.sh/ruff/)

Pre-filled for your repo (lazyxeon/Genesis-Code-Protocol):
<!-- PR Mentor badges -->
[![PR Mentor](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/pr-mentor.yml/badge.svg)](https://github.com/lazyxeon/Genesis-Code-Protocol/actions/workflows/pr-mentor.yml)
[![LLM Reviewer: optional](https://img.shields.io/badge/LLM%20Reviewer-optional-lightgrey)](docs/llm-reviewer.md)
[![Danger JS](https://img.shields.io/badge/Danger%20JS-enabled-blue?logo=npm)](https://danger.systems/js/)
[![reviewdog](https://img.shields.io/badge/reviewdog-enabled-blue)](https://github.com/reviewdog/reviewdog)
[![Semgrep CI](https://img.shields.io/badge/Semgrep-ci--ready-blue)](https://semgrep.dev/docs/deployment/add-semgrep-to-ci)
[![Ruff](https://img.shields.io/badge/Ruff-linting-blue)](https://docs.astral.sh/ruff/)

Notes: GitHub’s native workflow status badge is the .../actions/workflows/<file>.yml/badge.svg form; click any workflow’s “••• → Create status badge” to copy a pre-wired snippet. For custom styling or extra labels, you can use Shields’ GitHub Actions Workflow Status badge. GitHub DocsShields

🧪 Demo PR description template (teams + checklists)
Save as either .github/PULL_REQUEST_TEMPLATE.md (to make it the default) or as docs/pr-template-demo.md for one-off copy/paste. GitHub supports multiple PR templates too. GitHub Docs+1
# PR Title: <scope>: <short summary>

## Summary
- What & why in 2–4 bullets.
- Link issues/tickets.

## Changes
- [ ] Code
- [ ] Tests
- [ ] Docs
- [ ] Config/Infra

## Risk
- [ ] Low  [ ] Medium  [ ] High  
Describe fallout + rollback plan.

## Testing
- [ ] Unit tests added/updated
- [ ] Integration/CLI verified
- [ ] Manual steps documented
Notes:

## Performance
- Touched hot paths? If yes, include micro-bench notes or rationale.

## Ownership / Teams Review
- Request the teams you need, check when acknowledged:
- [ ] Backend
- [ ] Frontend
- [ ] DevOps/Infra
- [ ] Security
- [ ] Data/ML
- [ ] Docs

## Screenshots / Artifacts
<optional images, logs, links>

---

### Reviewer Guidance (quick reminders)
- **Design/clarity first**; style nits last.
- Prefer **small, focused** changes; explain large diffs.
- Ensure **tests** cover changed behavior.
(Adapted from Google’s public code-review guidance.) 

Why this layout? It nudges authors/reviewers toward the same high-signal areas codified in widely referenced guides (design, tests, clarity) and pairs clean checklists with Danger/reviewdog automation you’ve already wired. Google GitHub+1

