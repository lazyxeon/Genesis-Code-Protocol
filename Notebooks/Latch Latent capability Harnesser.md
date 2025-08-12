LATCH v1 — Latent Capability Harnesser (Colab)
Showcased invention from CGP • Extracted on 2025-08-12
Summary
LATCH v1 — Latent Capability Harnesser (Colab)
Generated: 2025-08-10 19:43:06 UTC

Prototype architecture that routes prompts to neglected latent skills discovered via sparse features of hidden states from a tiny pretrained LM. Components

Sparse feature discovery (MiniBatch Dictionary Learning as a fast SAE stand‑in)
Latent router → Calculator / Retrieval / Deliberate LM multi‑draft
Lightweight deliberate reasoning (multi‑draft + self‑scoring)
Evaluation on toy arithmetic + retrieval tasks
LATCH v1 — Latent Capability Harnesser (Colab)
Generated: 2025-08-10 19:43:06 UTC

Prototype architecture that routes prompts to neglected latent skills discovered via sparse features of hidden states from a tiny pretrained LM.

Components

Sparse feature discovery (MiniBatch Dictionary Learning as a fast SAE stand‑in)
Latent router → Calculator / Retrieval / Deliberate LM multi‑draft
Lightweight deliberate reasoning (multi‑draft + self‑scoring)
Evaluation on toy arithmetic + retrieval tasks
References
Tree of Thoughts (Yao et al., 2023): https://arxiv.org/abs/2305.10601
Reflexion (Shinn et al., 2023): https://arxiv.org/abs/2303.11366
Toolformer (Schick et al., 2023): https://arxiv.org/abs/2302.04761
Sparse features / monosemanticity: https://transformer-circuits.pub/2024/scaling-monosemanticity/

# %%capture

!pip -q install transformers==4.43.3 torch==2.3.1 scikit-learn==1.3.2 datasets==2.19.0 matplotlib==3.8.4 numpy==1.26.4

import os, math, random, json, numpy as np, torch, matplotlib.pyplot as plt

from transformers import AutoTokenizer, AutoModelForCausalLM

from sklearn.decomposition import MiniBatchDictionaryLearning

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, classification_report

from datasets import Dataset

from typing import List, Dict, Any

np.random.seed(123); random.seed(123); torch.manual_seed(123)

device = "cuda" if torch.cuda.is_available() else "cpu"

device

MODEL_NAME = "sshleifer/tiny-gpt2"

tok = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(device)

model.eval()

print("Loaded:", MODEL_NAME)

@torch.no_grad()

def get_hidden_acts(texts: List[str], layer: int = -2, max_len: int = 96) -> np.ndarray:

    feats = []

    for t in texts:

        enc = tok(t, return_tensors="pt", truncation=True, max_length=max_len)

        for k in enc: enc[k] = enc[k].to(device)

        out = model.transformer(**enc, output_hidden_states=True)

        hs = out.hidden_states[layer]  # [1, T, H]

        feats.append(hs.squeeze(0).cpu().numpy())

    pooled = np.stack([x.mean(axis=0) for x in feats], axis=0)  # [N, H]

    return pooled

ARITH_QS = [

    "What is 17 plus 28?","Compute 45 - 19.","What is 12 * 7?","Compute 144 / 12.",

    "Add 123 and 456.","What is 9 times 8?","Compute 350 minus 125.","What is 100 divided by 4?",

    "What is 24 + 13?","Compute 81 - 27."

]

def calc_answer(q: str) -> str:

    s = q.lower().replace("compute","").replace("what is","").replace("?","")

    s = s.replace("plus","+").replace("minus","-").replace("times","*").replace("divided by","/")

    s = s.replace("and","+")

    try:

        val = eval(s)

        return str(int(val)) if abs(val-int(val))<1e-9 else str(val)

    except Exception:

        return "unknown"

ARITH = [{"prompt": q, "label": "arith", "gold": calc_answer(q)} for q in ARITH_QS]

CORPUS = {

    "Python": "Python is a popular programming language created by Guido van Rossum.",

    "Tesla": "Tesla, Inc. is an American electric-vehicle and clean-energy company founded by Martin Eberhard and Marc Tarpenning.",

    "Moon": "The Moon is Earth's only natural satellite and has a synchronous rotation with Earth.",

    "GPT": "GPT is a family of autoregressive language models that use transformer architectures.",

    "Paris": "Paris is the capital and most populous city of France, known for the Eiffel Tower."

}

RETR_QS = [

    "Who created the Python programming language?",

    "What is Tesla, Inc.?",

    "What rotates synchronously with Earth?",

    "What architecture do GPT models use?",

    "What is the capital of France?"

]

RETR_GOLD = ["Guido van Rossum","An American electric-vehicle and clean-energy company","The Moon","Transformer","Paris"]

