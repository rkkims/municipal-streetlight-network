# Inventory handoff

The normalized GeoPackage layers are the system-of-record handoff from this
project. They provide stable, reviewable fields that could be loaded into an
inventory tool such as Zoho Creator after municipal and application-specific
requirements are confirmed.

## Handoff fields

| Field | Purpose |
| --- | --- |
| `municipality` | Identifies the source municipality |
| `source_layer` | Preserves the original layer name |
| `asset_type` | Broad role such as pole, conduit, or fitting |
| `classification` | Optional source-supported subtype |
| `status` | Source-supported lifecycle status |
| `source_asset_id` | Original municipal asset identifier |
| `source_global_id` | Original global identifier, when published |
| `network_id` | Original municipal network grouping, when published |
| `source_comments` | Preserved free-text source evidence |
| `source_crs` | CRS of the retained source geometry |
| `geometry` | Mapped asset location or line geometry |

Trace and QA results should remain linked by `municipality`, `network_id`, and
source asset IDs rather than replacing the source inventory.
