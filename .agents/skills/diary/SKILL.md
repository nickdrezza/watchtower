---
name: diary
description: >
  Turns a personal text dump, voice note, or conversation into a lightly cleaned diary entry in the
  personal year/month/day hierarchy, preserving your own wording and voice. Use when he says
  "write a diary entry", "add this to my journal", "log my day", "save this as today's note", "here's
  what happened today", or dictates a day's events. Never polishes a dump into an essay. For a past
  event use personal-memory; for an opinion or ramble use personal-reflection.
user-invocable: true
argument-hint: [what happened]
---

# Diary

Capture personal diary dumps with basic cleanup while preserving your voice, wording, and
personal thoughts.

## Preview before saving

Follow the vault-wide verification preview. Unless the current request contains an explicit,
positive bypass such as `full permissions`, `auto merge`, `just merge`, `skip verification`, or
`write it directly`, show the complete proposed diary Markdown and all landing-page changes here before
writing. The bypass skips only the human preview; preserve the hard rules and do not guess.

## Workflow

1. Identify the entry date from your words. Use an explicit date or a clear relative date such
   as "today"; ask before writing if the date is unclear. Never invent a date.
2. Read `Spaces/Personal/Personal Vault Guide.md`, `Spaces/Personal/Diary.md`, and the relevant
   landing pages under `Spaces/Personal/Diary/` before adding an entry.
3. Follow the vault's ask-before-writing rule in `AGENTS.md`: verify what is checkable, then batch
   any unresolved choices into one concise question set before writing.
4. Store entries at `Spaces/Personal/Diary/YYYY/MM/YYYY-MM-DD.md`. Create the missing year and month
   landing pages and add links to them when a new period appears. Add the day link to the month page,
   removing its `_No entries yet._` placeholder when the first entry is added.
5. Use this frontmatter for a daily entry:

   ```yaml
   type: diary-entry
   status: active
   date: YYYY-MM-DD
   year: YYYY
   month: MM
   domain: personal
   workspace: personal
   tags:
     - "personal"
   people: []
   locations: []
   pets: []
   related:
     - "[[Diary]]"
   ```

6. If the dump clearly involves a person, location, or pet, add explicit `people:`, `locations:`, or
   `pets:` links after checking existing entities. Do not create an entity note for every incidental
   mention; use the `personal-entities` skill when a durable entity is warranted. Add `work` too only
   when the entry genuinely spans personal and work life; add `ACME` only for employer-specific content.
7. If the date file already exists, preserve its saved wording and add the new material without
   overwriting it. Use a small heading only when it helps separate distinct dumps from the same day.

## Editing the dump

- Keep first person, personal thoughts, concrete details, sequence, and the words the user actually
  used.
- Fix typos, grammar hiccups, obvious accidental repetitions, and rough punctuation.
- Treat an explicit correction such as "scratch that" as authoritative: remove the superseded fragment
  and keep the corrected version.
- Use light paragraphing or a small amount of local reordering only when it makes the same thought
  readable. Do not reorganize the day into a polished chronology unless asked.
- Preserve informal language and natural texture. Do not make it sound literary, professional, robotic,
  or like a list of activities.
- Do not summarize, embellish, interpret, infer feelings, add conclusions, or invent missing details.
- Do not turn thoughts into tasks or headings unless the user did so or the structure is needed to keep
  the dump readable.
- Preserve uncertainty instead of resolving it by guesswork. Ask when the uncertainty changes what gets
  written.

## Landing pages

- `Spaces/Personal/Diary.md` links to year landing pages.
- `Spaces/Personal/Diary/YYYY/YYYY.md` links to month landing pages.
- `Spaces/Personal/Diary/YYYY/MM/YYYY-MM.md` links to the daily entries for that month.
- Use ISO dates for filenames and frontmatter; display dates naturally inside prose when appropriate.
- Do not create an empty daily note just because a date exists. Create it when the user provides a dump
  to save.
