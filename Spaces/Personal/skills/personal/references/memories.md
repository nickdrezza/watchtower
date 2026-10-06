# Personal memory

Read `watchtower` and `Spaces/Personal/Personal Vault Guide.md` first. Use this skill only when
the user's intent is a past event or life-history record, not an ordinary entry for today.

## The PR is the preview

Write on a branch and open a PR. The diff is the preview (`AGENTS.md` → *Write to the vault*). Show
the Markdown in chat only when the user asks. Keep the hard rules and do not guess.

## Filing

- Exact date → `Spaces/Personal/Memories/YYYY/MM/YYYY-MM-DD--<slug>.md`
- Month and year → `Spaces/Personal/Memories/YYYY/MM/<slug>.md`
- Year only → `Spaces/Personal/Memories/YYYY/<slug>.md`
- No usable date → `Spaces/Personal/Memories/Undated/<slug>.md`

Use a short, stable slug. Record partial or approximate dates with `date_precision: day|month|year|
approximate|unknown`; never manufacture a day from a year or a relative phrase.

## Note contract

```yaml
type: memory
status: active
date: YYYY-MM-DD          # blank when unknown
date_precision: day      # or month, year, approximate, unknown
year: YYYY
domain: personal
workspace: personal
tags:
  - "personal"
people: []
locations: []
pets: []
related:
  - "[[Memories]]"
```

Link explicit people, meaningful locations, and pets. Link existing entities when identity is certain;
delegate creation or identity checks to `personal-entities`. If the memory has a substantial
present-day reflection, keep the memory as the primary note and add a link only when a separate
reflection is clearly requested.

## Voice and safety

Keep first person, chronology, uncertainty, and the words the user actually used. Fix only basic
cleanup and explicit corrections. Do not fill gaps, dramatize, diagnose, or turn the event into a
generic biography. Follow the repo's ask-before-writing rule, preserve the complete source, update
the `Memories` landing page or year index, and verify links and tags before committing.
