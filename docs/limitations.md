# Limitations

This project demonstrates a small, reproducible GIS and network-analysis
workflow. Its findings describe what is represented in the published data;
they are not engineering certification or a design for 5G deployment.

## Electrical capacity

The public Vancouver and DNV layers do not provide the circuit ratings, panel
ratings, conductor sizes, phase, existing load, or spare capacity needed to
calculate available electrical capacity. The project therefore does not model
or infer spare capacity. Any capacity conclusion requires records from the
municipality or utility and review by a qualified electrical professional.

## Connectivity and trace interpretation

The DNV trace uses `Network_Id` as an exploratory grouping signal and checks it
against conduit geometry. It identifies mapped reachable and unreachable poles
within the selected example network. This does not prove that a conduit is
energized, that a fitting is a service panel, or that electricity reaches every
pole in the component.

The DNV fittings layer combines several feature types. A small subset of
records receives a subtype from explicit or uncertain `Comments` wording; the
remaining fittings are unclassified. Comments such as “assumed” or
“proposed” remain flagged and are not treated as confirmed infrastructure.

The measured gap between the two example conduit components is evidence of a
mapped discontinuity. It may represent missing mapping, a different asset,
positional error, or a real break. No automatic snapping or gap repair is
performed.

Vancouver publishes separate poles, conduits, junction-box, and service-panel
layers, but the inspected exports do not provide a shared connectivity ID.
Vancouver network tracing is therefore outside the current evidence-supported
scope.

## Candidate-site decisions outside this project

The inventory does not establish structural suitability, antenna height,
radio coverage, permitting availability, heritage status, sightline impacts,
or carrier attachment rights. Those require structural, radio-frequency,
municipal, legal, or carrier records.

## Source quality and currency

Municipal datasets can be incomplete, stale, generalized, or maintained at
different times. Published geometry and attributes are preserved as received;
the project does not claim positional accuracy beyond the source metadata.
