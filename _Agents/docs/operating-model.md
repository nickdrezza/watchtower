# The operating model

How agents are meant to work across this vault. [`platforms.md`](platforms.md) covers *where* each
harness reads from; this covers *how* to behave once loaded.

The short version: **one brain, many disposable agents.** The vault is the memory. Agents are not.

## One brain, no hierarchy

Every agent — every Claude Code session, Codex session, Cursor chat — reads this same vault. There is
no manager agent, no per-agent private memory, and no message-passing between agents.

- **Delegate bounded, objectively verifiable work to smaller, cheaper models.** A frontier agent may
  plan an epic, divide it into independent implementation tasks, and assign those tasks to a smaller
  model such as Luna at `xhigh`. Each assignment must define its inputs, expected output, implementation
  boundaries, acceptance criteria, and required tests. Keep ambiguous work, architectural decisions,
  sensitive judgment, and mistakes that are difficult to detect with the frontier agent. The delegating
  agent reviews the changes, runs or independently checks the tests, and owns the final result.
- **Subagents are for parallel work, never for holding context.** Spawn one when a task genuinely
  splits into independent pieces — roughly one per feature or commit on a large change. Don't spawn
  one to "own" a topic: it would own context nothing else can read, which is the failure this model
  exists to avoid.
- **A new chat is a new agent.** Nothing is inherited except what is written down. That is the point,
  not a limitation.

## Fetch context before asking

**Search prior sessions before making the user re-explain anything.** Most questions about what was
decided, tried, or already solved are answerable from history.

Cheapest first:

1. **This vault** — [`../memory/`](../memory/README.md), then the relevant note.
2. **Prior sessions, across chats** — the session-mgmt MCP (`list_sessions`,
   `search_session_transcripts`) for Claude Code; `<codex-home>/session_index.jsonl` for Codex. Paths
   per machine: [`../memory/machines/`](../memory/machines/README.md).
3. **Connectors** — [`Spaces/Work/memory/connectors/`](../../Spaces/Work/memory/connectors/index.md) says which one is
   authoritative for what, and where each one lies to you.
4. **Ask him.**

Reaching step 4 with 1–3 unattempted is the most common way to waste his time.

## Decide vs ask

Fetching first is not the same as asking first. Root [`AGENTS.md`](../../AGENTS.md) → **Ask instead of
assuming** is the rule for claims that go into an artifact; it is not an instruction to seek approval
for ordinary judgement.

- **Decide** when it's reversible, conventional, cheap to undo, or answerable from the repo.
- **Ask** when it's irreversible, expensive, unrecoverable if wrong, or a matter of his taste.

An agent that asks about everything is as unusable as one that assumes everything.

## Chats are disposable

Ending a session loses nothing that was written down. Picking work up weeks later is a **new chat**,
not an expedition to find the old one.

This only holds if memory actually gets written. The duty is in
[`../memory/README.md`](../memory/README.md) → **When to write memory** — the fast path exists so a
fact learned mid-session doesn't wait for a sync that may never come.

## Load context precisely

Spend input tokens deliberately. Start from the prompt, search for precise terms, and open only the
matching skill, memory file, note, or prior-session evidence. `environment.md` plus one machine profile
is required only for machine-dependent actions; `credentials.md` is required only for authentication,
secret-location, profile, or connection work. Retrieval should expand when evidence points outward,
not because a file is adjacent or linked.

## Structure exists to make retrieval cheap

The tag registry, the property templates, the folder boundaries, and the memory index are not
housekeeping. They are what lets an agent fetch exactly what a task needs and pull in nothing else.

- A vault that grows without that discipline gets slower and *worse* to work in, because every fetch
  drags in unrelated material. This matters more as the vault grows, not less.
- So: register a tag before using it, put a fact in the one file that owns it, and never duplicate a
  body across two notes. Authority: [`../../Maps/Tag Registry.md`](../../Maps/Tag%20Registry.md).

## Connectors are peers, not memory

| Kind of fact | Source of truth |
|---|---|
| How a system connects, where a credential lives, a gotcha that cost hours | [`../memory/`](../memory/README.md) |
| Ticket status, row counts, what shipped this week, who's on call | The connector — query it |

**Never cache live state into memory.** A ticket status written into a memory file is wrong within
days and will be believed anyway. Full routing and per-connector limits:
[`Spaces/Work/memory/connectors/`](../../Spaces/Work/memory/connectors/index.md).

## Verify before reporting

Finishing is a claim, and claims need evidence. [`verification.md`](verification.md) has the doctrine;
the short form is that "it should work" is not a result.

## Skills live here, not in a harness

Skills are canonical at [`../skills/`](../skills/) and shared by every platform, so a capability
written once works everywhere. Never author a skill into a harness's private directory — see
[`portability.md`](portability.md).
