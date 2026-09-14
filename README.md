# Municipal Streetlight Network

This project is a working response to Antenna Management Corp.'s municipal
street-light data pilot. It uses public data from Vancouver and the District
of North Vancouver (DNV) to show how I acquire, inspect, normalize, QA, and
trace municipal infrastructure while documenting what the source data cannot
support.

```text
Municipal sources → ingest → inspect → normalize → QA → graph → trace → QGIS
```

## How it addresses the requirements

| AMC requirement | Evidence in this repository |
| --- | --- |
| Acquire municipal street-light data | Source inventory and reproducible downloads for Vancouver and DNV |
| Normalize incoming data | YAML mappings, reusable GeoPandas normalizer, common pole/asset fields |
| Build a repeatable import script | `scripts/normalize_dnv.py` and `scripts/normalize_vancouver.py` use the same package logic |
| Work with GIS formats and CRS | Vancouver GeoJSON/EPSG:4326; DNV FGDB/EPSG:26910; GeoPackage and KML inspection |
| Perform network tracing | NetworkX conduit graph and DNV all-network trace output |
| Use QGIS and produce exhibits | Manual QGIS filtering, labels, layouts, and map exports below |
| Assess data quality honestly | QA summary, trace findings, assumptions, and limitations |
| Prepare an inventory handoff | Documented field-level handoff suitable for a later inventory system |

## Pilot deliverables and handoff

The repository is structured as a small paid-pilot starting point:

1. Acquire the municipality's current source files and record provenance.
2. Add or revise a YAML mapping after inspecting fields, geometry, and CRS.
3. Run the shared normalizer and produce a cleaned pole inventory.
4. Run QA and return counts, missing data, and ambiguous records.
5. Trace networks where source connectivity supports it.
6. Produce QGIS exhibits for technical and municipal review.
7. Request panel, circuit, structural, and permitting records that public data
   does not contain.
8. Add those records as a documented next input for capacity and candidate
   screening.

Adding another municipality should be primarily a configuration and source-
inspection task; format-specific adapters remain possible when delivery formats
differ.

## Current evidence

- DNV: 5,474 poles, 4,641 conduit features, and 1,576 fittings normalized in
  native EPSG:26910; 446 source networks traced on an exploratory basis.
- Vancouver: 57,984 poles normalized and QA-checked in native EPSG:4326;
  tracing intentionally stops because the inspected exports lack a shared
  connectivity identifier.
- DNV fitting comments support only a subset of service-box or service-panel
  classifications; uncertain wording remains flagged.

## Assumptions and limits

`Network_Id` is used as an exploratory grouping signal, then checked against
conduit geometry. Exact endpoint matching is conservative and exposes small
positional gaps; no arbitrary snapping or automatic gap repair is applied.
Conduit geometry does not prove energized service. The public data does not
provide the panel ratings, circuit loads, conductor information, or spare
capacity required for a real capacity summary, so electrical capacity is not
inferred.

## Map exhibits

![DNV network example](docs/images/dnv_trace_network_example.png)

![DNV conduit gap](docs/images/dnv_gap_LGTLT01611_LGTCON00377.png)

## Reproduce

```bash
python scripts/normalize_dnv.py
python scripts/normalize_vancouver.py
python scripts/run_qa.py
python scripts/run_trace.py
```

## Application materials

- [Case study](docs/application-case-study.md)
- [Resume bullets](docs/resume-bullets.md)
- [Application note](docs/application-note.md)
- [Source inventory](docs/data-sources.md)
- [Limitations](docs/limitations.md)
- [Network model](docs/network-model.md)
