# Data sources

This inventory records the official sources used for the project. Download
timestamps, response headers, byte sizes, and SHA-256 checksums are stored in
the adjacent `.acquisition.json` files in `data/raw/`.

## Vancouver

Publisher: [City of Vancouver Open Data](https://opendata.vancouver.ca/)
License: [Open Government Licence - Vancouver](https://opendata.vancouver.ca/pages/licence/)
Native CRS selected: EPSG:4326 (GeoJSON export)

| Dataset | Official metadata | Records | Geometry | Local file |
| --- | --- | ---: | --- | --- |
| Street-light poles | [metadata](https://opendata.vancouver.ca/explore/dataset/street-lighting-poles/information/) | 57,984 | Point | `data/raw/vancouver/street-lighting-poles.geojson` |
| Street-light conduits | [metadata](https://opendata.vancouver.ca/explore/dataset/street-lighting-conduits/information/) | 65,456 | LineString, MultiLineString, Point | `data/raw/vancouver/street-lighting-conduits.geojson` |
| Junction boxes | [metadata](https://opendata.vancouver.ca/explore/dataset/street-lighting-junction-boxes/information/) | 7,947 | Point | `data/raw/vancouver/street-lighting-junction-boxes.geojson` |
| Service panels | [metadata](https://opendata.vancouver.ca/explore/dataset/street-lighting-service-panels/information/) | 1,455 | Point | `data/raw/vancouver/street-lighting-service-panels.geojson` |
| Abandoned conduits | [metadata](https://opendata.vancouver.ca/explore/dataset/street-lighting-abandoned-conduits/information/) | 774 | LineString | `data/raw/vancouver/street-lighting-abandoned-conduits.geojson` |

The portal describes these layers as parts of one street-lighting network. The
inspected exports do not provide a shared connectivity identifier across the
layers. Vancouver is therefore normalized and QA-checked, but network tracing
is deferred.

## District of North Vancouver

Publisher: [District of North Vancouver GEOweb](https://geoweb.dnv.org/data/)
License: Open Government Licence - North Vancouver, version 2.0 (as stated in
the linked metadata pages)
Native CRS observed in downloaded FGDB layers: EPSG:26910

| Dataset | Metadata | Description | Local working source |
| --- | --- | --- | --- |
| Street-light poles | [metadata](https://geoweb.dnv.org/data/metadata.php?dataset=LgtStreetLightPoles) | Pole/standard locations | `data/raw/dnv/LgtStreetLightPoles_fgdb.zip` |
| Street-light conduit | [metadata](https://geoweb.dnv.org/data/metadata.php?dataset=LgtStreetLightConduit) | Wiring encased in conduit; power-supply paths | `data/raw/dnv/LgtStreetLightConduit_fgdb.zip` |
| Street-light network fittings | [metadata](https://geoweb.dnv.org/data/metadata.php?dataset=LgtStreetLightFittings) | Service panels, boxes, caps, and kiosks in one layer | `data/raw/dnv/LgtStreetLightFittings_fgdb.zip` |

DNV also publishes SHP, DWG, and KML exports. The fittings KML and SHP were
inspected as corroborating formats; the FGDB is the working source. The fittings
layer contains `Asset_Id`, `GlobalID`, `Network_Id`, `AM_Type`, and `Comments`.
`Comments` provide sparse free-text descriptions, while `AM_Type` values `1`
and `2` have no published code dictionary. No separate DNV service-panel or
junction-box layer was identified.

## Acquisition and reproduction

The selected files were downloaded on 2026-09-10 UTC using direct HTTP GET
requests with no feature filters or pagination. Vancouver used complete
GeoJSON exports with `epsg=4326`; DNV used the official FGDB ZIP archives.

Run a future acquisition with:

```bash
python3 scripts/download_data.py
```

The script preserves raw files, validates GeoJSON/ZIP structure, records
acquisition sidecars, and skips files whose recorded checksum already matches.
Portal timestamps and HTTP file timestamps identify the downloaded snapshot;
they are not survey dates. Raw files remain outside Git.
