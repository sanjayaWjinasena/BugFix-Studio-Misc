# BugFix-Studio-Misc — `temp_consignment_hea`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `temp_consignment_hea` — Temp Consignment Header

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_temp_consignment_header_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_temp_consignment_header_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_temp_consignment_hea_user` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_select_all_in_copy_po_lines` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_clear_all_in_copy_po_lines` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_apply_selected_po_lines_to_consignment` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_consignment_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_consignment_header_2` (BugFix-Stock)<details><summary>+7 more</summary>`window action BugFix-Stock.action_temp_consignment_header_3` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_consignment_header_4` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_consignment_header_5` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_consignment_header_6` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_consignment_header_7` (BugFix-Stock)<br>`window action BugFix-Stock.action_temp_consignment_header_8` (BugFix-Stock)<br>`temp_consignment_lin.temp_consignment_header_id` (BugFix-Stock)</details>

**Summary:**

<!-- SUMMARY:model:temp_consignment_hea -->
Temp Consignment Header is created by BugFix-Stock. This repo only adds full access for Purchase / Jin - Procurement - End User - Imports.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| temp_consignment_hea | `access_g_temp_consignment_hea_temp_consignment_hea_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create/delete access to Temp Consignment Header records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model temp_consignment_hea` (BugFix-Stock) |  |
