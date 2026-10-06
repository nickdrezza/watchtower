---
type: memory
title: "Credentials — where they live: Rules"
description: "Credential rules: inject secrets as env vars, never echo a token, filter values out of list output, and record each rotation date."
updated: 2026-08-05
tags:
  - ACME
---

# Credentials — where they live: Rules


1. **Prefer injection over retrieval.** Hand a secret to a child process as an env var rather than
   printing it. Most secret CLIs have a `run --` form for exactly this.
2. **Never echo a token**, not even to confirm it loaded. Check exit status instead.
3. **Some list commands print values in every output format** — project them away in the same pipe
   before anything reaches the terminal.
4. **Record rotation obligations here.** A token with an expiry nobody wrote down is an outage waiting.
