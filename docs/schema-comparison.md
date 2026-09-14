# Schema comparison and candidate common schema

This is a documented proposal based on the downloaded source schemas. Original source fields remain authoritative and are preserved where needed for provenance.

## Observed source fields

| Municipality | Source layer | Geometry | CRS | Identifier evidence | Connectivity evidence | Classification evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Vancouver | street-lighting-poles | Point | EPSG:4326 | `node_number` | None shared across layers | Layer role: pole |
| Vancouver | street-lighting-conduits | LineString, MultiLineString, Point | EPSG:4326 | No source ID field published | None | `wireset_type` |
| Vancouver | street-lighting-abandoned-conduits | LineString | EPSG:4326 | No source ID field published | None | `wireset_type`; source layer indicates abandoned status |
| Vancouver | street-lighting-junction-boxes | Point | EPSG:4326 | No source ID field published | None | Layer role: junction box; `material` |
| Vancouver | street-lighting-service-panels | Point | EPSG:4326 | `service_panel_number` | None | Layer role: service panel |
| DNV | LgtStreetLightPoles | Point | EPSG:26910 | `Asset_Id`, `GlobalID` | `Network_Id` | Layer role: pole; extensive asset fields |
| DNV | LgtStreetLightConduit | MultiLineString | EPSG:26910 | `Asset_Id`, `GlobalID` | `Network_Id` | `ConduitStatus`, comments |
| DNV | LgtStreetLightFittings | Point | EPSG:26910 | `ASSET_ID`, `GLOBALID` in SHP; full names in FGDB/KML | `NETWORK_ID` | `AM_TYPE`; `COMMENTS` provides incomplete descriptions |

Vancouver’s fields above come from the downloaded GeoJSON exports. DNV’s CRS and fields come from the downloaded FGDB/SHP/KML exports. A missing source ID is recorded as unavailable; it must not be synthesized and presented as an original identifier.

## Candidate normalized fields

These fields are proposed for review before implementation. A normalized record would retain the original source record and carry these common fields:

| Candidate field | Required? | Meaning | Vancouver mapping | DNV mapping | Notes |
| --- | --- | --- | --- | --- | --- |
| `municipality` | Yes | Source municipality | Constant `vancouver` | Constant `dnv` | Project provenance, not source data |
| `source_layer` | Yes | Exact source layer name | Dataset identifier | FGDB/KML layer name | Preserve exact source name |
| `asset_type` | Yes | Broad conceptual role | Layer-derived: `pole`, `conduit`, `junction_box`, `service_panel` | Layer-derived: `pole`, `conduit`, `network_fitting` | Fitting subtype remains separate and may be null; abandoned conduits remain `conduit` |
| `source_asset_id` | Nullable | Original unique asset identifier | Null for Vancouver in the inspected exports because `node_number` is not unique; otherwise use a verified unique source field | `Asset_Id`/`ASSET_ID` | Do not invent IDs for Vancouver conduits or boxes; retain non-unique source fields separately |
| `source_global_id` | Nullable | Original global identifier, when published | Null in the inspected exports | `GlobalID` where published | Preserve separately from asset IDs |
| `network_id` | Nullable | Published network grouping identifier | Null: no shared field published | `Network_Id`/`NETWORK_ID` | Copy DNV values only; do not synthesize Vancouver values; not an electrical proof |
| `classification` | Nullable | More specific source-supported subtype | Layer role; no extra subtype for most layers | Fittings: only verified classification evidence; otherwise null | Do not map `AM_TYPE` without a code dictionary |
| `classification_source` | Nullable | Field supplying a derived classification | Null | `comments` when classification is derived | Makes the evidence path explicit |
| `classification_confidence` | Nullable | Whether wording is explicit or uncertain | Null | `explicit` or `assumed` from comment wording | “Assumed”, “proposed”, and similar wording remain flagged |
| `source_comments` | Nullable | Preserved raw source comment | When published | `Comments` | Free text is retained; it is not treated as a coded domain |
| `status` | Nullable | Source-supported lifecycle/status | `abandoned` for abandoned-conduit layer; otherwise null | `ConduitStatus` where present; otherwise null | Layer-derived abandoned status must remain traceable |
| `geometry` | Yes | Original feature geometry | Source geometry in EPSG:4326 | Source geometry in EPSG:26910 | No shared analysis CRS selected |
| `source_crs` | Yes | CRS of the retained source geometry | EPSG:4326 | EPSG:26910 | Preserve native source CRS in normalized municipality outputs; defer shared analysis CRS |
| `source_url` | Yes | Official acquisition URL | Exact export URL | Exact archive URL | Enables provenance and reproduction |

## Deliberate omissions

Electrical capacity, circuit relationships, conduit endpoint IDs, junction connectivity, and service-panel certainty are not common fields because the public sources do not support them consistently. Geometry-derived values such as endpoint distances should be QA outputs, not silently added source attributes.

## Review required before implementation

Confirm whether the candidate fields and names are acceptable, especially:

- **Accepted:** use `asset_type = network_fitting` for all DNV fittings; keep a nullable `classification` for source-supported descriptions such as service box.
- Whether Vancouver layer-derived roles should be represented as `classification` as well as `asset_type`.
- **Accepted:** preserve separate nullable `source_asset_id` and `source_global_id` fields; do not synthesize missing source IDs.
- **Accepted:** preserve native source CRS in normalized municipality outputs and defer a shared analysis CRS until distance/topology requirements are defined.
- **Accepted:** map Vancouver abandoned-conduit records as `asset_type = conduit` with `status = abandoned`.
- **Accepted:** copy DNV `Network_Id` to `network_id`; leave Vancouver `network_id` null; never synthesize IDs from geometry.
- **Accepted:** retain common provenance fields in normalized output; keep source-specific attributes in raw/interim data rather than expanding the common schema.
- **Accepted:** use `asset_type` for broad roles; populate nullable `classification` only for specific, source-supported subtypes; do not use `wireset_type` as a cross-municipality classification.
- Whether the DNV `network_id` interpretation should be used only for exploratory components.

Until these choices are approved, no normalized files or municipality-specific mappings should be generated.

## Configuration-format decision

There is no universal standard for source-to-target field-mapping files. We use YAML because these two files are small, reviewed by hand, and easy to read. This is a project convention; the mapping keys and transformations remain specific to this project.

Use a small YAML subset only: mappings, lists, strings, numbers, booleans, and explicit nulls. Parse with a safe loader, validate before processing, and keep the files versioned with the code that uses them. `pyproject.toml` remains TOML because Python packaging tools require that format for project metadata.
