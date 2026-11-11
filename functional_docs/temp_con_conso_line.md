# BugFix-Studio-Misc — `temp_con_conso_line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `temp_con_conso_line` — Temp Con. Conso. Line

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_temp_con_conso_line_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_temp_con_conso_line_group_user` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_select_all_in_copy_pi_lines` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_clear_all_in_copy_po_lines_2` (BugFix-Stock)<br>`temp_con_consolidate.con_lines` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:temp_con_conso_line -->
Temp Con. Conso. Line is created by BugFix-Stock. This repo only adds read/write/create access for Purchase / Jin - Procurement - End User - Imports.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| temp_con_conso_line | `access_g_temp_con_conso_line_temp_con_conso_line_purchase_jin_procurement_end_user_imp` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create access to Temp Con. Conso. Line records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model temp_con_conso_line` (BugFix-Stock) |  |
