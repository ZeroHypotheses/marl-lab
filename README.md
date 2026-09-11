# marl-lab

A personal laboratory for studying **multi-agent reinforcement learning**, built
around Albrecht, Christianos & Schäfer, *[Multi-Agent Reinforcement Learning:
Foundations and Modern Approaches](https://www.marl-book.com)* (MIT Press, 2024).

It is agent-first by design: a coding agent is a full participant here. It reads
the book with you, hints at exercises without solving them, scaffolds
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

## Credits & licensing

The book, slides, codebase, and exercises are the work of Stefano V. Albrecht,
Filippos Christianos, and Lukas Schäfer, and remain under their own licences —
see each submodule. The textbook PDF is free for personal use and **not**
redistributable, which is why it isn't in this repo.

Everything original here (the wiki, experiments, workflows) is mine.
