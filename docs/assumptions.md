# Assumptions and decision guardrails

No GIS or network assumptions have been adopted. Preserve raw data, make transformations reproducible, and prefer clarity over sophistication. Do not hide ambiguity through automatic cleaning.

Before selecting CRS, snapping tolerance, connectivity rules, line-crossing treatment, ambiguous service-panel handling, or common-schema fields: collect source evidence, explain options and consequences, and ask the project owner to decide. Do not silently choose defaults. Record each accepted decision with its evidence and effect on conclusions.

| Decision | Evidence | Options / consequences | Owner decision | Date |
| --- | --- | --- | --- | --- |
| DNV candidate connectivity | DNV poles, conduits, and fittings share `Network_Id` in the inspected network group; the group also showed coincident endpoints and an unconnected crossing | Treat matching IDs as one exploratory connected component; do not invent direct edges between every feature; this can group features without proving electrical connectivity | Same `Network_Id` means same exploratory network component; report geometry gaps, crossings, and uncertainty separately | 2026-09-11 |
| DNV fitting asset type | DNV publishes service boxes, boxes, caps, and kiosks in one fittings layer; most comments are blank and `AM_TYPE` is undocumented | Use one broad type or infer subtypes; inference would overstate incomplete evidence | Use `asset_type = network_fitting`; populate nullable `classification` only from source-supported descriptions | 2026-09-11 |
| Original identifiers | Vancouver publishes layer-specific identifiers and some layers have none; DNV publishes `Asset_Id` and `GlobalID` | Combine, synthesize, or preserve separately | Preserve nullable `source_asset_id` and `source_global_id`; do not synthesize missing IDs | 2026-09-11 |
| Geometry CRS | Vancouver exports report EPSG:4326; DNV FGDB layers report EPSG:26910 | Reproject during normalization or preserve native CRS | Preserve native CRS per municipality and defer shared analysis CRS | 2026-09-11 |
| Abandoned Vancouver conduits | Published as a separate conduit dataset | Drop them, create a separate asset type, or retain lifecycle status | Use `asset_type = conduit`, `status = abandoned`; exclude from active trace unless explicitly included | 2026-09-11 |
| Network ID normalization | DNV publishes `Network_Id`; Vancouver has no shared network ID | Derive IDs, leave null, or use geometry | Copy DNV values; leave Vancouver null; use DNV values only for the approved exploratory component rule | 2026-09-11 |
| Provenance retention | Source fields differ substantially | Copy all fields, drop source detail, or keep a compact common schema with provenance | Keep common provenance fields and raw/interim source attributes; do not expand the common schema unnecessarily | 2026-09-11 |
| Classification field | Vancouver layer names provide broad roles; DNV fittings have incomplete comments and undocumented `AM_Type` codes | Duplicate roles, infer subtypes, or keep classification nullable | Use `asset_type` for broad roles; populate nullable `classification` only from supported source descriptions | 2026-09-11 |

Keep this project small. Do not automate QGIS or introduce infrastructure outside the application scope.
