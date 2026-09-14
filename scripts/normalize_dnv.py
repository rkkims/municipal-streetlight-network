"""Normalize DNV layers using the municipality YAML configuration."""

from pathlib import Path
import tempfile
import zipfile

from streetlight_network.normalize import load_config, normalize_layer


PROJECT_ROOT = Path(__file__).resolve().parents[1]

dnv_config = load_config(PROJECT_ROOT / "configs" / "dnv.yaml")

def extract_geodatabase(zip_path, destination):
    with zipfile.ZipFile(zip_path) as archive:
        archive.extractall(destination)

    geodatabases = list(Path(destination).glob("*.gdb"))
    if len(geodatabases) != 1:
        raise ValueError(
            f"Expected one .gdb directory in {zip_path}; "
            f"found {len(geodatabases)}"
        )

    return geodatabases[0]


def main():
    output_directory = PROJECT_ROOT / "data" / "normalized" / "dnv"
    output_directory.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as temporary_directory:
        for layer_config in dnv_config["layers"]:
            layer_name = layer_config["source_layer"]
            layer_key = layer_config["output_name"]

            layer_directory = Path(temporary_directory) / layer_key
            layer_directory.mkdir()
            gdb_path = extract_geodatabase(
                PROJECT_ROOT / layer_config["source_path"],
                layer_directory,
            )

            normalized = normalize_layer(
                source_path=gdb_path,
                config=dnv_config,
                layer=layer_config,
            )

            output_path = output_directory / f"{layer_key}.gpkg"
            normalized.to_file(output_path, driver="GPKG")

            print(f"{layer_name}: {len(normalized)} features -> {output_path}")


if __name__ == "__main__":
    main()
