"""Summarize DNV network IDs across normalized layers."""

from pathlib import Path

import geopandas as gpd
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

NORMALIZED_FILES = {
    "poles": PROJECT_ROOT / "data/normalized/dnv/poles.gpkg",
    "conduit": PROJECT_ROOT / "data/normalized/dnv/conduit.gpkg",
    "fittings": PROJECT_ROOT / "data/normalized/dnv/fittings.gpkg",
}


def main():
    layers = {
        name: gpd.read_file(path)
        for name, path in NORMALIZED_FILES.items()
    }

    network_ids = {
        name: set(gdf["network_id"].dropna())
        for name, gdf in layers.items()
    }

    all_ids = set().union(*network_ids.values())
    rows = []

    for network_id in sorted(all_ids):
        present_in = [
            name
            for name, ids in network_ids.items()
            if network_id in ids
        ]

        rows.append(
            {
                "network_id": network_id,
                "present_in": ",".join(present_in),
                "has_poles": "poles" in present_in,
                "has_conduit": "conduit" in present_in,
                "has_fittings": "fittings" in present_in,
            }
        )

    report = pd.DataFrame(rows).sort_values("network_id")

    output_path = (
        PROJECT_ROOT / "outputs" / "qa" / "dnv_network_id_coverage.csv"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(output_path, index=False)

    print(report.to_string(index=False))
    print(f"\nWrote network-ID coverage: {output_path}")


if __name__ == "__main__":
    main()
