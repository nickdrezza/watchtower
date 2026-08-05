---
name: skill-template
description: >
  ONE sentence on what this skill does, then when to use it. This field is the trigger — every
  platform reads it to decide whether to load the skill. Include concrete phrases the user would
  type. Example: "Extracts tables from PDFs into CSV. Use when the user uploads a PDF and asks to
  pull tabular data, convert a PDF table to a spreadsheet, or scrape figures from a report."
# --- optional, tool-specific fields below (safe to delete; ignored by tools that don't support them) ---
# allowed-tools: [Read, Write, Bash]
# model: claude-opus-4-8
# user-invocable: true
# argument-hint: "<arg>"
---

# Skill name

One line restating the purpose for a human reader.

## When to use

- Bullet the concrete situations that should trigger this skill.
- Mirror the trigger phrases from the `description`.

## Steps

1. First do this.
2. Then this.
3. Keep the always-loaded body lean. For heavy detail (long tables, full field maps, edge cases),
   create `reference.md` next to this file and say: "Read `reference.md` for X." The agent loads it
   only when needed — that's progressive disclosure.

## Notes / portability

- Prefer portable tooling (POSIX shell, `python3`, common CLIs).
- If any step relies on a tool-specific feature, say so here and give the fallback.

<!--
  Reminder (delete this comment in real skills):
  - Folder name, the `name:` field, and the heading should all agree.
  - Keep this file < ~500 lines; push detail into reference.md / examples.md / scripts/.
  - See ../../CONVENTIONS.md for the full spec.
-->
