# BugFix-Studio-Misc — `x_tariff_rates`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_tariff_rates` — Tariff Rates

*Extends a model created by `BugFix-Purchase`.*

Other repos that use this model: `access right BugFix-Purchase.access_1226_tariff_rates_group_system` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_1227_tariff_rates_group_user` (BugFix-Purchase)<br>`automation BugFix-Purchase.base_automation_322_jin_company_id_in_tariff_rates` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_574_jin_multi_company_tariff_rates` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_f7_x_tariff_rates_jin_multi_company_tariff_rates` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_tariff_date_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_tariff_rates_jin_company_id_in_tariff_rates` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1169_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<details><summary>+14 more</summary>`server action BugFix-Purchase.server_action_1212_imp_allocate_header_charges` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2689_jin_company_id_in_tariff_rates` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges` (BugFix-Stock)<br>`window action BugFix-Purchase.act_window_1162_tariff_rates` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_1170_rates` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_1331_tariff_rates` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_1689_tariff_rates` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2040_tariff_rates` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2043_tariff_rates` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2047_tariff_rates` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2051_tariff_rates` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2059_tariff_rates` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_2866_tariff_rates` (BugFix-Purchase)<br>`x_tariff_date.x_studio_rates` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:x_tariff_rates -->
Tariff Rates is created by BugFix-Purchase. This repo only adds read-only access for the Jin Procurement End User - Imports and PR View Only groups.
<!-- /SUMMARY -->

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Tariff Rates | `access_g_tariff_rates_x_tariff_rates_purchase_jin_procurement_end_user_import` | Gives **Purchase / Jin - Procurement - End User - Imports** read access to Tariff Rates records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_tariff_rates` (BugFix-Purchase) |  |
| x_tariff_rates | `access_g_x_tariff_rates_x_tariff_rates_purchase_jin_pr_view_only` | Gives **Purchase / Jin - PR View Only** read access to Tariff Rates records. | `group BugFix-Studio-Misc.group_g_purchase_jin_pr_view_only`<br>`model x_tariff_rates` (BugFix-Purchase) |  |
