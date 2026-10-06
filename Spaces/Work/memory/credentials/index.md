---
title: "Credentials — where they live"
tags:
  - ACME
---

# Credentials — where they live

## Agent memory

**Locations, never values.** Recording the path, the env-var name, the secret-manager item, or the role
is the entire point of this file. Recording the value is the repo's first hard rule, broken.

If you find a secret value in this repo: strip it, tell the user, and point them at where it belongs.
The `.gitignore` check is extension-based and misses inline secrets — you are the backstop.

```okf-view
kind: pages
under: Spaces/Work/memory/credentials/
as: list
describe: description
```

<!-- okf-view:snapshot (generated: do not edit, recomputed on save) -->
- [Credentials — where they live: Rules](Rules.md) - Credential rules: inject secrets as env vars, never echo a token, filter values out of list output, and record each rotation date.
- [The map](<The map.md>) - Example table of each credential, where it is kept, and what expires; replace the example rows with your own and keep the columns.
<!-- /okf-view:snapshot -->
