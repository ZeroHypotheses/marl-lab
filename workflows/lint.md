# Workflow: Lint the wiki

Periodic health check. Run when the wiki has grown, before a long break, or
when something feels inconsistent.

**Output:** a report to the human, the cheap fixes applied, and a log entry.

## Checks

1. **Broken/orphan wikilinks** — `[[links]]` pointing at pages that don't exist.
   Each is a gap: propose creating it or removing the link.
   ```bash
   grep -rho '\[\[[^]]*\]\]' wiki/ | tr -d '[]' | sort -u   # all link targets
   ls wiki/*/*.md | xargs -n1 basename | sed 's/\.md$//' | sort -u   # all pages
   ```
   Diff the two.

2. **Orphan pages** — pages nothing links to. Either link them or question why
   they exist.

3. **Contradictions** — scan `⚠️ conflict:` markers. Have any been resolved by a
   later source? Resolve and cite, or escalate to the human.

4. **Errata drift** — run `./scripts/fetch-errata.sh`. It warns if the upstream
   errata has changed since the `sha256` recorded in
   [`wiki/sources/errata.md`](../wiki/sources/errata.md). If it has: read the new
   entries, check whether any touches a section cited in `wiki/`, fix those
   pages, then update the record (text, `sha256`, `checked:`) and log it.
   **A wiki page that was right when written can be made wrong by a new
   erratum — this check is the only thing that catches it.**

5. **Stale claims** — pages whose `sources:` have since been superseded.

6. **Unverified claims** — `❓ unverified:` markers. Can any be settled from a
   source now in `book/` or `upstream/`? Settle them.

7. **Missing pages** — concepts referenced repeatedly across pages with no page
   of their own. These are the highest-value pages to write next.

8. **Index drift** — every file in `wiki/*/` appears in `index.md`, and every
   `index.md` row points at a real file. `status` values still honest?

9. **Citation coverage** — non-obvious claims carrying no citation. Flag them.

## Output

Report grouped by check, most actionable first. Apply mechanical fixes
(index drift, missing backlinks) directly. Ask before deleting anything.

End with **the three questions worth investigating next** and **the sources
worth acquiring** — this is the most useful part of a lint pass.

Log it:
```
## [YYYY-MM-DD] lint | <n> pages checked
Fixed: ... · Flagged: ... · Suggested next: ...
```
