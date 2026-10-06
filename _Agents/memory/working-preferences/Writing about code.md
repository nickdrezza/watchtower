---
type: memory
title: "Writing about code"
description: "How to write PR bodies, review comments, and commit messages: say what changed and why first, keep key numbers and caveats, cut the audit trail."
updated: 2026-08-05
---

# Writing about code


Applies to PR bodies, review comments, commit messages, and how work is reported back in chat.

- **Functional and plain.** A PR body should read in a minute.
- **Lead with what changed and why it matters** — not the investigation that got you there.
- **Keep the numbers that earn trust.** "397 of 404 rows" convinces in one line where prose takes five.
- **Cut the audit trail.** Which greps ran, every candidate eliminated: not valuable. If it mattered
  it's a finding; if it didn't, drop it.
- **Caveats stay in, short.** "Not tested against a real timeout" is one line and must survive.
