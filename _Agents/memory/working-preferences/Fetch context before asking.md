---
type: memory
title: "Fetch context before asking"
description: "Before you ask the user, search the vault, then prior sessions, then connectors; asking with those unchecked wastes the user's time."
updated: 2026-10-06
---

# Fetch context before asking

**Search prior sessions before making the user re-explain anything.** Most questions about what was
decided, tried, or already solved are answerable from history.

Cheapest first:

1. **This vault** — [`_Agents/memory/`](../README.md), then the relevant note.
2. **Prior sessions, across chats** — the session-mgmt MCP (`list_sessions`,
   `search_session_transcripts`) for Claude Code; `<codex-home>/session_index.jsonl` for Codex. Paths
   per machine: [`_Agents/memory/machines/`](../machines/index.md).
3. **Connectors** — [`Spaces/Work/memory/connectors/`](../../../Spaces/Work/memory/connectors/index.md) says which one is
   authoritative for what, and where each one lies to you.
4. **Ask him.**

Reaching step 4 with 1–3 unattempted is the most common way to waste his time.
