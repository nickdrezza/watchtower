---
type: memory
title: "Layers"
description: "The grain and use of the three warehouse layers: do not query RAW for analysis, STAGING is typed views, and consumers read MARTS."
updated: 2026-08-05
tags:
  - ACME
---

# Layers


| Layer | Grain | Notes |
|---|---|---|
| `RAW` | source-shaped | Never query for analysis; it has no dedup |
| `STAGING` | one row per source record, typed and renamed | Views, cheap |
| `MARTS` | one row per business entity | What consumers read |
