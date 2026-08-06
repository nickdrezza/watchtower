#!/usr/bin/env python3
"""Mechanical integrity checks for the vault. Deterministic only — no judgement calls.

Backs the `vault-doctor` skill. Everything here is objectively right or wrong: a link resolves or it
doesn't, a tag is registered or it isn't. Anything needing taste (is this note any good?) belongs to
`vault-prune`, not here.

Usage:
    _Agents/scripts/check_vault.py [--json] [--only CHECK[,CHECK...]]

Exit 0 = clean, 1 = findings, 2 = could not run.
"""
import json
import os
import re
import subprocess
import sys
import urllib.parse
from collections import defaultdict

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
if not ROOT:
    print("error: not in a git repo", file=sys.stderr)
    sys.exit(2)
os.chdir(ROOT)

# Placeholders used in prose *about* wiki-links, not real links.
# Placeholders that appear in prose *about* links — including in this repo's own skill docs.
GENERIC_LINKS = {"link", "links", "wiki-links", "name", "their-name", "concept", "…", "...",
                 "old name", "Note Name", "_Templates/Weekly Work Log"}
FRONTMATTER_EXEMPT_DIRS = ("_Agents/", ".github/")
FRONTMATTER_EXEMPT_FILES = {"README.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md", "TODO.md"}


def tracked():
    out = subprocess.run(["git", "ls-files", "-z"], capture_output=True, text=True).stdout
    return [p for p in out.split("\0") if p]


FILES = tracked()
MD = [p for p in FILES if p.endswith(".md")]
NOTE_NAMES = {os.path.splitext(os.path.basename(p))[0] for p in FILES if p.endswith((".md", ".base"))}
findings = defaultdict(list)


def read(p):
    try:
        with open(p, encoding="utf-8") as f:
            return f.read()
    except (OSError, UnicodeDecodeError):
        return ""


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else None


def yaml_list(fm, key):
    """Values of a `key:` in frontmatter — block or inline form.

    Parsed line-wise on purpose. A regex with DOTALL will run past the key's own block and swallow
    the next one (`related:` read as `tags:`), which is a bug this script existed to catch.
    """
    lines = fm.split("\n")
    for i, line in enumerate(lines):
        if not line.startswith(key + ":"):
            continue
        rest = line[len(key) + 1:].strip()
        if rest.startswith("["):
            return [v.strip().strip("\"'") for v in rest.strip("[]").split(",") if v.strip()]
        if rest:
            return [rest.strip("\"'")]
        vals = []
        for nxt in lines[i + 1:]:
            if nxt.strip().startswith("-"):
                vals.append(nxt.strip()[1:].strip().strip("\"'"))
            elif nxt.strip() == "":
                continue
            else:
                break          # next top-level key
        return vals
    return []


# ---------- checks ----------

def check_relative_links():
    for p in MD:
        for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", read(p)):
            t = m.group(1).split("#")[0].strip()
            if not t or t.startswith(("http://", "https://", "mailto:", "obsidian://", "#")) or "…" in t:
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(p), urllib.parse.unquote(t)))
            if not os.path.exists(target):
                findings["broken-relative-link"].append(f"{p} -> {t}")


def check_wiki_links():
    for p in MD:
        for m in re.finditer(r"\[\[([^\]|#]+)", read(p)):
            name = m.group(1).strip()
            if name in NOTE_NAMES or name in GENERIC_LINKS or name.endswith(".base"):
                continue
            findings["broken-wiki-link"].append(f"{p} -> [[{name}]]")


def check_tags_registered():
    reg = read("Maps/Tag Registry.md")
    if not reg:
        findings["missing-file"].append("Maps/Tag Registry.md not found — cannot validate tags")
        return
    allowed = set(re.findall(r"`([A-Za-z][\w/-]*)`", reg))
    for p in MD:
        if p.startswith("_Agents/"):
            continue
        fm = frontmatter(read(p))
        if not fm:
            continue
        for v in yaml_list(fm, "tags"):
            if v and v not in allowed:
                findings["unregistered-tag"].append(f"{p} -> {v}")


def check_frontmatter():
    for p in MD:
        if p.startswith(FRONTMATTER_EXEMPT_DIRS) or os.path.basename(p) in FRONTMATTER_EXEMPT_FILES:
            continue
        if frontmatter(read(p)) is None:
            findings["missing-frontmatter"].append(p)


