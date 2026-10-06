---
name: bootstrap
description: >
  Sets up this vault for a new user or machine: installs skills, writes the machine profile, and seeds
  the credential and connector maps. Use for "set me up", "I just cloned this", "onboard me", or
  "configure this vault".
user-invocable: true
argument-hint: "set me up"
---

# Bootstrap

Someone just cloned this template. Your job is to get them from "a folder of Markdown" to "my agents
know how I work" in one sitting — and to explain *why* as you go, because the model is the point.

Read [`../../docs/operating-model.md`](../../docs/operating-model.md) first. You're about to teach it.

## Ask two things before you start

Batched, once, per the `watchtower` skill → *Ask instead of assuming*:

1. **What do you do, and what systems do you work in daily?** Drives which platform memory files to
   create and which example content to delete.
2. **What's your employer scope tag?** The template uses `ACME`. Anything only true while they're at
   this job carries it, so a job change is one query to archive rather than a rewrite.

Don't ask about anything the repo can answer.

## 1. Wire the harnesses

```bash
_Agents/wt install          # or --copy across a Windows↔WSL boundary; safe to re-run
```

It writes the global instruction stubs, links the skills, and adds the search and pre-commit hooks.
The instruction stubs are the step people skip. Without it, agents only see these rules when opened *on* this
repo — so the vault stops working the moment they're in a different project, which is most of the time.

**Verify it took:** open a new chat in any harness, from a directory that is *not* this repo, and ask
what the vault's hard rules are. A blank stare means the bridge missed that harness.

## 2. Write the machine profile

`_Agents/memory/machines/<target>.md`. Copy the closest existing profile. Record paths, shell, git
identity, harness history locations, and — **most importantly** — what is deliberately *not* installed.

Then route to it from `environment.md`.

## 3. Seed the maps

- **`credentials.md`** — every credential, what it authenticates, **where it lives**. Never a value.
- **`connectors.md`** — which live system is authoritative for what, and each one's limit.
- **One file per platform they named.** `warehouse.md` is the worked example: how to connect, the
  limits, and the gotchas. Copy its shape; delete it once they have their own.

Don't invent facts to fill these. An empty row is honest; a guessed account id is the failure this repo
cares most about.

## 4. Make it theirs

- **`working-preferences.md`** — replace the examples with how *they* want agents to work. This file
  earns its keep by recording corrections so they only get made once.
- **`Maps/Tag Registry.md`** — rename the example `topic/*` tags to their subjects. Register before use.
- **Delete the example content** — `warehouse.md`, the example project block, the sample notes. Say what
  you deleted.
- **`README.md`, `LICENSE`** — their name, their description.

## 5. Explain the model

Not optional. Walk them through, in their own vault:

- **One brain, many disposable agents.** Chats are throwaway because the vault holds the memory.
- **Fetch before asking.** Agents search the vault and prior sessions before making them re-explain.
- **When memory gets written** — the fast path vs the reviewed pass. This is the habit the whole thing
  depends on, and the one most people never build.
- **Why the organization is strict** — retrieval precision, so loading context aggressively stays cheap.

Point at `_Docs/Usage Guide.md` and stop. Don't recite it.

## 6. Verify and report

```bash
_Agents/wt doctor
```

Report: what's wired, what's still empty, and what they should do first. Their first real task is
usually to dump a week of context in and let it get filed — that's the fastest way to feel why it works.

## Related

- `vault-doctor` — the integrity checks. Run at the end.
- `watchtower` — vault-specific context, loaded only for vault work.
- `_Docs/Setup Guide.md` — the human version of steps 1–4.
