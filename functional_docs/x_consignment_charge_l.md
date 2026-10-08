# BugFix-Studio-Misc — `x_consignment_charge_l`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_consignment_charge_l` — Consignment Charge Line

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_1335_consignment_charge_line_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_1336_consignment_charge_line_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_x_consignment_charge_l_user` (BugFix-Stock)<br>`automation BugFix-Stock.automation_290_jin_company_id_in_consignment_charge_line` (BugFix-Stock)<br>`record rule BugFix-Stock.rule_522_jin_multi_company_consignment_charge_line` (BugFix-Stock)<br>`server action BugFix-Stock.sa_f5_x_consignment_charge_l_jin_company_id_in_consignment_charge_line` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_2199_imp_reset_header_charges_consignment` (BugFix-Stock)<details><summary>+6 more</summary>`server action BugFix-Stock.server_action_2618_jin_company_id_in_consignment_charge_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_1315_consignment_charge_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_1319_line_charges` (BugFix-Stock)<br>`window action BugFix-Stock.action_2231_custom_duty` (BugFix-Stock)<br>`window action BugFix-Stock.action_2849_consignment_charge_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_2859_consignment_charge_line` (BugFix-Stock)</details>

**Summary:**

<!-- SUMMARY:model:x_consignment_charge_l -->
This repo only adds one access right, giving the Purchase / Jin - Procurement - End User - Imports group (defined in this repo) full read, write, create and delete access to Consignment Charge Lines.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_consignment_charge_l | `access_g_x_consignment_charge_l_x_consignment_charge_l_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create/delete access to Consignment Charge Line records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_consignment_charge_l` (BugFix-Stock) |  |
