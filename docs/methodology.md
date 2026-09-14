# Methodology (planned)

No analysis has been performed. Follow the phases in [project-plan.md](project-plan.md).

1. Verify official sources and record metadata and reproducible acquisition details.
2. Preserve originals and inspect formats, CRS, geometry, identifiers and connectivity evidence.
3. Review DNV layers manually in QGIS; measure gaps and present decisions to the owner.
4. After decisions, construct a graph and validate one pole-to-panel trace and one failure mode manually.
5. Compare municipalities and agree a minimal common schema with source IDs and provenance retained.
6. Run geometry and topology QA; record counts, denominators, exclusions and uncertainty.
7. Package screenshots, reproduction steps and supported versus unsupported findings.

## Municipality stopping points

Vancouver is intentionally carried through acquisition, source inspection,
normalization, and QA only. The inspected Vancouver exports do not contain a
shared connectivity identifier, so network tracing is deferred until an
evidence-supported rule or additional municipal records are available. DNV is
used for the current trace demonstration because its source `Network_Id` and
conduit geometry support an exploratory trace.

Pending sections: verified acquisition commands; environment versions; approved transformations; graph/traversal rules; validation evidence; QA definitions and results. Do not report planned procedures as completed work.
