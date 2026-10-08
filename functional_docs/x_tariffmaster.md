# BugFix-Studio-Misc — `x_tariffmaster`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_tariffmaster` — TariffMaster

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Stock.access_1220_tariffmaster_group_system` (BugFix-Stock)<br>`access right BugFix-Stock.access_1221_tariffmaster_group_user` (BugFix-Stock)<br>`access right BugFix-Stock.access_x_tariffmaster_user` (BugFix-Stock)<br>`automation BugFix-Stock.base_automation_320_jin_company_id_in_tariffmaster` (BugFix-Stock)<br>`product.product.x_studio_many2one_field_AS0wC` (BugFix-Sales)<br>`product.product.x_studio_tariff_code` (BugFix-Sales)<br>`product.template.x_studio_tariff_code` (BugFix-Sales)<br>`record rule BugFix-Stock.rule_572_jin_multi_company_tariffmaster` (BugFix-Stock)<details><summary>+14 more</summary>`server action BugFix-Stock.sa_f5_x_tariffmaster_jin_company_id_in_tariffmaster` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_2686_jin_company_id_in_tariffmaster` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_1159_tariffmaster` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_2038_tariffs_master` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_2041_tariff_master` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_2044_tariff` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_2045_tariff_master` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_2048_tariff_master` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_2049_tariff_master` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_2057_tariff_master` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_2069_tariff_master` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_2867_tariff_master` (BugFix-Stock)<br>`x_consignment_line.x_studio_tariff_code` (BugFix-Stock)<br>`x_tariff_date.x_studio_tariff_master_ids` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:x_tariffmaster -->
TariffMaster is created by BugFix-Stock. This repo only adds read-only access for the Jin Procurement End User - Imports and PR View Only groups.
<!-- /SUMMARY -->

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Tariff Master | `access_g_tariff_master_x_tariffmaster_purchase_jin_procurement_end_user_import` | Gives **Purchase / Jin - Procurement - End User - Imports** read access to TariffMaster records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_tariffmaster` (BugFix-Stock) |  |
| x_tariffmaster | `access_g_x_tariffmaster_x_tariffmaster_purchase_jin_pr_view_only` | Gives **Purchase / Jin - PR View Only** read access to TariffMaster records. | `group BugFix-Studio-Misc.group_g_purchase_jin_pr_view_only`<br>`model x_tariffmaster` (BugFix-Stock) |  |
