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
[`<you>/skills`](https://github.com/<you>/skills) (clone at `~/Linux Dev/skills` in WSL).
In July 2026 that repo was merged into the vault so one repo carries both the knowledge and the
skills that operate on it. Treat the old repo as archived.

Canonical location: **`.agents/`** — a dot-directory, so Obsidian ignores it completely while every
coding agent can read it. Its own map is `.agents/README.md`.

## Why merge them

The goal is a one-stop shop: load Claude Code, Codex, Cursor, Gemini CLI, or Copilot on this repo
and each one behaves the same. Two repos meant an agent could know how to do something in one place
and not the other — and skills that describe the vault drifted from the vault's own governance. One
repo, one `AGENTS.md`, one skills path.

## The division of labor

- **Skill *behavior* lives in `.agents/skills/`.** How an AI should read/write the vault, route a
  question, run a catch-up, write the weekly log, SSH the EC2 box — that's a skill.
- **Environment *facts* live in `.agents/memory/`.** Which shell has the SSH key, where a credential
  lives, which the warehouse role to use, what a table's grain is. A skill that hard-codes an account id or
  a path is doing memory's job. See [[Agent Memory]].
- **Vault *content and governance* live in the vault half.** The notes themselves, plus the
  authoritative rules in `AGENTS.md` and `_Docs/`. The skills distill these; if they ever disagree,
  the vault's own governance wins.

## Layout

```text
.agents/
  README.md                 map of the agent layer
  CONVENTIONS.md            the SKILL.md authoring spec + pre-commit checklist
  memory/                   operational memory — see [[Agent Memory]]
  skills/<name>/SKILL.md    the skills (+ optional reference.md, scripts/)
  docs/platforms.md         per-tool path matrix
  docs/portability.md       the portability model
  templates/skill-template/ starter SKILL.md
  scripts/new-skill.sh      scaffold a new skill
  scripts/install-skills.sh deploy to ~/.agents/skills or ./.claude/skills
```

Repo root: `AGENTS.md` is authoritative for all agents; `CLAUDE.md`, `GEMINI.md`, and
`.github/copilot-instructions.md` are stubs pointing at it.

## How it ships

`.agents/skills/` **is** the universal project-level location — Codex, Cursor, Gemini CLI, Copilot,
and Antigravity read it natively with no setup when opened on this repo. Claude Code reads
`.claude/skills/`, so mirror once:

```bash
.agents/scripts/install-skills.sh --here      # -> ./.claude/skills (gitignored copy)
.agents/scripts/install-skills.sh             # or global: ~/.agents/skills + ~/.claude/skills
```

Same `SKILL.md` read byte-for-byte by every tool — no per-tool conversion. And if a harness discovers
nothing, an agent can simply read `.agents/skills/<name>/SKILL.md`; `AGENTS.md` says so explicitly.

## The skills

| Skill | What it does |
|---|---|
| `watchtower` | **The primary context. Load it first, every session.** Layout, hard rules, how to write here, the employer-scope tag, the memory index. |
| `bootstrap` | Sets up a new user or machine, seeds the memory maps, and teaches the operating model. |
| `vault-memory` | Refreshes `.agents/memory/` from prior sessions and your connectors. |
| `vault-sync` | Pull → refresh → commit → PR → merge → concise summary. The single entry point for "sync my vault". |
| `vault-doctor` | Mechanical integrity checks — links, tags, frontmatter, skill-index drift, stale mirror. Read-only, script-backed. |
| `vault-prune` | Quality pass — slop, near-duplicates, bloat, stale claims, orphans, gaps. Per-item approval; never deletes unasked. |
| `vault-edit` | Safe create / move / rename / merge / split / archive / delete, and what must move with the file. |
| `knowledge-router` | Decides which knowledge base owns a task — this vault or the team's shared one. |
| `shared-vault-sync` | Both directions with the team vault in one command, drift check first. |
| `shared-vault-promote` | Outbound: what the team should have, rewritten for a team audience and stripped of anything private. |
| `shared-vault-ingest` | Inbound: indexes the team vault and absorbs its gotchas and constraints into memory. Never copies it. |
| `secrets` | Get, store, rotate, and inject credentials. **Never surfaces a value.** |
| `playwright-testing` | Real-browser tests for user-visible behavior — uploads, downloads, forms, navigation, responsive layout. |
| `personal-vault` | The front door for personal material; routes to the right section. |
| `personal-memory` | Past events, milestones, and life-history notes. |
| `personal-reflection` | Opinions, values, identity questions, and rambles. |
| `personal-entities` | People, pet, and location notes, and the links to them. |
| `personal-triage` | Classifies personal material staged in Uncategorized. |
| `diary` | Lightly cleaned daily entries that preserve your voice. |

## The `#ACME` convention

Anything only meaningful while I'm at Acme Analytics carries `ACME` in its frontmatter `tags:` —
Acme projects, tickets, systems, people, work logs, client/event material, and the employer-specific
memory files. Portable material (this machine's setup, agent conventions, personal and career notes)
stays untagged. The point: one query can sweep the non-reusable content into an archive if I change
jobs, and the rest of the vault survives intact. Agents set this when they create or substantially edit
a file.

## Related knowledge bases

- **shared-vault** (team repo `Acme-Healthcare/shared-vault`; clone path per machine in
  `.agents/memory/git-and-tickets.md`) — the Acme team "how it works" wiki. Kept fully separate.
  `knowledge-router` decides which repo a task belongs to; `shared-vault-promote` carries material
  across when it should travel. Team-relevant, non-personal material goes there (or its
  `notebooks/<you>/` scratch), never private vault content from here — and never as a paste.
  Every call is logged in Shared Vault Promotions.
