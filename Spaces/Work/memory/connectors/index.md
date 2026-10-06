---
title: "Connectors — what's available, what each owns, where each lies"
tags:
  - ACME
---

# Connectors — what's available, what each owns, where each lies

## Agent memory

The routing index for live systems. **Memory holds durable facts; connectors hold live state.** This
file says which connector answers what, and the limit that will bite you.

```okf-view
kind: pages
under: Spaces/Work/memory/connectors/
as: list
describe: description
```

<!-- okf-view:snapshot (generated: do not edit, recomputed on save) -->
- [Check availability before planning around one](<Check availability before planning around one.md>) - Connectors change per session and harness, so confirm which ones you have before you make a plan that uses one.
- [Connectors — what's available, what each owns, where each lies: Rules](Rules.md) - Three connector rules: do not write live state into memory, a live connector answer wins, and business-side actions belong to the user.
- [Known limits — fill in yours](<Known limits.md>) - Table of known connector limits: the warehouse is read-only, tracker queries hit token limits, docs make new copies, unshared sheets fail.
- [Session history — the cross-chat source](<Session history.md>) - Use the session-history connector to find what past chats decided before you ask the user again; each machine has only its own history.
- [Who owns what](<Who owns what.md>) - Table that tells which source to ask for each type of question, for example the tracker for ticket status and git for what shipped.
<!-- /okf-view:snapshot -->
