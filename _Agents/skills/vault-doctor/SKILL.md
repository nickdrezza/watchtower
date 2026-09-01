---
name: vault-doctor
description: >
  Runs the vault's mechanical integrity checks and reports what is objectively broken — dead relative
  and wiki links, tags missing from the Tag Registry, notes without frontmatter, skills missing from
  the three hand-maintained index tables, skill name/folder mismatches, thin skill descriptions, machine
  paths hardcoded into skills, and a stale .claude/skills mirror. Use when the user says "check my
  vault", "vault health", "is anything broken", "run the integrity checks", "did I break any links",
  "audit the skills", or before shipping a large structural change. Read-only and safe to run anytime.
  For quality judgement — bad notes, duplicates, notes to simplify — use vault-prune instead.
user-invocable: true
argument-hint: "[check,check]"
---

# Vault doctor

Deterministic checks only. Everything this reports is objectively right or wrong; nothing here needs
taste. **Read-only** — it never edits, so it needs no preview gate and is safe to run at any time.

Quality judgement (is this note worth keeping? should these two merge?) belongs to **`vault-prune`**.
Keeping the two apart matters: this one can run unattended, that one cannot.

## Run it

```bash
_Agents/scripts/check_vault.py                        # all checks, human-readable
_Agents/scripts/check_vault.py --json                 # machine-readable
_Agents/scripts/check_vault.py --only wiki-links,tags # a subset
```

Exit `0` clean, `1` findings, `2` couldn't run. Checks available: `relative-links`, `wiki-links`,
`tags`, `frontmatter`, `skill-indexes`, `skill-descriptions`, `hardcoded-paths`, `mirror`.

## What each finding means, and the fix

| Finding | Why it matters | Fix |
|---|---|---|
| `broken-relative-link` | A pointer an agent will follow and fail | Correct the path, or delete the link |
| `broken-wiki-link` | Obsidian shows it dead; the graph loses a node | Create the note, fix the name, or drop the link. Wiki-links resolve by **note name**, not path |
| `unregistered-tag` | Vocabulary drift — the thing that makes a big vault slow to search | Register it in `Maps/Tag Registry.md` **in the same commit**, or remove it |
| `missing-frontmatter` | Dashboards filter on `type ==`, so the note is invisible to every view | Add frontmatter from `_Templates/` |
| `skill-not-indexed` | Three index tables are hand-maintained; an unlisted skill is invisible to a reader | Add the row. |
| `skill-name-mismatch` | Folder name must equal the `name:` field | Rename one to match |
| `thin-skill-description` | **The description is the trigger.** Under ~200 chars it silently fails to load | Rewrite it with real phrases the user would type |
| `hardcoded-machine-path` | `CONVENTIONS.md`: skills say *how*, memory says *what is true*. A baked path breaks on the other machine | Move the fact to `_Agents/memory/machines/` and point at it |
| `stale-skills-mirror` | `.claude/skills/` is a copy, so Claude Code is running old text | `_Agents/scripts/install-skills.sh --here` |

## Reporting

Lead with the count, then only the findings that need a decision. **Don't paste the whole output** —
hard rule 7. If it's clean, say so in one line.

Known-benign findings exist (template placeholders like `[[_Templates/Weekly Work Log]]`). Say which
you're treating as benign rather than silently dropping them; if one is *permanently* benign, add it to
the script's `GENERIC_LINKS` instead of re-explaining it every run.

## Fixing what it finds

Mechanical fixes (a typo'd path, a missing index row, refreshing the mirror) are yours to make — they
are reversible and verifiable, which is exactly the `AGENTS.md` → *…and when not to ask* case. Anything
that deletes content, or that needs a judgement call about what a note *should* say, goes to
`vault-prune` and its per-item approval.

Re-run after fixing. A fix that introduces a new finding is common with links.

## Related

- `vault-prune` — the judgement half: bad notes, duplicates, over-long notes, knowledge gaps.
- `vault-edit` — the safe way to move, rename, merge, or delete a note without breaking links.
- `vault-sync` — ships the fixes. Run this before syncing a large structural change.
