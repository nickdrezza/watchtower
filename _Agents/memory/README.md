# `_Agents/memory/` — operational memory

The knowledge an agent needs to actually *do* your work: which machine it's on, where every credential
lives, how to reach each platform, and how you like to work.

Skills say *how to perform a task*. Memory says *what is true about this environment*. A skill that
hard-codes an account id or a file path is doing memory's job — put the fact here and let the skill
point at it.

**Read `environment.md` and `credentials.md` at the start of any hands-on task.** They're short, and
almost every failure mode (wrong machine, wrong shell, expired session, read-only MCP) is in one of them.

## Files

| File | What's in it |
|---|---|
| [`environment.md`](environment.md) | **Start here.** How to tell which target you're on, and what's true on all of them. |
| [`machines/`](machines/README.md) | One profile per target. Paths, shells, installed tooling, and what is deliberately *not* installed. |
| [`credentials.md`](credentials.md) | Every key, token, and profile — what it authenticates and **where it lives**. Locations only, never values. |
| [`connectors.md`](connectors.md) | The live systems: which one is authoritative for what, and the limit that will bite you. |
| [`warehouse.md`](warehouse.md) | **Worked example** of a platform file. Copy its shape for each system you actually use. |
| [`working-preferences.md`](working-preferences.md) | Standing instructions — how you want agents to work. |
| [`projects.md`](projects.md) | Active work, one compact block each. |

**Add one file per platform you use** — the CRM, the tracker, the orchestration tool, the cloud account.
`warehouse.md` is the template for what a good one looks like: how to connect, what the limits are, and
the gotchas that have cost hours.

## When to write memory

Chats are disposable **only because this folder gets written** — see
[`../docs/operating-model.md`](../docs/operating-model.md). A fact learned in a session that ends
without being recorded is a fact re-derived from scratch next month.

The test:

> Would a fresh agent, six weeks from now, do the job worse without this?

### Fast path — write it now, no preview

A durable fact that clears the test goes in **the moment it's learned**. All five must hold:

1. **One fact**, not a batch.
2. **Appended to an existing file** — no new files, no restructuring.
3. **Nothing existing is rewritten or deleted.**
4. **Locations, never values.**
5. **It contradicts nothing already written.**

### Full path — preview required

Everything else: multi-fact runs, **anything contradicting an existing claim**, pruning, restructuring,
new files. Goes through `vault-memory` and the verification preview.

A contradiction is never a fast-path write. Memory that disagrees with itself is worse than memory
that's missing.

### Never written here

- **Live state** — ticket status, row counts, who's on call. Query the connector.
- **Session narrative.** What was tried and in what order is not a durable fact.
- **One-off numbers with no decision attached.**
- **Anything the code already says.**

## Employer scope — the `ACME` tag

Anything only meaningful **while you're at this employer** carries a short employer tag in its
frontmatter `tags:` — this template uses `ACME`; rename it to yours. One query can then archive the
non-reusable material if you change jobs, and the rest of the vault survives.

**Tagged:** the platform files, `credentials.md`, `connectors.md`, `projects.md`.
**Untagged (portable):** this README, `environment.md`, the `machines/` profiles, `working-preferences.md`.

## Rules

1. **Locations, never values.** The path, the env-var name, the secret-manager item, the role. Never
   the key material.
2. **Point-in-time.** Environment facts are stable; code and data facts drift — verify before
   asserting, and date anything that will age.
3. **If a skill and a memory file disagree about a *system*, verify.** If they disagree about *this
   machine*, memory wins — it's the more specific claim.
4. **Machine-specific facts go in a `machines/` profile**, never in a topic file or a skill.
