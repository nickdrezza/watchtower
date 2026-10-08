---
type: memory
title: "Known limits — fill in yours"
description: "Table of known connector limits: the warehouse is read-only, tracker queries hit token limits, docs make new copies, unshared sheets fail."
updated: 2026-08-05
tags:
  - ACME
---

# Known limits — fill in yours


| Connector | Limit |
|---|---|
| Warehouse | **Read-only.** DDL goes through the console — see [`warehouse/`](../warehouse/index.md) |
| Tracker | Large multi-issue queries blow the token budget; request only the fields you need, in small batches |
| Docs/Drive | Often cannot edit in place — each revision may be a new document and URL |
| Spreadsheets | A sheet not shared with the service account fails in a way that looks like a code bug |
