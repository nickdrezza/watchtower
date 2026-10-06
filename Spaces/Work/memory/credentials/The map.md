---
type: memory
title: "The map"
description: "Example table of each credential, where it is kept, and what expires; replace the example rows with your own and keep the columns."
updated: 2026-08-05
tags:
  - ACME
---

# The map


| What it authenticates | Where it lives | Notes |
|---|---|---|
| Warehouse key pair | Secret manager, item `warehouse-keypair` | Private key file mode `600` |
| The CRM private-app token | Secret manager, item `crm-token` | Rotate every 180 days |
| Git push | SSH key at `~/.ssh/id_ed25519` | Per-machine; see the profile |
| Secret-manager access token | `~/.secrets/token.env` (read-only), `token-rw.env` (write) | The one credential that cannot come from the secret manager itself |

Replace the rows above with yours. Keep the shape: what it authenticates, where it lives, what ages.
