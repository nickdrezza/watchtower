# Personal triage

Read `watchtower`, `Spaces/Personal/Personal Vault Guide.md`, and `Spaces/Personal/Uncategorized.md`
first. Triage is a later classification pass, not permission to rewrite or discard a raw dump.

## The PR is the preview

Write on a branch and open a PR. The diff is the preview (`AGENTS.md` → *Write to the vault*). Show
the Markdown in chat only when the user asks. Keep the hard rules and do not guess.

## Workflow

1. Inventory `Spaces/Personal/Uncategorized/` and read each candidate in full.
2. Preserve the original text. Identify only dates, people, locations, and routing evidence that are
   explicit in the note or verified elsewhere in the vault.
3. Propose the destination in one batched question set when a move, split, merge, or entity link is
   not mechanically certain. Do not infer from a filename alone.
4. Move or split only after the destination is supported. Keep the original wording in the target;
   if splitting, retain a traceable link or “Source” note so nothing disappears.
5. Update the relevant landing page, `people:`/`locations:`/`pets:` links, `personal`/`work` scope tags,
   and any backlinks affected by a move.
6. Leave genuinely unresolved items in Uncategorized with `status: needs-triage` and a short,
   factual routing note.

## Classification cues

- A dated account of a day → `diary`
- A past event or milestone → `personal-memory`
- A belief, value, opinion, or identity exploration → `personal-reflection`
- A durable named person, place, or pet → `personal-entities`
- A reading-list item → `Literature.md`

Never make a note more polished than the source, never silently delete an uncategorized item, and
verify the final diff and links before committing.
