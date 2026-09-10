# Conceptual network model

Potential node types are pole, service panel, junction box, and network fitting. A potential edge type is a conduit segment. These are conceptual roles, not a selected schema or confirmed source feature classes. Service-panel availability and identification in DNV require verification.

Actual connectivity rules must be determined from source inspection, including documented identifiers, endpoint relationships, attributes, and manual QGIS review. Present the evidence and ask the user to decide before implementing rules.

- Geometric proximity does not automatically prove electrical connectivity.
- Line crossings do not automatically imply connection.
- Snapping tolerance must not be chosen arbitrarily; measured gaps, source accuracy and metadata must inform a user decision.
- Missing conduit segments may create false disconnections.
- One pole reaching multiple service panels may indicate ambiguity or incorrect topology.
- Electrical capacity is outside scope unless relevant attributes are present.

Graph direction, node creation, edge splitting, endpoint attachment, traversal semantics, and handling of ambiguous service panels remain undecided. A geometric path alone does not establish an energized circuit or actual supply relationship. Preserve uncertainty in outputs and document unsupported conclusions. No network rules are implemented in this scaffold.
