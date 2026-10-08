# BugFix-Studio-Misc — `x_temp_con_consolidate`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_temp_con_consolidate` — Temp Con. Consolidated Header

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_1382_temp_con__consolidated_header_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_1383_temp_con__consolidated_header_group_user` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1417_imp_select_all_in_copy_pi_lines` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1419_imp_clear_all_in_copy_po_lines` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1420_imp_apply_selected_pi_lines_to_consolidation` (BugFix-Stock)<br>`x_temp_con_conso_line.x_studio_temp_consolidated_header_id` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:x_temp_con_consolidate -->
Temp Con. Consolidated Header is created by BugFix-Stock. This repo only adds full access for Purchase / Jin - Procurement - End User - Imports.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_temp_con_consolidate | `access_g_x_temp_con_consolidate_x_temp_con_consolidate_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create/delete access to Temp Con. Consolidated Header records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_temp_con_consolidate` (BugFix-Stock) |  |
