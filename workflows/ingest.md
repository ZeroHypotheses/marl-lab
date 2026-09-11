# Workflow: Ingest a source

File a book chapter, paper, lecture, or code module into `wiki/`.
Read [`wiki/SCHEMA.md`](../wiki/SCHEMA.md) first.

**Input:** a source — a chapter number, a PDF path, a URL, a codebase path.
**Output:** a new `wiki/sources/` page, updated topic/algorithm pages, an
updated `wiki/index.md`, and an entry in `wiki/log.md`.

One source typically touches 5–15 wiki pages. That is normal and correct.

## Steps

**1. Locate and read the source in full.**
- Book chapter → `book/text/ch<NN>.md` if extracted, else the PDF in `book/`.
- Slides → `upstream/slides/marl-book-ch<N>-*.pdf`.
- Code → read the actual files under `upstream/`.
- Paper/URL → fetch it. If you cannot, say so and stop; do not summarise from memory.

**2. Check the errata.** Read [`wiki/sources/errata.md`](../wiki/sources/errata.md).
If any correction falls in the pages you're ingesting, confirm how it lands in
our PDF before transcribing anything from that page. If the record is stale
(`checked:` is old, or you have reason to doubt it), run
`./scripts/fetch-errata.sh` first.

Where our PDF predates a correction, transcribe the **corrected** version and
mark it:
```
> 📕 errata: the printed text has `k=0`; corrected to `k=1` upstream.
```

**3. Read `wiki/index.md`** to see what already exists. You are integrating into
a body of knowledge, not writing in a vacuum.

**4. Discuss before writing.** Surface the 3–5 key takeaways to the human and
what you propose to create or change. This is a learning lab — the conversation
is part of the point. Wait for a steer unless told to batch.

**5. Write `wiki/sources/<slug>.md`.** Frontmatter per the schema, then:
what this source establishes, the key definitions and results (with equation
numbers), what it assumes, and what it connects to.

**6. Propagate.** For every concept and algorithm the source touches:
- page exists → update it, and *note if the new source contradicts it*
  (`> ⚠️ conflict:` with both citations — never silently overwrite)
- page doesn't exist → create it, at minimum as a stub with a real one-liner
- always add the `[[backlink]]` in both directions

**7. Update `wiki/index.md`** — add new pages, promote `status` where earned.

**8. Append to `wiki/log.md`:**
```
## [YYYY-MM-DD] ingest | <source title>
Pages created: ... · Pages updated: ... · Conflicts flagged: ...
Open questions raised: ...
```

## Rules

- Never summarise a source you have not actually read in this session.
- Preserve the source's own hedging. If the book says "under the assumption
  that rewards are common", that assumption survives into the wiki.
- Equations get transcribed with every symbol defined, or not transcribed.
- Prefer updating an existing page over creating a near-duplicate.
