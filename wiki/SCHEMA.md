# Wiki Schema

How this knowledge base is structured and maintained. Read this before writing
to `wiki/`. This follows the [Karpathy LLM-wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
raw sources stay immutable, the agent compiles them once into a persistent,
interlinked wiki, and keeps that wiki current instead of re-deriving knowledge
on every question.

## Three layers

| Layer | Where | Who owns it |
|---|---|---|
| Raw sources (immutable) | `book/`, `upstream/`, papers, talks | the human curates |
| The wiki (compiled knowledge) | `wiki/` | the **agent** writes all of it |
| The schema (this file + `AGENTS.md`) | repo root | co-evolved by both |

The human rarely writes wiki pages. The human sources, directs, and questions;
the agent summarises, cross-references, files, and does the bookkeeping.

## Page types

**`sources/<slug>.md`** — one per ingested source (a book chapter, a paper, a
lecture, a codebase module). What it claims, what's new, what it contradicts.
Slug convention: `ch03-games`, `maddpg-2017`, `bcn-summer-school-s2`.

**`topics/<slug>.md`** — a concept that outlives any single source: `normal-form-games`,
`nash-equilibrium`, `centralised-training-decentralised-execution`, `non-stationarity`.

**`algorithms/<slug>.md`** — one per algorithm. Use the template below.

**`notes/<slug>.md`** — synthesis the agent or human produced: comparisons,
answered questions worth keeping, open questions, experiment post-mortems.

## Frontmatter (required on every page)

```yaml
---
title: Independent Q-Learning (IQL)
type: algorithm          # source | topic | algorithm | note
status: stub             # stub | drafted | solid
sources: ["[[ch06-marl-algorithms]]", "[[tan-1993]]"]
updated: 2026-09-11
---
```

`status` is honest self-assessment: `stub` = a title and a link; `drafted` =
written but unverified against the source; `solid` = checked against a cited
source and consistent with the rest of the wiki.

## Algorithm page template

```markdown
## One-line
What it does, in a sentence a tired reader understands.

## Setting
Game model, observability, reward structure, training regime (CTDE? fully
decentralised?). Be specific — most MARL confusion is a setting mismatch.

## Update rule
The equation, with every symbol defined. Cite where it comes from.

## Why it works / when it breaks
The assumption it leans on, and the first thing that violates it.

## Relation to
[[other-algorithms]] — what it generalises, specialises, or fixes.

## In the codebase
`upstream/codebase/marlbase/<path>` — where the real implementation lives,
and where the code departs from the book's presentation.

## Open questions
```

## Conventions

- **Wikilinks**: `[[slug]]`, matching the filename without `.md`. Linking to a
  page that doesn't exist yet is *encouraged* — it marks a gap. `/marl-lint`
  reports these.
- **Citations**: every non-obvious claim carries one — `[Ch. 9.3]`,
  `[Lowe et al. 2017, §4.2]`, `upstream/codebase/marlbase/qmix/train.py:88`.
- **Uncertainty**: mark it inline with `> ❓ unverified:` rather than dropping it.
- **Contradictions**: when sources disagree, record both and mark
  `> ⚠️ conflict:` with both citations. Do not silently resolve.
- **Maths**: LaTeX in `$…$` / `$$…$$`. Define every symbol on first use in a page.
- Every page is self-contained. No page may depend on chat history.

## Operations

`index.md` is the catalog — the agent reads it *first* to find relevant pages,
then drills in. Updated on every ingest.

`log.md` is the append-only timeline. Entry prefix is fixed so it stays
greppable: `## [YYYY-MM-DD] <op> | <subject>` where `<op>` is
`ingest` / `query` / `lint` / `experiment`. So `grep "^## \[" wiki/log.md | tail -5`
shows recent activity.

The three operations — ingest, query, lint — are specified in
[`workflows/`](../workflows/).
