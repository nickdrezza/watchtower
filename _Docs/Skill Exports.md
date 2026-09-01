---
type: documentation
status: active
domain: system
workspace: vault
tags:
  - "topic/agents"
related:
  - "[[Skills Repo]]"
  - "[[Agent Memory]]"
---

# Skill Exports

Which skills have been published from this vault to an external destination, in what shape, and from
which revision. Maintained by `skills-sync`: the registry says where destinations are and how they're
formatted; the ledger says what has gone and lets it compute drift.

Empty in a fresh vault. Add a registry row the first time you publish somewhere.

## The vault is the source

Authored here, published there; a destination copy is a build artifact, and `AGENTS.md` → *Context
loading* makes the vault's copy the one agents invoke. Edit a destination copy directly and the two
have forked with nothing detecting it — hence the drift check, and hence recording a deliberate fork
rather than silently re-clobbering it on the next export.

## Destination registry

| Destination | Repo | Adapter | Reviewer | Notes |
|---|---|---|---|---|
| *example* | `your-org/skills-marketplace` | **A — Claude Code plugin marketplace** (`skills-sync/reference.md`) | whoever merges | If the repo auto-syncs to everyone's client, **merging deploys** — the PR review is the only gate. Note any per-plugin review rules and any vendored skills that must be fixed upstream. |

Clone paths are per-machine — `_Agents/memory/machines/<target>.md`, routed by `environment.md`.

## Ledger

| Date | Skill | Destination | Decision | PR | Source SHA | Note |
|---|---|---|---|---|---|---|

Column meanings and the row spec: `_Agents/skills/skills-sync/reference.md` → *Ledger row*.

## Known shadowing

Skills offered under both the unprefixed name and a `plugin:skill` one, because a copy published from
here came back as an installed plugin. Which copy answers is settled — `AGENTS.md` → *Context loading*
makes it the vault's — so the local copies **stay**. They still drift, and only `skills-sync`'s drift
check surfaces it.

List them here as you publish, so the drift check has something to compare against.
