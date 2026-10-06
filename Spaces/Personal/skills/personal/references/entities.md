# Personal people, pets, and locations

Read `watchtower`, `Spaces/Personal/Personal Vault Guide.md`, and the relevant `People.md`,
`Pets.md`, or `Locations.md` page first. Entity notes are useful graph anchors, not a reason to create
a stub for every incidental mention.

## Preview before saving

Follow the vault-wide verification preview. Unless the current request contains an explicit,
positive bypass such as `full perms`, `skip verification`, or `write it directly`, show every entity path and the exact proposed Markdown or diff for each entity,
index, and narrative-link change before writing. The bypass skips only the human preview; do not guess.

## People

- Personal entity path: `Spaces/Personal/People/<slug>.md`
- Work profiles stay under `Spaces/Work/People/`.
- Inspect existing names, aliases, and links before creating anything.
- Create or update a personal note only when the person is explicitly important, recurring, or
  the user asks for the entity. Do not guess a surname, relationship, or identity from a first name.
- When identity is certain, a personal note may carry a path-qualified `work_profile` link. Do not
  copy work facts or personal details between the notes; the link is enough.

Personal person frontmatter uses:

```yaml
type: person
status: active
domain: personal
workspace: personal
tags:
  - "personal"
aliases: []
work_profile:
people: []
related:
  - "[[People]]"
```

## Locations

- Personal entity path: `Spaces/Personal/Locations/<slug>.md`
- Work locations remain in the work space when they are work-specific.
- Use the name and level of detail actually provided. Never infer an address, exact neighborhood,
  or relationship to a place.

Location frontmatter uses `type: location`, `domain: personal`, `workspace: personal`, `tags:
["personal"]`, `location_type`, `people: []`, and `related: ["[[Locations]]"]`.

## Pets

- Personal pet path: `Spaces/Personal/Pets/<slug>.md`
- Pets are separate entities from people. Do not file a pet under `People` or guess its species,
  breed, age, ownership, or dates.
- Create or update a pet note only when the pet is explicitly important, recurring, or the user asks
  for the entity.

Pet frontmatter uses `type: pet`, `domain: personal`, `workspace: personal`, `tags: ["personal"]`,
`aliases: []`, `people: []`, and `related: ["[[Pets]]"]`.

## Linking narrative notes

Add explicit entities to `people:`, `locations:`, or `pets:` on the primary diary, memory, reflection,
or uncategorized note. If a person, place, or pet is ambiguous, leave it unlinked and preserve the
wording; ask one batched clarification set rather than silently resolving it. Check every new link and
landing page before committing.
