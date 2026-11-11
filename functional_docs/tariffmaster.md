# BugFix-Studio-Misc — `tariffmaster`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `tariffmaster` — TariffMaster

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_tariffmaster_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_tariffmaster_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_tariffmaster_user` (BugFix-Stock)<br>`automation BugFix-Stock.automation_jin_company_id_in_tariffmaster` (BugFix-Stock)<br>`product.product.many2one_field_AS0wC` (BugFix-Sales)<br>`product.product.tariff_code` (BugFix-Sales)<br>`product.template.tariff_code` (BugFix-Sales)<br>`record rule BugFix-Stock.rule_jin_multi_company_tariffmaster` (BugFix-Stock)<details><summary>+14 more</summary>`server action BugFix-Stock.action_tariffmaster_jin_company_id_in_tariffmaster` (BugFix-Stock)<br>`server action BugFix-Stock.action_jin_company_id_in_tariffmaster` (BugFix-Stock)<br>`window action BugFix-Stock.action_tariffmaster` (BugFix-Stock)<br>`window action BugFix-Stock.action_tariffs_master` (BugFix-Stock)<br>`window action BugFix-Stock.action_tariff_master` (BugFix-Stock)<br>`window action BugFix-Stock.action_tariff` (BugFix-Stock)<br>`window action BugFix-Stock.action_tariff_master_2` (BugFix-Stock)<br>`window action BugFix-Stock.action_tariff_master_3` (BugFix-Stock)<br>`window action BugFix-Stock.action_tariff_master_4` (BugFix-Stock)<br>`window action BugFix-Stock.action_tariff_master_5` (BugFix-Stock)<br>`window action BugFix-Stock.action_tariff_master_6` (BugFix-Stock)<br>`window action BugFix-Stock.action_tariff_master_7` (BugFix-Stock)<br>`consignment_line.tariff_code` (BugFix-Stock)<br>`tariff_date.tariff_master_ids` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:tariffmaster -->
TariffMaster is created by BugFix-Stock. This repo only adds read-only access for the Jin Procurement End User - Imports and PR View Only groups.
<!-- /SUMMARY -->

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Tariff Master | `access_g_tariff_master_tariffmaster_purchase_jin_procurement_end_user_import` | Gives **Purchase / Jin - Procurement - End User - Imports** read access to TariffMaster records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model tariffmaster` (BugFix-Stock) |  |
| tariffmaster | `access_g_tariffmaster_tariffmaster_purchase_jin_pr_view_only` | Gives **Purchase / Jin - PR View Only** read access to TariffMaster records. | `group BugFix-Studio-Misc.group_g_purchase_jin_pr_view_only`<br>`model tariffmaster` (BugFix-Stock) |  |
