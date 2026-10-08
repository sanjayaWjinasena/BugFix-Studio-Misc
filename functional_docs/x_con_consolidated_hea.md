# BugFix-Studio-Misc — `x_con_consolidated_hea`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_con_consolidated_hea` — Con. Consolidated Header

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_1378_con__consolidated_header_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_1378_con_consolidated_header_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_1379_con__consolidated_header_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_1379_con_consolidated_header_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_x_con_consolidated_hea_user` (BugFix-Stock)<br>`automation BugFix-Stock.automation_282_jin_company_id_in_consolidated_header` (BugFix-Stock)<br>`automation BugFix-Stock.automation_74_jin_consignment_consolidated_seq_no` (BugFix-Stock)<br>`automation BugFix-Stock.automation_75_imp_restrict_delete_in_consolidation` (BugFix-Stock)<details><summary>+19 more</summary>`record rule BugFix-Stock.rule_514_jin_multi_company_consolidated_header` (BugFix-Stock)<br>`server action BugFix-Purchase.server_action_2375_reverse_pr_status_in_po_2` (BugFix-Purchase)<br>`server action BugFix-Stock.sa_f5_x_con_consolidated_hea_con_consolidated_seq_no` (BugFix-Stock)<br>`server action BugFix-Stock.sa_f5_x_con_consolidated_hea_imp_restrict_delete_in_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.sa_f5_x_con_consolidated_hea_jin_company_id_in_consolidated_header` (BugFix-Stock)<br>`server action BugFix-Stock.sa_f5_x_con_consolidated_lin_imp_con_lines_make_available_in_delete` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1412_con_consolidated_seq_no` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1413_imp_copy_consignment_lines_to_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1414_imp_clear_consignment_lines_from_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1420_imp_apply_selected_pi_lines_to_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1421_imp_confirm_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1423_imp_restrict_delete_in_consolidation` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1424_imp_con_lines_make_available_in_delete` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_2609_jin_company_id_in_consolidated_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_1410_con_consolidated_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_2054_consolidated_consignments` (BugFix-Stock)<br>`window action BugFix-Stock.action_2888_consolidated_consignments` (BugFix-Stock)<br>`x_con_consolidated_lin.x_studio_consolidated_header_id` (BugFix-Stock)<br>`x_temp_con_consolidate.x_studio_consolidated_header_id` (BugFix-Stock)</details>

**Summary:**

<!-- SUMMARY:model:x_con_consolidated_hea -->
This repo only adds one access right, giving the Purchase / Jin - Procurement - End User - Imports group (defined in this repo) read, write and create access to Consolidated Header records. The model itself comes from BugFix-Stock.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_con_consolidated_hea | `access_g_x_con_consolidated_hea_x_con_consolidated_hea_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create access to Con. Consolidated Header records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_con_consolidated_hea` (BugFix-Stock) |  |
