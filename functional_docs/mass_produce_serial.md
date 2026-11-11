# BugFix-Studio-Misc — `mass_produce_serial`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `mass_produce_serial` — Mass Produce Serial

*Extends a model created by `BugFix-MRP`.*

Other repos that use this model: `access right BugFix-MRP.access_mass_produce_serial_group_system` (BugFix-MRP)<br>`access right BugFix-MRP.access_mass_produce_serial_group_user` (BugFix-MRP)<br>`access right BugFix-MRP.access_mass_produce_serial_user` (BugFix-MRP)<br>`automation BugFix-MRP.automation_jin_company_id_in_mass_produce_serial` (BugFix-MRP)<br>`automation BugFix-MRP.base_automation_45_mass_produce_serial_nos_find_last` (BugFix-MRP)<br>`record rule BugFix-MRP.rule_jin_multi_company_mass_produce_serial` (BugFix-MRP)<br>`record rule BugFix-MRP.rule_f7_mass_produce_serial_jin_multi_company_mass_produce_serial` (BugFix-MRP)<br>`server action BugFix-MRP.action_mass_produce_serial_jin_company_id_in_mass_produce_serial` (BugFix-MRP)<details><summary>+8 more</summary>`server action BugFix-MRP.action_mass_produce_serial_mass_produce_serial_nos_find_last` (BugFix-MRP)<br>`server action BugFix-MRP.action_mass_produce_serial_numbers_generate` (BugFix-MRP)<br>`server action BugFix-MRP.action_mass_produce_serial_numbers_clear` (BugFix-MRP)<br>`server action BugFix-MRP.action_mass_produce_serial_numbers_create_original` (BugFix-MRP)<br>`server action BugFix-MRP.action_mass_produce_serial_nos_find_last` (BugFix-MRP)<br>`server action BugFix-MRP.action_jin_company_id_in_mass_produce_serial` (BugFix-MRP)<br>`window action BugFix-MRP.action_mass_produce_serial` (BugFix-MRP)<br>`mass_produce_serial_.mass_produce_serial_ids` (BugFix-MRP)</details>

**Summary:**

<!-- SUMMARY:model:mass_produce_serial -->
This repo only adds three access rights that give full access to Mass Produce Serial records to three manufacturing groups defined in this repo: Master Plan Creator, Master Plan Operator and MO Creator. The model itself comes from BugFix-MRP.
<!-- /SUMMARY -->

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Jin - Manufacturing -  MO Full Writes  + MPS | `access_g_jin_manufacturing_mo_full_writes_mps_mass_produce_serial_manufacturing_jin_manu` | Gives **Manufacturing / Jin - Manufacturing - Master Plan Creator [ Add a Product ]** read/write/create/delete access to Mass Produce Serial records. | `group BugFix-Studio-Misc.group_g_manufacturing_jin_manufacturing_master_plan_creator_add_a_product`<br>`model mass_produce_serial` (BugFix-MRP) |  |
| Jin - Manufacturing -  MO Full Writes  + MPS | `access_g_jin_manufacturing_mo_full_writes_mps_mass_produce_serial_manufacturing_jin_manu_1` | Gives **Manufacturing / Jin - Manufacturing - Master Plan Operator [ Replenish ]** read/write/create/delete access to Mass Produce Serial records. | `group BugFix-Studio-Misc.group_g_manufacturing_jin_manufacturing_master_plan_operator_replenish`<br>`model mass_produce_serial` (BugFix-MRP) |  |
| Mass Produce Serial group_user | `access_g_mass_produce_serial_group_user_mass_produce_serial_manufacturing_jin_manufactur` | Gives **Manufacturing / Jin - Manufacturing - MO Creator** read/write/create/delete access to Mass Produce Serial records. | `group BugFix-Studio-Misc.group_g_manufacturing_jin_manufacturing_mo_creator`<br>`model mass_produce_serial` (BugFix-MRP) |  |
