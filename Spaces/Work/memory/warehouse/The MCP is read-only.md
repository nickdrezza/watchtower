---
type: memory
title: "⚠️ The MCP is read-only"
description: "The warehouse connector cannot run DDL; give the user SQL to run in the console, then use a SELECT to verify the change."
updated: 2026-08-05
tags:
  - ACME
---

# ⚠️ The MCP is read-only


The warehouse connector cannot run DDL. This is deliberate, not a misconfiguration.

**To change schema:** hand the user copy-paste SQL for the console, then verify with a `SELECT`. Don't
try to route around it, and don't report the change as done until the `SELECT` confirms it.
