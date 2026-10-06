---
title: "How I want agents to work"
---

# How I want agents to work

## Agent memory

Standing instructions, not suggestions. **Replace these with your own** — the value of this file is that
it records corrections you've actually had to make, so they only get made once.

```okf-view
kind: pages
under: _Agents/memory/working-preferences/
as: list
describe: description
```

<!-- okf-view:snapshot (generated: do not edit, recomputed on save) -->
- [Comment, don't edit](<Comment, don't edit.md>) - To propose a change to a ticket, add a comment and keep the original text; do not rewrite the ticket description.
- [Concise — and no AI-slop](<Concise — and no AI-slop.md>) - Write each fact one time in plain words, with no preamble or extra advice, but keep every detail that changes an outcome.
- [Each skill exists once](<Each skill exists once.md>) - Personal skills are only in the vault and team skills are only in the team repo; never copy a skill from one to the other.
- [Git and shipping](<Git and shipping.md>) - Always open a PR and never commit or push directly to main; you can merge your own PR on a solo repo.
- [Prod writes](<Prod writes.md>) - The user runs production DDL; give the user copy-paste SQL, then verify the change with a SELECT.
- [Reporting](Reporting.md) - Report what actually happened, show failed test output, name skipped steps, and do not trust a tool or subagent summary without a check.
- [Verify; never fabricate](<Verify; never fabricate.md>) - Every claim in a deliverable must come from a PR, ticket, email, command output, or the user; never invent counts or metrics.
- [Worktrees, ports, and the other agents you can't see](<Worktrees, ports, and the other agents you can't see.md>) - Rules for parallel agents: keep the primary clone on main, use one worktree per branch, check port owners, and remove worktrees at merge.
- [Writing about code](<Writing about code.md>) - How to write PR bodies, review comments, and commit messages: say what changed and why first, keep key numbers and caveats, cut the audit trail.
<!-- /okf-view:snapshot -->
