"""Normalize Vancouver layers using the municipality YAML configuration."""

from pathlib import Path

from streetlight_network.normalize import load_config, normalize_layer


PROJECT_ROOT = Path(__file__).resolve().parents[1]

vancouver_config = load_config(
    PROJECT_ROOT / "configs" / "vancouver.yaml"
)

def main():
    output_directory = PROJECT_ROOT / "data" / "normalized" / "vancouver"
    output_directory.mkdir(parents=True, exist_ok=True)

    for layer_config in vancouver_config["layers"]:
        layer_name = layer_config["source_layer"]

        normalized = normalize_layer(
            source_path=PROJECT_ROOT / layer_config["source_path"],
            config=vancouver_config,
            layer=layer_config,
        )

        output_path = output_directory / f"{layer_config['output_name']}.gpkg"
        normalized.to_file(output_path, driver="GPKG")

        print(f"{layer_name}: {len(normalized)} features -> {output_path}")


if __name__ == "__main__":
    main()
