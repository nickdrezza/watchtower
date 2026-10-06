---
type: memory
title: "Session history — the cross-chat source"
description: "Use the session-history connector to find what past chats decided before you ask the user again; each machine has only its own history."
updated: 2026-10-06
tags:
  - ACME
---

# Session history — the cross-chat source


The one connector that makes chats disposable. Use it before asking the user to re-explain anything.

| Harness | Where |
|---|---|
| Claude Code | The session-management MCP — list sessions, search transcripts. Plus its own per-project `memory/` store, which is already-distilled facts |
| Codex | `<codex-home>/session_index.jsonl`, `sessions/`, `memories/` — read the index first, filter by date |

Paths are per-machine — [`machines/`](../../../../_Agents/memory/machines/index.md). **If you work on more than one machine, each
holds its own history and you can only see the one you're on** — say which you covered rather than
implying full coverage.
