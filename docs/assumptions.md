# Assumptions and decision guardrails

No GIS or network assumptions have been adopted. Preserve raw data, make transformations reproducible, and prefer clarity over sophistication. Do not hide ambiguity through automatic cleaning.

Before selecting CRS, snapping tolerance, connectivity rules, line-crossing treatment, ambiguous service-panel handling, or common-schema fields: collect source evidence, explain options and consequences, and ask the project owner to decide. Do not silently choose defaults. Record each accepted decision with its evidence and effect on conclusions.

| Decision | Evidence | Options / consequences | Owner decision | Date |
| --- | --- | --- | --- | --- |
| Pending source inspection | Not collected | Not evaluated | Not decided | — |

Keep this project small. Do not automate QGIS or introduce infrastructure outside the application scope.
