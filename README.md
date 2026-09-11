# marl-lab

> **A personal study repo — me learning multi-agent reinforcement learning.**
> Not a library, not a course, not a product, and not a redistribution of
> anyone's material. It's my notes, my experiments, and the scaffolding that
> helps an AI agent study alongside me.

Everything here is built around one textbook:

> **[Multi-Agent Reinforcement Learning: Foundations and Modern Approaches](https://www.marl-book.com)**
> Stefano V. Albrecht, Filippos Christianos, and Lukas Schäfer
> MIT Press, 2024

The book, its slides, its codebase, and its exercises are **entirely the work of
those authors**. This repo adds nothing to them — it references them as
submodules and builds my own notes on top. Full credits below.

It's agent-first by design: a coding agent is a full participant here. It reads
the book with me, hints at exercises without solving them, scaffolds
experiments, and maintains a knowledge base that compounds instead of
evaporating into chat history.

## Quick start

```bash
git clone --recurse-submodules git@github.com:ZeroHypotheses/marl-lab.git
cd marl-lab
./scripts/bootstrap.sh
```

Then download the textbook PDF by hand into `book/` — see
[`book/README.md`](book/README.md). It can't be scripted (marl-book.com blocks
non-browser clients) and it's deliberately not committed.

Point your agent at [`AGENTS.md`](AGENTS.md).

## Layout

