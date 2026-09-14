import networkx as nx
from shapely.geometry import Point


def line_parts(geometry):
    if geometry.geom_type == "LineString":
        return [geometry]
    if geometry.geom_type == "MultiLineString":
        return list(geometry.geoms)
    return []


def point_key(point):
    return (point.x, point.y)


def build_conduit_graph(conduit):
    """Build an undirected graph from exact conduit endpoints.

    No snapping, proximity connection, or line-crossing connection is applied.
    """
    graph = nx.Graph()
    for _, row in conduit.iterrows():
        for part in line_parts(row.geometry):
            start = Point(part.coords[0])
            end = Point(part.coords[-1])
            graph.add_edge(
                point_key(start),
                point_key(end),
                conduit_id=str(row["source_asset_id"]),
            )
    return graph


def point_nodes(gdf):
    return {
        str(row["source_asset_id"]): point_key(row.geometry)
        for _, row in gdf.iterrows()
        if row.geometry is not None and not row.geometry.is_empty
    }


def trace_poles(poles, conduit, fittings, fitting_id, network_id):
    """Return reachability and conduit paths from one fitting to poles."""
    graph = build_conduit_graph(conduit)
    pole_nodes = point_nodes(poles)
    fitting_nodes = point_nodes(fittings)
    if fitting_id not in fitting_nodes:
        raise ValueError(f"Fitting not found: {fitting_id}")

    fitting_node = fitting_nodes[fitting_id]
    fitting_component = next(
        component for component in nx.connected_components(graph)
        if fitting_node in component
    )
    results = []
    for pole_id, pole_node in pole_nodes.items():
        reachable = pole_node in fitting_component
        conduit_ids = []
        if reachable:
            path = nx.shortest_path(graph, fitting_node, pole_node)
            conduit_ids = [
                graph.edges[start, end]["conduit_id"]
                for start, end in zip(path, path[1:])
            ]
        results.append({
            "network_id": network_id,
            "pole_id": pole_id,
            "fitting_id": fitting_id if reachable else "",
            "conduit_ids": ";".join(conduit_ids),
            "trace_status": "reachable" if reachable else "unreachable",
        })
    return results


def trace_network_fittings(poles, conduit, fittings, network_id):
    """Trace every fitting in one source network to every pole in that network.

    Each fitting is retained as a separate candidate start. This avoids
    assuming that a DNV fitting is a service panel when the source does not
    provide a dedicated, verified service-panel classification. ``inferred``
    is reserved for a future documented inference rule; it is not assigned
    from geometry alone.
    """
    graph = build_conduit_graph(conduit)
    pole_nodes = point_nodes(poles)
    fitting_nodes = point_nodes(fittings)
    results = []
    fitting_rows = fittings.set_index("source_asset_id", drop=False)
    for fitting_id, fitting_node in fitting_nodes.items():
        fitting_row = fitting_rows.loc[fitting_id]
        classification = fitting_row.get("classification")
        confidence = fitting_row.get("classification_confidence")
        if classification in {"service_box", "service_panel"}:
            service_origin = confidence if confidence in {"explicit", "assumed"} else "inferred"
        else:
            service_origin = "unclassified_fitting"
        if fitting_node in graph:
            component = next(
                component for component in nx.connected_components(graph)
                if fitting_node in component
            )
            paths = nx.single_source_shortest_path(graph, fitting_node)
        else:
            component = set()
            paths = {}
        for pole_id, pole_node in pole_nodes.items():
            reachable = pole_node in component
            path = paths.get(pole_node, [])
            conduit_ids = [
                graph.edges[start, end]["conduit_id"]
                for start, end in zip(path, path[1:])
            ]
            results.append({
                "network_id": network_id,
                "fitting_id": fitting_id,
                "fitting_classification": classification or "",
                "service_origin": service_origin,
                "pole_id": pole_id,
                "conduit_ids": ";".join(conduit_ids),
                "trace_status": "reachable" if reachable else "unreachable",
                "trace_note": "" if fitting_node in graph else "fitting_not_on_conduit_graph",
            })
    return results


def remove_subtraces(rows):
    """Drop redundant fitting-start traces using set containment.

    A fitting trace is redundant when its reachable pole IDs and conduit IDs
    are both subsets of another fitting trace in the same source network.
    Identical traces keep the strongest available service-origin evidence.
    """
    by_fitting = {}
    for row in rows:
        by_fitting.setdefault((row["network_id"], row["fitting_id"]), []).append(row)

    signatures = {}
    for key, fitting_rows in by_fitting.items():
        reachable = [r for r in fitting_rows if r["trace_status"] == "reachable"]
        signatures[key] = (
            {r["pole_id"] for r in reachable},
            {cid for r in reachable for cid in r["conduit_ids"].split(";") if cid},
        )

    priority = {"explicit": 0, "assumed": 1, "unclassified_fitting": 2, "inferred": 3}
    keep = set(by_fitting)
    keys = list(signatures)
    for key in keys:
        poles_a, conduits_a = signatures[key]
        for other in keys:
            if key == other:
                continue
            poles_b, conduits_b = signatures[other]
            proper = poles_a < poles_b or conduits_a < conduits_b
            if poles_a <= poles_b and conduits_a <= conduits_b and proper:
                keep.discard(key)
                break
            if poles_a == poles_b and conduits_a == conduits_b:
                origin_a = by_fitting[key][0].get("service_origin", "unclassified_fitting")
                origin_b = by_fitting[other][0].get("service_origin", "unclassified_fitting")
                if (priority.get(origin_a, 99), key[1]) > (priority.get(origin_b, 99), other[1]):
                    keep.discard(key)
                    break
    return [row for key in keep for row in by_fitting[key]]
