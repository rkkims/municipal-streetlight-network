# Municipal Streetlight Network

Investigate public street-light infrastructure data from the City of Vancouver and District of North Vancouver (DNV), normalize documented source differences, and build one evidence-based DNV pole-to-service-panel network trace. This small job-application project for a geospatial/data-engineering role at Antenna Management Corp emphasizes reproducible acquisition, GIS and topology QA, and clear explanations of missing or ambiguous infrastructure.

## Planned architecture

```text
Municipal GIS sources
↓
ingest
↓
source inspection
↓
normalization
↓
geometry + topology QA
↓
network graph
↓
pole-to-service-panel trace
↓
QGIS visualization + findings
```

## Status

Scaffold only. Sources have not been verified or downloaded; no analysis, schema, CRS, snapping tolerance, or connectivity rules have been selected. Scripts and notebooks are placeholders. QGIS work will be manual.

This project evaluates what can and cannot be inferred from public GIS data. Electrical capacity will not be inferred unless source data actually supports it.

## Planned outputs

- Documented source inventory and reproducible acquisition steps.
- Minimal common schema with original IDs and source provenance retained.
- One validated DNV trace and one broken or ambiguous trace with an explanation.
- Concise geometry/topology QA and supported versus unsupported conclusions.
- QGIS overview and highlighted-trace screenshots, methodology, and limitations.

## Working layout and environment

`data/raw/` preserves original downloads; `data/interim/` holds intermediate work; `data/processed/` holds derived datasets. Generated data and `outputs/` contents are ignored by Git. Review tiny publication artifacts explicitly before adding any exception. Keep notebook outputs cleared before committing.

`configs/` will hold reviewed municipality mappings; `src/streetlight_network/` will hold reusable processing; `scripts/` will provide entry points. No processing is implemented yet.

Python dependencies are declared in `pyproject.toml`; `requirements.txt` installs this project. No packages were installed during scaffolding. Preserve the VM's working GIS environment and system QGIS. If a separate environment is needed later, create a project-local virtual environment and use `python -m pip install -r requirements.txt` there. Do not install into system Python or pin low-level GDAL to force compatibility. Dependency versions and full reproduction commands will be recorded after a workflow is validated; this scaffold is not a locked environment.

Start with the [Kanban board](docs/kanban.md), [project plan](docs/project-plan.md), and [source inventory](docs/data-sources.md). [Decision guardrails](docs/assumptions.md) apply before implementation.
