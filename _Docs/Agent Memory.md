---
type: documentation
status: active
domain: system
workspace: vault
tags:
  - "topic/agents"
related:
  - "[[Home]]"
  - "[[Skills Repo]]"
  - "[[Vault Architecture]]"
---

# Agent Memory

the vault carries an **operational memory layer** for AI agents at **`.agents/memory/`**. It is the
answer to "why does my agent know how to connect to the warehouse in one session and not the next" — the
facts live in the repo instead of in whichever tool happened to be configured.

Like `.agents/skills/`, it's a dot-directory, so **Obsidian does not index it**. Read it in an editor, on
GitHub, or ask an agent. This note is the human-facing index.

Kept current by the **`vault-memory`** skill — it scans local AI-platform history (Claude Code sessions,
Codex sessions and its own memory store) plus the tracker, Gmail, GitHub, and Drive meeting notes since memory
was last committed, proposes a candidate table, asks, then writes. `vault-sync` runs it as part of a
full sync.

## What's in it

| File | Covers |
|---|---|
| `README.md` | The index and the rules for writing memory. |
| `environment.md` | **Start here.** How to tell which of the four targets you're on, what's true on all of them, and what must be looked up per-machine. |
| `machines/` | One profile per target — `macos`, `windows-wsl`, `ec2`, `mobile`: paths, shells, installed tooling, and what's deliberately *not* installed. |
| `credentials.md` | The credential map — every key, token, and profile, what it authenticates, and **where it lives**. |
| `connectors.md` | The live systems — which connector is authoritative for what, the limit that will bite you, and where cross-chat session history lives. |
| `warehouse.md` | Account, databases, roles, warehouses, key-pair auth, the read-only MCP limit and the way around it. |
| `transform.md` | dbt Cloud ids and MCP config, why local `dbt build` fails, slow-CI diagnosis. |
| `cloud-and-servers.md` | AWS accounts and profiles, SSO re-auth, the EC2 automation server, cron, CloudWatch, the DR kit. |
| `workspace.md` | Sheets/Drive/Gmail: the service account, the Editor-share gotcha, key sheet ids. |
| `crm.md` | The two the warehouse→the CRM mechanisms, object ids, association types, token gotchas. |
| `events-platform.md` | the events platform_API subprojects, cron cadence, adding a custom field, field-id discovery. |
| `newsletter.md` | The data share, the SFTP jobs, the CC-email mapping job, email validity, subscription classes, sending domains. |
| `messaging.md` | The three the messaging platform pipelines, and why its open rates are overstated. |
| `git-and-tickets.md` | Which `gh` identity each shell has, the repo inventory, the tracker, shared-vault write access. |
| `warehouse-project.md` | Layers, key table grains, and the gotchas that have cost hours. |
| `vendor-platform.md` | The vendor integration: personas, the filter UDF, the recurring CI failure. |
| `internal-apps.md` | the pipeline dashboard and the list-builder app, and the Streamlit-in-the warehouse gotchas. |
| `people.md` | Who's who and what each person owns. |
| `working-preferences.md` | Standing instructions — the PR rule, verify-don't-fabricate, comment-don't-edit. |
| `projects.md` | Active and recent work, one compact block each. |

## When it gets written

The folder's own `README.md` holds the rule. In short: **a single durable fact goes in the moment it's
learned** — appended to an existing file, locations-only, contradicting nothing — with no preview
needed. Everything larger (multi-fact runs, contradictions, pruning, new files) goes through
`vault-memory` and the normal verification preview. This is what makes a chat safe to throw away.

## Three rules

1. **Locations, never values.** A path, an env-var name, a your secret manager item name, a the warehouse user/role —
   yes, and that's the point. The secret itself — never, in any file in this repo.
2. **Point-in-time.** Environment facts (paths, accounts, which shell holds the SSH key) are stable.
   Facts about code and data drift — an agent should verify before asserting, and date anything that ages.
3. **`#ACME` on the employer-specific files.** All but `README.md`, `environment.md`,
   `working-preferences.md`, and the portable `machines/` profiles carry `ACME` in their frontmatter
   `tags:`, so the non-reusable material can be archived in one query if I change jobs. Those files mark
   their few Acme rows inline; `machines/ec2.md` is fully tagged, since that box is Acme-only.

## Relationship to the vault's own notes

Memory is written **for agents**: terse, operational, "run this, watch for that." The vault's
`Concepts/` notes and `Spaces/Work/Current Work/Reference/` are written **for you**. They can
cover the same systems from different angles; neither replaces the other. Deep project narrative belongs
in `Projects/` notes and the tracker — `projects.md` holds only the pointer plus what's needed to resume.

See also [[Skills Repo]] for the skills half of `.agents/`.
