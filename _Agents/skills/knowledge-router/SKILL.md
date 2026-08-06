---
name: knowledge-router
description: >
  Decides WHICH knowledge base to use for a question or task, so an agent can reference your
  personal repo ("the vault" — his vault plus the agent skills and memory that run his work) and
  the Acme team shared-vault seamlessly without mixing them up. Use at the START of any task that
  involves reading or writing notes/docs/knowledge — especially when it's unclear whether something is
  personal vs team, or where a piece of knowledge should live. Trigger phrases: "where does this go",
  "check my notes / the wiki", "how does X work", "add this to my knowledge base", "is this personal
  or team", "document this". Routes to watchtower, shared-vault-read, or shared-vault-promote.
---

# Knowledge router

Two separate knowledge bases. They stay separate; this skill picks the right one and hands off.

| Knowledge base | What it is | Repo | Defer to |
|---|---|---|---|
| **the vault** | your *personal* repo: the Obsidian vault (work context, projects, meeting/interview notes, work logs, career, personal) **plus** `_Agents/` — the skills and the operational memory his agents run on (environment, credential locations, per-platform connect guides). Holds PII, comp material, and Acme internals. | `<you>/<your-vault>` (private) | `watchtower` skill |
| **shared-vault** | The Acme *team* knowledge base — how systems work, runbooks, policies, ADRs, incidents, guides. Team audience, no PII. | `acme-analytics/shared-vault` (private team repo) | `shared-vault-read` to read it; `shared-vault-promote` to write into it |

Clone paths differ per machine — `_Agents/memory/environment.md` and `git-and-tickets.md` have the
current ones. Don't assume either path from an older doc.

> The personal skills repo `<you>/skills` was **merged into the vault** in July 2026.
> Skills now live at `_Agents/skills/` inside this repo; treat the old repo as archived. "How do I
> write/install a skill" → `_Agents/CONVENTIONS.md` + `_Agents/README.md`.

## How to route

Match the request to a destination:

- **Personal / career / "my" anything** → vault. ("my project notes", "my interviews", "my
  raise doc", "organize these notes", "what was I working on").
- **"How does X work / why did we decide Y / what broke / runbook / team policy / onboarding"** →
  shared-vault. This is team-owned "how we build and operate" knowledge.
- **Acme *work context* that's personal to the user** (his planning, his daily logs, his take on
  a project) → vault. The *shared* explanation of the same system → shared-vault.
- **"How do I connect to X / where do the credentials live / how do I run Y here"** → vault
  `_Agents/memory/` first — it's written for agents and covers this machine and every connector. Then
  the shared vault for the team-facing explanation of the *system*. If they disagree about a **system**,
  the shared vault wins; if they disagree about **this machine**, memory wins (it's the more specific
  claim). Either way, verify.
- **"How do I write/install a skill"** → `_Agents/CONVENTIONS.md` in the vault.
- **A raw dump that's a mix** → default to vault `Inbox/Processed/`; promote team-relevant,
  non-personal pieces to the shared vault *as a separate step the user approves*.
- **"Should the team know this / put this in the dev wiki / what's undocumented"** →
  `shared-vault-promote`. It owns the promotion path: what's worth carrying across, what must be
  stripped first, and the flag-it-with-him loop. Don't hand-roll a wiki write.

When a task spans both (e.g. "log my work AND document the new pipeline for the team"), do the
personal part in the vault and the team part in the shared vault as **two distinct writes** — never
one note that lives in both.

## Hard boundary (non-negotiable)

**vault content is never copied into the team shared-vault.** It holds PII, interview notes,
salary/comp material, and Acme internals. Cross-reference by pointer ("see personal notes"), never
by paste. The reverse is fine: the vault may link to or quote public-to-team shared-vault content.

Note the one nuance: the shared vault has a per-person scratch area `notebooks/<you>/` for
personal-but-team-relevant WIP thinking. Personal-and-team-relevant → that notebook is OK.
Personal-and-private → vault only.

## Related skills

- `watchtower` — operating rules for the personal repo (load it first, always).
- `vault-memory` — refresh `_Agents/memory/` from local AI-platform history + GitHub/the tracker/email/Drive.
- `vault-sync` — the single entry point that runs the whole refresh and ships it.
- `shared-vault-read` — operating rules for the team wiki (separate, team-managed skill). Its pre-flight
  reports `NO_TOKEN`; **don't create a PAT** — `_Agents/memory/git-and-tickets.md` has the working
  access path and the PR-not-push flow.
- `shared-vault-promote` — the *write* direction: deciding what in the vault the team should have,
  sanitizing it, asking before asserting, and shipping it as a PR. Enforces the boundary above rather
  than restating it.
