"""Create the normalized-layer QA summary used for review and the application package."""

from pathlib import Path

import geopandas as gpd
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT = PROJECT_ROOT / "outputs" / "qa" / "normalized_summary.csv"
NORMALIZED_FILES = {
    "DNV poles": "data/normalized/dnv/poles.gpkg",
    "DNV conduits": "data/normalized/dnv/conduit.gpkg",
    "DNV fittings": "data/normalized/dnv/fittings.gpkg",
    "Vancouver poles": "data/normalized/vancouver/poles.gpkg",
    "Vancouver conduits": "data/normalized/vancouver/conduits.gpkg",
    "Vancouver abandoned conduits": "data/normalized/vancouver/abandoned_conduits.gpkg",
    "Vancouver junction boxes": "data/normalized/vancouver/junction_boxes.gpkg",
    "Vancouver service panels": "data/normalized/vancouver/service_panels.gpkg",
}
INTERPRETATIONS = {
    "DNV poles": "Network_Id is present for some poles; same-ID grouping is exploratory and must be checked against conduit geometry.",
    "DNV conduits": "Network_Id is available; endpoint continuity is not proof of energized service.",
    "DNV fittings": "Combined fittings layer; comments provide sparse, sometimes assumed subtypes.",
    "Vancouver poles": "No shared connectivity identifier was found in the inspected source.",
    "Vancouver conduits": "No shared connectivity identifier was found in the inspected source.",
    "Vancouver abandoned conduits": "Lifecycle status is abandoned; exclude from active traces unless justified.",
    "Vancouver junction boxes": "Layer role identifies junction boxes; connectivity is not encoded.",
    "Vancouver service panels": "Layer role identifies service panels; electrical capacity is unavailable.",
}

def check_layer(name, relative_path):
    path = PROJECT_ROOT / relative_path
    if not path.exists():
        return {"layer": name, "path": str(path), "exists": False}
    gdf = gpd.read_file(path)
    rows = len(gdf)
    missing = int(gdf.geometry.isna().sum())
    invalid = int((~gdf.geometry.is_valid).sum())
    result = {
        "layer": name, "path": str(path), "exists": True, "rows": rows,
        "crs": gdf.crs.to_string() if gdf.crs else None,
        "missing_geometry": missing,
        "missing_geometry_pct": round(100 * missing / rows, 3) if rows else None,
        "invalid_geometry": invalid,
        "invalid_geometry_pct": round(100 * invalid / rows, 3) if rows else None,
        "missing_source_asset_id": None, "duplicate_source_asset_id": None,
        "missing_network_id": None, "unique_network_id": None,
        "interpretation": INTERPRETATIONS.get(name),
    }
    if "source_asset_id" in gdf:
        result["missing_source_asset_id"] = int(gdf.source_asset_id.isna().sum())
        result["duplicate_source_asset_id"] = int(
            gdf.source_asset_id.dropna().duplicated().sum()
        )
    if "network_id" in gdf:
        result["missing_network_id"] = int(gdf.network_id.isna().sum())
        result["unique_network_id"] = int(gdf.network_id.nunique(dropna=True))
    return result

def main():
    report = pd.DataFrame(check_layer(name, path) for name, path in NORMALIZED_FILES.items())
    report = report[[column for column in report.columns if column != "path"] + ["path"]]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(OUTPUT, index=False)
    print(report.to_string(index=False))
    print(f"\nWrote QA summary: {OUTPUT}")

if __name__ == "__main__":
    main()
