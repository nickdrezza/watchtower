# Profile: Windows + WSL

Example profile — replace with yours. **The two-shell split is the thing to get right.**

| Fact | Value |
|---|---|
| This repo | `C:\Users\<you>\<vault>` = `/mnt/c/Users/<you>/<vault>` in WSL |
| Shells | **Two.** The harness's Bash tool is Git Bash, *not* WSL |
| Where `git push` works | **WSL only** — the SSH key and CLI auth live there |
| Git Bash | API/HTTPS access only. Pushing fails with `Permission denied (publickey)` |

## The rules that follow from that

- **Run `git`/`gh` from WSL:** `wsl.exe -d <distro> -e bash -lc '...'`.
- **Spell paths out in full and quote them.** The 8.3 short name won't resolve across the boundary.
- **Write commit messages and PR bodies to a file**, then use `-F` / `--body-file`. Inline `-m` through
  the wrapper mangles multi-line text and backticks. Custom shell vars get mangled too — use literal
  paths and `$HOME` only.
- **Symlinks don't cross the boundary reliably.** Use `_Agents/wt install --copy`, and re-run it after
  editing a skill.

## Deliberately not installed

List it here. The list is as important as the paths.
