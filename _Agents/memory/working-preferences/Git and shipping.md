---
type: memory
title: "Git and shipping"
description: "Always open a PR and never commit or push directly to main; you can merge your own PR on a solo repo."
updated: 2026-08-05
---

# Git and shipping


**Always open a PR. Never commit or push straight to `main`.** Branch → commit → push → open the PR.
Self-merging on a solo repo is expected; skipping the PR is not.

**Exception — this vault:** agents open the PR and the user merges it. Only a routine `vault-sync` (memory and work logs only, CI green) merges its own PR. See `AGENTS.md` → "Write to the vault".
