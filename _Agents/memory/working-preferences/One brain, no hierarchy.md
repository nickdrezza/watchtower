---
type: memory
title: "One brain, no hierarchy"
description: "Every agent reads the same vault; delegate bounded, testable work to smaller models and use subagents for parallel work, not to hold context."
updated: 2026-10-06
---

# One brain, no hierarchy

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
