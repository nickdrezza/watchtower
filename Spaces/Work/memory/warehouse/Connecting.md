---
type: memory
title: "Connecting"
description: "Warehouse connection facts: the account, the read-only default role, the write role, the compute warehouses, the database, and key-pair auth."
updated: 2026-08-05
tags:
  - ACME
---

# Connecting


| Fact | Value |
|---|---|
| Account | `acme-analytics.example` |
| Default role | `ANALYST_RO` — read-only, the default for everything |
| Write role | `LOADER_RW` — deliberate, not the default |
| Warehouse | `WH_ANALYST_XS` for queries, `WH_LOAD_M` for loads |
| Production database | `ANALYTICS` |
| Auth | Key pair. Location in [`credentials/`](../credentials/index.md) — never the key itself |
