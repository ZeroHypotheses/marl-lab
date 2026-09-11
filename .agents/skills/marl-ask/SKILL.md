---
name: marl-ask
description: Answer a MARL question against the wiki with citations, and file answers worth keeping back into wiki/notes/. Trigger when the user asks a conceptual MARL question, or says: ask the wiki, what do we know about X, how does X relate to Y. Do NOT trigger for ingesting new sources (use marl-ingest).
---

# marl-ask

**This skill is a wrapper. The instructions live in a harness-neutral playbook
so every agent in this repo behaves the same way.**

Read and follow [`workflows/query.md`](../../../workflows/query.md) in full, plus the
operating principles in [`AGENTS.md`](../../../AGENTS.md).

Start from [`wiki/index.md`](../../../wiki/index.md) — it is the catalog, and reading
it first is what makes this cheaper than grepping.

Key constraint: do not answer from model memory when the wiki, `book/`, or
`upstream/` covers it. Cite what you actually read. Good answers get filed back
into `wiki/notes/` — that is the step that makes the wiki compound.
