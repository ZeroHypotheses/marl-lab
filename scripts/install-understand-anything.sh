#!/usr/bin/env bash
# Install the Understand Anything skills for a non-Claude agent harness.
#
# Understand Anything (https://github.com/Egonex-AI/Understand-Anything, MIT)
# builds interactive knowledge graphs over a codebase — and, via
# /understand-knowledge, over a Karpathy-pattern LLM wiki, which is exactly what
# wiki/ is. Useful here for mapping upstream/codebase and for seeing the shape
# of the wiki as it grows.
#
# On Claude Code you don't need this script — use the plugin marketplace:
#   /plugin marketplace add Egonex-AI/Understand-Anything
#   /plugin install understand-anything@understand-anything
#
# For codex / gemini / opencode / pi / vscode / cline / trae / … this delegates
# to the project's own installer. It clones first and runs the script from
# disk rather than piping the network into a shell, so you can read it before
# it runs.
set -euo pipefail

PLATFORM="${1:-}"
REPO_DIR="${UA_DIR:-$HOME/.understand-anything/repo}"
REPO_URL="https://github.com/Egonex-AI/Understand-Anything.git"

if [ -z "$PLATFORM" ]; then
  cat <<'USAGE'
usage: scripts/install-understand-anything.sh <platform>

platforms: codex gemini opencode pi vibe vscode trae cline kimi hermes
           openclaw antigravity nanobot kiro

Claude Code users: use the plugin marketplace instead —
  /plugin marketplace add Egonex-AI/Understand-Anything
  /plugin install understand-anything@understand-anything
USAGE
  exit 1
fi

if [ -d "$REPO_DIR/.git" ]; then
  echo "==> Updating $REPO_DIR"
  git -C "$REPO_DIR" pull --ff-only
else
  echo "==> Cloning Understand Anything into $REPO_DIR"
  mkdir -p "$(dirname "$REPO_DIR")"
  git clone --depth 1 "$REPO_URL" "$REPO_DIR"
fi

echo
echo "==> Third-party installer: $REPO_DIR/install.sh"
echo "    Read it before continuing if you haven't. It symlinks skills into"
echo "    your harness's skills directory."
read -r -p "    Run it for platform '$PLATFORM'? [y/N] " reply
case "$reply" in
  [yY]*) bash "$REPO_DIR/install.sh" "$PLATFORM" ;;
  *) echo "    Aborted."; exit 1 ;;
esac

cat <<'NEXT'

Done. From the repo root:
  /understand upstream/codebase     map the book's reference implementations
  /understand-knowledge wiki/       graph the wiki (reads wiki/index.md)
NEXT
