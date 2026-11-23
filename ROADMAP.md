# Roadmap

## v0.1.0 — Initial prototype
- [x] CLI for UTF-8 reference lists
- [x] Heuristic missing-field indicators
- [x] Possible exact-duplicate detection
- [x] DOI syntax extraction/check
- [x] JSON report
- [x] Basic unit tests

## v0.2.0 — Better parsing
- [ ] Explicit input formats (BibTeX, RIS, CSL-JSON)
- [ ] Improved Arabic author/title segmentation
- [ ] Configurable APA 7 / MLA / Chicago checks
- [ ] Confidence labels for each heuristic

## v0.3.0 — Registry-backed metadata checks
- [ ] Optional Crossref API lookup
- [ ] Optional DataCite API lookup
- [ ] Compare DOI metadata with submitted metadata
- [ ] Cache and rate-limit external requests
- [ ] Clearly distinguish registry match, mismatch, and no result

## v0.4.0 — Citation consistency
- [ ] Parse in-text citations
- [ ] Compare citations with reference list
- [ ] Report uncited references and unresolved citations

## Research and quality principles
- Never fabricate bibliographic metadata.
- Never treat a missing registry result as proof that a work does not exist.
- Keep automated findings reviewable by a human.
- Document language and style limitations.
