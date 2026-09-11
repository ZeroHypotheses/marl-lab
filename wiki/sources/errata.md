---
title: Book Errata
type: source
status: solid
sources: ["https://www.marl-book.com/errata.txt"]
sha256: d64ee2d8dbf8e819b60481f93acfed087978a63b457cad6e3c70750de8687be8
checked: 2026-09-11
updated: 2026-09-11
---

# Book Errata

Author-published corrections to the textbook:
<https://www.marl-book.com/errata.txt>

The raw file is fetched to `book/errata.txt` (gitignored, like the PDF). This
page is the committed record of **what state we're in** — refresh both with:

```bash
./scripts/fetch-errata.sh
```

## Our PDF is the SECOND PRINTING

Verified 2026-09-11 against four sentinel corrections from the errata, checked
directly in the extracted text:

| Erratum | First printing | Ours |
|---|---|---|
| p12 | "fourth, or year" | **"quarter, or year"** ✅ |
| p33, Eq 2.54 | sums from `k=0` | **sums from `k=1`** ✅ |
| p84 | "…exponential time by a deterministic Turing machine" | **absent** ✅ |
| p198 | equations after Eq 8.8 missing | **present** ✅ |
| p285, Fig 9.25a | "InitialiseNode" | **"InitializeNode"** ✅ |
| p294, Fig 9.28 | caption refers to "blue bars" | **absent** ✅ |

**Consequence: every correction listed in the errata is already applied to our
PDF.** Nothing needs correcting during ingest, and page numbers in the errata
line up with ours.

> ⚠️ This holds only for the *current* errata. If the authors publish a third
> printing or add entries, the new ones may be unapplied. `fetch-errata.sh`
> compares the upstream checksum against the `sha256` in this page's
> frontmatter and warns on drift — that check runs as part of
> [`/marl-lint`](../../workflows/lint.md).

## Why this matters for citations

Pagination **shifts between printings** — the errata itself says
"p203 (previously p202)". A page-number citation is therefore only meaningful
alongside a printing.

**So: cite by section or equation number, not by page.** `[Ch. 9.3]` and
`[Eq. 2.54]` are stable across printings; `[p. 203]` is not. Where a page
number is genuinely the only handle, write it as `[p. 203, 2nd printing]`.

## Current corrections

Ten line-item corrections plus one insertion, spanning pp. 12–323. They are
mostly typographic (two footnotes removed, a spelling, a caption), but five
touch the **mathematics** and would have been real errors to propagate:

- **p33, Eq 2.54** — summation index `k=0` → `k=1`
- **p80** — missing index $i$ in $U(\pi)$
- **p203, Eqs 8.30–8.31** — `u(h^…)` → `u^…`, and `:T` removed
- **p233, Eq 9.10** — in $y_i$, `t` → `t+1` for $h$ and $z$
- **p198** — previously missing equations after Eq 8.8 added (unnumbered, to
  keep later numbering consistent with the first printing)

See `book/errata.txt` for the verbatim list.

## Related

[[ch02-reinforcement-learning]] (Eq 2.54) · [[ch04-solution-concepts]] (p80) ·
[[ch08-deep-rl]] (Eqs 8.8, 8.30–8.31) · [[ch09-deep-marl]] (Eq 9.10, Figs 9.25a, 9.28)
