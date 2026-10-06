---
type: memory
title: "Connectors — what's available, what each owns, where each lies: Rules"
description: "Three connector rules: do not write live state into memory, a live connector answer wins, and business-side actions belong to the user."
updated: 2026-08-05
tags:
  - ACME
---

# Connectors — what's available, what each owns, where each lies: Rules


1. **Never cache live state into memory.** A ticket status written here is wrong within days and will be
   believed anyway. Record the *mechanism*, not the reading.
2. **A connector answer beats a written one** for anything live. Memory wins only for environment facts.
3. **Business-side actions are the user's.** Say so plainly and ask; don't engineer around them.
