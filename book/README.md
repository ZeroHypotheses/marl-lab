# The Book

> Stefano V. Albrecht, Filippos Christianos, Lukas Schäfer.
> **Multi-Agent Reinforcement Learning: Foundations and Modern Approaches.**
> MIT Press, 2024. — <https://www.marl-book.com>

This is the foundational knowledge base for the whole lab. Everything in
`wiki/` ultimately cites back to it.

## Getting the PDF (you have to do this by hand)

The authors provide a free, non-printable pre-publication PDF, but
marl-book.com rejects non-browser clients (`curl` gets a 403), so this can't be
scripted:

1. Open <https://www.marl-book.com/download/> in a browser
2. Download the PDF
3. Save it here as `book/marl-book.pdf`

## Why it isn't committed

The PDF is free to download **for personal use** and is **not
redistributable** — it's MIT Press material. This repo has a public remote, so
`book/` is gitignored apart from this README. Same goes for any text extracted
from it. Don't commit either, and don't paste long verbatim passages into
`wiki/` — summarise, cite, and quote sparingly.

## Extracting per-chapter text

Once the PDF is in place, `scripts/extract-book-text.sh` splits it into
`book/text/ch<NN>.md` so agents can read a single chapter without loading 600
pages of context. Also gitignored.

```bash
./scripts/extract-book-text.sh
```

## Companion material

| What | Where |
|---|---|
| Lecture slides, per chapter | `upstream/slides/` |
| Reference implementations (`marlbase`) | `upstream/codebase/` |
| Code exercises | `upstream/exercises/` |
| Summer school lecture videos | [iiia.csic.es MARL course](https://iiia.csic.es/en-us/marl-course/) |

## Citing it

```bibtex
@book{marl-book,
    author    = {Stefano V. Albrecht and Filippos Christianos and Lukas Sch\"afer},
    title     = {Multi-Agent Reinforcement Learning: Foundations and Modern Approaches},
    publisher = {MIT Press},
    year      = {2024},
    url       = {https://www.marl-book.com}
}
```
