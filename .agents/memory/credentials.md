---
tags:
  - ACME
---

# Credentials — where they live

**Locations, never values.** Recording the path, the env-var name, the secret-manager item, or the role
is the entire point of this file. Recording the value is the repo's first hard rule, broken.

If you find a secret value in this repo: strip it, tell the user, and point them at where it belongs.
The `.gitignore` check is extension-based and misses inline secrets — you are the backstop.

## The map

| What it authenticates | Where it lives | Notes |
|---|---|---|
| Warehouse key pair | Secret manager, item `warehouse-keypair` | Private key file mode `600` |
| The CRM private-app token | Secret manager, item `crm-token` | Rotate every 180 days |
| Git push | SSH key at `~/.ssh/id_ed25519` | Per-machine; see the profile |
| Secret-manager access token | `~/.secrets/token.env` (read-only), `token-rw.env` (write) | The one credential that cannot come from the secret manager itself |

Replace the rows above with yours. Keep the shape: what it authenticates, where it lives, what ages.

## Rules

1. **Prefer injection over retrieval.** Hand a secret to a child process as an env var rather than
   printing it. Most secret CLIs have a `run --` form for exactly this.
2. **Never echo a token**, not even to confirm it loaded. Check exit status instead.
3. **Some list commands print values in every output format** — project them away in the same pipe
   before anything reaches the terminal.
4. **Record rotation obligations here.** A token with an expiry nobody wrote down is an outage waiting.
