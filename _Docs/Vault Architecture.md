---
type: documentation
status: active
domain: system
workspace: vault
related:
  - "[[Home]]"
  - "[[Spaces Index]]"
  - "[[AI Note Intake Workflow]]"
---

# Vault Architecture

the vault is one vault with multiple clearly separated spaces.

## Top-Level Folders

- `Spaces`: domain-specific content.
- `Concepts`: reusable topic notes, one per durable subject. Ships with [[AI Agents]]; add yours as
  the vault grows. Every one is listed in [[Concept Index]] and owns a `topic/*` tag.
- `Maps`: navigation notes and indexes.
- `Dashboards`: Obsidian Bases for database-style views.
- `Inbox`: raw note dumps and processed intake notes.
- `Daily Notes`: vault-level daily notes.
- `_Templates`: note templates.
- `_Docs`: repo and workflow documentation.
- `_Vault Maintenance`: local maintenance notes and archived helper files.

## Spaces

`Spaces/Work/Current Work` is the current-work space for employer-specific material:

- `Projects`
- `Work Logs`
- `Meeting Notes`
- `People` — one note per person he works with; see [[People Index]] and People Roster
- `Partners` — one note per external team; see Partner Index
- `Reference`
- `Training`
- `Interviews`
- `Visual Notes`

`Spaces/Work/Future Work` is for future roles, career planning, reusable professional material, and non-Acme work.

`Spaces/Personal` is for personal notes and life material. Its durable framework is:

- `Diary` — dated daily entries under year/month folders
- `Memories` — past events, milestones, and life-history notes
- `Reflections` — opinions, values, identity questions, and personal rambles
- `People` and `Locations` — personal-context entity notes
- `Literature` — the reading-list landing page, with future detail notes below it
- `Uncategorized` — preserved personal material awaiting routing

[[Personal Vault Guide]] is the routing and writing contract for this space.

`Spaces/Shared` is for cross-domain material that intentionally belongs to more than one area.

## Properties

Durable notes should use these properties when applicable:

```yaml
type:
status:
domain:
workspace:
organization:
tags:
related:
people:
```

`people:` holds `[[links]]` to notes in the relevant personal or work `People/` directory — who was
involved. Work person notes use `type: person` with `person_org`, `person_group`, `role`, `email`,
and `github`; personal person notes intentionally record only details you provides.

Recommended values:

- `domain`: `work`, `personal`, `shared`, or `system`
- `workspace`: `current-work`, `future-work`, `personal`, `shared`, or `vault`
- `organization`: use `Acme Analytics` only for employer-specific material

## Tags

[[Tag Registry]] lists every allowed tag and when to apply it. It is the authority, and it is updated in
the same commit as any tag change.

Properties describe *what a note is*. Tags describe **graph scope, employer scope, and subject matter**.
`personal` and `work` are deliberate Graph-view filters even though `domain`/`workspace` also record
the note's primary home.

- `personal` — personal graph scope; mixed notes may also carry `work`.
- `work` — professional graph scope; mixed notes may also carry `personal`.
- `ACME` — employer-specific, archivable in one query on a job change.
- `topic/*` — one per note in `Concepts/`, listed in [[Concept Index]]. A `topic/*` tag always
  accompanies a `[[link]]` to that concept.

Do not add a tag merely to restate `type:`, `domain:`, or `workspace:`. Scope tags are the intentional
exception because Graph view needs cross-folder filters. Tags echoing structural roles were retired on
2026-07-30 — the Dashboards filter on `type ==`, and Graph view groups structural roles by path.

`source/pdf-converted`, `assets/images-converted`, and `excalidraw` are provenance/plugin tags and stay
as they are.

## Design Intent

The vault should be easy for both Obsidian and coding agents to operate on:

- notes are Markdown;
- structure lives in properties and links;
- maps/indexes provide navigation;
- Bases provide filtered views;
- AI agents use `AGENTS.md`, `CLAUDE.md`, and `_Docs/AI Note Intake Workflow.md`.

**Structure exists to make retrieval cheap.** The properties, the folder boundaries, the tag registry,
and the memory index are not housekeeping — they are what lets an agent load exactly what a task needs
and nothing else. That is what makes it affordable to load context aggressively rather than
sparingly, and it matters more as the vault grows. The agent-side statement of this is
`_Agents/docs/operating-model.md`.

### Two `docs` folders, on purpose

- **`_Docs/`** — human and vault governance, indexed by Obsidian. Architecture, intake workflow,
  ledgers, and the vault-side windows into the agent layer ([[Skills Repo]], [[Agent Memory]]).
- **`_Agents/docs/`** — agent doctrine. Visible in Obsidian since the folder has no dot, but written
  for agents, not for the graph. How to behave (`operating-model.md`),
  how to know you're done (`verification.md`), where each harness reads from (`platforms.md`), and how
  skills travel (`portability.md`).

Same word, different audience. When in doubt: would a person browsing the vault read it, or only an
agent about to do work?

## Text-First Policy

This vault is hosted in a private git repo as text.

Do not add:
- images;
- PDFs;
- private keys;
- plugin bundles;
- local cache files;
- environment files.

External assets are intentionally kept outside the vault.

Image embeds were replaced with text descriptions. See [[Image Descriptions]].
