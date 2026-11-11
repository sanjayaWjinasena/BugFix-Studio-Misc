# BugFix-Studio-Misc — `res.currency`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `res.currency` — Currency

*Extends a model created by `base`.*

Other repos that use this model: `crossovered.budget.currency_id` (BugFix-Accounting)<br>`mrp.bom.accounting_currency_id` (BugFix-MRP)<br>`mrp.production.accounting_currency_id` (BugFix-MRP)<br>`server action BugFix-Accounting.action_custom_currency_imp_pass_currency_information_to_custom_currency` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_pass_currency_information_to_custom_currency` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_update_lc_status_to_paid_2` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi` (BugFix-Accounting)<details><summary>+28 more</summary>`stock.lot.currency_id` (BugFix-Stock)<br>`con_consolidated_lin.accounting_currency_id` (BugFix-Stock)<br>`consignment_header.accounting_currency_id` (BugFix-Stock)<br>`consignment_line.currency_id` (BugFix-Stock)<br>`custom_currency.accounting_currency_id` (BugFix-Accounting)<br>`custom_reports.accounting_currency_id` (BugFix-Custom-Reports)<br>`lc_header.accounting_currency_id` (BugFix-Accounting)<br>`material_request_m.accounting_currency_id` (BugFix-MRP)<br>`material_request_mt.accounting_currency_id` (BugFix-Stock)<br>`material_request_tes.accounting_currency_id` (BugFix-Stock)<br>`mr_config.currency_id` (BugFix-Stock)<br>`mrp_bom_general_cost.accounting_currency_id` (BugFix-MRP)<br>`mrp_bom_labour_cost.accounting_currency_id` (BugFix-MRP)<br>`mrp_bom_material_cos.accounting_currency_id` (BugFix-MRP)<br>`mrp_bom_overhead_cos.accounting_currency_id` (BugFix-MRP)<br>`po_line_non_inventor.currency_id` (BugFix-Purchase)<br>`po_non_inventory.currency_id` (BugFix-Purchase)<br>`pr_line_cash.currency_id` (BugFix-Purchase)<br>`purchase_request_cas.currency_id` (BugFix-Purchase)<br>`purchase_request_mt.accounting_currency_id` (BugFix-Purchase)<br>`purchase_request_t.accounting_currency_id` (BugFix-Purchase)<br>`structure_details.accounting_currency_id` (BugFix-Purchase)<br>`temp_actual_budget.currency_id` (BugFix-Accounting)<br>`temp_con_conso_line.accounting_currency_id` (BugFix-Stock)<br>`temp_consignment_lin.currency_id` (BugFix-Stock)<br>`temp_estimated.currency_id` (BugFix-Accounting)<br>`tp_invoice_header.currency_id` (BugFix-Accounting)<br>`tp_invoice_header.accounting_currency_id` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:res.currency -->
This repo only adds a Studio list customization that shows an optional record ID column in the Currencies list.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: res.currency.tree customization | `view_res_currency_tree_inherit` | tree | after `//field[@name='active']`: add field id | Adds an optional record ID column to the Currencies list. | `view base.view_currency_tree` (base) |  |
