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

## [2026-09-11] ingest | Chapter 1, plus skeleton pass over chapters 2-11

**Chapter 1 fully ingested** (pp. 1-18, read in full; zero numbered equations,
which is why it was safe to do in one pass). 10 pages created:
[[ch01-introduction]], [[multi-agent-system]], [[reward-structures]],
[[training-execution-modes]], [[marl-agendas]], [[non-stationarity]],
[[credit-assignment]], [[scaling-in-number-of-agents]],
[[centralised-training-decentralised-execution]], [[level-based-foraging]].

Topic pages kept deliberately thin and marked `stub`: ch. 1 *names* these
concepts but chapters 3-6 define them. Writing them out now would mean drawing
on unsourced knowledge (P4, P6). [[marl-agendas]] is the exception at `drafted`
— ch. 1.5 is the book's main treatment of it.

Two things worth flagging from ch. 1:
- **Conflict recorded on [[level-based-foraging]]**: §1.1-1.2 present the running
  example as fully cooperative (+1 to all), but §1.1 also says the
  implementation actually used (§11.3.1) rewards only agents *involved* in a
  collection — making it mixed-motive. Resolve at [[ch11-environments]].
- **Open question on [[scaling-in-number-of-agents]]**: §1.4 hedges that
  joint-action growth is not always exponential, pointing at §5.4.4. Resolve at
  [[ch05-marl-in-games]].

**Skeleton pass over chapters 2-11 + Appendix A.** Each gets a source page with
verified section structure (from the TOC, including sub-sections), page range,
numbered-equation count, and the errata entries falling in it — but **no summary
of content, because they have not been read.** Each carries a banner saying so.
This makes the wiki navigable ("where is IGM defined?" -> §9.5.1) without
inventing anything.

Deliberately *not* doing full ingests of all 11 chapters at once: the book has
336 numbered equations (ch. 9 alone has 98) and the extracted text is lossy.
Bulk transcription without checking each against the PDF is precisely the
failure the errata work guards against. Chapter 1 was safe because it has none.

Lint: 24 pages, no orphans. 19 unwritten link targets, all intentional gaps.
Highest-value gap by inbound links: **[[solution-concepts]]** (6 inbound) ->
[[ch04-solution-concepts]], followed by [[value-decomposition]] (5) ->
[[ch09-deep-marl]] §9.5.

**Next:** `/marl-ingest 2` (65 equations - check each against the PDF), or jump
to [[ch03-games]] (8 equations) for the game models that ch. 1 keeps deferring to.

## [2026-09-11] ingest | Chapters 2-5 (all of Part I)

Read in full and ingested. 29 new pages, 4 rewritten. Wiki now 53 pages.

**Ch. 2** (65 eqs) → [[markov-decision-process]], [[returns-and-discounting]],
[[value-functions-and-bellman]], [[dynamic-programming]],
[[temporal-difference-learning]], [[learning-curves]].
Eq. 2.54 verified as errata-corrected (`k=1`).

**Ch. 3** (8 eqs) → [[normal-form-games]], [[repeated-normal-form-games]],
[[stochastic-games]], [[partial-observability]], [[knowledge-assumptions]],
[[communication-in-games]], [[rl-game-theory-dictionary]].

**Ch. 4** (30 eqs) → [[solution-concepts]], [[best-response]], [[minimax]],
[[nash-equilibrium]], [[correlated-equilibrium]], [[pareto-optimality]],
[[social-welfare-and-fairness]], [[no-regret]], [[complexity-of-equilibria]].

**Ch. 5** (11 eqs) → [[general-learning-process]], [[convergence-types]],
[[central-learning]], [[independent-learning]], [[equilibrium-selection]],
[[agent-modelling]]; rewrote [[non-stationarity]], [[credit-assignment]],
[[scaling-in-number-of-agents]], [[self-play]].

### Open questions resolved

- ✅ **[[scaling-in-number-of-agents]]** — §5.4.4 supplies ch. 1.4's promised
  counter-example. A power plant with 1,000 control variables has $k^{1000}$
  actions whether controlled by 1 agent or $n$: factoring a **fixed** action
  vector among agents leaves $|A|$ **independent of $n$**. Exponential growth
  only occurs when each added agent brings **new** action variables. So the
  scaling argument for decentralisation is narrower than ch. 1 implies.
- ✅ **[[level-based-foraging]]** — the ch. 1 "conflict" was not one. §3.3 states
  both a common-reward variant (+1 to all) and a general-sum variant (+1 only to
  agents involved) as intended options. Which is in play must be stated when
  comparing results. Still open: which §11.3.1 makes the default.
