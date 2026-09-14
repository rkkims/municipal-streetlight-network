# Conceptual network model

Potential node types are pole, service panel, junction box, and network fitting. A potential edge type is a conduit segment. These are conceptual roles, not a selected schema or confirmed source feature classes. DNV provides a combined network-fittings layer rather than separate junction-box and service-panel layers; service-panel and junction-box identification within it requires source inspection and verification.

Actual connectivity rules must be determined from source inspection, including documented identifiers, endpoint relationships, attributes, and manual QGIS review. For the DNV exploratory trace, the project owner has selected matching `Network_Id` as the rule for treating elements as members of the same connected network component. This is a project interpretation of the public data, not proof of electrical connectivity; geometry gaps, crossings, and contradictory evidence must still be reported.

- Geometric proximity does not automatically prove electrical connectivity.
- Line crossings do not automatically imply connection.
- Snapping tolerance must not be chosen arbitrarily; measured gaps, source accuracy and metadata must inform a user decision.
- Missing conduit segments may create false disconnections.
- One pole reaching multiple service panels may indicate ambiguity or incorrect topology.
- Electrical capacity is outside scope unless relevant attributes are present.

The current DNV implementation uses an undirected graph whose nodes are exact
conduit endpoint coordinates and whose edges are conduit segments. Elements
with different `Network_Id` values are not mixed. Matching IDs are not
represented as invented direct edges between every pair of features. The
all-network runner traces from each fitting as a candidate start and keeps the
source fitting ID explicit because a dedicated service-panel classification is
not verified. A geometric path or matching ID alone does not establish an
energized circuit or actual supply relationship. Preserve uncertainty in
outputs and document unsupported conclusions.

When running all DNV networks, redundant fitting-start traces are removed only
when both their reachable pole set and conduit set are contained in another
trace. Identical traces retain the strongest available source classification:
explicit, then assumed, then unclassified. This is a reporting reduction, not
a new connectivity rule.
