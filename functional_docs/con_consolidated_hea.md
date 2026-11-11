# BugFix-Studio-Misc — `con_consolidated_hea`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `con_consolidated_hea` — Con. Consolidated Header

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_con_consolidated_header_group_system_2` (BugFix-Stock)<br>`access right BugFix-Stock.access_con_consolidated_header_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_con_consolidated_header_group_user_2` (BugFix-Stock)<br>`access right BugFix-Stock.access_con_consolidated_header_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_con_consolidated_hea_user` (BugFix-Stock)<br>`automation BugFix-Stock.automation_jin_company_id_in_consolidated_header` (BugFix-Stock)<br>`automation BugFix-Stock.automation_74_jin_consignment_consolidated_seq_no` (BugFix-Stock)<br>`automation BugFix-Stock.automation_75_imp_restrict_delete_in_consolidation` (BugFix-Stock)<details><summary>+19 more</summary>`record rule BugFix-Stock.rule_jin_multi_company_consolidated_header` (BugFix-Stock)<br>`server action BugFix-Purchase.action_reverse_pr_status_in_po_2` (BugFix-Purchase)<br>`server action BugFix-Stock.action_con_consolidated_hea_con_consolidated_seq_no` (BugFix-Stock)<br>`server action BugFix-Stock.action_con_consolidated_hea_imp_restrict_delete_in_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.action_con_consolidated_hea_jin_company_id_in_consolidated_header` (BugFix-Stock)<br>`server action BugFix-Stock.action_con_consolidated_lin_imp_con_lines_make_available_in_delete` (BugFix-Stock)<br>`server action BugFix-Stock.action_con_consolidated_seq_no` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_copy_consignment_lines_to_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_clear_consignment_lines_from_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_apply_selected_pi_lines_to_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_confirm_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_restrict_delete_in_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_con_lines_make_available_in_delete` (BugFix-Stock)<br>`server action BugFix-Stock.action_jin_company_id_in_consolidated_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_con_consolidated_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_consolidated_consignments` (BugFix-Stock)<br>`window action BugFix-Stock.action_consolidated_consignments_2` (BugFix-Stock)<br>`con_consolidated_lin.consolidated_header_id` (BugFix-Stock)<br>`temp_con_consolidate.consolidated_header_id` (BugFix-Stock)</details>

**Summary:**

<!-- SUMMARY:model:con_consolidated_hea -->
This repo only adds one access right, giving the Purchase / Jin - Procurement - End User - Imports group (defined in this repo) read, write and create access to Consolidated Header records. The model itself comes from BugFix-Stock.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| con_consolidated_hea | `access_g_con_consolidated_hea_con_consolidated_hea_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create access to Con. Consolidated Header records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model con_consolidated_hea` (BugFix-Stock) |  |
