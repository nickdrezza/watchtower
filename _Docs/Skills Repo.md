---
type: documentation
status: active
domain: system
workspace: vault
tags:
  - "topic/agents"
related:
  - "[[Home]]"
  - "[[Vault Architecture]]"
  - "[[AI Note Intake Workflow]]"
  - "[[Vault Maintenance]]"
  - "[[Agent Memory]]"
---

# Skills Repo

**The skills now live in this repo.** They used to be a separate private repo,
[`<you>/skills`](https://github.com/<you>/skills). That repo was merged into the vault so one repo
carries both the knowledge and the skills that operate on it. Treat the old repo as archived.

Canonical location: **`_Agents/`**, with a `.agents` symlink beside it so every coding agent finds
the universal path. Its own map is `_Agents/README.md`.

## Why merge them

The goal is a one-stop shop: load Claude Code, Codex, Cursor, Gemini CLI, or Copilot on this repo
and each one behaves the same. Two repos meant an agent could know how to do something in one place
and not the other — and skills that describe the vault drifted from the vault's own governance. One
repo, one `AGENTS.md`, one skills path.

## The division of labor

- **Skill *behavior* lives in `_Agents/skills/`.** How an AI should read/write the vault, route a
  question, run a catch-up, write the weekly log, SSH a server — that's a skill.
- **Environment *facts* live in `_Agents/memory/`.** Which shell has the SSH key, where a credential
  lives, which warehouse role to use, what a table's grain is. A skill that hard-codes an account id or
  a path is doing memory's job. See [[Agent Memory]].
- **Vault *content and governance* live in the vault half.** The notes themselves, plus the
  authoritative rules in `AGENTS.md` and `_Docs/`. The skills distill these; if they ever disagree,
  the vault's own governance wins.

## Layout

```text
_Agents/
  README.md                 map of the agent layer
  CONVENTIONS.md            the SKILL.md authoring spec + pre-commit checklist
  memory/                   operational memory — see [[Agent Memory]]
  skills/<name>/SKILL.md    the skills (+ optional reference.md, scripts/)
  docs/platforms.md         per-tool path matrix
  docs/portability.md       the portability model
  templates/skill-template/ starter SKILL.md
  wt                        search · doctor · install · index
```

Repo root: `AGENTS.md` is authoritative for all agents; `CLAUDE.md`, `GEMINI.md`, and
`.github/copilot-instructions.md` are stubs pointing at it.

## How it ships

`_Agents/skills/` **is** the universal project-level location — Codex, Cursor, Gemini CLI, Copilot,
and Antigravity read it natively with no setup when opened on this repo. Claude Code reads
`.claude/skills/`, so link once:

```bash
_Agents/wt install          # one link per skill in ~/.agents/skills and ~/.claude/skills
_Agents/wt install --copy   # copies instead of links, across a Windows↔WSL boundary
```

Same `SKILL.md` read byte-for-byte by every tool — no per-tool conversion. And if a harness discovers
nothing, an agent can simply read `_Agents/skills/<name>/SKILL.md`; `AGENTS.md` says so explicitly.

## The skills

**The index is `_Agents/README.md`** — one table, one place to update. It used to be duplicated here and
in the `watchtower` skill; `vault-doctor` now checks only the one.

`vault-sync` is the entry point to the **vault family** — it calls `weekly-work-log` and `vault-memory`,
so "sync my vault" brings the log, the memory directory, and the remote current in one pass.

Marketplace and plugin skills are deliberately **not** copied in here — they're managed by their
marketplaces and would go stale. If you publish skills *out* to one, `skills-sync` owns that direction
and [Skill Exports](Skill%20Exports.md) is its ledger.

## The `#ACME` convention

Anything only meaningful while I'm at Acme Analytics carries `ACME` in its frontmatter `tags:` —
Acme projects, tickets, systems, people, work logs, client/event material, and the employer-specific
memory files. Portable material (this machine's setup, agent conventions, personal and career notes)
stays untagged. The point: one query can sweep the non-reusable content into an archive if I change
jobs, and the rest of the vault survives intact. Agents set this when they create or substantially edit
a file.

## Related knowledge bases

- **shared-vault** (team repo `Acme/shared-vault`; clone path per machine in
  `_Agents/memory/git-and-tickets.md`) — the Acme team "how it works" wiki. Kept fully separate.
  `knowledge-router` decides which repo a task belongs to; `shared-vault-promote` carries material
  across when it should travel. Team-relevant, non-personal material goes there (or its
  `notebooks/<you>/` scratch), never private vault content from here — and never as a paste.
  Every call is logged in Shared Vault Promotions.
