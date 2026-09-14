# Data sources

## City of Vancouver

### Street-light poles

https://opendata.vancouver.ca/explore/dataset/street-lighting-poles/information/

The City's Street Lighting network includes:

street lighting poles (nodes)
conduits (ducts)
abandoned conduits
junction boxes
service panels

### Street-light conduits

https://opendata.vancouver.ca/explore/dataset/street-lighting-conduits/information/

The street light conduits (ducts) dataset represents part of the City's Street Lighting network, which also includes:

street lighting poles (nodes)
abandoned conduits
junction boxes
service panels

### Junction boxes

https://opendata.vancouver.ca/explore/dataset/street-lighting-junction-boxes/information/

The City's Street Lighting network includes:

street lighting poles (nodes)
conduits (ducts)
abandoned conduits
junction boxes
service panels

### Service panels

https://opendata.vancouver.ca/explore/dataset/street-lighting-service-panels/information/

The City's Street Lighting network includes:

street lighting poles (nodes)
conduits (ducts)
abandoned conduits
junction boxes
service panels

### Abandoned conduits (if useful)

https://opendata.vancouver.ca/explore/dataset/street-lighting-abandoned-conduits/information

The City's Street Lighting network includes:

street lighting poles (nodes)
conduits (ducts)
abandoned conduits
junction boxes
service panels

## District of North Vancouver

### Street-light poles

https://geoweb.dnv.org/data/metadata.php?dataset=LgtStreetLightPoles

Street light poles, or standards, that are both owned and maintained by BC Hydro and by the District of North Vancouver. These street lights are typically mounted on wooden poles or metal ornamental poles.

SHP
https://geoweb.dnv.org/Products/Data/SHP/LgtStreetLightPoles_shp.zip

FGDB
https://geoweb.dnv.org/Products/Data/FGDB/LgtStreetLightPoles_fgdb.zip

DWG
https://geoweb.dnv.org/Products/Data/DWG/LgtStreetLightPoles_dwg.zip

KML
https://geoweb.dnv.org/Products/Data/KML/LgtStreetLightPoles_kml.zip

### Street-light conduit

https://geoweb.dnv.org/data/metadata.php?dataset=LgtStreetLightConduit

Linear features that represent the location of street lighting wiring encased in a conduit. These lines represent the power supply for the street lighting network.

SHP
https://geoweb.dnv.org/Products/Data/SHP/LgtStreetLightConduit_shp.zip

FGDB
https://geoweb.dnv.org/Products/Data/FGDB/LgtStreetLightConduit_fgdb.zip

DWG
https://geoweb.dnv.org/Products/Data/DWG/LgtStreetLightConduit_dwg.zip

KML
https://geoweb.dnv.org/Products/Data/KML/LgtStreetLightConduit_kml.zip

### Street-light network fittings

Street lighting network features including service panels, boxes, caps and kiosks. These features represent various fittings that are part of the street lighting network.

DNV does not publish separate junction-box or service-panel layers in the source inventory used here. Those feature types, if present, must be identified as records within this combined fittings layer using verified attributes and/or careful QGIS inspection. The existence of a fittings layer does not establish that every fitting is a service panel or that all junction boxes are represented.

The DNV KML export was also inspected as a human-readable attribute aid. It contains 1,576 placemarks and exposes fields including `Asset_Id`, `Network_Id`, `AM_Type`, `AM_Owner`, `Comments`, and `GlobalID`. `Comments` includes service-box descriptions such as `BC Hydro Service Box`, `Service Box`, and `Assumed location of service box`, but many records have blank comments. `AM_Type` has only the values `1` and `2`; no type-code dictionary was supplied, so those codes are not interpreted here. `Network_Id` is populated for 1,551 of 1,576 placemarks and may be useful evidence for grouping, but it has not been accepted as a connectivity rule.

The DNV SHP export was inspected as well. It contains the same 1,576 features and reports EPSG:26910. Its attribute values match the KML inspection, but Shapefile field names are abbreviated to ten characters (for example, `ASSET_ID`, `NETWORK_ID`, `AM_TYPE`, and `COMMENTS`). It adds no verified fitting-type dictionary. The FGDB remains the preferred working source; KML and SHP are retained as corroborating format exports.

The DNV fittings layer includes a `Network_Id` field, but its connectivity meaning still requires comparison with the pole and conduit layers. Shared values across layers would be useful evidence; the field must not be treated as a graph edge or electrical connection until that comparison and visual validation are complete.

Initial cross-layer inspection found that `Network_Id` values are shared across DNV asset layers. This supports treating the field as a candidate network-grouping key for further investigation. Counts of shared values, missing values, and one-to-many relationships should be recorded before any graph construction; shared IDs still do not by themselves prove physical or electrical connectivity.

