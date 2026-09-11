# Workflow: Query the wiki

Answer a question against accumulated knowledge, then decide whether the answer
itself is worth keeping.

**Input:** a question.
**Output:** a cited answer — and, when the answer has lasting value, a new
`wiki/notes/` page.

## Steps

**1. Read `wiki/index.md` first.** Find the candidate pages. The index exists so
you don't have to grep blind.

**2. Read those pages fully**, and follow their `[[wikilinks]]` one hop.

**3. Answer with citations** back to wiki pages *and* through them to the
original sources — `[[qmix]] → [Ch. 9.5]`. If the wiki doesn't cover it, say so
plainly, then answer from the raw sources in `book/` or `upstream/` and treat
the gap as an ingest candidate.

**4. Flag conflicts.** If two pages disagree, surface both rather than picking.

**5. File good answers back.** This is the step that makes the wiki compound.
If the answer is a comparison, a synthesis, a derivation, or a connection that
wasn't already written down, write it to `wiki/notes/<slug>.md`, link it from
the pages it draws on, add it to `index.md`, and log it:
```
## [YYYY-MM-DD] query | <question>
Answered from: ... · Filed as: [[note-slug]] · Gaps found: ...
```
Ephemeral lookups ("what's the config key for QMIX?") don't need filing. Use
judgement; when unsure, ask.

## Rules

- Never answer MARL questions from model memory when the wiki or `book/` covers
  it — the point of this lab is grounding. Cite what you actually read.
- "I don't know, and here's what would settle it" is a valid, valuable answer.