- ✅ **[[reward-structures]]** — §3.1 gives the formal definitions. Common-reward
  is $R_i = R_j$; zero-sum is $\sum_i R_i(a) = 0$ (a special case of
  constant-sum). "Fully cooperative" is ch. 1's informal phrasing with no
  separate formal definition.
- ✅ **[[credit-assignment]]** — §5.4.3 lists the counterfactual methods ch. 1.4
  gestured at: difference rewards (Wolpert & Tumer 2002) and learned value
  decomposition (Rashid, Sunehag, Son et al.), i.e. §9.4.4 and §9.5.

### Corrections to earlier pages

- **Credit assignment is not a common-reward problem.** Ch. 1 introduces it via a
  common-reward example; §5.4.3 states explicitly it "exists more generally and
  does not depend on common rewards." Page rewritten.
- **Non-stationarity already exists in single-agent RL** (the moving target in
  TD bootstrapping). What MARL adds is that the *environment* becomes
  non-stationary and, critically, **non-Markovian** from each agent's view
  (Laurent et al. 2011). Ch. 1's framing was incomplete.

### Worth flagging

- §4.11: **computing Nash equilibria is PPAD-complete**, and because the result
  covers ε-Nash it covers MARL algorithms too. "MARL is unlikely to be a magic
  bullet." Reframes ch. 6/9 as *structure exploitation* → [[complexity-of-equilibria]]
- §5.2: **a converged learning curve does not imply convergence to a solution**
  — expected returns can converge while $\pi^z$ satisfies none of Eqs. 5.3–5.8.
  Carried into [[convergence-types]] and relevant to `workflows/experiment.md`.
- §5.3.3: in the book's own LBF experiment **IQL beats CQL**, and §5.3.2 notes IL
  is often competitive with state-of-the-art (Papoudakis et al. 2021). Baseline
  discipline for `experiments/`.
- §5.3.2: idealised IQL in Prisoner's Dilemma can be **chaotically
  non-convergent while averaging above the Nash equilibrium reward** — failing
  to converge outperforms converging.

Lint: 53 pages, no orphans. 13 unwritten link targets, **all belonging to
ch. 6, 9 or 11** — the un-ingested chapters. Highest demand:
[[value-decomposition]] (7 inbound, → §9.5), [[iql-tabular]] (6, → the tabular
exercise), [[vdn]]/[[qmix]] (4 each, → §9.5.2–9.5.3).

**Next:** ch. 6 (64 eqs — the user is starting it). Then ch. 9 (98 eqs), worth
splitting across sessions.

## [2026-09-11] lint | Fixed non-rendering wikilinks in index.md

All 65 wikilinks in [[index]] were wrapped in backticks — `` `[[slug]]` `` —
making them **code spans, not links**. They looked correct in plain text and in
git diffs, and were dead in Obsidian. Unwrapped all 65; 53 now resolve to pages
and 13 are intentional gaps (ch. 6/9/11 algorithms and environments).

The single backtick-wrapped example left in `SCHEMA.md` is correct — it
documents the wikilink syntax rather than linking.

Added this as lint check 2 in `workflows/lint.md`. **The existing broken-link
check could not have caught it:** it greps `\[\[...\]\]` regardless of
surrounding backticks, so every one of these looked like a healthy link.

## [2026-09-11] ingest | Tabular IQL exercise

Wrote [[iql-tabular]] — the highest-demand gap after [[value-decomposition]]
(6 inbound links). Landing page for `upstream/exercises/tabular_marl/`:
what the two stubbed methods correspond to in the book, how to run it in the
project venv, and what to expect. **Hints and references only — no solution**
(P3).

**Discrepancy recorded:** the exercise's `create_pd_game` uses a
positive-reward Prisoner's Dilemma — (C,C)=(3,3), (C,D)=(0,5), (D,C)=(5,0),
(D,D)=(1,1) — while the book's Fig. 3.2(c) uses negatives: (−1,−1), (−5,0),
(0,−5), (−3,−3). Both are genuine PDs (ordinal structure $T>R>P>S$ holds for
$5>3>1>0$ and $0>-1>-3>-5$), but plotted numbers won't match the book.

Verified the exercise imports and the environment constructs under `.venv`;
`gymnasium`/`numpy`/`matplotlib` come with `uv sync`, no extra install needed.

Connection worth pursuing: PD is **class 3b** in Fig. 5.2, where IQL's
convergence is "Y/N", and Wunder, Littman & Babes (2010) report chaotic
non-convergence averaging *above* the Nash reward. Good first experiment.

## [2026-09-11] query | Most efficient hands-on path after the first chapters

