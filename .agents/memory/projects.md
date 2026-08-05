---
tags:
  - ACME
---

# Active projects

One compact block per project — enough for an agent to pick the work up, not a narrative. Deep history
belongs in the project note in `Spaces/`; this is the pointer.

**Keep it pruned.** A closed project's block gets deleted, not archived here.

## Example — Customer region fan-out fix

- **Status:** in progress, as of 2026-01-15.
- **Ticket:** `PROJ-142`. **Repo:** `acme-analytics/warehouse-project`, branch `fix/customer-region`.
- **Problem:** `DIM_CUSTOMER` is one row per customer *per region*; three downstream marts join it
  without the region key and inflate their counts.
- **Decision:** fix the grain at the dimension, not with `DISTINCT` downstream — a structural fix, not
  a patch. See [`warehouse.md`](warehouse.md).
- **Next:** the third mart still needs the join corrected; the first two are merged.
- **Open question:** whether the legacy export keys on the old hash or the resolved id. Unresolved —
  do not assume either.

Replace this with your own. Keep the shape: status + date, ticket and repo, the problem, the decision
and its reason, what's next, and anything genuinely unresolved.
