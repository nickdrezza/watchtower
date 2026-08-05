---
name: personal-vault
description: >
  The front door for personal material — routes a natural-language personal update to diary, memories,
  reflections, people, locations, pets, literature, or Uncategorized staging. Use when the user says
  "add this to my personal vault", "save this somewhere personal", describes what happened today,
  shares a life event, or asks the agent to organize a personal conversation when it isn't obvious
  which section owns it. Picks one primary note and links the rest; hands off to the specialized
  personal-* skills when a memory, reflection, or entity needs its own behavior.
user-invocable: true
argument-hint: [update]
---

# Personal vault router

Load `.agents/skills/watchtower/SKILL.md` and `Spaces/Personal/Personal Vault Guide.md` before
reading or writing personal notes. This skill is the front door; use the specialized skills when a
memory, reflection, or entity needs its own behavior.

## Route first

Identify the user's main intent, not every noun in the dump:

- day-in-the-life, daily thoughts, or what happened today → `diary`
- past event, milestone, period, or life history → `personal-memory`
- belief, opinion, value, identity question, or ramble → `personal-reflection`
- durable person, meaningful place, or pet → `personal-entities`
- book or short story read → `Literature.md` and its future detail-note convention
- unclear destination → `Uncategorized.md` and `personal-triage` later

Choose one primary narrative note. Link secondary people, locations, and pets through `people:`,
`locations:`, and `pets:`; do not duplicate the same story across categories unless the user asks.

## Preview before saving

Follow the vault-wide verification preview. Unless the current request contains an explicit,
positive bypass such as `full permissions`, `auto merge`, `just merge`, `skip verification`, or
`write it directly`, show every destination and the exact proposed Markdown plus frontmatter, links,
tags, and landing-page changes here before writing. The bypass skips only the human preview; preserve
the hard rules and do not guess.

## Capture rules

1. Use only dates and identities explicit in the conversation or verified in the vault. Ask a single
   batched question set before writing when a material ambiguity remains.
2. Keep the first-person voice. Apply only basic cleanup, including explicit “scratch that”
   corrections and accidental repetition. Never turn a dump into a polished essay or checklist.
3. Add `personal` to every note created under `Spaces/Personal`. Add `work` too when the same note
   genuinely spans both contexts; employer-specific work also carries `ACME`.
4. Read the destination landing page, preserve its placeholder conventions, and add the smallest
   necessary index link and explicit `people:`, `locations:`, or `pets:` links.
5. If classification is uncertain, preserve the complete source in `Spaces/Personal/Uncategorized/`
   with `status: needs-triage`; uncertainty is data, not permission to guess.

## Before finishing

Check the path, frontmatter, scope tags, people/location/pet links, landing-page backlinks, and that
no source wording or personal detail was silently dropped. Apply the vault preview/bypass gate,
then commit vault edits on the active feature branch; do not push `main`.
