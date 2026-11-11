# BugFix-Studio-Misc — `temp_tp_invoice_head`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `temp_tp_invoice_head` — Temp TP Invoice Header

*Extends a model created by `BugFix-Accounting`.*

Other repos that use this model: `access right BugFix-Accounting.access_temp_tp_invoice_header_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_temp_tp_invoice_header_group_user` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_temp_tp_invoice_head_user` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_apply_selected_charge_lines_to_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_apply_charges` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_temp_tp_invoice_header` (BugFix-Accounting)<br>`temp_tp_invoice_line.temp_tp_invoice_header_id` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:temp_tp_invoice_head -->
Temp TP Invoice Header is created by BugFix-Accounting. This repo only adds full access for Purchase / Jin - PO Invoicing & Payment - Imports.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| temp_tp_invoice_head | `access_g_temp_tp_invoice_head_temp_tp_invoice_head_purchase_jin_po_invoicing_payment_i` | Gives **Purchase / Jin - PO Invoicing & Payment - Imports** read/write/create/delete access to Temp TP Invoice Header records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_imports`<br>`model temp_tp_invoice_head` (BugFix-Accounting) |  |
