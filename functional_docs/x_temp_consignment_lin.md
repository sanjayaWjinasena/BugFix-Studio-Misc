# BugFix-Studio-Misc — `x_temp_consignment_lin`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_temp_consignment_lin` — Temp Consignment Line

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_1297_temp_consignment_line_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_1298_temp_consignment_line_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_x_temp_consignment_lin_user` (BugFix-Stock)<br>`window action BugFix-Stock.action_1262_temp_consignment_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_1300_temp_consignment_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_1356_temp_consignment_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_1656_temp_conn_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_1657_temp123` (BugFix-Stock)<details><summary>+5 more</summary>`window action BugFix-Stock.action_1658_test66` (BugFix-Stock)<br>`window action BugFix-Stock.action_2847_consignment_lines` (BugFix-Stock)<br>`window action BugFix-Stock.action_2850_temp_consignment_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_2860_temp_consignment_line` (BugFix-Stock)<br>`x_temp_consignment_hea.x_studio_temp_consignment_line_ids` (BugFix-Stock)</details>

**Summary:**

<!-- SUMMARY:model:x_temp_consignment_lin -->
Temp Consignment Line is created by BugFix-Stock. This repo only adds read/write/create access for Purchase / Jin - Procurement - End User - Imports.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_temp_consignment_lin | `access_g_x_temp_consignment_lin_x_temp_consignment_lin_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create access to Temp Consignment Line records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_temp_consignment_lin` (BugFix-Stock) |  |
