# BugFix-Studio-Misc — `res.config.settings`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `res.config.settings` — Config Settings

*Extends a model created by `base`.*

Other repos that use this model: `access right BugFix-Sales.access_1531_res_config_settings_group_system` (BugFix-Sales)<br>`access right BugFix-Sales.access_1532_res_config_settings_group_user` (BugFix-Sales)<br>`server action BugFix-Accounting.server_action_1370_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:res.config.settings -->
This repo only adds one access right, giving Administration / Settings full read, write, create and delete access to Config Settings. No fields, views or logic are changed.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| res.config.settings group_system | `access_res_config_settings_group_system` | Gives **Administration / Settings** read/write/create/delete access to Config Settings records. | `group base.group_system` (base)<br>`model res.config.settings` (base) |  |
