#!/usr/bin/env bash
# Split the book PDF into per-chapter text so agents can read one chapter
# without loading all 600 pages. Output is gitignored (see book/README.md).
#
# Chapter openers are detected structurally: a page whose first text line looks
# like "<N>   <Title>" (and is not an even-page "<pagenum> ... Chapter <N>"
# running header). Titles are taken from the table of contents, so they're the
# book's own wording rather than a guess from a wrapped heading.
set -euo pipefail
cd "$(dirname "$0")/.."

PDF="book/marl-book.pdf"
OUT="book/text"

if [ ! -f "$PDF" ]; then
  echo "error: $PDF not found. Download it by hand — see book/README.md" >&2
  exit 1
fi

if ! command -v pdftotext >/dev/null 2>&1; then
  echo "error: pdftotext not found. Install poppler:" >&2
  echo "  macOS:  brew install poppler" >&2
  echo "  Debian: apt install poppler-utils" >&2
  exit 1
fi

mkdir -p "$OUT"
echo "==> Extracting full text"
pdftotext -layout "$PDF" "$OUT/full.txt"

echo "==> Splitting into chapters"
python3 - "$OUT" <<'PY'
import pathlib, re, sys

out = pathlib.Path(sys.argv[1])
pages = (out / "full.txt").read_text(encoding="utf-8", errors="replace").split("\f")

def first_text_line(page):
    for line in page.split("\n"):
        if line.strip():
            return line
    return ""

# A chapter/appendix opener: page starts with "<N>  <Title>" or "<A>  <Title>".
# Running headers on even pages look like "42        Chapter 3" — exclude those.
OPENER = re.compile(r"^\s*(\d{1,2}|[A-Z])\s{2,}(\S.*)$")
RUNNING_HEADER = re.compile(r"Chapter\s*\d")
PART_NUMERALS = {"I", "II", "III", "IV", "V"}

# Authoritative titles from the table of contents: "<N>   <Title>  <page>".
# Long titles wrap onto a second line, so join until the page number shows up.
TOC = re.compile(r"^\s*(\d{1,2}|[A-Z])\s{2,}([A-Z][^.]*)$")
PAGE_NO = re.compile(r"\s+\d{1,3}\s*$")
titles = {}
toc_lines = [ln for page in pages[:40] for ln in page.split("\n")]  # front matter only
for i, line in enumerate(toc_lines):
    m = TOC.match(line)
    if not m:
        continue
    num, title = m.group(1), m.group(2).rstrip()
    if not PAGE_NO.search(title):            # wrapped — pull in the continuation
        nxt = next((l for l in toc_lines[i + 1 : i + 3] if l.strip()), "")
        if nxt and not TOC.match(nxt):
            title = f"{title} {nxt.strip()}"
    title = PAGE_NO.sub("", title).strip()
    if title:
        titles.setdefault(num, title)

opens = []
for i, page in enumerate(pages):
    line = first_text_line(page)
    m = OPENER.match(line)
    if not m or RUNNING_HEADER.search(line) or m.group(2)[0].islower():
        continue
    num, heading = m.group(1), m.group(2).strip()
    # Part dividers ("I  FOUNDATIONS OF ...") are all-caps roman numerals,
    # not chapters. Skip them.
    if num in PART_NUMERALS or heading.upper() == heading:
        continue
    opens.append((i, num, heading))

# Drop anything before the real chapter 1 (catches stray front-matter matches).
first_one = next((k for k, (_, num, _) in enumerate(opens) if num == "1"), None)
if first_one is None:
    print("  could not find chapter 1 — work from full.txt", file=sys.stderr)
    sys.exit(0)
opens = opens[first_one:]

for k, (start, num, heading) in enumerate(opens):
    end = opens[k + 1][0] if k + 1 < len(opens) else len(pages)
    title = titles.get(num, heading)
    name = f"ch{int(num):02d}" if num.isdigit() else f"appendix-{num.lower()}"
    label = f"Chapter {num}" if num.isdigit() else f"Appendix {num}"
    body = "\f".join(pages[start:end])
    (out / f"{name}.md").write_text(
        f"# {label}. {title}\n\n"
        f"> Extracted from `book/marl-book.pdf` (PDF pages {start + 1}-{end}).\n"
        f"> Lossy — **always check equations and figures against the PDF.**\n"
        f"> Not redistributable; do not commit or quote at length.\n\n"
        f"{body}",
        encoding="utf-8",
    )
    print(f"  {name}.md  {label}. {title[:58]}")
PY

echo
echo "Done. $(ls "$OUT"/ch*.md "$OUT"/appendix-*.md 2>/dev/null | wc -l | tr -d ' ') chapter files in $OUT/"
echo "PDF text extraction is lossy — verify equations against the PDF before"
echo "putting them in the wiki."
