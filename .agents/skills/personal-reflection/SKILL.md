---
name: personal-reflection
description: >
  Captures personal reflections, opinions, values, identity questions, and free-form rambles in
  your natural voice. Use when he says "I think...", "I've been wondering whether...", explores
  a moral, political, or religious view, talks through a friendship or a decision, or asks to record a
  ramble. Preserves the thinking as-is — never resolves the question, argues back, or tidies it into a
  conclusion. For a past event use personal-memory; for a day's log use diary.
---

# Personal reflection

Read `watchtower` and `Spaces/Personal/Personal Vault Guide.md` before writing. This is for
what the user thinks, believes, values, or is trying to understand about himself—not a polished
essay and not a list of completed tasks.

## Preview before saving

Follow the vault-wide verification preview. Unless the current request contains an explicit,
positive bypass such as `full permissions`, `auto merge`, `just merge`, `skip verification`, or
`write it directly`, show every path and the exact proposed Markdown or diff, including frontmatter,
body, links, tags, and landing-page changes, before writing. The bypass skips only the human preview;
do not guess.

## Filing

- Default dated note → `Spaces/Personal/Reflections/YYYY/MM/YYYY-MM-DD--<slug>.md`
- Explicitly evergreen idea → `Spaces/Personal/Reflections/Topics/<slug>.md`

Use a separate reflection only when the user's intent makes it a durable reflection or he asks for
one. If a reflection is simply part of today's diary dump, keep it in the diary and link entities;
do not create duplicate prose.

## Note contract

```yaml
type: reflection
status: active
date: YYYY-MM-DD
date_precision: day
domain: personal
workspace: personal
tags:
  - "personal"
people: []
locations: []
pets: []
related:
  - "[[Reflections]]"
```

Use additional descriptive properties only when they are explicit, such as `reflection_kind:
values|identity|politics|relationships|other`. Add `work` only when the reflection directly covers
work as well as personal life; add `ACME` only for genuinely employer-specific content.

## Voice

Preserve first person, hedging, strong language, questions, and the words the user chose. Make
minor punctuation/grammar cleanup, remove accidental repetition, and apply “scratch that”
corrections. Do not argue with the reflection, normalize it, summarize it, or make it sound
objective. Ask before writing if the date, scope, or intended permanence is materially unclear.
