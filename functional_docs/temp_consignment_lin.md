# BugFix-Studio-Misc — `temp_consignment_lin`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `temp_consignment_lin` — Temp Consignment Line

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_temp_consignment_line_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_temp_consignment_line_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_temp_consignment_lin_user` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_consignment_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_consignment_line_2` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_consignment_line_3` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_conn_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp123` (BugFix-Stock)<details><summary>+5 more</summary>`window action BugFix-Stock.action_1658_test66` (BugFix-Stock)<br>`window action BugFix-Stock.action_consignment_lines_3` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_consignment_line_4` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_consignment_line_5` (BugFix-Stock)<br>`temp_consignment_hea.temp_consignment_line_ids` (BugFix-Stock)</details>

**Summary:**

<!-- SUMMARY:model:temp_consignment_lin -->
Temp Consignment Line is created by BugFix-Stock. This repo only adds read/write/create access for Purchase / Jin - Procurement - End User - Imports.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| temp_consignment_lin | `access_g_temp_consignment_lin_temp_consignment_lin_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create access to Temp Consignment Line records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model temp_consignment_lin` (BugFix-Stock) |  |
