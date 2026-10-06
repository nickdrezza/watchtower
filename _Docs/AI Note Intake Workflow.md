---
type: documentation
status: active
domain: system
workspace: vault
tags:
  - "topic/agents"
related:
  - "[[Home]]"
  - "[[Spaces Index]]"
  - "[[Spaces/Work/index|Current Work Home]]"
  - "[[Spaces/Career/index|Future Work Home]]"
  - "[[Spaces/Personal/index|Personal Home]]"
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
  links, tags, and index changes. An explicit `full perms` or clear equivalent
  in the current request may bypass that preview.

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

- Acme/current work: `Spaces/Work/...`
- Future professional work or career planning: `Spaces/Career/...`
- Personal notes: `Spaces/Personal/...`
- Unclear or mixed notes: `Inbox/Processed/...`

## Acme Current Work

- Daily or weekly work updates: `Spaces/Work/Work Logs/2. Systems Dev Weekly Notes/...`
- Project-specific context: `Spaces/Work/Projects/...`
- Reusable instructions/snippets/processes: `Spaces/Work/Reference/...`
- Meeting-specific notes: `Spaces/Work/Meeting Notes/...`
- Training notes: `Spaces/Work/Training/...`
- Interview notes: `Spaces/Work/Interviews/...`

## Processing Rules

1. Preserve all links, ticket IDs, names, and dates.
2. Keep rough bullets if they are useful.
3. Add headings only where they make the note easier to scan.
4. Add properties that include `domain`, `workspace`, and `organization` when applicable.
5. Link recurring concepts — every note in [[Concept Index]] that the dump actually touches, and its
   `topic/*` tag alongside. Ships with one, [[AI Agents]]; the list grows as you add concepts.
6. If a project note already exists, append or merge under a dated heading instead of creating a duplicate.
7. If the dump contains tasks, keep them as Markdown checkboxes.
8. If anything is ambiguous, add `## Open questions` rather than inventing context.

## Verification Checklist

- A `vault preview` was shown here and approved, unless the current request explicitly bypassed it.
- Raw dump content is still present somewhere in the vault.
- Notes landed in the right space.
- employer-specific content did not land in the personal or career spaces.
- Personal or career content did not land under Acme.
- No binary files were added.
- No secrets were added.
- New links resolve or intentionally create useful future notes.
- Relevant index/map notes still point to the updated content.
