---
type: memory
title: "Example — Customer region fan-out fix"
description: "Example project note: fix the DIM_CUSTOMER region grain at the dimension, not with DISTINCT; shows the shape a project note must have."
updated: 2026-08-05
tags:
  - ACME
---

# Example — Customer region fan-out fix


- **Status:** in progress, as of 2026-01-15.
- **Ticket:** `PROJ-142`. **Repo:** `acme-analytics/warehouse-project`, branch `fix/customer-region`.
- **Problem:** `DIM_CUSTOMER` is one row per customer *per region*; three downstream marts join it
  without the region key and inflate their counts.
- **Decision:** fix the grain at the dimension, not with `DISTINCT` downstream — a structural fix, not
  a patch. See [`warehouse/`](../warehouse/index.md).
- **Next:** the third mart still needs the join corrected; the first two are merged.
- **Open question:** whether the legacy export keys on the old hash or the resolved id. Unresolved —
  do not assume either.

Replace this with your own. Keep the shape: status + date, ticket and repo, the problem, the decision
and its reason, what's next, and anything genuinely unresolved.
