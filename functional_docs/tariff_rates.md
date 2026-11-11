# BugFix-Studio-Misc — `tariff_rates`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `tariff_rates` — Tariff Rates

*Extends a model created by `BugFix-Purchase`.*

Other repos that use this model: `access right BugFix-Purchase.access_tariff_rates_group_system` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_tariff_rates_group_user` (BugFix-Purchase)<br>`automation BugFix-Purchase.automation_jin_company_id_in_tariff_rates` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_jin_multi_company_tariff_rates` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_f7_tariff_rates_jin_multi_company_tariff_rates` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_tariff_date_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_tariff_rates_jin_company_id_in_tariff_rates` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<details><summary>+14 more</summary>`server action BugFix-Purchase.action_imp_allocate_header_charges` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_jin_company_id_in_tariff_rates` (BugFix-Purchase)<br>`server action BugFix-Stock.action_imp_allocate_consignment_header_charges` (BugFix-Stock)<br>`window action BugFix-Purchase.action_tariff_rates` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_rates` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_rates_2` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_rates_3` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_rates_4` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_rates_5` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_rates_6` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_rates_7` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_rates_8` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_rates_9` (BugFix-Purchase)<br>`tariff_date.rates` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:tariff_rates -->
Tariff Rates is created by BugFix-Purchase. This repo only adds read-only access for the Jin Procurement End User - Imports and PR View Only groups.
<!-- /SUMMARY -->

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Tariff Rates | `access_g_tariff_rates_tariff_rates_purchase_jin_procurement_end_user_import` | Gives **Purchase / Jin - Procurement - End User - Imports** read access to Tariff Rates records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model tariff_rates` (BugFix-Purchase) |  |
| tariff_rates | `access_g_tariff_rates_tariff_rates_purchase_jin_pr_view_only` | Gives **Purchase / Jin - PR View Only** read access to Tariff Rates records. | `group BugFix-Studio-Misc.group_g_purchase_jin_pr_view_only`<br>`model tariff_rates` (BugFix-Purchase) |  |