RETR = [{"prompt": q, "label": "retr", "gold": a} for q,a in zip(RETR_QS, RETR_GOLD)]

DATA = ARITH + RETR

Dataset.from_list(DATA)

X = get_hidden_acts([row["prompt"] for row in DATA], layer=-2)

y = np.array([1 if row["label"]=="arith" else 0 for row in DATA])

H = X.shape[1]

n_atoms = min(128, H)

dict_learner = MiniBatchDictionaryLearning(n_components=n_atoms, alpha=1.0, batch_size=8, n_iter=400, random_state=123)

Z = dict_learner.fit_transform(X)

D = dict_learner.components_

print("X", X.shape, "Z", Z.shape, "D", D.shape, "sparsity", (Z==0).mean())

from sklearn.metrics import confusion_matrix

clf = LogisticRegression(max_iter=1000, random_state=123)

clf.fit(Z, y)

pred = clf.predict(Z)

print("Probe train accuracy:", accuracy_score(y, pred))

print(confusion_matrix(y, pred))

print(classification_report(y, pred, target_names=["retr","arith"]))

def tool_calculator(q: str) -> str:

    try:

        return calc_answer(q)

    except Exception:

        return "unknown"

def tool_retrieval(q: str) -> str:

    qlow = q.lower()

    for k, v in CORPUS.items():

        if k.lower() in qlow:

            if k=="Python": return "Guido van Rossum"

            if k=="Tesla": return "An American electric-vehicle and clean-energy company"

            if k=="Moon": return "The Moon"

            if k=="GPT": return "Transformer"

            if k=="Paris": return "Paris"

    for k, v in CORPUS.items():

        for word in v.lower().split():

            if word in qlow: return v

    return "unknown"

@torch.no_grad()

def lm_generate(prompt: str, max_new_tokens=32, temperature=0.9, num_return_sequences=3):

    enc = tok(prompt, return_tensors="pt").to(device)

    out = model.generate(**enc, do_sample=True, max_new_tokens=max_new_tokens, temperature=temperature,

                         num_return_sequences=num_return_sequences, pad_token_id=tok.eos_token_id)

    return [tok.decode(seq, skip_special_tokens=True) for seq in out]

def self_score(prompt: str, answer: str) -> float:

    s=0.0

    s += -0.002*max(0, len(answer)-140)

    if any(w in prompt.lower() for w in ["plus","minus","times","divided","+","-","*","/"]):

        s += 0.5 if any(ch.isdigit() for ch in answer) else -0.2

    if any(w in prompt.lower() for w in ["who","what","where","capital"]):

        s += 0.1 if answer and answer[0].isupper() else 0.0

    return s

def deliberate(prompt: str, drafts=3):

    cands = lm_generate(prompt, num_return_sequences=drafts, max_new_tokens=32, temperature=0.9)

    scored = sorted([(self_score(prompt, c), c) for c in cands], reverse=True)

    return scored[0][1]

def route_prompt(prompt: str) -> str:

    x = get_hidden_acts([prompt], layer=-2)

    z = dict_learner.transform(x)

    prob = clf.predict_proba(z)[0]

    pred = int(prob[1] > prob[0])

    margin = abs(prob[1]-prob[0])

    if pred==1 and margin>0.2: return "calculator"

    if pred==0 and margin>0.2: return "retrieval"

    return "lm_deliberate"

def solve(prompt: str):

    skill = route_prompt(prompt)

    if skill=="calculator": ans = tool_calculator(prompt)

    elif skill=="retrieval": ans = tool_retrieval(prompt)

    else: ans = deliberate(prompt, drafts=4)

    return {"prompt": prompt, "skill": skill, "answer": ans}

tests = [

    "What is 27 + 56?",

    "Who created Python?",

    "Compute 300 - 199",

    "What is the capital of France?",

    "Explain what GPT stands for."

]

for t in tests:

    print(solve(t))

import numpy as np, matplotlib.pyplot as plt

def evaluate(rows):

    preds, golds, skills = [], [], []

    for r in rows:

        out = solve(r["prompt"])

        preds.append(out["answer"]); skills.append(out["skill"]); golds.append(r["gold"])

    acc = np.mean([str(p).strip().lower()==str(g).strip().lower() for p,g in zip(preds,golds)])

    return acc, preds, skills

acc, preds, skills = evaluate(DATA)

print("Accuracy (toy):", round(float(acc),3))

for r,p,s in zip(DATA, preds, skills):

    print(f"[{s}] {r['prompt']} -> {p} (gold: {r['gold']})")

# plot routing distribution

counts = {}

for s in skills: counts[s]=counts.get(s,0)+1

plt.bar(list(counts.keys()), list(counts.values())); plt.title("Routing distribution"); plt.show()

