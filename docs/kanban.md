# Kanban

P0 = required before application; P1 = useful if time allows; P2 = explicitly defer.

Each checkbox is a card. Move cards between columns as work progresses; include evidence or artifact links when done, and a reason plus next action when blocked. Only source verification is READY initially. Documentation placeholders do not complete later implementation or packaging cards. The initial README includes a text pipeline; the P1 diagram card remains a later presentation enhancement.

## BACKLOG

### P0 — Source understanding

- [ ] Download one sample/source set from each municipality
- [ ] Inspect file formats
- [ ] Inspect CRS
- [ ] Inspect geometry types
- [ ] Inspect key attributes
- [ ] Determine whether IDs encode connectivity
- [ ] Determine whether conduit endpoints coincide with nodes

### P0 — DNV network trace

- [ ] Load DNV pole/conduit/fitting layers in QGIS
- [ ] Identify service-panel features
- [ ] Inspect actual topology visually
- [ ] Measure endpoint gaps
- [ ] Define evidence-based connectivity rules
- [ ] Build initial graph
- [ ] Select one pole
- [ ] Trace pole to service panel
- [ ] Validate the trace visually in QGIS
- [ ] Identify at least one broken or ambiguous trace
- [ ] Document how the broken trace was handled

### P0 — Cross-municipality normalization

- [ ] Compare Vancouver and DNV schemas
- [ ] Define minimal common schema
- [ ] Create municipality-specific config mappings
- [ ] Implement normalized output
- [ ] Preserve original source IDs
- [ ] Preserve provenance/source information

### P0 — QA

- [ ] Invalid geometry check
- [ ] Duplicate identifier check
- [ ] Missing geometry check
- [ ] Dangling conduit endpoint check
- [ ] Isolated-node check
- [ ] Poles traceable to service panel
- [ ] Ambiguous multi-panel trace check
- [ ] Produce concise QA summary

### P0 — Application package

- [ ] Produce one clean QGIS map screenshot
- [ ] Produce one highlighted network trace screenshot
- [ ] Finish README
- [ ] Write methodology
- [ ] Write limitations
- [ ] Document unavailable electrical information
- [ ] Add reproduction instructions
- [ ] Prepare resume project bullets
- [ ] Prepare short application message
- [ ] Final repo cleanup
- [ ] Apply

### P1 — Useful if time allows

- [ ] Add Vancouver network trace
- [ ] Compare traceability between municipalities
- [ ] Export normalized GeoPackage
- [ ] Create small CSV QA summary
- [ ] Add simple automated tests
- [ ] Add one architecture diagram
- [ ] Add one network-model diagram

### P2 — Do not do before application

- [ ] PostGIS
- [ ] Docker
- [ ] cloud deployment
- [ ] web application
- [ ] dashboard
- [ ] API
- [ ] advanced cartography
- [ ] electrical load-flow analysis
- [ ] structural-capacity modeling
- [ ] large-scale optimization
- [ ] second asset domain
- [ ] additional municipalities

## READY

### P0 — Source understanding

- [ ] Verify official Vancouver street-light datasets
- [ ] Verify official DNV street-light datasets

Record evidence in [data-sources.md](data-sources.md). Verification means locating official source pages, confirming available categories, and recording verified metadata or explicit unknowns. No network assumptions are required.

## IN PROGRESS

Empty.

## BLOCKED

Empty. Move a card here only when an actual blocker is identified.

## DONE

Empty. This board tracks the planned investigation and application work.
