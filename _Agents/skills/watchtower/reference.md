# the vault — reference

Deep detail for the `watchtower` skill. Loaded on demand.

## Full folder map

```
Obsidian Vault/                            # = watchtower repo
├── AGENTS.md                              # authoritative always-on instructions for ALL agents
├── CLAUDE.md, GEMINI.md,                  # stubs -> AGENTS.md (so no harness sees different rules)
│   .github/copilot-instructions.md
├── README.md                              # human-facing overview
├── _Agents/                               # the agent layer (.agents/ symlinks here)
│   ├── README.md                          #   map of this folder
│   ├── CONVENTIONS.md                     #   skill-authoring spec + pre-commit checklist
│   ├── skills/<name>/SKILL.md             #   CANONICAL skills (+ optional reference.md, scripts/)
│   ├── docs/platforms.md, portability.md  #   per-tool paths; the portability model
│   ├── templates/skill-template/          #   starter SKILL.md
│   └── wt                                 #   search · doctor · install · index
├── Concepts/                              # durable concept notes (AI Agents, AWS, the warehouse project,
│                                          #   Data Quality, dbt, the CRM, the newsletter platform, the warehouse, the events platform…)
├── Dashboards/                            # Obsidian .base files
│   ├── Active Projects.base               #   filters type==project AND status != "done"
│   ├── Interviews.base, Reference Notes.base, Training.base, Weekly Logs.base
├── Maps/                                  # MOCs / index notes
│   ├── Home.md, the vault.md, Spaces Index.md, Work Home.md, Work Index.md
│   ├── Project Index.md, Meeting Notes Index.md, Reference Index.md, Training Index.md
│   ├── Interview Index.md, Weekly Work Log Index.md, Visual Notes Index.md
│   ├── AWS and DevOps Index.md, Vault Maintenance.md, Template Index.md
├── Spaces/
│   ├── Work/                              # the employer space (tag ACME)
│   │   ├── index.md, AGENTS.md, memory/, skills/
│   │   ├── Projects/2026/Q<n>/            # project notes (+ Archive/ for completed)
│   │   ├── Meeting Notes/<year>/
│   │   ├── Work Logs/2. Systems Dev Weekly Notes/<year>/Q<n>/MM-DD-YYYY.md
│   │   ├── Reference/                     # Advisory Calls, AI Prompts, Data Requests, …
│   │   ├── Training/, Interviews/, Visual Notes/
│   ├── Career/index.md
│   ├── Personal/index.md, Personal Vault Guide.md, skills/
│   │   ├── Diary/, Memories/, Reflections/, People/, Locations/, Literature/, Uncategorized/
├── _Templates/                            # Daily Note, Meeting Note, Project Note, Reference Note,
│                                          #   Weekly Work Log, Interview Note, Raw Note Dump, …
├── _Docs/                                 # AI Note Intake Workflow, Vault Architecture,
│                                          #   Private Repo Setup, Image Descriptions, Skills Repo
└── Inbox/Raw Dumps/, Inbox/Processed/
```

When unsure where something goes, prefer `Inbox/Processed/` over forcing it into the wrong space.

## Property templates (copy the one matching the destination)

Every work-space note carries **`work`** in `tags:`; employer-specific notes also carry **`ACME`** for
the job-change escape hatch, see the `#ACME` section in `SKILL.md`. Personal-space notes carry
`personal`; a genuinely mixed note may carry both `personal` and `work`.

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
  - topic/…            # one per concept the note links
related:
  - "[[Project Index]]"
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
  - topic/…            # one per concept the note links
related:
  - "Weekly Work Log Index"
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

Match existing notes in the destination folder if their frontmatter differs from the above —
consistency within a folder wins.

## Status & dashboards convention

- `Active Projects.base` shows `type == project` AND `status != "done"`. So to retire a project,
  set `status: done` (and add a `> [!success] Outcome` callout + `completed:` date); optionally move
  the file into a sibling `Archive/` folder — links still resolve by name.
- Use `status: backlog` for ideas/strands with no tickets yet so they leave the active view without
  being marked done.

## Secret-handling checklist (the backstop)

The repo's setup-time check (`_Docs/Private Repo Setup.md`) only greps **file extensions**, not note
bodies. A 2026-06-30 cleanup found AWS/Google/RSA secrets pasted **inline** in tracked notes. So:

1. Before committing, grep the diff for: `BEGIN .*PRIVATE KEY`, `password`, `client_secret`,
   `AKIA`, `aws_secret`, `gho_`, `ghp_`, bearer tokens, long base64 blobs.
2. If found: remove it from the note, replace with a `> [!warning] Secret removed — stored in <X>`
   callout, and tell the user to rotate it if it was ever pushed.
3. Real secrets belong in a secret manager, your secret manager, `~/.ssh/`, or `~/.credentials/` — never in
   the vault, never in the backup (`Obsidian Vault Backups/` is plaintext too).
4. **Locations are not secrets.** Writing down *where* a credential lives — a file path, an env-var
   name, a secret-manager item name, a warehouse user/role/warehouse, an AWS profile name — is the whole
   point of this repo being useful to agents, and it is explicitly allowed. The rule is only about
   values: never the key material, never the password, never the token string.
5. Never add images/PDFs/plugin bundles/JS/CSS. `.gitignore` should already exclude them (and
   `*.pem`, `*.key`, `*.p8`, `*.p12`, `*.env`); if you see one staged, unstage it.
6. `.claude/skills/` in this repo is an old copy and is gitignored; `wt install` removes it. Make
   edits in `_Agents/skills/`.
