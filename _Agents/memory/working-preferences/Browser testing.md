---
type: memory
title: "Browser testing"
description: "For user-visible behavior, load the real page with the playwright-testing skill; reading source is not a test."
updated: 2026-10-06
---

# Browser testing

Warranted when the thing being changed is user-visible behavior — uploads, downloads, forms,
navigation, responsive layout, or a multi-step flow. Reading the source is not a substitute for
loading the page.

The executable arm is the **`playwright-testing`** skill: reusable tests that live in the repo, not
one-off manual clicks. Platform-specific auth and iframe constraints are in
[`Spaces/Work/memory/connectors/`](../../../Spaces/Work/memory/connectors/index.md) — check it before concluding an app can't be tested.