Answered from: [[ch02-reinforcement-learning]], [[ch05-marl-in-games]],
[[iql-tabular]] · Filed as: [[hands-on-study-loop]] · Gaps found: none.

Recommended the tabular IQL Prisoner's Dilemma exercise as the first bridge
from Chapters 1–5 into implementation, followed by one-factor perturbations of
the ε schedule, learning rate, and seed. The durable loop is: predict,
implement the smallest mechanism, run the supplied baseline, explain the
result, vary one cause, and record the conclusion.

## [2026-09-11] lint | Make hands-on study links portable

The body of [[hands-on-study-loop]] used Obsidian-style wikilinks, which its
standard Markdown preview did not resolve. Converted its navigational links,
its index entry, and the backlink from [[iql-tabular]] to relative Markdown
links. Verified that every target exists and that the note body contains no
remaining unsupported wikilinks.

## [2026-09-12] query | Does `iql_eval` use a solution concept?

Answered from: [[iql-tabular]], [[solution-concepts]],
[[independent-learning]] · Filed as: [[iql-evaluation-vs-solution-concepts]] ·
Gaps found: none.

Distinguished empirical return evaluation from solution-concept evaluation.
For the exercise's one-step Prisoner's Dilemma, a Nash-aware evaluator would
measure each agent's unilateral-deviation gain; Pareto/welfare evaluation would
compare against the feasible return set; and no-regret would require the
episode-level action history. `iql_eval` does none of these—it reports only the
mean and standard deviation of returns under an exploratory policy.

## [2026-09-15] exercise | Tabular IQL in Prisoner's Dilemma

Learned: the game exposes a constant observation rather than joint actions;
each agent selects from its own `Discrete` action space; `learn()` mutates the
Q-tables in place; terminal transitions learn the immediate reward without a
bootstrap; and strict `< epsilon` preserves the exact zero/one exploration
boundaries. Verified greedy selection, exploration coverage, terminal and
non-terminal Q-learning updates, and the full training run. Filed as:
[[first-tabular-iql-exercise]] · Still unclear: none.

## [2026-09-15] query | Why are Wikipedia's Prisoner's Dilemma values reversed?

Answered from: [[normal-form-games]], [[rl-game-theory-dictionary]],
[[iql-tabular]], and Wikipedia's “Prisoner's dilemma” article · Filed into:
[[iql-tabular]] · Gaps found: none.

Wikipedia's narrative table reports years in prison, which are costs to
minimise; the exercise reports rewards to maximise. Negating sentence lengths
restores the reward convention. Both representations preserve the defining
ordinal relation $T>R>P>S$: mutual cooperation is collectively better than
mutual defection, while unilateral defection is individually dominant.

## [2026-09-15] query | What does Nash buy if it is not used for learning?

Answered from: [[solution-concepts]], [[best-response]], [[convergence-types]],
and [[marl-agendas]] · Filed as: [[solution-concepts-as-specifications]] · Gaps
found: none.

Distinguished the learning algorithm as a search procedure from the solution
concept as its specification. Nash provides an acceptance condition, a
deviation-based evaluation metric, a target for convergence guarantees, and
constraints on algorithm representation and tractability even when it is
absent from the update rule. If it changes none of training, algorithm choice,
evaluation, guarantees, or deployment, merely naming it has no operational
value.

## [2026-09-17] experiment | 02-iql-stag-hunt-selection

Hypothesis: unchanged tabular IQL would select risk-dominant hare/hare in more
than 10 of 20 preregistered Stag Hunt seeds · Result: confirmed, with hare/hare
in 20/20 seeds, stag/stag in 0/20, and mismatched in 0/20 · Filed as:
[[exp-02-iql-stag-hunt-selection]].

## [2026-09-17] query | Apply different solution concepts to Stag Hunt?

Answered from: [[solution-concepts-as-specifications]], [[nash-equilibrium]],
[[pareto-optimality]], [[social-welfare-and-fairness]],
[[correlated-equilibrium]], and [[no-regret]] · Filed into:
[[exp-02-iql-stag-hunt-selection]] · Gap found: Experiment 02 did not retain
the episode-level history required to evaluate external or internal regret.

## [2026-09-18] query | Can solution concepts be part of training?

Answered from: [[solution-concepts-as-specifications]],
[[ch06-foundational-algorithms]], and the Chapter 6 introduction · Filed into:
[[solution-concepts-as-specifications]] and Experiment 03's README · Gap found:
our discussion had emphasized the post-training role used with plain IQL.
Recorded three distinct roles: a solution concept can supply an operator inside
learning, define the learning objective, or evaluate the learned output after
training.
