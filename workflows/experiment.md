# Workflow: Start an experiment

The human's own work lives in `experiments/<nn>-<slug>/`. One directory per
question. Copy `experiments/_template/`.

**Every experiment states its hypothesis before it states its code** (P7).

## Steps

**1. Pin down the question.** Push for something falsifiable. "Try QMIX" is not
an experiment. "Does QMIX beat VDN on LBF `8x8-2p-3f-coop` because of the
mixing network, or just because of the extra parameters?" is.

**2. Create the directory:**
```
experiments/03-qmix-vs-vdn-capacity/
├── HYPOTHESIS.md    ← written BEFORE any code
├── README.md        ← how to run it, what it found
├── run.py
└── runs/            ← gitignored outputs
```

**3. Fill `HYPOTHESIS.md` first** (template in `experiments/_template/`):
the question, the prediction *with a reason*, what would falsify it, the
smallest setup that could answer it, and what's already known from the wiki.

**4. Build the smallest thing that answers it.** Reuse `upstream/codebase`'s
`marlbase` rather than reimplementing — but never edit it in place (P5); import
it, wrap it, or copy the file in with a provenance comment.

**5. Run it, and record the result honestly** — including when the hypothesis
was wrong. A falsified prediction is a better wiki page than a confirmed one.

**6. File it.** Write `wiki/notes/exp-<nn>-<slug>.md` with what was found, link
it from the topic and algorithm pages it bears on, add it to `index.md`, log it:
```
## [YYYY-MM-DD] experiment | <nn>-<slug>
Hypothesis: ... · Result: confirmed|falsified|inconclusive · Filed as: [[...]]
```

## Rules

- Set and record seeds. Report over several of them — single-seed MARL results
  are noise, and the book says so.
- Record the exact command and the config that produced every number.
- Never report a number you did not actually produce in a run.
- If a result surprises you, suspect the harness before the science.
