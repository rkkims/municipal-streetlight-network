# Kanban

Clikan is now the live task board; this five-column list is the migration snapshot. Run `./scripts/clikan show` from the repository root. Task priorities and original columns are preserved in labels because Clikan has only todo/inprogress/done states. Update a stale READY/BACKLOG label when describing a moved task; the Clikan column is its current execution state. P2 remains deferred.

Commands: `./scripts/clikan promote ID` starts a todo task; promoting it again marks it done. `./scripts/clikan regress ID` moves it back. The project board is stored in `.clikan/board.yaml`, separate from the personal board. The wrapper requires Clikan on this VM at `/home/ubuntu/.local/bin/clikan`; adjust that executable path on another machine.

P0 = required before application; P1 = useful if time allows; P2 = explicitly defer.

Each checkbox is a card. Move cards between columns as work progresses; include evidence or artifact links when done, and a reason plus next action when blocked. Source verification and acquisition are complete; source inspection is next. Documentation placeholders do not complete later implementation or packaging cards. The initial README includes a text pipeline; the P1 diagram card remains a later presentation enhancement.

## BACKLOG

### P0 — Source understanding

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

- [ ] Inspect key attributes

- [ ] Inspect geometry types

- [ ] Inspect CRS

- [ ] Inspect file formats

### P0 — Source understanding


Record evidence in [data-sources.md](data-sources.md). Verification means locating official source pages, confirming available categories, and recording verified metadata or explicit unknowns. No network assumptions are required.

## IN PROGRESS

Empty.

## BLOCKED

Empty. Move a card here only when an actual blocker is identified.

## DONE

### P0 — Source understanding

- [x] Verify official Vancouver street-light datasets — [source evidence](data-sources.md)
- [x] Verify official DNV street-light datasets — [source evidence](data-sources.md)
- [x] Download one sample/source set from each municipality — five Vancouver GeoJSONs (EPSG:4326) and three DNV FGDB ZIPs; [acquisition ledger](data-sources.md#per-source-download-ledger)
