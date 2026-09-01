#!/usr/bin/env bash
# Find prompt-relevant vault context and print pointers, never file bodies.
set -o pipefail

VAULT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SEARCH_ROOTS=(
    "$VAULT/_Agents/memory"
    "$VAULT/_Agents/skills"
    "$VAULT/_Agents/docs"
    "$VAULT/Concepts"
    "$VAULT/Maps"
    "$VAULT/Spaces"
    "$VAULT/_Docs"
)
MAX_FILES=15
TRIGGERS=(
    vault agents instructions context token efficiency
    warehouse cloud crm github tracker tickets connector credentials secrets
    deployment worktree project meeting interview diary personal career
)

matched_terms() {
    local prompt_lc="$1" t out=()
    for t in "${TRIGGERS[@]}"; do
        case "$prompt_lc" in *"$t"*) out+=("$t") ;; esac
    done
    [ ${#out[@]} -gt 0 ] && printf '%s\n' "${out[@]}"
    return 0
}

search_terms() {
    local t
    for t in "$@"; do
        [ -n "$t" ] || continue
        grep -ril --include='*.md' --exclude-dir='.git' -- "$t" "${SEARCH_ROOTS[@]}" 2>/dev/null |
            sed -e "s|^$VAULT/||" -e "s|\$|\t$t|"
    done | awk -F'\t' '
        { if (f[$1] == "") { f[$1] = $2; n[$1] = 1 } else { f[$1] = f[$1] ", " $2; n[$1]++ } }
        END { for (k in f) printf "%s\t%s\t%s\n", n[k], k, f[k] }
    ' | sort -rn
}

emit_report() {
    local terms=("$@") hits total
    hits="$(search_terms "${terms[@]}")"
    [ -n "$hits" ] || return 1
    echo "Vault context — matched: ${terms[*]}"
    echo "READ ONLY THE RELEVANT RESULTS. Root: $VAULT"
    echo
    printf '%s\n' "$hits" | head -n "$MAX_FILES" |
        awk -F'\t' '{ printf "  %-46s %s\n", $2, $3 }'
    total="$(printf '%s\n' "$hits" | wc -l | tr -d ' ')"
    [ "$total" -le "$MAX_FILES" ] || echo "  … $((total - MAX_FILES)) more. Re-run with narrower terms."
}

if [ "${1:-}" = "--hook" ]; then
    prompt="$(python3 -c '
import json, sys
try: print(json.load(sys.stdin).get("prompt", ""))
except Exception: pass
' 2>/dev/null || true)"
    [ -n "$prompt" ] || exit 0
    terms=()
    while IFS= read -r line; do [ -n "$line" ] && terms+=("$line"); done < <(
        matched_terms "$(printf '%s' "$prompt" | tr '[:upper:]' '[:lower:]')"
    )
    [ ${#terms[@]} -gt 0 ] || exit 0
    report="$(emit_report "${terms[@]}")" || exit 0
    python3 -c '
import json, sys
print(json.dumps({"hookSpecificOutput":{"hookEventName":"UserPromptSubmit","additionalContext":sys.stdin.read()},"suppressOutput":True}))
' <<<"$report" 2>/dev/null || true
    exit 0
fi

if [ "$#" -eq 0 ]; then
    echo "usage: wt-search.sh <term> [term…] | wt-search.sh --hook" >&2
    exit 0
fi
emit_report "$@" || echo "No vault hits for: $*"
