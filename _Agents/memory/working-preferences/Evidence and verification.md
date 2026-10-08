---
type: memory
title: "Evidence and verification"
description: "Each claim in a deliverable must trace to evidence that you ran or read. This page tells what is evidence and what to check before you say that a task is done."
updated: 2026-10-06
---

# Evidence and verification

This page joins 5 pages that had the same subject. Each section keeps the words of its source page.

## Verify; never fabricate


Every claim in a deliverable traces to a merged PR, a ticket, an email, a command's output, or my own
words. **Never invent specifics** — row counts, metrics, meetings, or "plan pending" work with no
evidence behind it.

## Every claim traces to evidence

Every claim in a deliverable traces to something checkable — a command's output, a merged PR, a
ticket, a query result, an email, or his own words. This is the standing instruction in
[*Verify; never fabricate*](#verify-never-fabricate);
it has gotten work rejected before.

## What counts as evidence

| Strong | Weak | Not evidence |
|---|---|---|
| Command output you ran and read | "The tests exist" | "This should pass" |
| A row count from the actual query | A count from a similar query | An estimated count |
| A merged PR / a ticket transition | An open PR | An intention to open one |
| A screenshot or DOM read of the real page | The component's source | The component's props |

**Numbers earn trust.** "397 of 404 rows" convinces in one line where prose takes five — see
[*Writing about code*](<Writing about code.md>).

## Verify before reporting

Finishing is a claim, and claims need evidence. [*What counts as evidence*](#what-counts-as-evidence) and the pages next to it have the doctrine;
the short form is that "it should work" is not a result.

## Before saying it's done

- [ ] The thing was actually run, not just written.
- [ ] The failure case was tried, not only the happy path.
- [ ] Anything that could differ at scale, on a re-run, or on another machine is named.
- [ ] Numbers in the report came from output you read, not from inference.
- [ ] Steps you skipped are stated as skipped.
