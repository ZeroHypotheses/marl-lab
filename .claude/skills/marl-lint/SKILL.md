---
name: marl-lint
description: Health-check the marl-lab wiki: broken wikilinks, orphan pages, contradictions, stale or unverified claims, missing pages, index drift, uncited claims. Trigger when the user says: lint the wiki, check the wiki, wiki health, is the wiki consistent.
---

# marl-lint

**This skill is a wrapper. The instructions live in a harness-neutral playbook
so every agent in this repo behaves the same way.**

Read and follow [`workflows/lint.md`](../../../workflows/lint.md) in full, plus the
operating principles in [`AGENTS.md`](../../../AGENTS.md).

Apply mechanical fixes (index drift, missing backlinks) directly; ask before
deleting anything.

End the report with the three questions worth investigating next and the sources
worth acquiring — that is the most useful output of a lint pass.
