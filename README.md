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

Official sources are documented and eight raw datasets are acquired: five Vancouver GeoJSON files in owner-selected EPSG:4326 and three DNV FGDB ZIPs. The initial normalized outputs and basic geometry QA are complete. DNV network-ID coverage and one exploratory trace have also been documented. Native CRS values are preserved; no shared analysis CRS or arbitrary snapping tolerance has been selected. QGIS work remains manual.

Vancouver is intentionally stopped at the normalization and QA stage. Its
public layers provide poles, conduits, junction boxes, and service panels, but
the inspected exports do not provide a shared connectivity identifier. A
Vancouver network trace would therefore require an additional, documented
connectivity rule or municipal records. DNV is the municipality used for the
current trace demonstration.

This project evaluates what can and cannot be inferred from public GIS data. Electrical capacity will not be inferred unless source data actually supports it.

## Normalized pole inventory

The normalized pole outputs contain the same common fields and have no missing geometries:

| Municipality | Pole records | Native CRS | Source IDs populated | Network IDs populated |
| --- | ---: | --- | ---: | ---: |
| DNV | 5,474 | EPSG:26910 | 5,474 | 3,501 |
| Vancouver | 57,984 | EPSG:4326 | 0 | 0 |

Vancouver source identifiers and network identifiers remain null because the inspected public pole dataset does not provide reliable values. Original source attributes remain available in the raw/interim data.

## Planned outputs

- Documented source inventory and reproducible acquisition steps.
- Minimal common schema with original IDs and source provenance retained.
- One validated DNV trace and one broken or ambiguous trace with an explanation.
- Concise geometry/topology QA and supported versus unsupported conclusions.
- QGIS overview and highlighted-trace screenshots, methodology, and limitations.

## Working layout and environment

`data/raw/` preserves original downloads; `data/interim/` holds intermediate work; `data/processed/` holds derived datasets. Generated data and `outputs/` contents are ignored by Git. Review tiny publication artifacts explicitly before adding any exception. Keep notebook outputs cleared before committing.

`configs/` holds reviewed municipality mappings; `src/streetlight_network/` holds reusable processing; `scripts/` provides entry points for normalization and QA. QGIS visualization and topology decisions remain manual and documented.

## Reproduce the current normalization and QA

From the repository root, run the scripts with the project virtual environment:

```bash
/home/ubuntu/amc_application_project/.venv/bin/python scripts/normalize_dnv.py
/home/ubuntu/amc_application_project/.venv/bin/python scripts/normalize_vancouver.py
/home/ubuntu/amc_application_project/.venv/bin/python scripts/run_qa.py
```

The normalization scripts read the raw downloads and YAML mappings, then write derived GeoPackage layers under `data/normalized/`. The QA script writes `outputs/qa/normalized_summary.csv`. Raw downloads are not modified.

Python dependencies are declared in `pyproject.toml`; `requirements.txt` installs this project. No packages were installed during scaffolding. Preserve the VM's working GIS environment and system QGIS. If a separate environment is needed later, create a project-local virtual environment and use `python -m pip install -r requirements.txt` there. Do not install into system Python or pin low-level GDAL to force compatibility. Dependency versions and full reproduction commands will be recorded after a workflow is validated; this scaffold is not a locked environment.

Start with the [Kanban board](docs/kanban.md), [project plan](docs/project-plan.md), [source inventory](docs/data-sources.md), and the [candidate schema comparison](docs/schema-comparison.md). [Decision guardrails](docs/assumptions.md) apply before implementation.

For the application package, see the [case study](docs/application-case-study.md),
[resume bullets](docs/resume-bullets.md), and [application note](docs/application-note.md).
