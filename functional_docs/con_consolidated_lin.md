# BugFix-Studio-Misc — `con_consolidated_lin`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `con_consolidated_lin` — Con. Consolidated Line

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_con_consolidated_line_group_system_2` (BugFix-Stock)<br>`access right BugFix-Stock.access_con_consolidated_line_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_con_consolidated_line_group_user_2` (BugFix-Stock)<br>`access right BugFix-Stock.access_con_consolidated_line_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_con_consolidated_lin_user` (BugFix-Stock)<br>`automation BugFix-Stock.automation_jin_company_id_in_consolidated_line` (BugFix-Stock)<br>`automation BugFix-Stock.automation_76_imp_con_lines_make_available_in_delete` (BugFix-Stock)<br>`record rule BugFix-Stock.rule_jin_multi_company_consolidated_line` (BugFix-Stock)<details><summary>+11 more</summary>`server action BugFix-Purchase.action_reverse_pr_status_in_po_2` (BugFix-Purchase)<br>`server action BugFix-Stock.action_con_consolidated_lin_imp_con_lines_make_available_in_delete` (BugFix-Stock)<br>`server action BugFix-Stock.action_con_consolidated_lin_jin_company_id_in_consolidated_line` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_clear_consignment_lines_from_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_apply_selected_pi_lines_to_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_confirm_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_con_lines_make_available_in_delete` (BugFix-Stock)<br>`server action BugFix-Stock.action_jin_company_id_in_consolidated_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_con_consolidated_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_con_consolidated_lin` (BugFix-Stock)<br>`con_consolidated_hea.con_line_ids` (BugFix-Stock)</details>

**Summary:**

<!-- SUMMARY:model:con_consolidated_lin -->
This repo only adds one access right, giving the Purchase / Jin - Procurement - End User - Imports group (defined in this repo) read, write and create access to Consolidated Line records. The model itself comes from BugFix-Stock.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_con_consolidated_line | `access_g_con_consolidated_line_con_consolidated_lin_purchase_jin_procurement_end_user_` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create access to Con. Consolidated Line records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model con_consolidated_lin` (BugFix-Stock) |  |
