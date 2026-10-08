# BugFix-Studio-Misc — `x_con_consolidated_lin`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_con_consolidated_lin` — Con. Consolidated Line

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_1380_con__consolidated_line_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_1380_con_consolidated_line_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_1381_con__consolidated_line_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_1381_con_consolidated_line_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_x_con_consolidated_lin_user` (BugFix-Stock)<br>`automation BugFix-Stock.automation_283_jin_company_id_in_consolidated_line` (BugFix-Stock)<br>`automation BugFix-Stock.automation_76_imp_con_lines_make_available_in_delete` (BugFix-Stock)<br>`record rule BugFix-Stock.rule_515_jin_multi_company_consolidated_line` (BugFix-Stock)<details><summary>+11 more</summary>`server action BugFix-Purchase.server_action_2375_reverse_pr_status_in_po_2` (BugFix-Purchase)<br>`server action BugFix-Stock.sa_f5_x_con_consolidated_lin_imp_con_lines_make_available_in_delete` (BugFix-Stock)<br>`server action BugFix-Stock.sa_f5_x_con_consolidated_lin_jin_company_id_in_consolidated_line` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1414_imp_clear_consignment_lines_from_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1420_imp_apply_selected_pi_lines_to_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1421_imp_confirm_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1424_imp_con_lines_make_available_in_delete` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_2611_jin_company_id_in_consolidated_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_1411_con_consolidated_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_2610_x_con_consolidated_lin` (BugFix-Stock)<br>`x_con_consolidated_hea.x_studio_con_line_ids` (BugFix-Stock)</details>

**Summary:**

<!-- SUMMARY:model:x_con_consolidated_lin -->
This repo only adds one access right, giving the Purchase / Jin - Procurement - End User - Imports group (defined in this repo) read, write and create access to Consolidated Line records. The model itself comes from BugFix-Stock.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_con_consolidated_line | `access_g_x_con_consolidated_line_x_con_consolidated_lin_purchase_jin_procurement_end_user_` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create access to Con. Consolidated Line records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_con_consolidated_lin` (BugFix-Stock) |  |
