"""Trace all DNV source networks from each fitting to poles."""

from pathlib import Path

import geopandas as gpd
import pandas as pd

from streetlight_network.trace import remove_subtraces, trace_network_fittings


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NORMALIZED_FILES = {
    "poles": PROJECT_ROOT / "data/normalized/dnv/poles.gpkg",
    "conduit": PROJECT_ROOT / "data/normalized/dnv/conduit.gpkg",
    "fittings": PROJECT_ROOT / "data/normalized/dnv/fittings.gpkg",
}
OUTPUT = PROJECT_ROOT / "outputs/traces/dnv_all_network_traces.csv"


def main():
    poles = gpd.read_file(NORMALIZED_FILES["poles"])
    conduit = gpd.read_file(NORMALIZED_FILES["conduit"])
    fittings = gpd.read_file(NORMALIZED_FILES["fittings"])

    network_ids = sorted(
        set(conduit["network_id"].dropna())
        & set(fittings["network_id"].dropna())
        & set(poles["network_id"].dropna())
    )
    rows = []
    for network_id in network_ids:
        network_poles = poles[poles["network_id"] == network_id]
        network_conduit = conduit[conduit["network_id"] == network_id]
        network_fittings = fittings[fittings["network_id"] == network_id]
        rows.extend(
            trace_network_fittings(
                poles=network_poles,
                conduit=network_conduit,
                fittings=network_fittings,
                network_id=network_id,
            )
        )

    raw_trace_rows = len(rows)
    rows = remove_subtraces(rows)
    result = pd.DataFrame(rows)
    if not result.empty:
        result = result.sort_values(["network_id", "fitting_id", "pole_id"])
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUTPUT, index=False)
    print(f"Networks traced: {len(network_ids)}")
    print(f"Raw trace rows: {raw_trace_rows}")
    print(f"Trace rows: {len(result)}")
    if not result.empty:
        print(result["trace_status"].value_counts().to_string())
    print(f"\nWrote all-network trace: {OUTPUT}")


if __name__ == "__main__":
    main()
