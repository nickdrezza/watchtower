---
type: memory
title: "What counts as evidence"
description: "Strong, weak, and non-evidence: output you ran beats tests that exist, which beats this should pass; real counts beat estimates."
updated: 2026-10-06
---

# What counts as evidence

| Strong | Weak | Not evidence |
|---|---|---|
| Command output you ran and read | "The tests exist" | "This should pass" |
| A row count from the actual query | A count from a similar query | An estimated count |
| A merged PR / a ticket transition | An open PR | An intention to open one |
| A screenshot or DOM read of the real page | The component's source | The component's props |

**Numbers earn trust.** "397 of 404 rows" convinces in one line where prose takes five — see
[*Writing about code*](<Writing about code.md>).
