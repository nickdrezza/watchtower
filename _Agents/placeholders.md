---
type: documentation
title: "Placeholders"
description: "Each file in this template that holds a stand-in value to replace after setup, with grep checks to find them."
updated: 2026-10-06
status: active
domain: system
workspace: vault
related:
  - "[[README|Watchtower]]"
---

# Placeholders

Every file in this template that carries a stand-in value you have to replace with your own.
[`README.md`](../README.md#set-up) → *Set up* walks the *process*; this is the *list of paths*, so
nothing is left half-renamed six months later.

Two classes, and they are not equally urgent:

- **Identity** — `<you>`, `<your-vault>`, `<vault-path>`. Wrong values here mean a command that
  doesn't run. Fix these first; there are only a handful.
- **Employer scope** — `ACME`, `Acme`, `Acme Analytics`. Wrong values here mean a *tag* that doesn't
  match your own, which fails quietly: notes get filed with a scope nobody queries. Fix these before
  you write many notes.

Counts are occurrences, not lines. Verify with:

```bash
grep -rn --exclude-dir=.git '<you>\|<your-vault>\|<vault-path>' .
grep -rn --exclude-dir=.git 'ACME\|Acme' .
```

Both greps also match this file, which names the placeholders in order to describe them. Delete it once
you're done — it has no purpose in a vault that's been set up.

**Every count below was verified against the files on 2026-10-06.** If they've drifted, trust the grep,
not the table.

## Identity — replace with your GitHub handle and vault name

| File | Count |
|---|---|
| `_Agents/skills/vault-sync/SKILL.md` | 2 |
| `_Agents/memory/machines/windows-wsl.md` | 2 |
| `README.md` | 1 |
| `_Agents/README.md` | 1 |
| `_Agents/skills/watchtower/reference.md` | 1 |
| `_Agents/memory/machines/macos.md` | 1 |
| `Spaces/Work/skills/shared-vault/SKILL.md` | 1 |
| `Concepts/AI Agents.md` | 1 |

## Employer scope — replace with your own employer tag and name

`ACME` is the frontmatter tag; `Acme` / `Acme Analytics` is the employer's name in prose. **Rename the
tag in [`_Agents/tags.md`](tags.md) and in `boundaries` in [`_Agents/wt.json`](wt.json) in the same
change** — the registry is the tag authority, and `wt doctor` checks notes against both.

| File | Count |
|---|---|
| `_Agents/skills/watchtower/SKILL.md` | 11 |
| `_Agents/skills/watchtower/reference.md` | 11 |
| `_Agents/tags.md` | 8 |
| `Spaces/Work/memory/connectors/` | 6 |
| `Spaces/Work/memory/warehouse/` | 6 |
| `_Agents/skills/vault-memory/SKILL.md` | 4 |
| `_Agents/skills/vault-sync/SKILL.md` | 3 |
| `Spaces/Work/skills/shared-vault/SKILL.md` | 3 |
| `Spaces/Work/memory/credentials/` | 3 |
| `AGENTS.md` | 2 |
| `README.md` | 2 |
| `_Agents/wt.json` | 2 |
| `_Agents/memory/README.md` | 2 |
| `_Agents/skills/vault-edit/SKILL.md` | 2 |
| `_Templates/Weekly Work Log.md` | 2 |
| `Spaces/Work/memory/projects/` | 2 |
| `_Agents/README.md` | 1 |
| `_Agents/wt` | 1 |
| `_Agents/skills/bootstrap/SKILL.md` | 1 |
| `_Agents/skills/vault-prune/SKILL.md` | 1 |
| `Spaces/Work/AGENTS.md` | 1 |
| `Spaces/Work/People/index.md` | 1 |
| `Spaces/Work/Projects/index.md` | 1 |
| `Spaces/Personal/skills/personal/SKILL.md` | 1 |
| `Spaces/Personal/skills/personal/references/diary.md` | 1 |
| `Spaces/Personal/skills/personal/references/reflections.md` | 1 |

If you have no employer scope to track — a purely personal vault — delete the tag and its rows instead
of renaming them. A scope tag nobody filters on is clutter.

## Example content to replace or delete

Not placeholders exactly; example rows written to show the shape, which read as facts if you leave
them:

| File | What |
|---|---|
| `_Agents/memory/machines/macos.md` · `windows-wsl.md` | Whole profiles are examples. Paths, installed tooling, and the **deliberately not installed** list all need your values — that last list is load-bearing, it stops an agent burning turns on a tool you don't have. |
| `Spaces/Work/memory/warehouse/` | Example platform memory. Rename it per system you actually use and shape the rest like it. |
| `Spaces/Work/memory/credentials/` · `connectors/` · `projects/` | Example rows only. **Locations only, never values.** |
| `_Agents/archive/Skill Exports.md` | One example destination row (`your-org/skills-marketplace`), kept as history. |

## Known gap

The `shared-vault` skill points at `_Agents/memory/git-and-tickets.md`, which this template does not
ship. Either create that memory file for your git host and tracker, or change the pointer to
`_Agents/memory/machines/index.md`.

## Machine paths never belong in a skill

Once you're past setup, the rule that keeps this from recurring: a skill describes *how*;
`_Agents/memory/` holds *what is true about this environment*. A literal path inside a skill breaks on
your other machine and rots without telling you. `wt doctor` has a `hardcoded-machine-path` check for
exactly this — add your account names to `users` in `_Agents/wt.json` to match your own home directory
shapes, or it will only catch the ones the template shipped with.
