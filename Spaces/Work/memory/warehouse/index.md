---
title: "The warehouse — worked example"
tags:
  - ACME
---

# The warehouse — worked example

## Agent memory

> **This is an example file.** It shows what a good platform memory file looks like: how to connect,
> what the limits are, and the gotchas that cost hours. Replace it with the systems you actually use,
> one file each. Delete it once you have your own.

Acme Analytics runs a cloud warehouse holding the company's modelled data.

```okf-view
kind: pages
under: Spaces/Work/memory/warehouse/
as: list
describe: description
```

<!-- okf-view:snapshot (generated: do not edit, recomputed on save) -->
- [Connecting](Connecting.md) - Warehouse connection facts: the account, the read-only default role, the write role, the compute warehouses, the database, and key-pair auth.
- [Gotchas that have cost hours](<Gotchas that have cost hours.md>) - Warehouse traps: DIM_CUSTOMER is per region, FCT_EVENTS backfills need --full-refresh, MARTS can be half-built after 04:00 UTC.
- [Layers](Layers.md) - The grain and use of the three warehouse layers: do not query RAW for analysis, STAGING is typed views, and consumers read MARTS.
- [⚠️ The MCP is read-only](<The MCP is read-only.md>) - The warehouse connector cannot run DDL; give the user SQL to run in the console, then use a SELECT to verify the change.
<!-- /okf-view:snapshot -->
