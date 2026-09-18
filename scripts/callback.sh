#!/usr/bin/env bash
# POST the C9 refresh callback. HMAC-SHA256 over the raw body in
# X-Refresh-Signature. Fires on EVERY terminal status — a UI that only learns
# about success shows a spinner forever on exactly the runs a user most needs
# told about. Wrapped with `|| true` by the caller: this is an optimization,
# .compile-state.json in git is the mechanism.
set -uo pipefail
# Unconfigured is the normal case for a scheduled run, and the header above says
# this is an optimization rather than the mechanism. `:?` turned that into a
# noisy "parameter null or not set" line in every run's log, which reads like a
# failure in a job that already failed for another reason.
if [ -z "${REFRESH_CALLBACK_URL:-}" ] || [ -z "${REFRESH_CALLBACK_SECRET:-}" ]; then
  echo "no refresh callback configured; .compile-state.json in git is the mechanism" >&2
  exit 0
fi
[ -f .compile-state.json ] || { echo "no .compile-state.json; nothing to report" >&2; exit 0; }
# The commit step decides what landed. Superseded means a newer source push
# won the race and the run it triggered recompiles — reported as such, not as
# failed. Any other non-landing means the state file describes output that is
# not on the branch: report failed.
if [ "${COMMIT_LANDED:-}" = "superseded" ]; then
  body=$(jq -c --arg head_after "$(git rev-parse HEAD)" --arg why "a newer push changed source documents while this compile ran; the run it triggered recompiles" \
           '. + {event: "refresh_complete", head_after: $head_after, status: "superseded", reason: $why}' .compile-state.json)
elif [ "${COMMIT_OUTCOME:-success}" != "success" ] || [ "${COMMIT_LANDED:-true}" = "false" ]; then
  body=$(jq -c --arg head_after "$(git rev-parse HEAD)" --arg why "compile finished but the commit did not land (${COMMIT_OUTCOME:-unknown}); nothing is on the branch" \
           '. + {event: "refresh_complete", head_after: $head_after, status: "failed", reason: $why}' .compile-state.json)
else
  body=$(jq -c --arg head_after "$(git rev-parse HEAD)" '. + {event: "refresh_complete", head_after: $head_after}' .compile-state.json)
fi
sig=$(printf '%s' "$body" | openssl dgst -sha256 -hmac "$REFRESH_CALLBACK_SECRET" | awk '{print $NF}')
code=$(curl -sS --max-time 20 -o /dev/null -w '%{http_code}' -X POST "$REFRESH_CALLBACK_URL" \
  -H 'content-type: application/json' -H "X-Refresh-Signature: sha256=$sig" -d "$body" || echo "000")
echo "callback -> $REFRESH_CALLBACK_URL : HTTP $code" >&2
