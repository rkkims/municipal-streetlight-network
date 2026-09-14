# Municipal street-light network audit

## Project

I built a small, reproducible GIS and data-engineering workflow for public
street-light infrastructure data from the City of Vancouver and the District
of North Vancouver (DNV).

## Problem

Municipal asset data arrives in different formats, schemas, coordinate systems,
and levels of completeness. The project tests how far public data can support a
normalized pole inventory and an exploratory pole-to-network trace before
additional municipal or electrical records are required.

## What I delivered

- Acquired and documented Vancouver GeoJSON and DNV File Geodatabase sources.
- Preserved source data and native CRS values.
- Built YAML-driven municipality mappings and reusable GeoPandas normalization.
- Produced normalized pole, conduit, and fitting GeoPackage layers.
- Ran geometry, identifier, CRS, and network-ID QA.
- Built a NetworkX conduit graph for DNV using exact conduit endpoints.
- Traced DNV fitting candidates to reachable and unreachable poles across source
  network IDs.
- Identified and documented a visually supported pole-mediated path and a
  0.0486 m conduit endpoint discrepancy.
- Created QGIS overview and gap exhibits.
- Documented missing connectivity, electrical, structural, radio, and
  permitting information.

## Key judgment

Vancouver was intentionally stopped after normalization and QA because the
inspected public exports do not provide a shared connectivity identifier. DNV
supports an exploratory trace through `Network_Id` and conduit geometry, but
the result does not prove energized service or electrical capacity.

The DNV fittings layer combines feature types. Service-box and service-panel
subtypes are populated only when comments provide explicit or uncertain
wording; unsupported fittings remain unclassified.

## Reproduction

From the repository root:

```bash
python scripts/normalize_dnv.py
python scripts/normalize_vancouver.py
python scripts/run_qa.py
python scripts/run_trace.py
```

The workflow writes normalized GeoPackages, a QA summary, and an all-network
trace CSV. QGIS layouts and visual checks remain manual.

## Application artifacts

- Repository: `municipal-streetlight-network`
- QA report: `outputs/qa/normalized_summary.csv`
- All-network trace: `outputs/traces/dnv_all_network_traces.csv`
- Trace documentation: `outputs/traces/dnv_trace_LGTNET00001.md`
- QGIS project: `outputs/maps/dnv_trace_exhibit.qgz`
- Overview exhibit: `outputs/maps/dnv_trace_network_example.png`
- Gap exhibit: `outputs/maps/dnv_gap_LGTLT01611_LGTCON00377.png`

