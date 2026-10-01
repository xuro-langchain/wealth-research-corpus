"""In-process reverse index over the claim sidecars."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field

from .anchors import parse_resource

#: Which document acts on which: guidance on regulators and research, regulators on research.
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
        """Claims whose evidence touches `document`, optionally overlapping a range."""
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
    """Pure function over the preloaded corpus — no filesystem access."""
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


#: Bumped for an incompatible shape; any other value falls back to scanning.
INDEX_SCHEMA_VERSION = 1


def relation_edges(index: ClaimsIndex) -> list[dict]:
    """Typed, directed document relations derived from multi-role claims."""
    from .relations import is_legal, normalize

    edges: dict[tuple[str, str], dict] = {}
    for claim in index.claims:
        roles = {
            e["document"]: document_role(e["document"])
            for e in claim["evidence"]
            if e["document"] and document_role(e["document"])
        }
        if len(set(roles.values())) < 2:
            # Two editions of one document are not a relationship.
            continue
        # Every distinct-role pair: a claim citing three roles carries more than one relation.
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
                # The wording gives a verb; the roles decide whether it is possible.
                if kind and is_legal(kind, acting_role, target_role):
                    edge["types"][kind] = edge["types"].get(kind, 0) + 1

    out = []
    for edge in edges.values():
        out.append(
            {
                "from": edge["from"],
                "to": edge["to"],
                # None rather than a guess: a wrong type can invert an answer.
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
    """sha256 over every sidecar's path and content, in path order."""
    h = hashlib.sha256()
    for rel in corpus.paths(prefix=SIDECAR_PREFIX, suffix=".json"):
        content = "\n".join(corpus.lines(rel)).encode("utf-8")
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(hashlib.sha256(content).hexdigest().encode("ascii"))
        h.update(b"\n")
    return h.hexdigest()


def to_committed(index: ClaimsIndex, corpus) -> dict:
    """Serialise for `.claims-index.json` (the committed index shape), written by the refresh workflow."""
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
        # Informational; validity is decided by sidecar_fingerprint.
        "compiled_from": index.corpus_sha,
        "sidecar_fingerprint": sidecar_fingerprint(corpus),
        "claim_count": len(index.claims),
        "evidence_count": index.evidence_count,
        "resources": dict(sorted(resources.items())),
        "relations": relation_edges(index),
        "claims": index.claims,
    }


def from_committed(text: str, sha: str, corpus) -> ClaimsIndex:
    """Rebuild a ClaimsIndex from `.claims-index.json`, for the tree in `corpus`."""
    data = json.loads(text)
    if data.get("schema_version") != INDEX_SCHEMA_VERSION:
        raise ValueError(f"unsupported .claims-index.json schema_version {data.get('schema_version')!r}")
    expected = sidecar_fingerprint(corpus)
    if data.get("sidecar_fingerprint") != expected:
        # Built from different sidecars than this tree holds.
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

#: Per SHA, whether ensure_index used the committed index or a scan. Shown by repo_status.
INDEX_SOURCE: dict[str, str] = {}


async def ensure_index(sha: str, blobs: dict[str, str] | None = None) -> ClaimsIndex:
    """Prefer the committed `.claims-index.json`, fall back to scanning sidecars."""
    index = _INDEXES.get(sha)
    if index is None:
        from .local_copy import ensure_local_corpus

        corpus = await ensure_local_corpus(sha, blobs)
        try:
            index = from_committed("\n".join(corpus.lines(".claims-index.json")), sha, corpus)
            INDEX_SOURCE[sha] = "committed"
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            index = ClaimsIndex(corpus_sha=sha, claims=_scan_sidecars(corpus))
            INDEX_SOURCE[sha] = "scan"
        _INDEXES[sha] = index
    return index
