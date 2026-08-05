#!/usr/bin/env bash
# Scaffold a new skill from .agents/templates/skill-template/.
# Usage: .agents/scripts/new-skill.sh my-skill-name
set -euo pipefail

AGENTS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE="$AGENTS_ROOT/templates/skill-template"

name="${1:-}"
if [[ -z "$name" ]]; then
  echo "usage: $0 <skill-name>   (lowercase-hyphenated, e.g. pdf-extract)" >&2
  exit 1
fi
if [[ ! "$name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "error: skill name must be lowercase-hyphenated (got '$name')" >&2
  exit 1
fi

dest="$AGENTS_ROOT/skills/$name"
if [[ -e "$dest" ]]; then
  echo "error: $dest already exists" >&2
  exit 1
fi

cp -r "$TEMPLATE" "$dest"
# set the name: field in the new SKILL.md to match the folder.
# `sed -i` is not portable: GNU takes a bare -i, BSD/macOS requires a backup suffix. Write to a temp
# file and move it, which behaves the same everywhere.
sed "s/^name: .*/name: $name/" "$dest/SKILL.md" > "$dest/SKILL.md.tmp"
mv "$dest/SKILL.md.tmp" "$dest/SKILL.md"

echo "created .agents/skills/$name/SKILL.md"
echo "next: edit its 'description' (the trigger) and body, then commit on a branch + open a PR."
echo "see .agents/CONVENTIONS.md for the spec and pre-commit checklist."
