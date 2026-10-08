# BugFix-Studio-Misc — `res.currency`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `res.currency` — Currency

*Extends a model created by `base`.*

Other repos that use this model: `crossovered.budget.x_currency_id` (BugFix-Accounting)<br>`mrp.bom.x_studio_currency_id` (BugFix-MRP)<br>`mrp.production.x_studio_currency_id` (BugFix-MRP)<br>`server action BugFix-Accounting.sa_f5_x_custom_currency_imp_pass_currency_information_to_custom_currency` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1312_imp_pass_currency_information_to_custom_currency` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1370_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1409_imp_update_lc_status_to_paid_2` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi` (BugFix-Accounting)<details><summary>+28 more</summary>`stock.lot.x_currency_id` (BugFix-Stock)<br>`x_con_consolidated_lin.x_studio_currency_id` (BugFix-Stock)<br>`x_consignment_header.x_studio_currency_id` (BugFix-Stock)<br>`x_consignment_line.x_currency_id` (BugFix-Stock)<br>`x_custom_currency.x_studio_currency_id` (BugFix-Accounting)<br>`x_custom_reports.x_studio_currency_id` (BugFix-Custom-Reports)<br>`x_lc_header.x_studio_currency_id` (BugFix-Accounting)<br>`x_material_request_m.x_studio_currency_id` (BugFix-MRP)<br>`x_material_request_mt.x_studio_currency_id` (BugFix-Stock)<br>`x_material_request_tes.x_studio_currency_id` (BugFix-Stock)<br>`x_mr_config.x_currency_id` (BugFix-Stock)<br>`x_mrp_bom_general_cost.x_studio_currency_id` (BugFix-MRP)<br>`x_mrp_bom_labour_cost.x_studio_currency_id` (BugFix-MRP)<br>`x_mrp_bom_material_cos.x_studio_currency_id` (BugFix-MRP)<br>`x_mrp_bom_overhead_cos.x_studio_currency_id` (BugFix-MRP)<br>`x_po_line_non_inventor.x_currency_id` (BugFix-Purchase)<br>`x_po_non_inventory.x_currency_id` (BugFix-Purchase)<br>`x_pr_line_cash.x_currency_id` (BugFix-Purchase)<br>`x_purchase_request_cas.x_currency_id` (BugFix-Purchase)<br>`x_purchase_request_mt.x_studio_currency_id` (BugFix-Purchase)<br>`x_purchase_request_t.x_studio_currency_id` (BugFix-Purchase)<br>`x_structure_details.x_studio_currency_id` (BugFix-Purchase)<br>`x_temp_actual_budget.x_currency_id` (BugFix-Accounting)<br>`x_temp_con_conso_line.x_studio_currency_id` (BugFix-Stock)<br>`x_temp_consignment_lin.x_currency_id` (BugFix-Stock)<br>`x_temp_estimated.x_currency_id` (BugFix-Accounting)<br>`x_tp_invoice_header.x_currency_id` (BugFix-Accounting)<br>`x_tp_invoice_header.x_studio_currency_id` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:res.currency -->
This repo only adds a Studio list customization that shows an optional record ID column in the Currencies list.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: res.currency.tree customization | `view_4901_odoo_studio_res_currency_tree_customization_ext` | tree | after `//field[@name='active']`: add field id | Adds an optional record ID column to the Currencies list. | `view base.view_currency_tree` (base) |  |
