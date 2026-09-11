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
