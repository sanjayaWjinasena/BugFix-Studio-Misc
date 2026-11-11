# BugFix-Studio-Misc — `consignment_charge_l`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `consignment_charge_l` — Consignment Charge Line

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_consignment_charge_line_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_consignment_charge_line_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_consignment_charge_l_user` (BugFix-Stock)<br>`automation BugFix-Stock.automation_jin_company_id_in_consignment_charge_line` (BugFix-Stock)<br>`record rule BugFix-Stock.rule_jin_multi_company_consignment_charge_line` (BugFix-Stock)<br>`server action BugFix-Stock.action_consignment_charge_l_jin_company_id_in_consignment_charge_line` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_allocate_consignment_header_charges` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_reset_header_charges_consignment` (BugFix-Stock)<details><summary>+6 more</summary>`server action BugFix-Stock.action_jin_company_id_in_consignment_charge_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_consignment_charge_line` (BugFix-Stock)<br>`window action BugFix-Stock.action_line_charges` (BugFix-Stock)<br>`window action BugFix-Stock.action_custom_duty` (BugFix-Stock)<br>`window action BugFix-Stock.action_consignment_charge_line_2` (BugFix-Stock)<br>`window action BugFix-Stock.action_consignment_charge_line_3` (BugFix-Stock)</details>

**Summary:**

<!-- SUMMARY:model:consignment_charge_l -->
This repo only adds one access right, giving the Purchase / Jin - Procurement - End User - Imports group (defined in this repo) full read, write, create and delete access to Consignment Charge Lines.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| consignment_charge_l | `access_g_consignment_charge_l_consignment_charge_l_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create/delete access to Consignment Charge Line records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model consignment_charge_l` (BugFix-Stock) |  |
