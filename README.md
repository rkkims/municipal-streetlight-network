# Municipal Streetlight Network

Small application project for Antenna Management Corp. using public street-
light data from Vancouver and the District of North Vancouver (DNV). It
demonstrates reproducible acquisition, schema normalization, GIS and topology
QA, and an evidence-based DNV pole/conduit trace. It also documents what the
public data cannot establish.

```text
Municipal sources → ingest → inspect → normalize → QA → graph → trace → QGIS
```

## Current status

- Vancouver: acquired, normalized, and QA-checked; tracing deferred because no
  shared connectivity identifier was found.
- DNV: normalized and QA-checked; all-network exploratory traces generated.
- QGIS: overview and gap exhibits prepared manually.
- Electrical capacity is not inferred without panel and circuit records.

## Exhibits

**DNV network example**

![DNV network example](docs/images/dnv_trace_network_example.png)

**Endpoint gap near `LGTLT01611`**

![DNV conduit gap](docs/images/dnv_gap_LGTLT01611_LGTCON00377.png)

## Reproduce

From the repository root:

```bash
python scripts/normalize_dnv.py
python scripts/normalize_vancouver.py
python scripts/run_qa.py
python scripts/run_trace.py
```

The scripts read raw downloads and YAML mappings, then write normalized
GeoPackages, a QA summary, and DNV trace CSVs. Raw data is kept out of Git.

## Application materials

- [Case study](docs/application-case-study.md)
- [Resume bullets](docs/resume-bullets.md)
- [Application note](docs/application-note.md)
- [Source inventory](docs/data-sources.md)
- [Limitations](docs/limitations.md)
- [Network model](docs/network-model.md)
- [QA script](scripts/run_qa.py)
