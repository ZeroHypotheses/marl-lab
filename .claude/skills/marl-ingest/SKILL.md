---
name: marl-ingest
description: File a source (book chapter, paper, lecture, or code module) into the marl-lab wiki: read it, write a source page, propagate to topic and algorithm pages, update index.md and log.md. Trigger when the user says: ingest chapter N, file this paper, add this to the wiki, process this source. Do NOT trigger for answering questions against the wiki (use marl-ask).
---

# marl-ingest

**This skill is a wrapper. The instructions live in a harness-neutral playbook
so every agent in this repo behaves the same way.**

Read and follow [`workflows/ingest.md`](../../../workflows/ingest.md) in full, plus the
operating principles in [`AGENTS.md`](../../../AGENTS.md).

Before starting, also read [`wiki/SCHEMA.md`](../../../wiki/SCHEMA.md) for page
types, frontmatter, and citation conventions, and [`wiki/index.md`](../../../wiki/index.md)
to see what already exists.

Key constraints: never summarise a source you have not read in this session;
flag contradictions rather than silently resolving them; one source usually
touches 5-15 pages.
