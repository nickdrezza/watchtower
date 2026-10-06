---
type: memory
title: "Gotchas that have cost hours"
description: "Warehouse traps: DIM_CUSTOMER is per region, FCT_EVENTS backfills need --full-refresh, MARTS can be half-built after 04:00 UTC."
updated: 2026-08-05
tags:
  - ACME
---

# Gotchas that have cost hours


- **`DIM_CUSTOMER` is one row per customer *per region*,** not per customer. Joining without the region
  key fans out silently and inflates every count downstream. This is the single most common bug here.
- **`FCT_EVENTS` is incremental.** A backfill needs `--full-refresh`; without it, corrections to old
  rows never land and the table looks fine.
- **A query against `MARTS` right after 04:00 UTC may read a half-built table.** Resolve
  `MAX(snapshot_date)` first and use that — never `CURRENT_DATE`.
- **Row counts drift.** Any count written down here is point-in-time; verify before quoting one.
