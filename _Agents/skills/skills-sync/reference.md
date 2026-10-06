# Skills sync — adapters, sanitization, and the gate in practice

Loaded on demand from `SKILL.md`. Four things live here: the layout adapters, the frontmatter
translation table, the sanitization checklist, and worked examples of the candidate table and the
confirmation gate.

## Layout adapters

An adapter is where a skill's folder goes at a destination and what else changes with it. **Derive it
from the destination every run** — these are recorded shapes, not a spec it's obliged to keep.

### A. Claude Code plugin marketplace

The shape a plugin marketplace repo uses. Skills are grouped into plugins; a plugin
is a bundle a person installs whole.

```text
.claude-plugin/marketplace.json      # plugin list + per-plugin description
plugins/<plugin>/.claude-plugin/plugin.json
plugins/<plugin>/skills/<skill>/SKILL.md
plugins/<plugin>/skills/<skill>/references/*.md      # note: plural
plugins/<plugin>/skills/<skill>/scripts/*
README.md                            # plugin map table
```

Landing a skill means four files, not one: the skill itself, the plugin map row in `README.md`, the
plugin's description in `marketplace.json` if the bundle's scope widened, and — for a new plugin — a
`plugin.json` plus a `marketplace.json` entry.

**Pick the plugin by who installs it, not by subject.** A skill that another skill hands off to must
be in the *same* plugin, or the reference dangles for anyone who installed only one of them.

**Merging deploys.** On a marketplace wired to auto-sync, a merge is live for everyone within minutes.
There is no staging step, so the PR review *is* the safety gate — which is why Step 5 asks for a PR
body a reviewer with no context can actually evaluate.

### B. Flat skills repo

```text
skills/<skill>/SKILL.md
```

Loaded by pointing a harness at the directory, or copied into a harness's own global skills folder.
No manifest, so the only index is whatever the README table says. The vault's own `_Agents/skills/` is this shape.

### C. Agent Skills spec repo

[agentskills.io](https://agentskills.io/specification) layout — the same folder shape as B, but the
frontmatter is held to the open spec: `name` and `description` required, everything else optional and
tool-specific. Strip Claude Code extensions unless the destination says it consumes them. This is the
most portable target and the least forgiving about proprietary fields.

### D. Documentation-only destination

Wants the knowledge, not an executable skill. Not this skill's job — hand off to
`shared-vault-promote`, or propose the target repo's own `docs/`.

## Frontmatter translation

| Vault field | Marketplace / flat | Agent Skills spec | Note |
|---|---|---|---|
| `name` | keep | keep | Must equal the folder name at the destination too |
| `description` | keep **verbatim** | keep verbatim | The trigger. Trimming it is the single most common way an exported skill silently never fires |
| `tags: [ACME]` | drop | drop | Vault-internal archival marker, meaningless elsewhere |
| `user-invocable` | keep only if the destination's own skills use it | drop | Claude Code extension |
| `argument-hint` | keep only if the destination's own skills use it | drop | Claude Code extension |
| `model` | drop unless asked | drop | Pinning someone else's model for them is rude and goes stale |
| `allowed-tools` | keep if present | keep | Genuinely portable, and a real safety property |

When in doubt, match what two existing skills at the destination actually carry. Their frontmatter is
the spec; the destination's README is only its intent.

## Sanitization checklist

Run per skill, on `SKILL.md` **and** every reference, script, and asset that travels with it.

- [ ] **No secret values.** Hard rule 1. A key, token, password, private key, `.env` line, or OAuth
      secret never travels. *Where* a credential lives — a secrets-manager item name, an env var, a vault
      path — is documentation and may travel.
- [ ] **No personal machine paths.** A home directory under any OS, a named WSL distro, a personal
      clone or worktree location. Replace with "ask the user for the path", and make the skill degrade
      if there isn't one. `_Agents/wt doctor` flags the common shapes.
- [ ] **No Watchtower-relative references.** `_Agents/memory/*`, `machines/<target>.md`,
      `environment.md`, Obsidian-style double-bracket links, `_Docs/*`. The destination has no memory layer: either
      inline the fact or have the skill ask.
- [ ] **No account identifiers the destination doesn't need.** AWS account ids, Snowflake account
      locators, cloud tenant ids. A Jira cloudId that every reader's tooling needs is fine; an account
      number that only the admin uses is not.
- [ ] **No PII beyond "who owns this system".** A named admin and their work email in an ops runbook
      is operationally necessary. Personal contact details, `People/` material, interview or comp
      notes, and performance opinions are not.
- [ ] **No unresolved internal shorthand.** Initials, a nickname for a system, "the box", "the usual
      list". Expand it or flag it — a reader outside their head cannot resolve it.
- [ ] **No stale dated claims** presented as current. Either date the claim or make the skill query it.
- [ ] **Substance survives.** If sanitization leaves a hollow skill, it was **not exportable**. Say so
      instead of shipping the shell.

## The candidate table

```markdown
| # | Skill | Why the destination wants it | Drift | Portability | Sanitization | Dangling refs |
|---|---|---|---|---|---|---|
| 1 | `playwright-testing` | Team writes browser tests ad hoc; this is the house pattern | vault ahead | portable | none | — |
| 2 | `weekly-work-log` | Managers elsewhere want the same evidence-only format | new | needs rewriting — reads the log path from `machines/` | machine path → ask user | `vault-sync` (**not present — ship together?**) |
| 3 | `secrets` | — | new | **not exportable** — documents this vault's own credential store | would remove the whole body | — |
```

Include rows like 3 rather than filtering them out — why something *shouldn't* go is how the user
calibrates the rest of the table.

## The gate, worked

After the table, one message, and then stop:

> Two of these are ready to propose and one isn't. **Which do you want me to export to the team
> marketplace?** Name them — I won't ship anything you haven't named.
>
> - `playwright-testing` → the `testing` plugin. Goes as-is; nothing to sanitize.
> - `weekly-work-log` + `vault-sync` → the `workflow` plugin. **These two only work together** — the
>   log skill hands the commit off to `vault-sync`. Ship both, or neither. I'd rewrite the log path to
>   ask the user instead of reading it from a machine profile.
> - `secrets` — my read is this one shouldn't go: it documents your credential store, machine
>   accounts, and token policy, so publishing it hands every reader a map of your vault. Tell me if
>   you disagree.

It names the skills, states each rewrite concretely enough to be contradicted, makes the coupling one
decision, and puts a recommendation *against* one item on the record. Then, per approved skill, before
committing:

> **Export preview — `weekly-work-log` → the `workflow` plugin**
>
> Frontmatter: dropping `tags: [ACME]`, `user-invocable`, `argument-hint`.
> Removed: the 3-row `_Agents/memory/` table, the "only runs where the vault is cloned" warning.
> Rewritten: memory table → "ask the user for the log path"; the clone warning → a capability check
> with a stated fallback.
> Unchanged: the evidence-gathering steps and the house format.
>
> Ship this?

## Ledger row

In `_Docs/Skill Exports.md`:

| Date | Skill | Destination | Decision | PR | Source SHA | Note |
|---|---|---|---|---|---|---|

- **Decision** — `shipped`, `declined`, `not-exportable`, or `forked` (destination copy deliberately
  diverges; the drift check will keep flagging it, and that's intended).
- **Source SHA** — the vault commit the export was cut from. Without it, Step 2's drift check is a
  guess rather than a comparison.
- **Note** — for `shipped`, what was rewritten to make it portable. For `declined`, **the condition
  that would reverse it.**
