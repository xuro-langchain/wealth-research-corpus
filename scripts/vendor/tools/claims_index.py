"""In-process reverse index over the claim sidecars. Phase 02 §3.

Read from the app-process corpus copy, so no runtime and no sandbox call.
Cached per SHA because the corpus is immutable at a commit.

Why an index rather than letting the model grep `.claims/`: answering "which
claims overlap L120-L131" is interval arithmetic across 20 JSON files, and a
model driving grep gets it subtly wrong in a way that looks exactly like a right
answer.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field

from contracts.evidence_anchor import parse_resource

#: Role precedence for relation direction: the acting document comes first.
#: A regulator acts on a research view; internal guidance acts on both, because
#: it is the thing that turns a view into something the firm is bound by. A
#: multi-asset note acts on a single-asset note — the cross-asset desk's regime
#: call modifies what the equity and fixed income desks conclude, not the other
#: way round.
PRECEDENCE = ("guideline", "bulletin", "cross-asset-note", "asset-note")
#: The desk code whose notes take a view across asset classes.
CROSS_ASSET = frozenset({"MA"})


def document_role(path: str) -> str | None:
    """Classify a source document. None for corpus scaffolding (README etc.)."""
    if path.startswith("external_sources/"):
        return "bulletin"
    if path.startswith("internal_guidelines/"):
        return "guideline"
    if path.startswith("internal_research/"):
        parts = path.split("/")
        if len(parts) < 5:
            return None
        _, asset_class, _region, _note, _edition = parts
        return "cross-asset-note" if asset_class in CROSS_ASSET else "asset-note"
    return None


@dataclass
class ClaimsIndex:
    corpus_sha: str
    claims: list[dict] = field(default_factory=list)

    @property
    def evidence_count(self) -> int:
        return sum(len(c["evidence"]) for c in self.claims)

    def by_id(self, claim_id: str) -> dict | None:
        return next((c for c in self.claims if c["id"] == claim_id), None)

    def citing(
        self, document: str, start: int | None = None, end: int | None = None
    ) -> list[dict]:
        """Claims whose evidence touches `document`, optionally overlapping a range.

        OVERLAP, not containment. A claim citing L120-L131 is affected by a
        change to L125 and by one spanning L100-L140 alike, so the test is the
        standard interval one. Containment would silently miss every
        partially-overlapping claim, which is most of them.
        """
        hits: list[dict] = []
        for claim in self.claims:
            for item in claim["evidence"]:
                if item["document"] != document:
                    continue
                if start is None or end is None:
                    hits.append(claim)
                    break
                if item["start"] is None:
                    continue
                if start <= item["end"] and end >= item["start"]:
                    hits.append(claim)
                    break
        return hits

    def documents(self) -> dict[str, int]:
        """Cited document -> evidence pointer count."""
        counts: dict[str, int] = {}
        for claim in self.claims:
            for item in claim["evidence"]:
                if item["document"]:
                    counts[item["document"]] = counts.get(item["document"], 0) + 1
        return counts


def _scan_sidecars(corpus) -> list[dict]:
    """Pure function over the preloaded corpus — no filesystem access.

    Filesystem work happens once, in a thread, inside ensure_local_corpus.
    Doing it here instead raised BlockingError from LangGraph's blockbuster,
    which catches rglob as well as reads.
    """
    prefix = "openwiki/.claims/"
    out: list[dict] = []
    for rel in corpus.paths(prefix=prefix, suffix=".json"):
        page = rel[len(prefix) : -len(".json")]
        data = json.loads("\n".join(corpus.lines(rel)))
        for claim in data.get("claims", []):
            evidence = []
            for item in claim.get("evidence", []):
                resource = item.get("resource", "")
                parsed = parse_resource(resource)
                evidence.append(
                    {
                        "resource": resource,
                        "version": item.get("version", ""),
                        "document": parsed[0] if parsed else None,
                        "start": parsed[1] if parsed else None,
                        "end": parsed[2] if parsed else None,
                    }
                )
            out.append(
                {
                    "id": claim.get("id"),
                    "page": page,
                    "statement": claim.get("statement", ""),
                    "evidence": evidence,
                }
            )
    return out


#: The committed index carries this. Bumped only for an incompatible shape; a
#: reader seeing another value falls back to scanning rather than guessing.
INDEX_SCHEMA_VERSION = 1


def relation_edges(index: ClaimsIndex) -> list[dict]:
    """Typed, directed document relations derived from multi-role claims.

    Moved here from find_relations in ph. 04 so the workflow's index builder and
    the tool share one implementation. Two copies of this logic would disagree
    on exactly the hard cases — a claim spanning three roles, a negated
    relation — and only one of them would be under test.
    """
    from contracts.relation_types import normalize

    edges: dict[tuple[str, str], dict] = {}
    for claim in index.claims:
        roles = {
            e["document"]: document_role(e["document"])
            for e in claim["evidence"]
            if e["document"] and document_role(e["document"])
        }
        if len(set(roles.values())) < 2:
            # Two editions of the same base form are the same provision in two
            # documents, not a relationship.
            continue
        # Every DISTINCT-ROLE PAIR, not just highest-to-lowest. A claim citing a
        # guideline, a regulator notice and a research note carries two real
        # relations — the guideline constrains the note, and the notice acts
        # back the base form. Collapsing to one edge loses the middle one.
        kind = normalize(claim["statement"])
        ordered = sorted(roles.items(), key=lambda kv: PRECEDENCE.index(kv[1]))
        for i, (acting, acting_role) in enumerate(ordered):
            for target, target_role in ordered[i + 1 :]:
                if acting_role == target_role:
                    continue
                edge = edges.setdefault(
                    (acting, target),
                    {"from": acting, "to": target, "types": {}, "claim_ids": []},
                )
                edge["claim_ids"].append(claim["id"])
                if kind:
                    edge["types"][kind] = edge["types"].get(kind, 0) + 1

    out = []
    for edge in edges.values():
        out.append(
            {
                "from": edge["from"],
                "to": edge["to"],
                # None rather than a guess: preserves and restores are
                # opposites, so a wrong type inverts a positioning answer.
                "type": max(edge["types"], key=edge["types"].get) if edge["types"] else None,
                "types": edge["types"],
                "claim_count": len(edge["claim_ids"]),
                "claim_ids": edge["claim_ids"],
            }
        )
    out.sort(key=lambda e: (-e["claim_count"], e["from"], e["to"]))
    return out


SIDECAR_PREFIX = "openwiki/.claims/"


def sidecar_fingerprint(corpus) -> str:
    """sha256 over every sidecar's path and content, in path order.

    This — not the commit — is what decides whether a committed index is valid
    for the tree a run is pinned to. The workflow builds the index at the
    compile commit and commits it together with the sidecars; every later commit
    that touches only source documents carries the SAME sidecars, so the index
    is still exactly right for it. Keying validity on commit equality would make
    every real run fall back to scanning. Keying it on the sidecars makes the
    index valid for precisely the commits it describes.
    """
    h = hashlib.sha256()
    for rel in corpus.paths(prefix=SIDECAR_PREFIX, suffix=".json"):
        content = "\n".join(corpus.lines(rel)).encode("utf-8")
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(hashlib.sha256(content).hexdigest().encode("ascii"))
        h.update(b"\n")
    return h.hexdigest()


def to_committed(index: ClaimsIndex, corpus) -> dict:
    """Serialise for `.claims-index.json` (C11), written by the refresh workflow.

    The C11 shape — `resources` and `relations` — is for humans and the UI.
    The `claims` array is the extra that makes this a COMPLETE replacement for
    scanning: it carries every evidence pointer with its anchor `version`, which
    read_evidence and grounding_status need and which C11's per-resource
    summary does not hold. Without it the committed index could answer "what
    depends on this" but never "is it still true", and the tools would have to
    scan sidecars anyway.
    """
    resources: dict[str, dict] = {}
    for claim in index.claims:
        for item in claim["evidence"]:
            doc = item["document"]
            if not doc:
                continue
            entry = resources.setdefault(doc, {"claim_count": 0, "pages": {}, "claims": []})
            entry["claims"].append(
                {
                    "id": claim["id"],
                    "page": claim["page"],
                    "lines": f"L{item['start']}-L{item['end']}",
                }
            )
    for entry in resources.values():
        ids = {c["id"] for c in entry["claims"]}
        entry["claim_count"] = len(ids)
        pages: dict[str, int] = {}
        seen: set[tuple[str, str]] = set()
        for c in entry["claims"]:
            key = (c["id"], c["page"])
            if key in seen:
                continue
            seen.add(key)
            pages[c["page"]] = pages.get(c["page"], 0) + 1
        entry["pages"] = dict(sorted(pages.items(), key=lambda kv: (-kv[1], kv[0])))

    return {
        "schema_version": INDEX_SCHEMA_VERSION,
        # Informational: the commit the compile ran against. Validity is decided
        # by sidecar_fingerprint, not by this — see that function.
        "compiled_from": index.corpus_sha,
        "sidecar_fingerprint": sidecar_fingerprint(corpus),
        "claim_count": len(index.claims),
        "evidence_count": index.evidence_count,
        "resources": dict(sorted(resources.items())),
        "relations": relation_edges(index),
        "claims": index.claims,
    }


def from_committed(text: str, sha: str, corpus) -> ClaimsIndex:
    """Rebuild a ClaimsIndex from `.claims-index.json`, for the tree in `corpus`.

    Raises ValueError for anything that is not a usable index for THIS tree —
    wrong schema version, a sidecar fingerprint that does not match the sidecars
    actually present, or a missing claims array. Callers fall back to scanning;
    they never guess.
    """
    data = json.loads(text)
    if data.get("schema_version") != INDEX_SCHEMA_VERSION:
        raise ValueError(f"unsupported .claims-index.json schema_version {data.get('schema_version')!r}")
    expected = sidecar_fingerprint(corpus)
    if data.get("sidecar_fingerprint") != expected:
        # The index describes a different set of sidecars than this tree holds.
        # Using it would answer blast-radius questions about claims that are
        # not the ones the run is pinned to.
        raise ValueError(".claims-index.json does not match the sidecars in this tree")
    claims = data.get("claims")
    if not isinstance(claims, list) or not claims:
        raise ValueError(".claims-index.json carries no claims array")
    for claim in claims:
        for item in claim.get("evidence", []):
            if "version" not in item or "document" not in item:
                raise ValueError("an evidence pointer in .claims-index.json lacks version or document")
    return ClaimsIndex(corpus_sha=sha, claims=claims)


_INDEXES: dict[str, ClaimsIndex] = {}

#: What ensure_index used last, per SHA: "committed" or "scan". Read by tests
#: and by repo_status so the source of an answer is observable (C13).
INDEX_SOURCE: dict[str, str] = {}


async def ensure_index(sha: str, blobs: dict[str, str] | None = None) -> ClaimsIndex:
    """No runtime parameter — see phase 02 §2.

    Ph. 04 (P1): prefer the committed `.claims-index.json`, fall back to
    scanning the sidecars. The signature is unchanged and both paths produce
    identical results — `test_the_committed_index_matches_a_live_scan` pins that.

    The fallback is not defensive padding. Every commit before ph. 04, including
    the pinned corpus every existing test runs against, has no index and never
    will. And a corrupt index must not take the agent down: scanning is slower
    and always correct.
    """
    index = _INDEXES.get(sha)
    if index is None:
        from tools.corpus_local import ensure_local_corpus

        corpus = await ensure_local_corpus(sha, blobs)
        try:
            index = from_committed("\n".join(corpus.lines(".claims-index.json")), sha, corpus)
            INDEX_SOURCE[sha] = "committed"
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            index = ClaimsIndex(corpus_sha=sha, claims=_scan_sidecars(corpus))
            INDEX_SOURCE[sha] = "scan"
        _INDEXES[sha] = index
    return index
