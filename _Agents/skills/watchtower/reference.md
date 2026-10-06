# the vault — reference

Detail for the `watchtower` skill. Load it when a task needs it. `_Agents/wt doctor` checks links,
tags, frontmatter presence, the skill index, and secret patterns; this file does not repeat those checks.

## Folder layout

```
<your-vault>/
├── AGENTS.md                      # instructions for all agents; CLAUDE.md, GEMINI.md,
│                                  #   .github/copilot-instructions.md are stubs that point to it
├── README.md                      # the guide for people and the Obsidian home page
├── Spaces/
│   ├── Work/                      # current employer; tag ACME. Space rules: AGENTS.md here
│   │   ├── index.md               #   space home
│   │   ├── Projects/<year>/Q<n>/  #   project notes (+ Archive/ for done)
│   │   ├── Work Logs/<year>/Q<n>/MM-DD-YYYY.md   # + index.md
│   │   ├── Meeting Notes/<year>/, Reference/, Training/, Interviews/
│   │   ├── People/                #   one note per person
│   │   ├── Dashboards/            #   Obsidian .base files (filter on type ==)
│   │   ├── memory/                #   work facts: credentials, connectors, platforms, projects
│   │   └── skills/                #   work-only skills
│   ├── Personal/                  # personal life; tag personal. Space rules: Personal Vault Guide.md
│   │   ├── index.md, Diary.md, Memories.md, Reflections.md, People.md, Locations.md,
│   │   │   Pets.md, Uncategorized.md       # landing pages
│   │   └── skills/personal/
│   └── Career/                    # resume, career plans, future work; Shared Home.md
├── Concepts/                      # one note per durable subject; the topic/* tag targets
├── _Agents/                       # the agent layer (.agents is a symlink to it)
│   ├── README.md                  #   map of the agent layer and the skill table
│   ├── skills/<name>/SKILL.md     #   shared skills (+ reference.md, references/, scripts/)
│   ├── memory/                    #   facts true in all spaces: machines/, working-preferences/
│   ├── templates/skill-template/  #   starter for a new skill
│   ├── archive/                   #   old pages, kept as history
│   ├── tags.md                    #   the tag registry
│   ├── image-descriptions.md      #   text for removed images
│   ├── placeholders.md            #   stand-in values to replace after setup
│   ├── global-instructions.md     #   the stub that `wt install` writes into each harness
│   └── wt, wt.json                #   search · doctor · install · index, and its settings
├── _Templates/                    # note templates for each space
└── Inbox/Raw Dumps/, Inbox/Processed/
```

Folders under `Spaces/Work/` that do not exist yet are made when the first note needs them. When you are
not sure where something goes, use `Inbox/Processed/`. Do not force it into the wrong space.

## Properties

`AGENTS.md` requires `type`, `description`, and `updated`. A durable note in a space also uses these
properties when they apply:

```yaml
type:
status:
domain:          # work | personal | shared | system
workspace:       # current-work | future-work | personal | shared | vault
organization:    # "Acme Analytics" only for employer material
tags:
related:
people:          # [[links]] to notes in the space's People/ folder: who was involved
```

- Dashboards filter on `type ==`, so properties drive the views, not tags.
- A work person note uses `type: person` with `person_org`, `person_group`, `role`, `email`, and
  `github`. A personal person note records only the details that the user gives.
- Copy the template from `_Templates/`. If the notes in the destination folder use different
  frontmatter, match them. Consistency in a folder wins.

Every work note carries `work` in `tags:`; an employer note also carries `ACME` (see `#ACME` in
`SKILL.md`). A personal note carries `personal`; a note that is truly mixed can carry `personal` and
`work`.

### Acme project note
```yaml
type: project
status: active            # active | backlog | done  (Archive/ when done, status: done)
completed: ""             # set YYYY-MM-DD when status: done
domain: work
workspace: current-work
organization: Acme Analytics
area: data-platform
quarter: YYYY-Q1
tags:
  - ACME
  - work
  - topic/…            # one for each concept the note links
related:
  - "[[Spaces/Work/Projects/index|Project Index]]"
tracker: []
```

### Acme weekly log
```yaml
type: weekly-log
date: YYYY-MM-DD
year: YYYY
quarter: Q1
domain: work
workspace: current-work
organization: Acme Analytics
area: work-log
role: systems-dev
status: active
tags:
  - ACME
  - work
  - topic/…            # one for each concept the note links
related:
  - "[[Spaces/Work/index|Current Work Home]]"
```

### Personal note
```yaml
type: note
status: active
domain: personal
workspace: personal
tags:
  - personal
related:
  - "[[Spaces/Personal/index|Personal Home]]"
```

## Status and dashboards

- `Spaces/Work/Dashboards/Active Projects.base` shows `type == project` AND `status != "done"`. To
  close a project, set `status: done`, add a `> [!success] Outcome` callout and a `completed:` date.
  You can move the file into a sibling `Archive/` folder; wiki-links resolve by note name, so they do
  not break.
- Use `status: backlog` for ideas with no tickets yet. They leave the active view and are not done.

## Filing a raw dump

Use these steps when the user gives raw notes to file (typed, pasted, or dictated).

1. Find the date range, projects, meetings, tasks, links, people, and open questions.
2. Choose the space before you edit:

   | Material | Destination |
   |---|---|
   | Work daily or weekly updates | `Spaces/Work/Work Logs/…` |
   | Work project context | `Spaces/Work/Projects/…` |
   | Work instructions, snippets, processes | `Spaces/Work/Reference/…` |
   | Work meetings, training, interviews | `Spaces/Work/Meeting Notes/…`, `Training/…`, `Interviews/…` |
   | Career and future work | `Spaces/Career/…` |
   | Personal | `Spaces/Personal/…` (load the `personal` skill) |
   | Unclear or mixed | `Inbox/Processed/…` with open questions |

