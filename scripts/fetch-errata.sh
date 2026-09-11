#!/usr/bin/env bash
# Fetch the book's errata and check it against our PDF.
#
# Two jobs:
#   1. Which printing is book/marl-book.pdf? Errata page numbers refer to the
#      *second* printing, and pagination shifted between printings, so this
#      determines whether the listed corrections still need applying.
#   2. Has the errata changed upstream since we last recorded it? A new
#      erratum can invalidate a wiki page that was correct when written.
#
# Run it before ingesting a chapter, and during `/marl-lint`.
set -euo pipefail
cd "$(dirname "$0")/.."

URL="https://www.marl-book.com/errata.txt"
DEST="book/errata.txt"
RECORD="wiki/sources/errata.md"
TEXT="book/text/full.txt"

echo "==> Fetching $URL"
if ! curl -fsSL -o "$DEST" "$URL"; then
  echo "error: could not fetch errata. Check the URL in a browser." >&2
  exit 1
fi
echo "    saved to $DEST ($(wc -c < "$DEST" | tr -d ' ') bytes, gitignored)"

new_sum="$(shasum -a 256 "$DEST" | cut -d' ' -f1)"
old_sum="$(grep -oE '^sha256: [0-9a-f]{64}' "$RECORD" 2>/dev/null | cut -d' ' -f2 || true)"

echo
echo "==> Errata version"
if [ -z "$old_sum" ]; then
  echo "    no recorded checksum yet"
  echo "    current: $new_sum"
elif [ "$new_sum" = "$old_sum" ]; then
  echo "    unchanged since last recorded ($new_sum)"
else
  echo "    !! ERRATA HAS CHANGED UPSTREAM"
  echo "       recorded: $old_sum"
  echo "       current:  $new_sum"
  echo
  echo "       Some wiki pages may now be wrong. Re-read $DEST, check whether"
  echo "       any new entry touches a page cited in wiki/, and update"
  echo "       $RECORD (including the sha256) and wiki/log.md."
fi

# --- Which printing? ---------------------------------------------------------
# Each sentinel is a correction from the errata, checked as raw text so no
# page-number arithmetic is needed. Format: label|first-printing|second-printing
sentinels() {
  cat <<'EOF'
p12 "fourth" -> "quarter"|fourth, or year|quarter, or year
p84 exponential-time phrase removed|exponential time by a deterministic Turing machine|
p285 Fig 9.25a spelling|InitialiseNode|InitializeNode
p294 Fig 9.28 caption colour reference removed|blue bars|
EOF
}

echo
echo "==> Printing check (sentinel corrections from the errata)"
if [ ! -f "$TEXT" ]; then
  echo "    skipped — $TEXT not found. Run scripts/extract-book-text.sh first."
  exit 0
fi

first=0; second=0
while IFS='|' read -r label old new; do
  [ -z "$label" ] && continue
  if [ -n "$old" ] && grep -qF -- "$old" "$TEXT"; then
    printf '    [1st printing] %s\n' "$label"; first=$((first + 1))
  elif [ -n "$new" ] && grep -qF -- "$new" "$TEXT"; then
    printf '    [2nd printing] %s\n' "$label"; second=$((second + 1))
  elif [ -z "$new" ]; then
    printf '    [2nd printing] %s (text absent, as corrected)\n' "$label"; second=$((second + 1))
  else
    printf '    [inconclusive]  %s\n' "$label"
  fi
done < <(sentinels)

echo
if [ "$first" -eq 0 ] && [ "$second" -gt 0 ]; then
  echo "    => SECOND PRINTING. The listed corrections are already applied."
  echo "       Cite page numbers as-is; they match the errata."
elif [ "$first" -gt 0 ] && [ "$second" -eq 0 ]; then
  echo "    => FIRST PRINTING. The corrections are NOT applied."
  echo "       Apply every erratum by hand when ingesting, and note that errata"
  echo "       page numbers are second-printing (e.g. 'p203 (previously p202)')."
else
  echo "    => MIXED/INCONCLUSIVE ($first first, $second second)."
  echo "       Check $DEST against the PDF by hand before trusting page cites."
fi
