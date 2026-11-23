"""Rule-based, transparent checks for academic reference strings."""
from __future__ import annotations
import re
import unicodedata
from collections import defaultdict

YEAR_RE = re.compile(r"\b(?:19|20)\d{2}[a-z]?\b", re.IGNORECASE)
DOI_RE = re.compile(r"(?:https?://(?:dx\.)?doi\.org/|doi:\s*)(10\.\d{4,9}/[^\s,;]+)", re.IGNORECASE)
DOI_SHAPE_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.IGNORECASE)

def normalize(text: str) -> str:
    """Normalize whitespace, Unicode composition and case for comparisons."""
    text = unicodedata.normalize("NFKC", text)
    return re.sub(r"\s+", " ", text).strip().casefold()

def extract_doi(reference: str) -> str | None:
    match = DOI_RE.search(reference)
    if not match:
        return None
    return match.group(1).rstrip(").,;]}>")

def inspect_reference(reference: str, index: int = 1) -> dict:
    raw = reference.strip()
    year_match = YEAR_RE.search(raw)
    doi = extract_doi(raw)

    # These are deliberately heuristic indicators, not bibliographic parsing.
    chunks = [part.strip() for part in re.split(r"[.!?]\s+", raw) if part.strip()]
    title_candidate = chunks[1] if len(chunks) >= 2 else None
    has_author_signal = bool(re.match(
        r"^[\u0600-\u06FFA-Za-z][^,]{1,80},", raw
    ))
    has_year = year_match is not None
    has_title_signal = bool(title_candidate and len(title_candidate) >= 5)
    has_source_signal = bool(
        re.search(r"\b(journal|review|press|university|vol\.|pp\.|doi)\b", raw, re.I)
        or re.search(r"(مجلة|دار النشر|جامعة|مجلد|العدد|ص\.|صص)", raw)
    )

    missing = []
    if not has_author_signal:
        missing.append("author_or_author_format")
    if not has_year:
        missing.append("year")
    if not has_title_signal:
        missing.append("title_candidate")
    if not has_source_signal:
        missing.append("source_or_publication_details")

    score = round(100 * (4 - len(missing)) / 4)
    warnings = []
    if doi and not DOI_SHAPE_RE.match(doi):
        warnings.append("doi_format_suspicious")
    if not raw:
        warnings.append("empty_reference")

    return {
        "index": index,
        "reference": raw,
        "year_detected": year_match.group(0) if year_match else None,
        "doi_detected": doi,
        "doi_syntax_valid": bool(doi and DOI_SHAPE_RE.match(doi)),
        "missing_indicators": missing,
        "format_completeness_score": score,
        "warnings": warnings,
        "assessment_scope": "heuristic_format_check_only"
    }

def validate_references(references: list[str]) -> dict:
    cleaned = [r.strip() for r in references if r and r.strip()]
    results = [inspect_reference(ref, i + 1) for i, ref in enumerate(cleaned)]

    groups = defaultdict(list)
    for item in results:
        groups[normalize(item["reference"])].append(item["index"])
    duplicates = [indices for indices in groups.values() if len(indices) > 1]

    return {
        "tool": "KH Reference Integrity",
        "version": "0.1.0",
        "reference_count": len(results),
        "possible_duplicate_groups": duplicates,
        "results": results,
        "disclaimer": (
            "Heuristic formatting checks only. This report does not establish "
            "the existence, authenticity, accuracy, or scholarly quality of any source."
        )
    }
