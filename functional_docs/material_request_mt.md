# BugFix-Studio-Misc — `material_request_mt`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `material_request_mt` — Material Request MT

*Extends a model created by `BugFix-Stock`.* Python: `models/material_request_mt_o2m.py`.

Other repos that use this model: `access right BugFix-Stock.access_8291_material_request_mt_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_8292_material_request_mt_group_user` (BugFix-Stock)<br>`automation BugFix-Stock.base_automation_346_generate_sequence_number_for_mr` (BugFix-Stock)<br>`record rule BugFix-Stock.rule_884_material_request_mt_multi_company` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_3399_execute_code` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_3384_material_request_mt` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:material_request_mt -->
This repo only adds a New Lines one-to-many field that links a Material Request MT to its lines (material_request_mt_line_9a011). The field is not shown on any view in this repo.
<!-- /SUMMARY -->

**Fields (1):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `material_request_mt_line_ids_7737e` | New Lines | one2many → `material_request_mt_line_9a011` | Lines (`material_request_mt_line_9a011`) belonging to a Material Request MT; not shown on any view in this repo. | stored | `model material_request_mt_line_9a011` |  |
