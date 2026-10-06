# `_Agents/memory/` — operational memory

> This folder holds only memory that is true in every space: `machines/` (with the environment
> page, `machines/index.md`) and `working-preferences/`. Each space keeps its own facts in
> `Spaces/<Name>/memory/`. The work examples are in `Spaces/Work/memory/`.

The knowledge an agent needs to actually *do* your work: which machine it's on, where every credential
lives, how to reach each platform, and how you like to work.

Skills say *how to perform a task*. Memory says *what is true about this environment*. A skill that
hard-codes an account id or a file path is doing memory's job — put the fact here and let the skill
point at it.

Load memory by task. Read `machines/index.md` and exactly one machine profile before machine-dependent
commands. Read the space's `memory/credentials/` only for authentication, secret locations, profiles, or connection
failures. Read a platform file only when the prompt or search results point to that platform.

## Topics

Each topic is a folder with one concept per file. Its `index.md` lists the files with a
one-line description, so open the index, then only the files you need.

| Topic | What's in it |
|---|---|
| [`machines/`](machines/index.md) | **Start here.** How to tell which target you're on, what's true on all of them, and one profile per target: paths, shells, installed tooling, and what is deliberately *not* installed. |
| [`Spaces/Work/memory/credentials/`](../../Spaces/Work/memory/credentials/index.md) | Every key, token, and profile — what it authenticates and **where it lives**. Locations only, never values. |
| [`Spaces/Work/memory/connectors/`](../../Spaces/Work/memory/connectors/index.md) | The live systems: which one is authoritative for what, and the limit that will bite you. |
| [`Spaces/Work/memory/warehouse/`](../../Spaces/Work/memory/warehouse/index.md) | **Worked example** of a platform file. Copy its shape for each system you actually use. |
| [`working-preferences/`](working-preferences/index.md) | Standing instructions — how you want agents to work. |
| [`Spaces/Work/memory/projects/`](../../Spaces/Work/memory/projects/index.md) | Active work, one compact block each. |

**Add one file per platform you use**, in the `memory/` folder of the space that uses it — the CRM, the tracker, the orchestration tool, the cloud account.
`warehouse.md` is the template for what a good one looks like: how to connect, what the limits are, and
the gotchas that have cost hours.

## When to write memory

Chats are disposable **only because this folder gets written** — see
[*Chats are disposable*](<working-preferences/Chats are disposable.md>). A fact learned in a session that ends
without being recorded is a fact re-derived from scratch next month.

The test:

> Would a fresh agent, six weeks from now, do the job worse without this?

Memory writes follow `AGENTS.md` → *Write to the vault*: the PR diff is the preview. No chat preview
is necessary.

### Fast path — commit one fact on the branch

Write a durable fact that passes the test **when you learn it**. Do not wait for a sync. Commit it
directly on the working branch, in the PR that the session already has. All five conditions must be
true:

1. **One fact**, not a batch.
2. **It goes in an existing topic folder** — one new concept file (`type: memory`, `description`,
   `updated`), or one line added to an existing concept file. No new topic folders and no restructuring.
3. **It rewrites or deletes nothing.**
4. **Locations, never values.**
5. **It contradicts nothing already written.**

Say it in the session's report.

### Larger changes — their own PR

All other memory changes go in a separate PR, through `vault-memory` when they come from history:
multi-fact runs, **anything that contradicts an existing claim**, pruning, restructuring, new topic
folders, and any change to this `README.md`. Ask the batched questions before you write; the user
reviews the diff.

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

**Tagged:** the platform files, `credentials.md`, `connectors.md`, `projects.md` (all in `Spaces/Work/memory/`).
**Untagged (portable):** this README, `machines/` (the environment page and the profiles), `working-preferences/`.

## Rules

1. **Locations, never values.** The path, the env-var name, the secret-manager item, the role. Never
   the key material.
2. **Point-in-time.** Environment facts are stable; code and data facts drift — verify before
   asserting, and date anything that will age.
3. **If a skill and a memory file disagree about a *system*, verify.** If they disagree about *this
   machine*, memory wins — it's the more specific claim.
4. **Machine-specific facts go in a `machines/` profile**, never in a topic file or a skill.
