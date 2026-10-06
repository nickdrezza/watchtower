---
type: memory
title: "Connectors are peers, not memory"
description: "Memory holds how systems connect and costly gotchas; ticket status, counts, and live state come from the connector, never memory."
updated: 2026-10-06
---

# Connectors are peers, not memory

| Kind of fact | Source of truth |
|---|---|
| How a system connects, where a credential lives, a gotcha that cost hours | [`_Agents/memory/`](../README.md) |
| Ticket status, row counts, what shipped this week, who's on call | The connector — query it |

**Never cache live state into memory.** A ticket status written into a memory file is wrong within
days and will be believed anyway. Full routing and per-connector limits:
[`Spaces/Work/memory/connectors/`](../../../Spaces/Work/memory/connectors/index.md).
