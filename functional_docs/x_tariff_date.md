# BugFix-Studio-Misc — `x_tariff_date`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_tariff_date` — Tariff Date

*Extends a model created by `BugFix-Purchase`.*

Other repos that use this model: `access right BugFix-Purchase.access_1222_tariff_date_group_system` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_1223_tariff_date_group_user` (BugFix-Purchase)<br>`automation BugFix-Purchase.base_automation_321_jin_company_id_in_tariff_date` (BugFix-Purchase)<br>`automation BugFix-Purchase.base_automation_49_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_573_jin_multi_company_tariff_date` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_f7_x_tariff_date_jin_multi_company_tariff_date` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_tariff_date_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_tariff_date_jin_company_id_in_tariff_date` (BugFix-Purchase)<details><summary>+17 more</summary>`server action BugFix-Purchase.server_action_1169_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1212_imp_allocate_header_charges` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2688_jin_company_id_in_tariff_date` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges` (BugFix-Stock)<br>`window action BugFix-Purchase.act_window_1160_tariff_date` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_1163_tariff_date` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_1688_tariff_periods` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2039_tariff_periods` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2042_tariff_periods` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2046_tariff_periods` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2050_tariff_periods` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2058_tariff_periods` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2068_tariff_periods_x_tariff_date` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2070_tariff_dates` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2687_x_tariff_date` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2868_tariff_dates` (BugFix-Purchase)<br>`x_tariff_rates.x_studio_tariff_date_ids` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:x_tariff_date -->
Tariff Date is created by BugFix-Purchase. This repo only adds read-only access for the Jin Procurement End User - Imports and PR View Only groups.
<!-- /SUMMARY -->

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Tariff Dates | `access_g_tariff_dates_x_tariff_date_purchase_jin_procurement_end_user_import` | Gives **Purchase / Jin - Procurement - End User - Imports** read access to Tariff Date records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_tariff_date` (BugFix-Purchase) |  |
| x_tariff_date | `access_g_x_tariff_date_x_tariff_date_purchase_jin_pr_view_only` | Gives **Purchase / Jin - PR View Only** read access to Tariff Date records. | `group BugFix-Studio-Misc.group_g_purchase_jin_pr_view_only`<br>`model x_tariff_date` (BugFix-Purchase) |  |