3. Keep the user's wording and tone. Keep all links, ticket IDs, names, and dates. Do not summarize
   away concrete details. Keep rough bullets when they are useful. Add headings only where they make
   the note easier to scan.
4. Add the properties for that space (above), with `ACME` where it applies.
5. Link recurring concepts from `Concepts/index.md`, and add each concept's `topic/*` tag with the link.
6. If a project note exists, add to it under a dated heading. Do not make a duplicate.
7. Update the weekly log, project, and reference notes that the dump changes.
8. Keep tasks as Markdown checkboxes.
9. If something is not clear, add `## Open questions`. Do not invent context.

**Dictated dumps.** Speech recognition changes identifiers and the result looks correct: ticket keys,
table and column names, paths, SQL, commands, URLs. When a dump reads as dictated, treat each
identifier as not verified. Check it against the tracker, the repo, or the database, or ask the user.

**Before you open the PR, check:**

- All content from the dump is still in the vault. Nothing was lost.
- Each note is in the correct space. Employer content is not in Personal or Career; personal or career
  content is not under Work.
- No binary files and no secrets were added.
- New links resolve, or they intentionally point to a useful future note.
- The related index and landing pages point to the new content.

## Memory and notes

Memory (`_Agents/memory/`, `Spaces/<Name>/memory/`) is for agents: short and operational ("run this,
watch for that"). The `Concepts/` and `Reference/` notes are for the user. Both can cover the same
system from different angles; one does not replace the other. Put the full history of a project in its
`Projects/` note and in the tracker; memory `projects/` keeps only a pointer and what an agent needs to
resume. The rules for writing memory are in `_Agents/memory/README.md`.

## Adding a skill

**Where skills live.** A skill that is true in all spaces goes in `_Agents/skills/<name>/`. A skill for
one space goes in `Spaces/<Name>/skills/<name>/`. Team skills live only in the team's skills repo (for
example a plugin marketplace); change them there by PR. Do not copy a team or marketplace skill into
the vault: the copy goes stale.

**Skill or memory?** A skill says how to do a task. Memory says what is true. If the content is mostly
facts (IDs, paths, credential locations, cron expressions, roles), put it in memory and let the skill
point to it. Machine-specific facts go in a `machines/` profile. If a skill and the vault rules
disagree, `AGENTS.md` and this skill win.

**Steps:**

1. Copy the template: `cp -r _Agents/templates/skill-template <skills folder>/<name>`. The folder name,
   the `name:` field, and the heading agree, in lowercase-hyphenated form.
2. Write the `description` first. It is the trigger that each platform reads: what the skill does,
   then when to use it, with phrases that the user types. Keep it 100–300 characters and specific
   enough that it does not trigger on unrelated requests.
3. Write the body as instructions to the agent. Keep `SKILL.md` short (less than about 500 lines).
   Put long detail in `reference.md` or `references/<topic>.md`, and say in `SKILL.md` when to read
   each file. Put runnable code in `scripts/` and tell the agent to run it, not to read it.
4. Use only the open SKILL.md spec for what must work: `name`, `description`, and the body.
   Tool-specific fields (`allowed-tools`, `model`, `user-invocable`, `argument-hint`) are optional; the
   skill must work without them. Use portable tools (POSIX shell, `python3`, common CLIs) and give a
   fallback for any tool-specific step.
5. Do not repeat the hard rules; point to `AGENTS.md`. Never put a secret value in a skill; record
   only where the secret is.
6. If the skill writes anything, it follows **Ask instead of assuming** in `SKILL.md`. Say what the
   questions are for this task.
7. Add a row to the skill table in `_Agents/README.md`.
8. Run `_Agents/wt install` to link the skill (in copy mode, run it again after each change).
9. Work on a branch and open a PR.

## Secret and binary checklist

CI runs gitleaks, and `wt doctor` matches common secret patterns, but neither reads meaning. Secrets
pasted inline in tracked notes are the common failure. You are the backstop.

1. Before a commit, search the diff for `BEGIN .*PRIVATE KEY`, `password`, `client_secret`, `AKIA`,
   `aws_secret`, `gho_`, `ghp_`, bearer tokens, and long base64 blobs:
   `git diff | grep -nEi 'private key|password|client_secret|AKIA|api[_-]?key|ghp_|pat-na1|xox'`
2. If you find one: remove it, put a `> [!warning] Secret removed — stored in <X>` callout in its
   place, and tell the user to rotate it if it was ever pushed.
3. Real secrets go in a secret manager, `~/.ssh/`, or `~/.credentials/`. Never in the vault, and never
   in a vault backup (backups are plain text too).
4. **Locations are not secrets.** A file path, an env-var name, a secret-manager item name, a warehouse
   user, role, or warehouse, and an AWS profile name are allowed and necessary. Only values are
   forbidden.
5. No images, PDFs, plugin bundles, JS, or CSS. `.gitignore` excludes them and `*.pem`, `*.key`,
   `*.p8`, `*.p12`, `.env*`. If one is staged, unstage it. This must print nothing:
   `git ls-files | grep -Ei '\.(png|jpe?g|gif|webp|svg|pdf|pem|key|p8|p12|env|css)$'`
6. `.claude/skills/` in this repo is an old copy and is gitignored; `wt install` removes it. Edit
   skills in their real folder.
