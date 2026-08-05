#!/usr/bin/env bash
# Deploy this repo's .agents/skills/ to wherever your agent harness looks for skills.
#
# Codex, Cursor, Gemini CLI, Copilot and Antigravity already read .agents/skills/ at project level,
# so you only need this for (a) Claude Code, which reads .claude/skills/, or (b) making these skills
# available globally, outside this repo.
#
# Usage:
#   .agents/scripts/install-skills.sh [--here | --project DIR] [--copy]
#
# Options:
#   --here           mirror into THIS repo's .claude/skills (gitignored). Smallest, safest option:
#                    Claude Code picks the skills up when opened on this repo. Always a copy.
#   --project DIR    install into DIR/.agents/skills (for a different project)
#   --copy           copy instead of symlink. Required across the Windows<->WSL boundary.
#   -h, --help       show this help
#
# With no options: installs globally to ~/.agents/skills and bridges ~/.claude/skills to it.
# See ../docs/portability.md for the symlink-vs-copy tradeoff.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SRC="$REPO_ROOT/.agents/skills"

[[ -d "$SRC" ]] || { echo "error: $SRC not found" >&2; exit 1; }

mode="symlink"; project=""; here="no"
while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help) sed -n '2,19p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    --here) here="yes"; mode="copy"; shift ;;
    --copy) mode="copy"; shift ;;
    --project) project="${2:?--project needs a directory}"; shift 2 ;;
    *) echo "unknown arg: $1 (try --help)" >&2; exit 1 ;;
  esac
done

deploy() {  # deploy <dest>
  local dest="$1"
  mkdir -p "$(dirname "$dest")"
  if [[ -e "$dest" || -L "$dest" ]]; then rm -rf "$dest"; fi
  if [[ "$mode" == "copy" ]]; then
    cp -r "$SRC" "$dest"; echo "copied   $SRC -> $dest"
  else
    ln -s "$SRC" "$dest"; echo "symlink  $SRC -> $dest"
  fi
}

if [[ "$here" == "yes" ]]; then
  deploy "$REPO_ROOT/.claude/skills"
  echo "done. Claude Code will find these skills when opened on this repo."
  echo "re-run after editing .agents/skills/ (it's a copy, not a live link)."
elif [[ -n "$project" ]]; then
  deploy "$project/.agents/skills"
  echo "done. For Claude Code in that project: also deploy to $project/.claude/skills"
else
  deploy "$HOME/.agents/skills"
  deploy_target="$HOME/.claude/skills"
  mkdir -p "$(dirname "$deploy_target")"
  if [[ -e "$deploy_target" || -L "$deploy_target" ]]; then rm -rf "$deploy_target"; fi
  if [[ "$mode" == "copy" ]]; then
    cp -r "$SRC" "$deploy_target"; echo "copied   $SRC -> $deploy_target"
  else
    ln -s "$HOME/.agents/skills" "$deploy_target"; echo "symlink  $HOME/.agents/skills -> $deploy_target"
  fi
  echo "done. Global install complete (~/.agents/skills + ~/.claude/skills)."
fi
