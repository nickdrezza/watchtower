---
type: memory
title: "Test the thing, not a model of the thing"
description: "Test against the real system and real data shape, name scale-only risks, and run idempotent or scheduled scripts twice."
updated: 2026-10-06
---

# Test the thing, not a model of the thing

- **Prefer the real system over a mock.** A mock proves your mock works.
- **Prefer the real data shape.** Empty and single-row cases pass almost anything.
- **Scale-only bugs slip past small supervised tests.** This is a lesson already paid for — the
  the enrichment vendor `personIds` cap only showed up above the tested batch size
  ([`Spaces/Work/memory/warehouse/`](../../../Spaces/Work/memory/warehouse/index.md)). If behavior can change with volume,
  concurrency, or time, say so explicitly rather than implying the small run generalizes.
- **Run it twice** when a script is meant to be idempotent or scheduled. Most re-run bugs are invisible
  on the first pass.
