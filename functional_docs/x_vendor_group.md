# BugFix-Studio-Misc — `x_vendor_group`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_vendor_group` — Vendor Group

*Extends a model created by `studio_usermodel_migration`.*

Other repos that use this model: `access right studio_usermodel_migration.access_1388_vendor_group_group_system` (studio_usermodel_migration)<br>`access right studio_usermodel_migration.access_1389_vendor_group_group_user` (studio_usermodel_migration)<br>`access right studio_usermodel_migration.access_x_vendor_group_system` (studio_usermodel_migration)<br>`access right studio_usermodel_migration.access_x_vendor_group_user` (studio_usermodel_migration)<br>`automation studio_usermodel_migration.base_automation_286_jin_company_id_in_vendor_group` (studio_usermodel_migration)<br>`record rule studio_usermodel_migration.rule_518_name_jin_multi_company_vendor_group` (studio_usermodel_migration)<br>`record rule studio_usermodel_migration.rule_f7_x_vendor_group_name_jin_multi_company_vendor_group` (studio_usermodel_migration)<br>`res.partner.x_studio_vendor_group` (studio_usermodel_migration)<details><summary>+6 more</summary>`res.users.x_studio_many2one_field_qX4FU` (studio_usermodel_migration)<br>`res.users.x_studio_vendor_group1` (studio_usermodel_migration)<br>`res.users.x_studio_vendor_group` (studio_usermodel_migration)<br>`server action studio_usermodel_migration.sa_f5_x_vendor_group_jin_company_id_in_vendor_group` (studio_usermodel_migration)<br>`server action studio_usermodel_migration.server_action_2614_jin_company_id_in_vendor_group` (studio_usermodel_migration)<br>`window action studio_usermodel_migration.act_window_1444_vendor_groups` (studio_usermodel_migration)</details>

**Summary:**

<!-- SUMMARY:model:x_vendor_group -->
Vendor Group is created by studio_usermodel_migration. This repo only adds full access for Accounting / Jin - AccountExecutive.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Vendors | `access_g_vendors_x_vendor_group_accounting_jin_accountexecutive` | Gives **Accounting / Jin - AccountExecutive** read/write/create/delete access to Vendor Group records. | `group BugFix-Studio-Misc.group_g_accounting_jin_accountexecutive`<br>`model x_vendor_group` (studio_usermodel_migration) |  |