def check_skill_indexes():
    """Every skill dir appears in each hand-maintained index, and vice versa."""
    skills = sorted(
        d for d in os.listdir("_Agents/skills")
        if os.path.isfile(f"_Agents/skills/{d}/SKILL.md")
    ) if os.path.isdir("_Agents/skills") else []
    indexes = [
        "_Agents/README.md",
        "_Agents/skills/watchtower/SKILL.md",
        "_Docs/Skills Repo.md",
        "AGENTS.md",
    ]
    for idx in indexes:
        text = read(idx)
        if not text:
            continue
        for s in skills:
            if not re.search(rf"`{re.escape(s)}`|\({re.escape(s)}/\)|skills/{re.escape(s)}/", text):
                findings["skill-not-indexed"].append(f"{idx} missing '{s}'")
    # name field must match folder
    for s in skills:
        fm = frontmatter(read(f"_Agents/skills/{s}/SKILL.md")) or ""
        m = re.search(r"(?m)^name:\s*(\S+)", fm)
        if not m:
            findings["skill-no-name"].append(s)
        elif m.group(1) != s:
            findings["skill-name-mismatch"].append(f"{s} declares name: {m.group(1)}")


def check_skill_descriptions():
    """The description is the trigger; a thin one silently fails to load."""
    base = "_Agents/skills"
    if not os.path.isdir(base):
        return
    for s in sorted(os.listdir(base)):
        f = f"{base}/{s}/SKILL.md"
        if not os.path.isfile(f):
            continue
        fm = frontmatter(read(f)) or ""
        m = re.search(r"(?ms)^description:\s*>?\s*\n?((?:\s+.+\n)+|.+\n)", fm)
        n = len(" ".join(m.group(1).split())) if m else 0
        if n < 200:
            findings["thin-skill-description"].append(f"{s} ({n} chars — weak trigger)")
        elif n > 1500:
            findings["long-skill-description"].append(f"{s} ({n} chars — over budget)")


def check_hardcoded_paths():
    """Skills describe HOW; machine facts belong in _Agents/memory/. See CONVENTIONS.md."""
    # Add your own usernames and checkout roots to USERS below — the point is to catch a path that
    # only works on one machine. A skill needing a path reads it from _Agents/memory/machines/.
    # Bare /Users/ and /home/ are deliberately NOT matched: they appear in generic examples, and
    # flagging every one of them trains you to ignore this check.
    USERS = r"alice|bob"  # ← your account names, pipe-separated
    pat = re.compile(
        rf"/mnt/c/|[A-Z]:\\Users\\|/(?:Users|home)/(?:{USERS})\b|~/\.claude/skills"
    )
    for p in FILES:
        if not p.startswith("_Agents/skills/"):
            continue
        for i, line in enumerate(read(p).splitlines(), 1):
            if pat.search(line):
                findings["hardcoded-machine-path"].append(f"{p}:{i}")


def check_mirror_stale():
    m = ".claude/skills"
    if not os.path.isdir(m) or os.path.islink(m):
        return
    src, dst = [], []
    for base, store in (("_Agents/skills", src), (m, dst)):
        for r, _, fs in os.walk(base):
            for f in fs:
                store.append(os.path.relpath(os.path.join(r, f), base))
    if set(src) != set(dst):
        findings["stale-skills-mirror"].append(
            f"{len(set(src) ^ set(dst))} file(s) differ — run install-skills.sh --here"
        )


CHECKS = {
    "relative-links": check_relative_links,
    "wiki-links": check_wiki_links,
    "tags": check_tags_registered,
    "frontmatter": check_frontmatter,
    "skill-indexes": check_skill_indexes,
    "skill-descriptions": check_skill_descriptions,
    "hardcoded-paths": check_hardcoded_paths,
    "mirror": check_mirror_stale,
}


def main():
    only = None
    as_json = "--json" in sys.argv
    for a in sys.argv[1:]:
        if a.startswith("--only"):
            only = set((a.split("=", 1)[1] if "=" in a else sys.argv[sys.argv.index(a) + 1]).split(","))
    for name, fn in CHECKS.items():
        if only and name not in only:
            continue
        fn()

    if as_json:
        print(json.dumps(findings, indent=2, sort_keys=True))
    else:
        print(f"vault-doctor — {len(MD)} markdown files, {len(FILES)} tracked\n")
        if not findings:
            print("clean — no findings")
        for k in sorted(findings):
            v = findings[k]
            print(f"{k}  ({len(v)})")
            for item in v[:25]:
                print(f"    {item}")
            if len(v) > 25:
                print(f"    … and {len(v) - 25} more")
            print()
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
