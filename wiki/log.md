# Wiki Log

Append-only, newest at the bottom. Fixed entry prefix keeps it greppable:

```
## [YYYY-MM-DD] <ingest|query|lint|experiment> | <subject>
```

`grep "^## \[" wiki/log.md | tail -5` → the last five things that happened.

---

## [2026-09-11] init | Lab scaffolded

Repo created: upstream submodules pinned (`codebase`, `slides`, `exercises`),
wiki schema and index seeded, workflows written. No sources ingested yet.

Index seeded with stubs derived from verified upstream content — chapter slugs
from `upstream/slides/` filenames, algorithm list from
`upstream/codebase/marlbase/configs/algorithm/`. Nothing here has been checked
against the book itself.

**Next:** download the textbook PDF (see `book/README.md`), then
`/marl-ingest` chapter 1.

## [2026-09-11] ingest | Book PDF extracted and chapter map verified

`book/marl-book.pdf` added locally (gitignored). `scripts/extract-book-text.sh`
split it into 11 chapter files plus `appendix-a.md` in `book/text/`.

Corrected `index.md` against the book's own table of contents:
- The real book has **11 chapters + Appendix A**, not the 9 the slide decks
  suggested. Chapters 10 (MARL in Practice) and 11 (Multi-Agent Environments)
  have no lecture slides.
- Chapter titles 5 and 6 are longer than the slide filenames implied:
  ch. 5 is "MARL in Games: First Steps **and Challenges**"; ch. 6 is
  "MARL: **Foundational Algorithms**".
- Part I covers ch. 2–6 and Part II ch. 7–11 — **chapter 1 sits outside both
  parts**. An earlier draft of the index had Part I starting at chapter 1;
  corrected against the part-divider pages (PDF pp. 46, 188).

No wiki content pages written yet — only the source map.

**Next:** `/marl-ingest` chapter 1.

## [2026-09-11] ingest | Errata integrated

Added <https://www.marl-book.com/errata.txt> as a tracked source.

**Our PDF is the second printing — all published corrections are already
applied.** Verified against six sentinels (p12 "quarter", Eq 2.54 `k=1`, p84
phrase absent, p198 equations present, "InitializeNode", "blue bars" absent),
not assumed. Recorded in [[errata]].

Ten line-item corrections plus one insertion; five touch the mathematics
(Eq 2.54, p80 $U(\pi)$ index, Eqs 8.30-8.31, Eq 9.10, and the equations added
after Eq 8.8). Those would have been real errors to propagate had we been on
the first printing.

Wired in so it can't be forgotten:
- `scripts/fetch-errata.sh` re-fetches, detects the printing from sentinels,
  and compares the upstream checksum against the `sha256` in [[errata]]
- ingest step 2 now checks errata before any transcription, with a
  `> 📕 errata:` marker convention
- lint check 4 is errata drift — **a new erratum can invalidate a wiki page
  that was correct when written, and nothing else would catch that**

New convention (AGENTS.md): **cite by section or equation, not page.**
Pagination shifts between printings — the errata says "p203 (previously p202)".

Recorded errata sha256: d64ee2d8dbf8e819b60481f93acfed087978a63b457cad6e3c70750de8687be8