| Path | What |
|---|---|
| [`AGENTS.md`](AGENTS.md) | the agent contract — principles, conventions, hard rules |
| [`book/`](book/) | the textbook PDF + extracted chapter text (gitignored) |
| `upstream/codebase` | [marl-book/codebase](https://github.com/marl-book/codebase) — `marlbase` reference implementations |
| `upstream/slides` | [marl-book/slides](https://github.com/marl-book/slides) — lecture slides per chapter |
| `upstream/exercises` | [marl-book/marl-book-exercises](https://github.com/marl-book/marl-book-exercises) — code exercises |
| [`wiki/`](wiki/) | the LLM-maintained knowledge base — start at [`wiki/index.md`](wiki/index.md) |
| [`experiments/`](experiments/) | your own work, one directory per question |
| [`workflows/`](workflows/) | harness-neutral playbooks the agent follows |

`upstream/` are pinned git submodules and are **read-only**. Update them
deliberately with `git submodule update --remote upstream/<name>`.

## The wiki

Rather than re-deriving knowledge from the PDF on every question, the agent
compiles what it reads into `wiki/` — interlinked markdown pages for sources,
topics, algorithms, and synthesis — and keeps them current as new sources
arrive. It follows [Karpathy's LLM-wiki
pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f);
the conventions are in [`wiki/SCHEMA.md`](wiki/SCHEMA.md).

Three operations drive it:

| | | |
|---|---|---|
| **ingest** | file a chapter, paper, or talk into the wiki | [`workflows/ingest.md`](workflows/ingest.md) |
| **query** | answer a question against it — and file good answers back | [`workflows/query.md`](workflows/query.md) |
| **lint** | health-check for contradictions, stale claims, gaps | [`workflows/lint.md`](workflows/lint.md) |

## Working with agents

`AGENTS.md` is canonical; `CLAUDE.md`, `GEMINI.md`, and
`.github/copilot-instructions.md` are symlinks to it. Codex, Cursor, OpenCode,
and Gemini CLI read `AGENTS.md` directly. Any harness works — the actual
instructions live in plain markdown under `workflows/`, and the
Claude Code skills in `.claude/skills/` are thin wrappers around those same files.

**Claude Code shortcuts:** `/marl-ingest` · `/marl-ask` · `/marl-lint` ·
`/marl-exercise` · `/marl-experiment`

**Optional — [Understand Anything](https://github.com/Egonex-AI/Understand-Anything):**
builds interactive knowledge graphs over both the code and the wiki.

```
/plugin marketplace add Egonex-AI/Understand-Anything
/plugin install understand-anything@understand-anything
```

Then `/understand upstream/codebase` to map the reference implementations, or
`/understand-knowledge wiki/` to get a force-directed graph over the wiki —
it parses the Karpathy-pattern `index.md` this repo already uses.
See `scripts/install-understand-anything.sh` for non-Claude harnesses.

## Principle

> The output of this repo is understanding. Code is how it gets tested; the
> wiki is where it's kept.

## Credits

**Everything of substance here originates with other people.** The list below is
not boilerplate — it's the actual provenance of this repo's contents.

### The textbook, slides, codebase, and exercises

All by **Stefano V. Albrecht**, **Filippos Christianos**, and **Lukas Schäfer**.

```bibtex
@book{marl-book,
    author    = {Stefano V. Albrecht and Filippos Christianos and Lukas Sch\"afer},
    title     = {Multi-Agent Reinforcement Learning: Foundations and Modern Approaches},
    publisher = {MIT Press},
    year      = {2024},
    url       = {https://www.marl-book.com}
}
```

| Resource | Authors | Licence |
|---|---|---|
| [The book](https://www.marl-book.com) (MIT Press, 2024) | Albrecht, Christianos & Schäfer | © MIT Press. Free PDF for **personal use**, **not redistributable** |
| [marl-book/slides](https://github.com/marl-book/slides) | primarily S. V. Albrecht, with L. Schäfer | MIT |
| [marl-book/codebase](https://github.com/marl-book/codebase) (`marlbase`) | primarily F. Christianos, with L. Schäfer, T. McInroe, B. Bolliet | **No licence file — all rights reserved** |
| [marl-book/marl-book-exercises](https://github.com/marl-book/marl-book-exercises) | L. Schäfer, S. V. Albrecht, Y. Poupart | **No licence file — all rights reserved** |
| [Barcelona MARL Summer School 2024](https://iiia.csic.es/en-us/marl-course/) ([lectures](https://www.youtube.com/playlist?list=PLkoCa1tf0XjCU6GkAfRCkChOOSH6-JC_2)) | the same authors | see source |

Two of those repos carry **no licence**, and the book PDF is explicitly
non-redistributable. That is precisely why they are **git submodules pinned to
upstream commits** rather than copied into this repo, and why `book/` is
gitignored: nothing of theirs is redistributed here. Cloning this repo fetches
their work from *their* repositories, under *their* terms.

Per the slides repo's request: these materials accompany the book above, by the
authors above — please go to [marl-book.com](https://www.marl-book.com) and to
the original repositories rather than treating this repo as a source.

**If you're here for MARL, buy the book and read theirs, not mine.**

### Environments

| Environment | Source |
|---|---|
| Level-Based Foraging | [uoe-agents/lb-foraging](https://github.com/uoe-agents/lb-foraging) |
| Multi-Robot Warehouse (RWARE) | [uoe-agents/robotic-warehouse](https://github.com/uoe-agents/robotic-warehouse) |
| SMAClite | [uoe-agents/smaclite](https://github.com/uoe-agents/smaclite) |

### Methods and tooling this repo borrows

| What | Whose |
|---|---|
| The LLM-wiki pattern that `wiki/` implements | [Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) |
| [Understand Anything](https://github.com/Egonex-AI/Understand-Anything) (optional) | [Egonex](https://github.com/Egonex-AI), originally by [Lum1104](https://github.com/Lum1104) — MIT |

### What's actually mine

Only the scaffolding and my own study output: `AGENTS.md`, `workflows/`,
`scripts/`, `.claude/skills/`, the structure of `wiki/`, and whatever notes and
experiments accumulate in `wiki/` and `experiments/`.

Any error in the wiki is mine, not the book's — the wiki is my compiled
understanding of the authors' work, and it can be wrong where they are not.
See [`wiki/sources/errata.md`](wiki/sources/errata.md) for the book's own
published corrections.
