---
name: vault-doctor
description: >
  Runs the vault's mechanical integrity checks and reports what is objectively broken — dead relative
  and wiki links, tags missing from the Tag Registry, notes without frontmatter, skills missing from
  the hand-maintained index table, skill name/folder mismatches, thin skill descriptions, machine
  paths hardcoded into skills, possible secrets, and stale okf-view snapshots. Use when the user says "check my
  vault", "vault health", "is anything broken", "run the integrity checks", "did I break any links",
  "audit the skills", or before shipping a large structural change. Safe to run anytime; only `--fix` edits files.
  For quality judgement — bad notes, duplicates, notes to simplify — use vault-prune instead.
user-invocable: true
argument-hint: "[--fix|--json|--errors-only]"
---

# Vault doctor

Deterministic checks only. Everything this reports is objectively right or wrong; nothing here needs
taste. **Read-only** — it never edits, so it needs no preview gate and is safe to run at any time.

Quality judgement (is this note worth keeping? should these two merge?) belongs to **`vault-prune`**.
Keeping the two apart matters: this one can run unattended, that one cannot.

## Run it

```bash
_Agents/wt doctor                 # all checks, human-readable
_Agents/wt doctor --json          # machine-readable
_Agents/wt doctor --errors-only   # what CI and the pre-commit hook run
_Agents/wt doctor --fix           # repoint links after moves/renames, refresh okf-view snapshots
```

Exit `0` no errors, `1` errors, `2` could not run. Warnings never fail; errors fail CI and the
pre-commit hook. Run `--fix` after any `git mv`, then run it again without `--fix`: merge only with 0
broken links.

## What each finding means, and the fix

| Finding | Severity | Fix |
|---|---|---|
| `broken-link` | error | Wiki-links resolve by **note name**, markdown links by path. After a move or rename, `--fix` repoints them. Otherwise correct the target or remove the link |
| `broken-anchor` | error | The heading is gone or renamed. Point at the heading that now holds the text |
| `missing-frontmatter` | error | Add frontmatter from `_Templates/` |
| `unregistered-tag` | error | Register it in `Maps/Tag Registry.md` **in the same commit**, or remove it |
| `skill-name-mismatch` / `skill-no-name` | error | `name:` must equal the folder name |
| `skill-not-indexed` | error | Add the row to `_Agents/README.md` |
| `hardcoded-machine-path` | error | Move the fact to `_Agents/memory/machines/` and point at it |
| `secret-pattern` | error | Remove the value, rotate it, and record only where it lives |
| `stale-snapshot` | error | `_Agents/wt index` |
| `skill-description-long` / `-short` | warning | The description is the trigger. Keep it 100–300 characters, so harnesses do not cut it from the skill list |
| `duplicate-title` | warning | Two content pages with one title. Rename one (Isomorphic and Obsidian both resolve by title) |
| `cross-space-link` | warning | A link between two spaces breaks when a space becomes its own brain. Link through a shared page |
| `oversized-file` / `stale-memory` | warning | Split the memory file by concept; check the fact against its source and update `updated:` |
| `empty-file` / `untitled-file` / `stray-folder` | warning | Remove it, or file it |

## Reporting

Lead with the count, then only the findings that need a decision. **Don't paste the whole output** —
hard rule 7. If it's clean, say so in one line.

Known-benign findings exist (template placeholders like `[[_Templates/Weekly Work Log]]`). Say which
you're treating as benign rather than silently dropping them; if one is *permanently* benign, add it to
the script's `GENERIC_LINKS` instead of re-explaining it every run.

## Fixing what it finds

Mechanical fixes (a typo'd path, a missing index row, `--fix` after a move) are yours to make — they
are reversible and verifiable, which is exactly the `AGENTS.md` → *Working model* case (decide reversible details). Anything
that deletes content, or that needs a judgement call about what a note *should* say, goes to
`vault-prune` and its per-item approval.

Re-run after fixing. A fix that introduces a new finding is common with links.

## Related

- `vault-prune` — the judgement half: bad notes, duplicates, over-long notes, knowledge gaps.
- `vault-edit` — the safe way to move, rename, merge, or delete a note without breaking links.
- `vault-sync` — ships the fixes. Run this before syncing a large structural change.
