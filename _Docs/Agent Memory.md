---
type: documentation
status: active
domain: system
workspace: vault
tags:
  - "topic/agents"
related:
  - "[[Home]]"
  - "[[Skills Repo]]"
  - "[[Vault Architecture]]"
---

# Agent Memory

the vault carries an **operational memory layer** for AI agents at **`_Agents/memory/`**. It is the
answer to "why does my agent know how to connect to the warehouse in one session and not the next" — the
facts live in the repo instead of in whichever tool happened to be configured.

**Obsidian indexes it**, because the folder has no leading dot — that is why it is `_Agents/` and not
`.agents/`. A committed `.agents` symlink points at it so every harness still finds the universal path
it auto-discovers. You can also read it in an editor, on
GitHub, or ask an agent. This note is the human-facing index.

Kept current by the **`vault-memory`** skill — it scans local AI-platform history (Claude Code sessions,
Codex sessions and its own memory store) plus the tracker, email, GitHub, and Drive meeting notes since memory
was last committed, proposes a candidate table, asks, then writes. `vault-sync` runs it as part of a
full sync.

## What's in it

| File | Covers |
|---|---|
| `README.md` | The index and the rules for writing memory. |
| `environment.md` | **Start here.** How to tell which target you're on, what's true on all of them, and what must be looked up per-machine. |
| `machines/` | One profile per target — paths, shells, installed tooling, and what's deliberately *not* installed. |
| `credentials.md` | The credential map — every key, token, and profile, what it authenticates, and **where it lives**. |
| `connectors.md` | The live systems — which connector is authoritative for what, the limit that will bite you, and where cross-chat session history lives. |
| `warehouse.md` | **The worked example of a platform file** — how to connect, the roles, the limit you'll hit, and the way around it. |
| `working-preferences.md` | Standing instructions — the PR rule, verify-don't-fabricate, comment-don't-edit. |
| `projects.md` | Active and recent work, one compact block each. |

**Add one file per platform you actually work in**, named for it, and a `people.md` once more than a
couple of names matter. `warehouse.md` is the shape to copy. The set ships small on purpose — a
pre-filled folder describing systems you don't use is worse than an empty one, because an agent
believes it.

## When it gets written

The folder's own `README.md` holds the rule. In short: **a single durable fact goes in the moment it's
learned** — appended to an existing file, locations-only, contradicting nothing — with no preview
needed. Everything larger (multi-fact runs, contradictions, pruning, new files) goes through
`vault-memory` and the normal verification preview. This is what makes a chat safe to throw away.

## Three rules

1. **Locations, never values.** A path, an env-var name, a your secret manager item name, a the warehouse user/role —
   yes, and that's the point. The secret itself — never, in any file in this repo.
2. **Point-in-time.** Environment facts (paths, accounts, which shell holds the SSH key) are stable.
   Facts about code and data drift — an agent should verify before asserting, and date anything that ages.
3. **`#ACME` on the employer-specific files.** All but `README.md`, `environment.md`,
   `working-preferences.md`, and the portable `machines/` profiles carry `ACME` in their frontmatter
   `tags:`, so the non-reusable material can be archived in one query if I change jobs. Those files mark
   their few Acme rows inline. A profile for a machine that exists only for work — a shared build or
   automation box — is fully tagged.

## Relationship to the vault's own notes

Memory is written **for agents**: terse, operational, "run this, watch for that." The vault's
`Concepts/` notes and `Spaces/Work/Current Work/Reference/` are written **for you**. They can
cover the same systems from different angles; neither replaces the other. Deep project narrative belongs
in `Projects/` notes and the tracker — `projects.md` holds only the pointer plus what's needed to resume.

See also [[Skills Repo]] for the skills half of `_Agents/`.
