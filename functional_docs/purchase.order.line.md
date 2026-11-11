# BugFix-Studio-Misc — `purchase.order.line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `purchase.order.line` — Purchase Order Line

*Extends a model created by `purchase`.*

Other repos that use this model: `access right BugFix-Purchase.access_inv_administrator_3` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_po_lines` (BugFix-Purchase)<br>`account.move.line.related_field_zy8mz` (BugFix-Accounting)<br>`automation BugFix-Purchase.automation_imp_track_unit_price_change` (BugFix-Purchase)<br>`automation BugFix-Purchase.automation_imp_track_quantity_change` (BugFix-Purchase)<br>`automation BugFix-Purchase.automation_update_analytic_tag_line_product` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_purchase_order_line_multi_company` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_portal_purchase_order_lines` (BugFix-Purchase)<details><summary>+21 more</summary>`server action BugFix-Accounting.action_sales_report_model_srm_rpt_sales_production_purchase_report` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_srm_auto_populate_data_2` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_srm_rpt_sales_production_purchase_report` (BugFix-Accounting)<br>`server action BugFix-Purchase.action_imp_allocate_header_charges` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_track_unit_price_change_in_po_line_3` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_track_unit_price_change_in_po_line` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_track_quantity_change_in_po_line` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_update_analytic_tag_parameters_purchase_line_produ` (BugFix-Purchase)<br>`server action BugFix-Stock.action_consignment_line_imp_invoice_qty_validation_in_consignment` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_copy_po_lines_to_consignment` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_invoice_qty_validation_in_consignment` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_update_consignment` (BugFix-Stock)<br>`window action BugFix-Purchase.action_purchase_order_lines_2` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_rfq_lines_2` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_purchase_order_lines` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_rfq_lines` (BugFix-Purchase)<br>`window action BugFix-Purchase.aw_f4_purchase_order_line_purchase_order_lines` (BugFix-Purchase)<br>`window action BugFix-Purchase.aw_f4_purchase_order_line_rfq_lines` (BugFix-Purchase)<br>`consignment_line.purchase_line_id` (BugFix-Stock)<br>`purchase_request._compute_related_purchase_order_line_count()` (BugFix-Purchase)<br>`temp_consignment_lin.purchase_line_id` (BugFix-Stock)</details>

**Summary:**

<!-- SUMMARY:model:purchase.order.line -->
This repo only adds three PDF reports for purchase order lines: Purchase Order Lines, a Backup copy and a New version. Each uses a Studio report template. No fields or logic are changed.
<!-- /SUMMARY -->

**Reports (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Purchase Order Lines | `report_purchase_order_lines` | Prints **Purchase Order Lines** (qweb-pdf) for purchase.order.line records using template `studio_customization.studio_report_docume_8a65ecd7-ad78-47e6-817e-7b59a80c4552_copy_4_copy_1`. | `model purchase.order.line` (purchase)<br>`record studio_customization.studio_report_docume_8a65ecd7-ad78-47e6-817e-7b59a80c4552_copy_4_copy_1` (studio_customization) |  |
| Purchase Order Lines - Backup | `report_purchase_order_lines_backup` | Prints **Purchase Order Lines - Backup** (qweb-pdf) for purchase.order.line records using template `studio_customization.studio_report_docume_8a65ecd7-ad78-47e6-817e-7b59a80c4552_copy_4`. | `model purchase.order.line` (purchase)<br>`record studio_customization.studio_report_docume_8a65ecd7-ad78-47e6-817e-7b59a80c4552_copy_4` (studio_customization) |  |
| Purchase Order Lines - New | `report_purchase_order_lines_new` | Prints **Purchase Order Lines - New** (qweb-pdf) for purchase.order.line records using template `studio_customization.studio_report_docume_c60b7e6a-dee4-416a-8c7d-136a80aef4a4`. | `model purchase.order.line` (purchase)<br>`record studio_customization.studio_report_docume_c60b7e6a-dee4-416a-8c7d-136a80aef4a4` (studio_customization) |  |
