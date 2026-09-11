#!/usr/bin/env bash
# Bring a fresh clone of marl-lab to a working state.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "==> Fetching upstream submodules (~260MB, this takes a minute)"
git submodule update --init --recursive

echo "==> Setting up the Python environment"
if command -v uv >/dev/null 2>&1; then
  uv sync   # add --extra book for the marlbase reference code
else
  echo "    uv not found — install it: https://docs.astral.sh/uv/getting-started/"
  echo "    (or fall back to: python3 -m venv .venv && .venv/bin/pip install -e .)"
fi

echo
echo "==> Status"
git submodule status | sed 's/^/    /'
if [ -f book/marl-book.pdf ]; then
  echo "    book/marl-book.pdf present"
else
  echo "    book/marl-book.pdf MISSING — download it by hand, see book/README.md"
fi

echo
echo "Ready. Point your agent at AGENTS.md."
