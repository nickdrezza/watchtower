---
name: shared-vault-sync
description: >
  The single entry point for syncing the personal vault and the team shared-vault in both directions —
  checks for drift, pulls the wiki's new gotchas and decisions inbound, and proposes vault knowledge
  the team should have outbound. Use when the user says "sync the dev wiki", "sync both ways", "what's
  new in the wiki and what should I contribute", "is my vault in step with the team wiki", or wants a
  periodic two-way catch-up. Orchestrates shared-vault-ingest (inbound) and shared-vault-promote (outbound);
  for one direction only, call that skill directly.
tags:
  - ACME
user-invocable: true
argument-hint: "[in|out|drift]"
---

# Dev-wiki sync

Two knowledge bases, deliberately separate, connected by two one-way skills. This orchestrates them the
way `vault-sync` orchestrates the vault family — so "sync the wiki" is one instruction instead of three.

**This skill authors nothing.** Boundary, tests, ledgers, and provenance all belong to the two skills it
calls; duplicating any of it here is how they drift apart.

| Direction | Skill | Ships |
|---|---|---|
| **Drift** | this skill, step 1 | A report. No writes |
| **Inbound** — wiki → vault | `shared-vault-ingest` | Index rows, concept links, and gotchas into `.agents/memory/` |
| **Outbound** — vault → wiki | `shared-vault-promote` | A PR to the wiki, logged in `_Docs/Shared Vault Promotions.md` |

## The asymmetry — why material must be rewritten, not copied

The two bases are different *in kind*, not just in audience:

| | Personal vault | Team shared-vault |
|---|---|---|
| Character | Broad, exploratory, agent-first | Strict, documentation-heavy, human-first |
| Filed by | Space and subject | Document type — policy, guide, system, runbook, decision, incident |
| Holds | PII, planning, opinions, credential locations | Durable team documentation. **No PII** |

So nothing crosses by paste. Outbound, the *mechanism* is rewritten for a team audience and the
personal material is stripped. Inbound, the *constraint a doc imposes* is absorbed — never the prose.
`knowledge-router` owns the boundary; read it if a call is unclear.

**The wiki stays the source of truth for team-system facts.** The vault holds a pointer plus the
payload, never a mirror — it moves several times a week and a copy would be confidently wrong within a
quarter.

## 1. Drift check — always first

Cheap, read-only, and the reason this skill exists. A page promoted from the vault and then edited by
the team silently rots the memory that came from it.

```bash
git -C <wiki-clone> fetch origin --prune && git -C <wiki-clone> log --oneline -10 origin/main
```

Clone path is per-machine — `.agents/memory/git-and-tickets.md` and the `machines/` profile. Compare
`origin/main` against the watermark in `_Docs/Shared Vault Ingest.md`, then read the wiki's own
`CHANGELOG.md` for the fastest account of what actually changed.

Report three things and write nothing:

- **Commits since the watermark** — the inbound candidate set.
- **Vault claims now contradicted by the wiki.** Surface both verbatim and ask. The wiki wins on
  team-system facts and memory wins on this-machine facts, but a contradiction is a question for him,
  never an auto-overwrite.
- **Pages he authored that the team has since edited** — the rot case. Highest value in the whole check.

If the watermark equals `origin/main` and nothing is dirty, say so in one line and stop.

## 2. Inbound

Hand off to **`shared-vault-ingest`**. It picks the mode (backfill / incremental / targeted / drift-only),
runs its four tests per candidate fact, asks in one batch, and records provenance plus the watermark.

Incidents and ADRs are the highest-value inbound material — a post-mortem is nothing but the gotcha and
the reason, which is exactly this vault's retention test.

## 3. Outbound

Hand off to **`shared-vault-promote`**. Scan mode surfaces candidates the team should have; on-demand
mode writes up work just finished. It re-reads the wiki's live governing docs every time, because their
conventions drift.

Two things worth raising here rather than leaving to it:

- A `GAPS.md` entry the vault can now answer is the strongest outbound candidate there is — the team
  has explicitly asked.
- A previously-declined item whose conditions changed is worth re-raising. A decline is a judgement at a
  date, not a standing no.

## 4. Report

One block. Direction by direction, counts not narration:

```
Drift      watermark <sha> → origin/main <sha>, <n> commits · <n> contradictions · <n> rotted pages
Inbound    <n> absorbed, <n> indexed, <n> skipped — <memory files touched>
Outbound   <n> proposed, <n> shipped (PR #<n>), <n> declined
Open       <questions>
Skipped    <what you deliberately didn't sweep>
```

Both halves stop before committing the vault side — **`vault-sync` ships that.** The wiki side goes as
its own PR to the wiki repo. Never push to either `main`.

## Related

- `shared-vault-ingest` · `shared-vault-promote` — the two directions. All the real rules live there.
- `knowledge-router` — which base owns a topic, and which side wins a disagreement.
- `vault-sync` — commits and ships whatever the inbound half wrote.
