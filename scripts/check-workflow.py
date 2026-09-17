#!/usr/bin/env python3
"""Static assertions over the refresh workflow. Phase 04 §11, stdlib only.

Run in CI on every push. Each check names the contract it enforces and the
failure it prevents; a check whose reason cannot be stated in a sentence is not
worth its false positives.
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
WF = (ROOT / ".github" / "workflows" / "openwiki-update.yml").read_text()
failures: list[str] = []


def check(ok: bool, why: str) -> None:
    print(("  ok    " if ok else "  FAIL  ") + why)
    if not ok:
        failures.append(why)


print("the trigger cannot fire on compiled output (the loop-breaker)")
paths_block = re.search(r"on:\s*\n\s*push:.*?paths:\s*\n((?:\s+- .*\n)+)", WF, re.S)
paths = re.findall(r"- '([^']+)'", paths_block.group(1)) if paths_block else []
check(sorted(paths) == ["bulletins/**", "guidelines/**", "research/**"], f"on.push.paths is exactly the three source dirs: {paths}")
check("openwiki/" not in " ".join(paths), "on.push.paths never includes openwiki/")

print("C6 — compiles serialize")
check("group: openwiki-refresh" in WF, "concurrency.group is openwiki-refresh")
check("cancel-in-progress: false" in WF, "cancel-in-progress is false (cancelling an in-progress run loses merged pages)")

print("fetch-depth: 0 (a shallow clone silently no-ops)")
check("fetch-depth: 0" in WF, "checkout uses fetch-depth: 0")

print("C6 — a queued run must see the CURRENT tip, not the sha frozen at event time")
check(re.search(r"uses:\s*actions/checkout@[0-9a-f]{40}[^\n]*\n\s+with:[^\n]*\n(?:[ \t]+#[^\n]*\n)*[ \t]+ref: main", WF) is not None,
      "checkout uses ref: main (a dispatch queued behind a push otherwise recompiles an already-compiled tree)")
check("COMMIT_OUTCOME: ${{ steps.commit.outcome }}" in WF and "id: commit" in WF,
      "the callback knows whether the commit landed (a rejected push must not report complete)")
check("COMMIT_LANDED: ${{ steps.commit.outputs.landed }}" in WF and "landed=superseded" in WF and "-- forms bulletins guidelines" in WF,
      "a push lost to a newer SOURCE commit is reported superseded, not failed; a non-source commit is rebased over")
check("steps.commit.outputs.landed != 'superseded'" in WF, "a superseded compile does not re-dispatch a resume")

print("every third-party action is pinned to a full commit SHA")
for use in re.findall(r"uses:\s*(\S+)", WF):
    check(bool(re.search(r"@[0-9a-f]{40}\b", use)), f"{use} is SHA-pinned")

print("C5 — the commit stages only the write domain")
staged = re.search(r"git add ([^\n]+)", WF)
check(staged is not None and staged.group(1).split() == ["openwiki", ".compile-state.json", ".claims-index.json"],
      f"git add stages exactly openwiki + the two state files: {staged.group(1) if staged else None}")
check("assert-write-domain.sh" in WF, "assert-write-domain.sh runs before the commit")
for bad in ("AGENTS.md", "CLAUDE.md", ".github/workflows"):
    check(bad not in (staged.group(1) if staged else ""), f"{bad} is not staged")

print("C4 — the reconciler has no staleness comparison")
check(not re.search(r"compiled_from[^\n]*rev-parse|rev-parse[^\n]*compiled_from", WF),
      "no compiled_from-versus-HEAD comparison anywhere (excluded paths move HEAD without changing the corpus)")
check("claim-diff.sh snapshot /tmp/claims-before.txt" in WF and "claim-diff.sh snapshot /tmp/claims-after.txt" in WF,
      "claim ids are snapshotted before AND after the compile")
before_i, after_i, write_i = WF.find("claims-before.txt"), WF.find("Record claim ids after"), WF.find("write-state")
check(before_i < WF.find("Run OpenWiki") < after_i < write_i, "snapshot-before < compile < snapshot-after < write-state")
check("continue-on-error: true" in WF and WF.count("continue-on-error") == 1,
      "only the compile step tolerates failure (a state file disagreeing with the tree must never be)")

print("C9 — the callback cannot fail the workflow and fires on every terminal status")
check("callback.sh || true" in WF, "callback is wrapped with || true")
check(re.search(r"Callback\n\s+if: \$\{\{ always\(\)", WF) is not None, "callback step runs if: always()")

print("C10 — the model key reaches only the compile step")
check(len(re.findall(r"^\s+OPENAI_API_KEY:", WF, re.M)) == 1,
      "OPENAI_API_KEY is assigned into exactly one step's env (the compile)")
check("OPENAI_BASE_URL" in WF, "OPENAI_BASE_URL is set (a gateway key against api.openai.com fails)")

print("compile mode rides on the commit, not the dispatch")
check("Compile-Mode:" in WF and "git log $range --format=%B" in WF and "$prev..HEAD" in WF, "the workflow reads the Compile-Mode trailer from the commits since the last compile (a refresh commit can sit on top of the ingest)")
check("steps.mode.outputs.model" in WF and "steps.mode.outputs.effort" in WF, "model and effort come from the resolved mode")
check("fast)" in WF and "deep)" in WF and "gpt-5.6-terra" in WF, "fast, normal and deep are all resolved")
check("model='gpt-5.4-mini'" not in WF, "gpt-5.4-mini is not a compile model (it over-plans; see the fast case comment)")
check("steps.state.outcome == 'success'" in WF, "the commit step runs only when the state file was written and validated")
check("Resume an interrupted compile" in WF and "actions: write" in WF, "an interrupted compile re-dispatches itself, bounded")

print(".openwikiignore excludes the machinery")
ignore = (ROOT / ".openwikiignore").read_text().splitlines()
for entry in (".compile-state.json", ".claims-index.json", ".github/", "scripts/", "contracts/"):
    check(entry in ignore, f"{entry} is OpenWiki-ignored")
for gen in (".compile-state.json", ".claims-index.json"):
    gitignored = subprocess.run(["git", "check-ignore", "-q", gen], cwd=ROOT).returncode == 0
    check(not gitignored, f"{gen} is NOT git-ignored (consumers read it from the tree)")

print("the vendored copy records its source")
check((ROOT / "scripts" / "vendor" / "VENDORED_FROM").read_text().strip().__len__() == 40, "scripts/vendor/VENDORED_FROM is a 40-hex poc commit")

print(f"\n{len(failures)} failure(s)")
sys.exit(1 if failures else 0)
