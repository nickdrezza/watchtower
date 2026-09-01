---
type: documentation
status: active
domain: system
workspace: vault
tags:
  - "topic/agents"
related:
  - "[[Setup Guide]]"
  - "[[Skills Repo]]"
  - "[[Vault Architecture]]"
---

# Placeholders

Every file in this template that carries a stand-in value you have to replace with your own. The
[Setup Guide](Setup%20Guide.md) walks the *process*; this is the *list of paths*, so nothing is left
half-renamed six months later.

Two classes, and they are not equally urgent:

- **Identity** — `<you>`, `<your-vault>`, `<vault-path>`. Wrong values here mean a command that
  doesn't run. Fix these first; there are only a handful.
- **Employer scope** — `ACME`, `Acme`, `Acme Analytics`. Wrong values here mean a *tag* that doesn't
  match your own, which fails quietly: notes get filed with a scope nobody queries. Fix these before
  you write many notes.

Counts are occurrences, not lines. Verify with:

```bash
grep -rn '<you>\|<your-vault>\|<vault-path>' --include='*.md' --include='*.sh' .
grep -rn 'ACME\|Acme' --include='*.md' --include='*.sh' .
```

Both greps also match this file, which names the placeholders in order to describe them. Delete it once
you're done — it has no purpose in a vault that's been set up.

**Every count below was verified against the files at the time of writing.** If they've drifted, trust
the grep, not the table.

## Identity — replace with your GitHub handle and vault name

| File | Count |
|---|---|
| `_Agents/skills/knowledge-router/SKILL.md` | 4 |
| `_Docs/Skills Repo.md` | 3 |
| `_Docs/Setup Guide.md` | 3 |
| `_Agents/memory/machines/windows-wsl.md` | 2 |
| `_Agents/skills/vault-sync/SKILL.md` | 2 |
| `README.md` | 1 |
| `_Agents/README.md` | 1 |
| `_Agents/memory/machines/macos.md` | 1 |
| `_Agents/skills/shared-vault-ingest/SKILL.md` | 1 |
| `_Agents/skills/shared-vault-promote/SKILL.md` | 1 |
| `Concepts/AI Agents.md` | 1 |

## Employer scope — replace with your own employer tag and name

`ACME` is the frontmatter tag; `Acme` / `Acme Analytics` is the employer's name in prose. **Rename the
tag in [Tag Registry](../Maps/Tag%20Registry.md) in the same change** — it is the tag authority, and
`vault-doctor` checks notes against it.

| File | Count |
|---|---|
| `_Agents/skills/watchtower/SKILL.md` | 12 |
| `_Agents/skills/watchtower/reference.md` | 9 |
| `Maps/Tag Registry.md` | 8 |
| `_Agents/skills/shared-vault-ingest/SKILL.md` | 7 |
| `_Docs/Skills Repo.md` | 6 |
| `_Agents/skills/knowledge-router/SKILL.md` | 5 |
| `_Docs/AI Note Intake Workflow.md` | 4 |
| `_Agents/skills/vault-memory/SKILL.md` | 4 |
| `_Agents/skills/shared-vault-promote/SKILL.md` | 4 |
| `_Docs/Agent Memory.md` | 3 |
| `_Docs/Vault Architecture.md` | 3 |
| `_Agents/skills/vault-sync/SKILL.md` | 3 |
| `_Templates/Weekly Work Log.md` | 2 |
| `_Agents/memory/README.md` | 2 |
| `_Agents/memory/warehouse.md` | 2 |
| `_Agents/skills/vault-edit/SKILL.md` | 2 |
| `_Agents/skills/skills-sync/reference.md` | 2 |
| `_Agents/README.md` | 1 |
| `_Agents/memory/projects.md` | 1 |
| `_Agents/memory/connectors.md` | 1 |
| `_Agents/memory/credentials.md` | 1 |
| `_Agents/skills/bootstrap/SKILL.md` | 1 |
| `_Agents/skills/shared-vault-sync/SKILL.md` | 1 |
| `_Agents/skills/personal-vault/SKILL.md` | 1 |
| `_Agents/skills/personal-reflection/SKILL.md` | 1 |
| `_Agents/skills/diary/SKILL.md` | 1 |
| `_Agents/skills/vault-prune/SKILL.md` | 1 |

If you have no employer scope to track — a purely personal vault — delete the tag and its rows instead
of renaming them. A scope tag nobody filters on is clutter.

## Example content to replace or delete

Not placeholders exactly; example rows written to show the shape, which read as facts if you leave
them:

| File | What |
|---|---|
| `_Agents/memory/machines/macos.md` · `windows-wsl.md` | Whole profiles are examples. Paths, installed tooling, and the **deliberately not installed** list all need your values — that last list is load-bearing, it stops an agent burning turns on a tool you don't have. |
| `_Agents/memory/warehouse.md` | Example platform memory. Rename it per system you actually use and shape the rest like it. |
| `_Agents/memory/credentials.md` · `connectors.md` · `projects.md` | Example rows only. **Locations only, never values.** |
| `_Docs/Skill Exports.md` | One example destination row (`your-org/skills-marketplace`). Replace it the first time you publish somewhere, or delete it. |

## Known gap

`_Docs/Skills Repo.md` → *Related knowledge bases* points at `_Agents/memory/git-and-tickets.md`, which
this template does not ship. Either create that memory file for your git host and tracker, or change
the pointer to `_Agents/memory/environment.md`.

## Machine paths never belong in a skill

Once you're past setup, the rule that keeps this from recurring: a skill describes *how*;
`_Agents/memory/` holds *what is true about this environment*. A literal path inside a skill breaks on
your other machine and rots without telling you. `vault-doctor` has a `hardcoded-machine-path` check for
exactly this — extend its pattern in `_Agents/scripts/check_vault.py` to match your own home directory
shapes, or it will only catch the ones the template shipped with.
