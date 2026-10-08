# BugFix-Studio-Misc — `x_temp_consignment_hea`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_temp_consignment_hea` — Temp Consignment Header

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_1295_temp_consignment_header_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_1296_temp_consignment_header_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_x_temp_consignment_hea_user` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1298_imp_select_all_in_copy_po_lines` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1301_imp_clear_all_in_copy_po_lines` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1302_imp_apply_selected_po_lines_to_consignment` (BugFix-Stock)<br>`window action BugFix-Stock.action_1259_temp_consignment_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_1260_temp_consignment_header` (BugFix-Stock)<details><summary>+7 more</summary>`window action BugFix-Stock.action_1261_temp_consignment_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_1295_temp_consignment_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_1299_temp_consignment_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_1357_temp_consignment_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_2851_temp_consignment_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_2861_temp_consignment_header` (BugFix-Stock)<br>`x_temp_consignment_lin.x_studio_temp_consignment_header_id` (BugFix-Stock)</details>

**Summary:**

<!-- SUMMARY:model:x_temp_consignment_hea -->
Temp Consignment Header is created by BugFix-Stock. This repo only adds full access for Purchase / Jin - Procurement - End User - Imports.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_temp_consignment_hea | `access_g_x_temp_consignment_hea_x_temp_consignment_hea_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create/delete access to Temp Consignment Header records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_temp_consignment_hea` (BugFix-Stock) |  |
