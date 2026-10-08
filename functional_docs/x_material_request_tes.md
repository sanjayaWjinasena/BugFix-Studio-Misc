# BugFix-Studio-Misc — `x_material_request_tes`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_material_request_tes` — Material Request Test

*Extends a model created by `BugFix-Stock`.* Python: `models/x_material_request_tes_o2m.py`.

Other repos that use this model: `access right BugFix-Stock.access_8267_material_request_test_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_8268_material_request_test_group_user` (BugFix-Stock)<br>`record rule BugFix-Stock.rule_881_material_request_test_multi_company` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_3374_material_request_test` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:x_material_request_tes -->
Material Request Test is created by BugFix-Stock. This repo adds one field: the one2many `x_material_request_tes_line_ids_661d3`, which lists the related material_request_tes_line records. It is not shown on any view in this repo.
<!-- /SUMMARY -->

**Fields (1):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_material_request_tes_line_ids_661d3` | New Lines | one2many → `x_material_request_tes_line_3301b` | Lines (`x_material_request_tes_line_3301b`) belonging to a Material Request Test; not shown on any view in this repo. | stored | `model x_material_request_tes_line_3301b` |  |
