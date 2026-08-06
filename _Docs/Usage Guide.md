---
type: documentation
status: active
domain: system
workspace: vault
tags:
  - "topic/agents"
related:
  - "[[Home]]"
  - "[[AI Agents]]"
  - "[[Setup Guide]]"
  - "[[AI Note Intake Workflow]]"
  - "[[Agent Memory]]"
---

# Usage Guide

Day-to-day use once [[Setup Guide]] is done. The model is [[AI Agents]]; the agent-side rules are
`_Agents/docs/operating-model.md`.

## Starting work

**Just say what you want.** Don't paste context, don't summarize where you left off, don't hunt for
the old chat. A correctly set-up agent reads the vault, searches prior sessions, and queries the
connectors before asking you anything.

If it asks you to re-explain something it could have looked up, that's a bug — usually a missing
memory file or a harness that never got the global bridge.

Worth saying out loud when it matters:

- *"Check what we decided about this before"* — nudges the cross-chat search.
- *"Don't ask me, go read it"* — when it's hedging on something checkable.
- *"Save that"* — when it says something you want to survive the session.

## Capturing raw material

The vault is built to absorb mess. `Inbox/Raw Dumps/` exists for exactly that, and
[[AI Note Intake Workflow]] is the prompt pattern: dump it, let an agent file it, keep your wording.

**Don't pre-organize.** Structuring notes by hand before handing them over is the work you installed
this to avoid.

## Use voice

Dictation is the highest-leverage habit here, because this system runs on raw context and speaking
produces far more of it per minute than typing. Use voice mode in the Claude or Codex apps for:

- **Meeting debriefs** — talk through what happened while it's fresh; let the agent file it.
- **Work-log material** — narrate the week, don't compose it.
- **Thinking out loud** — half-formed reasoning is exactly what a reflection or decision note wants.
- **Personal capture** — the `diary` and `personal-*` skills preserve your voice deliberately, so
  speaking gets a better result than writing does.

**The one real gotcha: transcription mangles identifiers.** Ticket keys, table and column names, file
paths, SQL, commands, and URLs come back wrong and *look* plausible. So:

> Speak the prose. Type or paste the exact strings.

Saying *"I'll paste the ticket numbers"* and then pasting them is faster than correcting a
transcription three turns later. And don't dictate credentials — voice makes it easy to blurt one, and
the no-secrets rule has no exception for convenience.

**On the phone** there is no vault — no clone, no shell. Dictate into the chat anyway and let a laptop
session file it later; that's the documented path in `machines/mobile.md`, not a workaround.

## Let chats end

Ending a session costs nothing that was written down. Resuming next month is a **new chat**, not an
excavation.

This only works if memory actually gets written, which is why the rule is bounded rather than
aspirational — `_Agents/memory/README.md` → *When to write memory*:

- **A single durable fact** gets appended the moment it's learned. No preview, no ceremony.
- **Anything larger** — multiple facts, a contradiction, pruning — goes through `vault-memory` with the
  normal review.
- **Live state is never written.** Ticket status and row counts get queried, not remembered.

The test: *would a fresh agent, six weeks from now, do the job worse without this?*

## Syncing

`vault-sync` is the single entry point. It pulls, refreshes the weekly log and memory, then commits →
PR → merge → summary. Say *"sync my vault."*

Never push to `main` directly, including from an agent. Branch and PR, every time.

## When to spawn subagents

Rarely. One thread carrying heavy context beats several coordinating.

Reach for them when a task genuinely splits into independent pieces — roughly one per feature or
commit on a large change. Never spawn one to "own" a topic: it would hold context nothing else can
read, which is the failure this whole setup exists to avoid.

## Keeping it healthy

- **Register a tag before using it.** `Maps/Tag Registry.md` is the authority. Vocabulary drift is
  what makes a big vault slow to search.
- **One fact, one home.** A fact that fits two files goes in the more specific one with a pointer from
  the other. Never duplicate the body.
- **Prune while you're in there.** Memory that grows without pruning stops being readable.
- **Verify before believing a report.** Including one from an agent — `_Agents/docs/verification.md`.

## When something goes wrong

| Symptom | Usually |
|---|---|
| Agent asks you to re-explain known context | The global bridge missed that harness — re-run `install-instructions.sh` |
| Agent says a skill is unavailable | It didn't auto-discover. `SKILL.md` is plain Markdown — tell it to read the file |
| Agent states something confidently wrong | A stale memory fact. Fix the file, don't just correct the chat |
| Agent asks permission for everything | It's over-applying *Ask instead of assuming* — see *…and when not to ask* in `AGENTS.md` |
| Commands fail with wrong paths | Wrong machine profile. `environment.md` routes to the right one |
