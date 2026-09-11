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

4. **Stale claims** — pages whose `sources:` have since been superseded.

5. **Unverified claims** — `❓ unverified:` markers. Can any be settled from a
   source now in `book/` or `upstream/`? Settle them.

6. **Missing pages** — concepts referenced repeatedly across pages with no page
   of their own. These are the highest-value pages to write next.

7. **Index drift** — every file in `wiki/*/` appears in `index.md`, and every
   `index.md` row points at a real file. `status` values still honest?

8. **Citation coverage** — non-obvious claims carrying no citation. Flag them.

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
