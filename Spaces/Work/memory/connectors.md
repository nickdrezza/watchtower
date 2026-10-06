---
tags:
  - ACME
---

# Connectors — what's available, what each owns, where each lies

The routing index for live systems. **Memory holds durable facts; connectors hold live state.** This
file says which connector answers what, and the limit that will bite you.

## Check availability before planning around one

**Connectors drop in and out**, and which are loaded differs per session and per harness. Confirm what
you have before building a plan on it. A missing connector is not evidence a system is unreachable, and
a present one is not evidence it can write.

## Who owns what

| Question | Ask | Not |
|---|---|---|
| Ticket status, sprint, assignee | The tracker | memory, which ages within days |
| What actually shipped | The git CLI — merged PRs | a project note's status line |
| Row counts, data truth | The warehouse | any number written down anywhere |
| Contacts, lists, campaign state | The CRM | the warehouse's copy, which lags |
| Requests, decisions, constraints | Email | recollection |
| What a past chat decided | The session-history MCP | asking the user again |
| How to connect, where a credential lives, a gotcha | **memory** — never a connector | — |

## Known limits — fill in yours

| Connector | Limit |
|---|---|
| Warehouse | **Read-only.** DDL goes through the console — see [`warehouse.md`](warehouse.md) |
| Tracker | Large multi-issue queries blow the token budget; request only the fields you need, in small batches |
| Docs/Drive | Often cannot edit in place — each revision may be a new document and URL |
| Spreadsheets | A sheet not shared with the service account fails in a way that looks like a code bug |

## Session history — the cross-chat source

The one connector that makes chats disposable. Use it before asking the user to re-explain anything.

| Harness | Where |
|---|---|
| Claude Code | The session-management MCP — list sessions, search transcripts. Plus its own per-project `memory/` store, which is already-distilled facts |
| Codex | `<codex-home>/session_index.jsonl`, `sessions/`, `memories/` — read the index first, filter by date |

Paths are per-machine — [`machines/`](../../../_Agents/memory/machines/README.md). **If you work on more than one machine, each
holds its own history and you can only see the one you're on** — say which you covered rather than
implying full coverage.

## Rules

1. **Never cache live state into memory.** A ticket status written here is wrong within days and will be
   believed anyway. Record the *mechanism*, not the reading.
2. **A connector answer beats a written one** for anything live. Memory wins only for environment facts.
3. **Business-side actions are the user's.** Say so plainly and ask; don't engineer around them.
