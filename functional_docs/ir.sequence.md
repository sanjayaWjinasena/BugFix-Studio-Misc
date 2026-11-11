# BugFix-Studio-Misc — `ir.sequence`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.sequence` — Sequence

*Extends a model created by `base`.*

Other repos that use this model: `helpdesk.ticket._repair_seq_no_on_create_or_write()` (Fix-repair)<br>`helpdesk.ticket._repair_studio_auto_create_repair_serial_nos()` (Fix-repair)<br>`server action BugFix-Accounting.action_lc_header_lc_registration_seq_no` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_sales_report_model_report_model_seq_no` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_tp_invoice_header_tp_invoice_seq_no` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_tp_invoice_seq_no` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_lc_registration_seq_no` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_report_model_seq_no` (BugFix-Accounting)<details><summary>+25 more</summary>`server action BugFix-HR.action_update_ot_update_ot_seq_no` (BugFix-HR)<br>`server action BugFix-HR.action_update_ot_seq_no` (BugFix-HR)<br>`server action BugFix-Maintenance.action_mnt_code_gen` (BugFix-Maintenance)<br>`server action BugFix-Purchase.action_material_request_material_req_gen` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_po_non_inventory_purchase_request_seq_no` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_pr_non_inventory_purchase_request_non_inventory_seq_no` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_purchase_request_cas_cash_purchase_request_seq_no` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_material_req_gen` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_purchase_request_seq_no` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_cash_purchase_request_seq_no` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_purchase_request_non_inventory_seq_no` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_purchase_request_seq_no_2` (BugFix-Purchase)<br>`server action BugFix-Sales.action_project_sales_order_seq_no` (BugFix-Sales)<br>`server action BugFix-Stock.action_con_consolidated_hea_con_consolidated_seq_no` (BugFix-Stock)<br>`server action BugFix-Stock.action_consignment_header_imp_consignment_details_seq_no` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_consignment_details_seq_no` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_consignment_custom_duty` (BugFix-Stock)<br>`server action BugFix-Stock.action_con_consolidated_seq_no` (BugFix-Stock)<br>`server action BugFix-Stock.action_material_req_gen` (BugFix-Stock)<br>`server action BugFix-Stock.action_rr_update_operation_type_in_help_desk_repairs` (BugFix-Stock)<br>`server action BugFix-Stock.action_execute_code` (BugFix-Stock)<br>`stock.location.return_sequence` (BugFix-Stock)<br>`stock.picking.return_sequence` (BugFix-Stock)<br>`stock.return.picking._next_warehouse_phan_name()` (Fix-repair)<br>`stock.return.picking._next_warehouse_ret_name()` (Fix-repair)</details>

**Summary:**

<!-- SUMMARY:model:ir.sequence -->
This repo adds a Sequence window action linked from a Studio-Misc menu and Studio tweaks to the Sequences list and form: an ID column, an optional Next Number column, the actual next number relabelled Next Number Actual, and a small popup form for editing a date range's next numbers. The repo's numbering sequences themselves are listed in the root document.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| ir.sequence | `aw_f4x_ir_sequence_ir_sequence` | Opens **Sequence** records (tree,form). | `model ir.sequence` (base) | `menu BugFix-Studio-Misc.menu_ir_sequence` |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: ir.sequence form customization | `view_ir_sequence_form_inherit` | form | after `//form[1]/sheet[1]/notebook[1]/page[@name='sequence']/field[@name='date_range_ids']/tree[1]/field[@name='date_to']`: add field number_next; set string=Next Number Actual on `//form[1]/sheet[1]/notebook[1]/page[@name='sequence']/field[@name='date_range_ids']/tree[1]/field[@name='number_next_actual']`; after `//form[1]/sheet[1]/notebook[1]/page[@name='sequence']/field[@name='date_range_ids']/tree[1]`: add form | In the Sequence form's date-range table, adds an optional Next Number column, relabels the actual next number 'Next Number Actual', and adds a small popup form for editing a date range's next numbers. | `ir.sequence.number_next_actual` (base)<br>`ir.sequence.number_next` (base)<br>`view base.sequence_view` (base) |  |
| Odoo Studio: ir.sequence tree customization | `view_ir_sequence_tree_inherit` | tree | after `//field[@name='code']`: add field id; after `//field[@name='company_id']`: add field number_next; set string=Next Number Actual on `//field[@name='number_next_actual']` | In the Sequences list view, adds the ID column after Code, an optional Next Number column after Company, and relabels the actual next number 'Next Number Actual'. | `ir.sequence.number_next` (base)<br>`view base.sequence_view_tree` (base) |  |
