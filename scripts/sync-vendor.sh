#!/usr/bin/env bash
# Vendor the phase 02 index and normaliser modules from the poc repo.
#
# WHY VENDOR (R1). The poc repo is private, so the workflow cannot clone it
# anonymously, and a PAT would be one more credential to custody. Vendoring
# drifts — the spec says so — which is why this is not blind: VENDORED_FROM
# records the poc commit, and the poc repo's test_vendored_copy.py fails the
# moment the two copies differ. Drift is detected on the next poc test run,
# which is the closest tier-3 check available without a shared package.
#
#   scripts/sync-vendor.sh [path-to-poc-repo]
set -euo pipefail
POC="${1:-../wealth-research}"
here="$(cd "$(dirname "$0")" && pwd)"
for rel in contracts/__init__.py contracts/evidence_anchor.py contracts/relation_types.py \
           contracts/corpus_manifest.py tools/__init__.py tools/claims_index.py tools/corpus_local.py; do
  mkdir -p "$here/vendor/$(dirname "$rel")"
  cp "$POC/agent/$rel" "$here/vendor/$rel"
done
git -C "$POC" rev-parse HEAD > "$here/vendor/VENDORED_FROM"
echo "vendored from poc $(cat "$here/vendor/VENDORED_FROM")"
