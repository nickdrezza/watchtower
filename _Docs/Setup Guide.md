---
type: documentation
status: active
domain: system
workspace: vault
tags:
  - "topic/agents"
related:
  - "[[Home]]"
  - "[[AI Agents]]"
  - "[[Usage Guide]]"
  - "[[Agent Memory]]"
  - "[[Skills Repo]]"
---

# Setup Guide

Standing this up on a new machine, or for the first time. Day-to-day work is [[Usage Guide]]; the
model behind it is [[AI Agents]].

Budget 15 minutes. Steps 1–4 are the whole thing; 5–8 are what make it *yours*.

## 1. Clone it

```bash
git clone git@github.com:<you>/<your-vault>.git <vault-path>
```

Path is per-machine — record whatever you choose in the machine profile (step 5). Nothing depends on
a specific location.

## 2. Point your agents at it

```bash
_Agents/scripts/install-instructions.sh
```

Writes a pointer stub into each installed harness's **global** instruction file, so agents load these
rules everywhere — not only when opened on this repo. It discovers targets by which config
directories exist, and **refuses to overwrite a hand-written file** without `--force`.

Use `--dry-run` first if you want to see what it would touch.

## 3. Install the skills

```bash
_Agents/scripts/install-skills.sh          # global: ~/.agents/skills + ~/.claude/skills
_Agents/scripts/install-skills.sh --here   # or just this repo: ./.claude/skills
_Agents/scripts/install-skills.sh --copy   # copy instead of symlink — required across Windows↔WSL
```

Most harnesses read `_Agents/skills/` natively. Claude Code reads `.claude/skills/`, which is why the
bridge exists. **If neither ran, nothing is broken** — `SKILL.md` is plain Markdown; an agent can read
it directly.

## 4. Verify it took

Open a **new** chat in any harness, from a directory that is *not* this repo, and ask:

> What are the hard rules of my vault, and where does my agent memory live?

A correct answer means the global bridge works. A blank stare means step 2 didn't reach that harness —
check whether its config directory existed when you ran it.

## 5. Write your machine profile

`_Agents/memory/machines/<target>.md`. Copy the closest existing profile and record:

- Paths — where this repo and your work repos live.
- Shell — real, wrapped, or absent. On Windows the Bash tool is Git Bash, **not** WSL.
- Which CLIs are installed — **and which deliberately are not.** That list is as load-bearing as the
  paths; it stops an agent burning turns on a tool that isn't there.
- Which `gh` identity you get, and the git author email.

Then add it to `machines/README.md` and the routing table in `environment.md`.

## 6. Set up credentials — locations only

Record *where* each credential lives in `_Agents/memory/credentials.md`: the path, the env-var name,
the secret-manager item, the role. **Never the value.** That is the repo's first hard rule and the
extension-based check won't catch a pasted secret — you're the backstop.

## 7. Connect what you use

Add MCP connectors for the systems you actually work in, then record what each one is authoritative
for — and where it lies — in `_Agents/memory/connectors.md`. That file is what stops an agent trusting
a stale number instead of querying the source.

## 8. Know the pre-push check

This vault is meant to be one **private** repo. Before pushing, confirm no binary or key slipped in —
both of these should print nothing:

```bash
git ls-files | grep -Ei '\.(png|jpe?g|gif|webp|svg|pdf|pem|key|p8|p12|env|js|css)$'
find . -path ./.git -prune -o -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.webp' -o -iname '*.gif' -o -iname '*.svg' -o -iname '*.pdf' -o -iname '*.pem' -o -iname '*.key' -o -iname '*.p8' -o -iname '*.env' -o -iname '*.js' -o -iname '*.css' \) -print
```

**This is extension-matching only — it cannot see a secret pasted into a note.** That's on you, and
it's the repo's first hard rule. `vault-sync` runs the value-level scan; see `AGENTS.md`.

## 9. Optional — Obsidian

Open the repo as a vault. `_Agents/` sits alongside `_Docs/` and `_Templates/`, and you also see
only your notes. Dashboards are `.base` files and filter on `type ==`, so keep frontmatter honest.

Everything works without Obsidian. It is a nice reading surface, not a dependency.

## Then

Read [[Usage Guide]]. The first real habit to build is letting a chat end.
