---
type: documentation
status: active
domain: system
workspace: vault
tags:
  - "ACME"
  - "topic/agents"
  - "topic/aws"
  - "topic/warehouse"
  - "topic/data-quality"
  - "topic/transform"
  - "topic/crm"
  - "topic/tickets"
  - "topic/segmentation"
  - "topic/warehouse-db"
  - "topic/events"
related:
  - "[[Home]]"
  - "[[Spaces Index]]"
  - "[[Current Work Home]]"
  - "[[Future Work Home]]"
  - "[[Personal Home]]"
---

# AI Note Intake Workflow

Use this when asking Claude, Codex, or another coding agent to organize a raw dump.

## Prompt Pattern

```text
Organize the raw notes below into the vault.

Rules:
- Keep my wording and tone.
- Do not summarize away concrete details.
- Decide whether each note belongs in Acme current work, future work, personal, shared, or Inbox.
- Add properties, links, headings, and file placement.
- Update weekly logs/projects/reference notes as appropriate.
- Put anything uncertain in Inbox/Processed with open questions.
- Do not add images or binary files.
- Verify no content from the dump was lost.
- Before writing, show a `vault preview` here with the exact Markdown, paths, frontmatter,
  links, tags, and index changes. An explicit `full permissions`, `auto merge`, `just merge`, or clear
  equivalent in the current request may bypass that preview.

Date range:
YYYY-MM-DD to YYYY-MM-DD

Raw notes:
...
```

## Dictated dumps

Raw dumps are often **spoken**, not typed — see [[Usage Guide]] → *Use voice*. Transcription mangles
identifiers while leaving them plausible-looking: ticket keys, table and column names, file paths,
SQL, commands, URLs.

So when a dump reads as dictated, **treat every identifier as unverified.** Check it against the tracker,
the repo, or the database, or ask. Never file a mangled ticket key or table name as fact — that's
hard rule 6 applied to the most common way it gets broken.

## Routing

Use the content to choose the right space:

- Acme/current work: `Spaces/Work/Current Work/...`
- Future professional work or career planning: `Spaces/Work/Future Work/...`
- Personal notes: `Spaces/Personal/...`
- Reusable cross-domain material: `Spaces/Shared/...`
- Unclear or mixed notes: `Inbox/Processed/...`

## Acme Current Work

- Daily or weekly work updates: `Spaces/Work/Current Work/Work Logs/2. Systems Dev Weekly Notes/...`
- Project-specific context: `Spaces/Work/Current Work/Projects/...`
- Reusable instructions/snippets/processes: `Spaces/Work/Current Work/Reference/...`
- Meeting-specific notes: `Spaces/Work/Current Work/Meeting Notes/...`
- Training notes: `Spaces/Work/Current Work/Training/...`
- Interview notes: `Spaces/Work/Current Work/Interviews/...`

## Processing Rules

1. Preserve all links, ticket IDs, names, and dates.
2. Keep rough bullets if they are useful.
3. Add headings only where they make the note easier to scan.
4. Add properties that include `domain`, `workspace`, and `organization` when applicable.
5. Link recurring concepts:
   - the warehouse project
   - Data Quality
   - dbt
   - the warehouse
   - AWS
   - the events platform
   - the CRM
   - [[AI Agents]]
   - Segmentation
   - Tickets
6. If a project note already exists, append or merge under a dated heading instead of creating a duplicate.
7. If the dump contains tasks, keep them as Markdown checkboxes.
8. If anything is ambiguous, add `## Open questions` rather than inventing context.

## Verification Checklist

- A `vault preview` was shown here and approved, unless the current request explicitly bypassed it.
- Raw dump content is still present somewhere in the vault.
- Notes landed in the right space.
- employer-specific content did not land in personal/future-work spaces.
- Personal or future-work content did not land under Acme.
- No binary files were added.
- No secrets were added.
- New links resolve or intentionally create useful future notes.
- Relevant index/map notes still point to the updated content.