https://geoweb.dnv.org/data/metadata.php?dataset=LgtStreetLightFittings

SHP
https://geoweb.dnv.org/Products/Data/SHP/LgtStreetLightFittings_shp.zip

FGDB
https://geoweb.dnv.org/Products/Data/FGDB/LgtStreetLightFittings_fgdb.zip

DWG
https://geoweb.dnv.org/Products/Data/DWG/LgtStreetLightFittings_dwg.zip

KML
https://geoweb.dnv.org/Products/Data/KML/LgtStreetLightFittings_kml.zip

## Acquisition record

### Status and scope

Metadata reviewed on **2026-09-10 (UTC)**. All eight source datasets were subsequently downloaded on 2026-09-10 (UTC); see the completed ledger below. The URLs and descriptions above are retained as collected by the project owner. This record distinguishes metadata access from actual data acquisition; the owner selected Vancouver GeoJSON in EPSG:4326 and DNV FGDB ZIP archives. No analysis CRS or connectivity rule has been selected.

### Vancouver: verified catalogue metadata

The links below are the exact JSON metadata requests used: HTTP GET, no query parameters, no feature filters, and no pagination. These requests return dataset metadata rather than feature records. The publisher is **City of Vancouver** for all five datasets. Each metadata response identifies the [Open Government Licence - Vancouver](https://opendata.vancouver.ca/pages/licence/).

| Dataset / metadata request | Reported records | Reported geometry types | Portal `data_processed` timestamp (UTC) |
| --- | ---: | --- | --- |
| [street-lighting-poles](https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/street-lighting-poles) | 57,984 | Point | 2026-09-07T13:36:17+00:00 |
| [street-lighting-conduits](https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/street-lighting-conduits) | 65,456 | LineString, MultiLineString, Point | 2026-08-03T13:36:46+00:00 |
| [street-lighting-junction-boxes](https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/street-lighting-junction-boxes) | 7,947 | Point | 2026-09-07T13:35:02+00:00 |
| [street-lighting-service-panels](https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/street-lighting-service-panels) | 1,455 | Point | 2026-09-07T13:35:13+00:00 |
| [street-lighting-abandoned-conduits](https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/street-lighting-abandoned-conduits) | 774 | LineString | 2024-11-18T14:35:55+00:00 |

These are catalogue-reported values, not results of inspecting downloaded features. A portal processing timestamp is not an asset survey date or an immutable source version. The dataset descriptions state that the website extract is refreshed weekly, with real-world changes subject to maintenance priorities. The native/source CRS has not been verified from these metadata responses. The downloaded Vancouver files are readable as EPSG:4326 through Fiona/GDAL. Feature geometry QA remains pending.

The inspected Vancouver attributes do not expose a shared network or connectivity identifier across poles, conduits, junction boxes, service panels, and abandoned conduits. Vancouver poles include `node_number`, service panels include `service_panel_number`, and conduits include `wireset_type`, but these fields do not by themselves define cross-layer connections. This is an observed schema limitation, not a conclusion that the underlying municipal system lacks connectivity relationships.

The City’s additional ArcGIS service endpoints were reviewed and excluded from the normalization inputs because they added no cross-layer connectivity information. The downloaded Open Data exports remain the sole Vancouver inputs for this project.

Acquisition used the complete GeoJSON API export for each dataset with `epsg=4326`, without feature filters or pagination. Original response bytes were saved unchanged.

| Dataset | Export page | Destination directory | Download state |
| --- | --- | --- | --- |
| street-lighting-poles | [Export options](https://opendata.vancouver.ca/explore/dataset/street-lighting-poles/export/) | `data/raw/vancouver/` | Downloaded: GeoJSON, EPSG:4326 |
| street-lighting-conduits | [Export options](https://opendata.vancouver.ca/explore/dataset/street-lighting-conduits/export/) | `data/raw/vancouver/` | Downloaded: GeoJSON, EPSG:4326 |
| street-lighting-junction-boxes | [Export options](https://opendata.vancouver.ca/explore/dataset/street-lighting-junction-boxes/export/) | `data/raw/vancouver/` | Downloaded: GeoJSON, EPSG:4326 |
| street-lighting-service-panels | [Export options](https://opendata.vancouver.ca/explore/dataset/street-lighting-service-panels/export/) | `data/raw/vancouver/` | Downloaded: GeoJSON, EPSG:4326 |
| street-lighting-abandoned-conduits | [Export options](https://opendata.vancouver.ca/explore/dataset/street-lighting-abandoned-conduits/export/) | `data/raw/vancouver/` | Downloaded: GeoJSON, EPSG:4326 |

### DNV: metadata and acquisition routes

Publisher: **District of North Vancouver**. Metadata pages were accessed by HTTP GET using their `dataset` query parameter; no feature query or download was performed. The [official catalogue](https://geoweb.dnv.org/data/) states weekly refreshes. The individual metadata pages describe maintenance from Transportation engineering drawings and give 2007 as the year first posted to GIS; **2007 is not the current dataset version**. No current per-file update timestamp was established.

Licence evidence: the Terms and Conditions section embedded in the DNV metadata pages identifies **Open Government Licence - North Vancouver, version 2.0**. Its default attribution is: “Contains information licensed under the Open Government Licence - North Vancouver.” Recheck the terms in force when acquiring data.

The three layer metadata pages leave coordinate system, projection, geometry type, and data dictionary unspecified (displayed as “Not Applicable”). This does not mean the downloadable files have no CRS or geometry. Inspection of the downloaded FGDB layers reports **EPSG:26910** for DNV. This is an observed source CRS, not a final cross-municipality analysis CRS. Metadata describes a network assembled from digitized engineering drawings and acknowledges incomplete spatial information; it does not establish usable electrical connectivity.

| Source identifier | Exact metadata URL | Available download links recorded above | Current file version |
| --- | --- | --- | --- |
| `LgtStreetLightPoles` | [Metadata](https://geoweb.dnv.org/data/metadata.php?dataset=LgtStreetLightPoles) | SHP, FGDB, DWG, KML ZIP links | Downloaded FGDB inspected; CRS EPSG:26910 |
| `LgtStreetLightConduit` | [Metadata](https://geoweb.dnv.org/data/metadata.php?dataset=LgtStreetLightConduit) | SHP, FGDB, DWG, KML ZIP links | Downloaded FGDB inspected; CRS EPSG:26910 |
| `LgtStreetLightFittings` | [Metadata](https://geoweb.dnv.org/data/metadata.php?dataset=LgtStreetLightFittings) | SHP, FGDB, DWG, KML ZIP links | Downloaded FGDB inspected; CRS EPSG:26910 |

Download method: HTTP GET of each recorded FGDB ZIP URL, without query parameters or pagination. Original archives are retained in `data/raw/dnv/`. All three passed ZIP CRC checks and contain `.gdb` directories. They have been inspected for source CRS; no reprojection or feature transformation has been performed. HTTP file dates below are not asset survey dates.

### Per-source download ledger

Nine downloads completed successfully, including the DNV fittings KML used for attribute inspection. Each raw file has an adjacent `.acquisition.json` recording request/final URLs, parameters, status, response headers, size, checksum, and validation evidence. No redirects occurred. HTTP status was 200 for all downloads; no feature filters or pagination were used.

| Source identifier / exact download URL | Downloaded at (UTC) | Local file | Bytes | SHA-256 | HTTP Last-Modified |
| --- | --- | --- | ---: | --- | --- |
| [LgtStreetLightConduit](https://geoweb.dnv.org/Products/Data/FGDB/LgtStreetLightConduit_fgdb.zip) | 2026-09-10T18:05:28.906691+00:00 | `data/raw/dnv/LgtStreetLightConduit_fgdb.zip` | 502490 | `ffdc62c8af6ad24fee5cc7274589d4c20b11ae4ab779fd734ff289a664acb261` | Sat, 05 Sep 2026 08:29:51 GMT |
| [LgtStreetLightFittings](https://geoweb.dnv.org/Products/Data/FGDB/LgtStreetLightFittings_fgdb.zip) | 2026-09-10T18:05:29.391479+00:00 | `data/raw/dnv/LgtStreetLightFittings_fgdb.zip` | 109596 | `7e5fc1b9f2ff32bcb06651cd762f98ec6b46aedd7cdc59f738462f906a2b23d7` | Sat, 05 Sep 2026 08:28:41 GMT |
| [LgtStreetLightFittings KML](https://geoweb.dnv.org/Products/Data/KML/LgtStreetLightFittings_kml.zip) | 2026-09-10T19:14:33.282500+00:00 | `data/raw/dnv/LgtStreetLightFittings_kml.zip` | 163508 | `246e51a0f6d995ab5cc91144caefd02b837119edf0f8faa370226977233afd22` | Not recorded |
| [LgtStreetLightFittings SHP](https://geoweb.dnv.org/Products/Data/SHP/LgtStreetLightFittings_shp.zip) | 2026-09-10T19:16:10.293828+00:00 | `data/raw/dnv/LgtStreetLightFittings_shp.zip` | 133026 | `7f1c8905de9f140d61f2536cbd4079935fec97a41e3285a76f433741a6910e2a` | Sat, 05 Sep 2026 08:28:42 GMT |
| [LgtStreetLightPoles](https://geoweb.dnv.org/Products/Data/FGDB/LgtStreetLightPoles_fgdb.zip) | 2026-09-10T18:05:28.190034+00:00 | `data/raw/dnv/LgtStreetLightPoles_fgdb.zip` | 408498 | `1bcf1423fb822e78e4fe9e31b2158d919ae641fd210065b3a6ae6d3ad9040f40` | Sat, 05 Sep 2026 08:31:54 GMT |
| [street-lighting-abandoned-conduits](https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/street-lighting-abandoned-conduits/exports/geojson?epsg=4326) | 2026-09-10T18:05:27.444143+00:00 | `data/raw/vancouver/street-lighting-abandoned-conduits.geojson` | 482463 | `05acbfa0575190200f2cf9376d9a8d8c58af72102f6f3b972fe35b39f5c130b7` | Not supplied |
| [street-lighting-conduits](https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/street-lighting-conduits/exports/geojson?epsg=4326) | 2026-09-10T18:05:25.743880+00:00 | `data/raw/vancouver/street-lighting-conduits.geojson` | 33487880 | `c374e48bb018d577a3689c151cde10c848d980eac3233c98c41fe864cf25708c` | Not supplied |
| [street-lighting-junction-boxes](https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/street-lighting-junction-boxes/exports/geojson?epsg=4326) | 2026-09-10T18:05:26.984107+00:00 | `data/raw/vancouver/street-lighting-junction-boxes.geojson` | 1843440 | `59a5896eb6917020d37cc28af1de01864739ea2304be0bbe14f03018dedfebed` | Not supplied |
| [street-lighting-poles](https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/street-lighting-poles/exports/geojson?epsg=4326) | 2026-09-10T18:05:14.214955+00:00 | `data/raw/vancouver/street-lighting-poles.geojson` | 14730079 | `93b32335f578a6c2052655bb415d7582a147d578242c28c633c53df9a30c2cf0` | Not supplied |
| [street-lighting-service-panels](https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/street-lighting-service-panels/exports/geojson?epsg=4326) | 2026-09-10T18:05:27.225820+00:00 | `data/raw/vancouver/street-lighting-service-panels.geojson` | 363364 | `71aaf37f37a0f6a35550f66867e7b6f23493b11468adb3cf266b0edc2eac0e94` | Not supplied |

Vancouver feature counts match the catalogue counts recorded above. All five files parse as GeoJSON FeatureCollections and Fiona/GDAL reports EPSG:4326. The inspected DNV FGDB layers report EPSG:26910. This verifies delivery and CRS interpretation, not geometry correctness or network connectivity. DNV ZIPs passed CRC checks; feature-level completeness remains unverified.

Vancouver responses supplied neither ETag nor Last-Modified. DNV supplied both; their exact values are preserved in the acquisition sidecars. Catalogue timestamps above remain separate from HTTP file timestamps. Metadata JSON/HTML and Vancouver licence HTML were saved alongside raw files; DNV metadata HTML includes its licence terms.

### Reproduce acquisition

From the repository root, with the existing Python environment containing `requests`:

```bash
python3 scripts/download_data.py
```

The script downloads the eight selected formats, checks GeoJSON/ZIP structure, records acquisition sidecars, and preserves originals. On repeat runs it verifies existing checksums and skips matching files; it refuses to overwrite unexplained existing files. Source URLs are live and may change, so a future fresh download is not guaranteed to reproduce the same bytes. Keep the current raw files and checksums to identify this snapshot. Metadata/licence snapshots were fetched separately from the linked metadata/licence URLs; the script does not refresh them.

### Procedure for future acquisitions

1. Record the exact request URL, redirects/final URL, query parameters, chosen format, UTC retrieval time, HTTP status, and any `ETag` or `Last-Modified` headers. Mark absent headers explicitly; do not treat them as survey dates.
2. Record the actual local filename and byte size, then compute SHA-256 from the saved file, for example `sha256sum data/raw/dnv/<actual-filename>.zip`. The current download script computes SHA-256 directly from each saved file.
3. Record all filters, limits, spatial subsets, and pagination if used. For a direct archive download, record no request filters/pagination and verify the archive's coverage separately.
4. Retain the unmodified original download. Extract working copies into `data/interim/`; never overwrite raw files with cleaned or reprojected outputs.
5. Preserve metadata/licence evidence alongside the raw acquisition and record source IDs and timestamps in this ledger. Do not store credentials in URLs or Git.

Raw downloads and extracted/generated data remain excluded from Git. No geometry QA, normalization, or network tracing has been performed as part of this documentation update.
