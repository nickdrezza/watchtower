---
tags:
  - ACME
---

# The warehouse — worked example

> **This is an example file.** It shows what a good platform memory file looks like: how to connect,
> what the limits are, and the gotchas that cost hours. Replace it with the systems you actually use,
> one file each. Delete it once you have your own.

Acme Analytics runs a cloud warehouse holding the company's modelled data.

## Connecting

| Fact | Value |
|---|---|
| Account | `acme-analytics.example` |
| Default role | `ANALYST_RO` — read-only, the default for everything |
| Write role | `LOADER_RW` — deliberate, not the default |
| Warehouse | `WH_ANALYST_XS` for queries, `WH_LOAD_M` for loads |
| Production database | `ANALYTICS` |
| Auth | Key pair. Location in [`credentials.md`](credentials.md) — never the key itself |

## ⚠️ The MCP is read-only

The warehouse connector cannot run DDL. This is deliberate, not a misconfiguration.

**To change schema:** hand the user copy-paste SQL for the console, then verify with a `SELECT`. Don't
try to route around it, and don't report the change as done until the `SELECT` confirms it.

## Layers

| Layer | Grain | Notes |
|---|---|---|
| `RAW` | source-shaped | Never query for analysis; it has no dedup |
| `STAGING` | one row per source record, typed and renamed | Views, cheap |
| `MARTS` | one row per business entity | What consumers read |

## Gotchas that have cost hours

- **`DIM_CUSTOMER` is one row per customer *per region*,** not per customer. Joining without the region
  key fans out silently and inflates every count downstream. This is the single most common bug here.
- **`FCT_EVENTS` is incremental.** A backfill needs `--full-refresh`; without it, corrections to old
  rows never land and the table looks fine.
- **A query against `MARTS` right after 04:00 UTC may read a half-built table.** Resolve
  `MAX(snapshot_date)` first and use that — never `CURRENT_DATE`.
- **Row counts drift.** Any count written down here is point-in-time; verify before quoting one.
