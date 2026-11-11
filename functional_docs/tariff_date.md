# BugFix-Studio-Misc — `tariff_date`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `tariff_date` — Tariff Date

*Extends a model created by `BugFix-Purchase`.*

Other repos that use this model: `access right BugFix-Purchase.access_tariff_date_group_system` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_tariff_date_group_user` (BugFix-Purchase)<br>`automation BugFix-Purchase.automation_jin_company_id_in_tariff_date` (BugFix-Purchase)<br>`automation BugFix-Purchase.base_automation_49_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_jin_multi_company_tariff_date` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_f7_tariff_date_jin_multi_company_tariff_date` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_tariff_date_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_tariff_date_jin_company_id_in_tariff_date` (BugFix-Purchase)<details><summary>+17 more</summary>`server action BugFix-Purchase.action_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_allocate_header_charges` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_jin_company_id_in_tariff_date` (BugFix-Purchase)<br>`server action BugFix-Stock.action_imp_allocate_consignment_header_charges` (BugFix-Stock)<br>`window action BugFix-Purchase.action_tariff_date` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_date_2` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_periods` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_periods_2` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_periods_3` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_periods_4` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_periods_5` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_periods_6` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_periods_tariff_date` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_dates` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_date_3` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_tariff_dates_2` (BugFix-Purchase)<br>`tariff_rates.tariff_date_ids` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:tariff_date -->
Tariff Date is created by BugFix-Purchase. This repo only adds read-only access for the Jin Procurement End User - Imports and PR View Only groups.
<!-- /SUMMARY -->

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Tariff Dates | `access_g_tariff_dates_tariff_date_purchase_jin_procurement_end_user_import` | Gives **Purchase / Jin - Procurement - End User - Imports** read access to Tariff Date records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model tariff_date` (BugFix-Purchase) |  |
| tariff_date | `access_g_tariff_date_tariff_date_purchase_jin_pr_view_only` | Gives **Purchase / Jin - PR View Only** read access to Tariff Date records. | `group BugFix-Studio-Misc.group_g_purchase_jin_pr_view_only`<br>`model tariff_date` (BugFix-Purchase) |  |
