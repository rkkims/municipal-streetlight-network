from pathlib import Path
import re

import geopandas as gpd
import yaml


_UNCERTAINTY_TERMS = re.compile(r"\b(assumed|approximate|approx|possibly|proposed|potential)\b", re.I)


def classify_fitting_comment(comment):
    """Return a conservative subtype and confidence from DNV free text.

    This intentionally returns no classification when the wording does not
    identify a fitting subtype.  It does not interpret AM_Type codes.
    """
    text = "" if comment is None else str(comment).strip()
    if not text:
        return None, None

    patterns = (
        ("service_panel", r"\bservice\s+panel\b"),
        ("junction_box", r"\bjunction\s+box\b|\bjunction\b"),
        ("service_box", r"\bservice\s+box\b"),
        ("service_pole", r"\bservice\s+pole\b|\bpower\s+supply\s+pole\b"),
    )
    for classification, pattern in patterns:
        if re.search(pattern, text, re.I):
            confidence = "assumed" if _UNCERTAINTY_TERMS.search(text) else "explicit"
            return classification, confidence
    return None, None

def load_config(path):
    path = Path(path)

    with path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    if not isinstance(config, dict):
        raise ValueError("Config must contain a top-level mapping")

    required_keys = {"municipality", "source_crs", "layers"}
    missing_keys = required_keys - config.keys()
    if missing_keys:
        raise ValueError(f"Missing configuration keys: {sorted(missing_keys)}")

    if not isinstance(config["layers"], list):
        raise ValueError("Config key 'layers' must contain a list")

    return config

def normalize_layer(source_path, config, layer):
    source = gpd.read_file(source_path)

    normalized = gpd.GeoDataFrame(
        {
            "municipality": config["municipality"],
            "source_crs": config["source_crs"],
            "source_layer": layer["source_layer"],
            "asset_type": layer["asset_type"],
            "status": layer.get("status"),
            "source_asset_id": None,
            "source_global_id": None,
            "network_id": None,
            "classification": None,
            "classification_source": None,
            "classification_confidence": None,
            "source_comments": None,
        },
        index=source.index,
        geometry=source.geometry,
        crs=source.crs,
    )

    for target_field, source_field in layer.get("fields", {}).items():
        if source_field is None:
            normalized[target_field] = None
        else:
            if source_field not in source.columns:
                raise ValueError(
                    f"Source field '{source_field}' was not found in "
                    f"layer '{layer['source_layer']}'"
                )

            normalized[target_field] = source[source_field]

    # Preserve free-text comments as provenance.  For DNV fittings, derive a
    # subtype only when the wording is clear; comments remain the evidence.
    comment_field = next(
        (field for field in source.columns if field.lower() == "comments"), None
    )
    if comment_field is not None:
        normalized["source_comments"] = source[comment_field]
        if layer["asset_type"] == "network_fitting":
            derived = source[comment_field].map(classify_fitting_comment)
            normalized["classification"] = derived.map(lambda value: value[0])
            normalized["classification_source"] = derived.map(
                lambda value: "comments" if value[0] is not None else None
            )
            normalized["classification_confidence"] = derived.map(lambda value: value[1])

    return normalized
