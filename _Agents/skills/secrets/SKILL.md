---
name: secrets
description: >
  Gets, stores, rotates, and injects credentials, and never shows a value. Use for "get the X key",
  "store this secret", "rotate the X credential", "where should this credential live", or when a
  script fails on a missing credential.
user-invocable: true
argument-hint: "<get|store|rotate> <name>"
---

# Secrets

**Never surface a secret value.** Not in a note, a log, a commit, a chat message, or a terminal echo.
That is hard rule 1, and this skill exists so it never has to be broken to get work done.

Where each credential lives is recorded in [`Spaces/Work/memory/credentials.md`](../../../Spaces/Work/memory/credentials.md)
— locations only. Read it first; the credential you need may already be reachable.

## The order of preference

1. **Already in the environment** — check before fetching. `[ -n "${VAR:-}" ] && echo set` tells you
   without printing anything.
2. **Inject it** — hand the secret to a child process as an environment variable. Most secret CLIs have
   a `run --` form. The value never enters your context, the terminal, or the transcript.
3. **Reference it** — pass a file path or an item name to the consumer and let *it* resolve the value.
4. **Retrieve it** — last resort, and only when a specific value must reach a specific consumer that
   supports nothing else. Pipe it straight there; never to stdout.

## Traps

- **Many `list` commands print values in *every* output format**, including table. Project the value
  column away in the same pipe, before anything reaches the terminal. Assuming `--format table` is safe
  is how values end up in a transcript.
- **Never echo a token to confirm it loaded.** Check exit status, or check that the length is non-zero.
- **A `set -x` shell prints every expansion.** Turn it off around anything holding a secret.
- **Some tokens are shown exactly once at creation and are not retrievable.** Capture straight into the
  final destination; a retry means a new token and a rotation.
- **Read-only vs read-write scopes are different credentials.** Default to read-only; reaching for the
  write scope should be a deliberate act, not the convenient one.

## Storing a new one

1. **Decide where it belongs** — the secret manager for anything shared or rotated; `~/.ssh` for keys;
   an untracked local env file only for machine-scoped throwaways.
2. **Record the location** in `credentials.md`: what it authenticates, where it lives, and any rotation
   obligation. **Never the value.**
3. **Never commit it.** `.gitignore` covers the usual extensions, but the check is extension-based and
   misses an inline paste — you are the backstop. Secret-scan the diff before committing.

## Rotating

1. Create the new credential; capture it straight into its destination.
2. Update every consumer — grep for the env-var name, not the value.
3. Verify with a real call, then revoke the old one.
4. Update the rotation date in `credentials.md`.

**If a secret was ever pushed, it is compromised.** Rotate it; don't just remove it from the tree. Say
so plainly rather than quietly deleting the line.

## Refusals worth holding

Co-locating a passphrase with the encrypted archive it protects defeats the encryption. If asked to
write one next to the other, say why not and offer the alternative. Being asked twice doesn't change the
maths.

## Adapting this skill

Replace the generic verbs with your secret manager's actual commands, and record the CLI's path and
token location in the `machines/` profile — not here. **A skill that hard-codes a path is doing memory's
job.**
