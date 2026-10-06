---
title: "How I want agents to work"
description: "Standing instructions for how agents work: evidence, decide vs ask, reporting, testing, and git."
---

# How I want agents to work

## Agent memory

Standing instructions, not suggestions. **Replace these with your own** — the value of this file is that
it records corrections you've actually had to make, so they only get made once.

## Operating model and verification

Moved here on 2026-10-06 from `_Agents/docs/operating-model.md` and `_Agents/docs/verification.md`, one
page for each section.

How agents are meant to work across this vault. [`README.md`](../../../README.md#set-up) covers *where*
each harness reads from; these pages cover *how* to behave once loaded.

The short version: **one brain, many disposable agents.** The vault is the memory. Agents are not.

How an agent knows it's done: the verification pages (the rule, evidence, testing, reporting) say how
to earn a claim; the operating-model pages say how to gather context.

**"It should work" is not a result.** Neither is "the code looks correct."

```okf-view
kind: pages
under: _Agents/memory/working-preferences/
as: list
describe: description
```

<!-- okf-view:snapshot (generated: do not edit, recomputed on save) -->
- [Before saying it's done](<Before saying it is done.md>) - Checklist: it ran, the failure case was tried, scale and re-run risks are named, numbers came from output, skips are stated.
- [Browser testing](<Browser testing.md>) - For user-visible behavior, load the real page with the playwright-testing skill; reading source is not a test.
- [Chats are disposable](<Chats are disposable.md>) - A new chat loses nothing that was written down, so write durable facts to memory when you learn them.
- [Comment, don't edit](<Comment, don't edit.md>) - To propose a change to a ticket, add a comment and keep the original text; do not rewrite the ticket description.
- [Concise — and no AI-slop](<Concise — and no AI-slop.md>) - Write each fact one time in plain words, with no preamble or extra advice, but keep every detail that changes an outcome.
- [Connectors are peers, not memory](<Connectors are peers, not memory.md>) - Memory holds how systems connect and costly gotchas; ticket status, counts, and live state come from the connector, never memory.
- [Decide vs ask](<Decide vs ask.md>) - Decide when a choice is reversible, conventional, or answerable from the repo; ask when it is irreversible, expensive, or a matter of taste.
- [Each skill exists once](<Each skill exists once.md>) - Personal skills are only in the vault and team skills are only in the team repo; never copy a skill from one to the other.
- [Every claim traces to evidence](<Every claim traces to evidence.md>) - Each claim in a deliverable must trace to a command output, merged PR, ticket, query result, email, or the user's own words.
- [Fetch context before asking](<Fetch context before asking.md>) - Before you ask the user, search the vault, then prior sessions, then connectors; asking with those unchecked wastes the user's time.
- [Git and shipping](<Git and shipping.md>) - Always open a PR and never commit or push directly to main; you can merge your own PR on a solo repo.
- [Load context precisely](<Load context precisely.md>) - Open only the skill, memory, or note the request needs; load machine and credential memory only for actions that need them.
- [One brain, no hierarchy](<One brain, no hierarchy.md>) - Every agent reads the same vault; delegate bounded, testable work to smaller models and use subagents for parallel work, not to hold context.
- [Prod writes](<Prod writes.md>) - The user runs production DDL; give the user copy-paste SQL, then verify the change with a SELECT.
- [Reporting](Reporting.md) - Report what actually happened, show failed test output, name skipped steps, and do not trust a tool or subagent summary without a check.
- [Reporting results](<Reporting results.md>) - State what happened, show failing output, name skipped steps, and never trust a subagent's all-clean summary without checking.
- [Skills live here, not in a harness](<Skills live in the vault.md>) - Write skills in the vault's skill folders, which every harness reads, never in one harness's private folder.
- [Structure exists to make retrieval cheap](<Structure makes retrieval cheap.md>) - Tags, templates, folder boundaries, and indexes let an agent fetch only what a task needs; keep one home for each fact.
- [Test design](<Test design.md>) - Write the smallest set of tests that covers each use case, failure mode, and edge case once, at the lowest reliable level.
- [Test the thing, not a model of the thing](<Test the real system.md>) - Test against the real system and real data shape, name scale-only risks, and run idempotent or scheduled scripts twice.
- [Testing checklists](<Testing checklists.md>) - Hand-off checklists for human testers: shortest set, numbered navigation, action, and verification steps per feature.
- [Verify before reporting](<Verify before reporting.md>) - A finished task is a claim that needs evidence; it should work is not a result.
- [Verify; never fabricate](<Verify; never fabricate.md>) - Every claim in a deliverable must come from a PR, ticket, email, command output, or the user; never invent counts or metrics.
- [What counts as evidence](<What counts as evidence.md>) - Strong, weak, and non-evidence: output you ran beats tests that exist, which beats this should pass; real counts beat estimates.
- [Worktrees, ports, and the other agents you can't see](<Worktrees, ports, and the other agents you can't see.md>) - Rules for parallel agents: keep the primary clone on main, use one worktree per branch, check port owners, and remove worktrees at merge.
- [Writing about code](<Writing about code.md>) - How to write PR bodies, review comments, and commit messages: say what changed and why first, keep key numbers and caveats, cut the audit trail.
<!-- /okf-view:snapshot -->
