---
type: "concept"
status: "active"
tags:
  - "topic/agents"
related:
  - "[[Agent Memory]]"
  - "[[Skills Repo]]"
---

# AI Agents

How I actually use AI agents day to day. The rules agents *follow* are in [`AGENTS.md`](../AGENTS.md)
and `_Agents/docs/operating-model.md`; this note is the human version — what the model is and why it
beats the alternative.

## The model: one brain, many disposable agents

Every chat — Claude Code, Codex, Cursor — reads this vault. The vault is the memory. The agents are
not.

The common alternative is a hierarchy: a manager agent that owns context and delegates to specialists
holding their own private memories. I don't run that. Every agent knowing everything beats every agent
knowing its own slice and having to ask.

What it buys:

- **A new chat is cheap.** It rehydrates from the vault, from prior sessions, and from the connectors.
- **Chats are disposable.** I end them freely. When a project resurfaces a month later I open a new
  chat instead of hunting the old one.
- **No orchestration to maintain.** No manager thread, no hand-off protocol, no context passing.

Subagents still earn their place on large work — roughly one per feature or commit — but for parallel
*execution*, never to hold context.

## What makes it work

**Memory that gets written.** `_Agents/memory/` is the sub-vault agents dump durable facts into — how
a platform connects, where a credential lives, the gotcha that cost hours. Without it every chat
re-derives the same things. The rule for *when* it gets written is in that folder's `README.md`; the
short version is that a single durable fact goes in the moment it's learned, and everything larger
waits for a reviewed pass. See [[Agent Memory]].

**Skills that live here, not in a tool.** `_Agents/skills/` is shared by every platform, so a
capability written once works everywhere — no per-tool copies to drift apart. See [[Skills Repo]].

**Connectors for anything live.** The vault holds durable facts; the tracker, the warehouse, email,
Drive, and the rest hold current state. Agents query those rather than trusting a number written down months ago.

**Organization, which matters more than it looks.** The tag registry, the properties, the folder
boundaries — that discipline is what lets a model fetch precisely instead of dragging in unrelated
context. The bigger the vault gets, the more it matters. See [[Tag Registry]].

**Long context that survives.** Loading heavily used to degrade a thread after a few compactions. That
stopped being true around Opus 4.6, which is why I now let chats consume a lot of input tokens without
worrying about output quality. Worth re-checking as models change.

## The open version

The same structure, anonymized and stripped of anything personal, is published as a template so other
people can run it: `<you>/watchtower`. Its team-facing counterpart is `<org>/shared-vault`.
What's private stays here; what's reusable is the scaffolding.

## Related
- AI Prompts
- [[Agent Memory]]
- [[Skills Repo]]
- [[Tag Registry]]
- Data Quality
- Segmentation
