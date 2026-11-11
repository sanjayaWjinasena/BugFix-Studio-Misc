# BugFix-Studio-Misc — `temp_tp_invoice_line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `temp_tp_invoice_line` — Temp TP Invoice Line

*Extends a model created by `BugFix-Accounting`.*

Other repos that use this model: `access right BugFix-Accounting.access_temp_tp_invoice_line_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_temp_tp_invoice_line_group_user` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_temp_tp_invoice_line_user` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_temp_tp_invoice_line` (BugFix-Accounting)<br>`temp_tp_invoice_head.charge_line` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:temp_tp_invoice_line -->
Temp TP Invoice Line is created by BugFix-Accounting. This repo only adds read/write/create access for Purchase / Jin - PO Invoicing & Payment - Imports.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| temp_tp_invoice_line | `access_g_temp_tp_invoice_line_temp_tp_invoice_line_purchase_jin_po_invoicing_payment_i` | Gives **Purchase / Jin - PO Invoicing & Payment - Imports** read/write/create access to Temp TP Invoice Line records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_imports`<br>`model temp_tp_invoice_line` (BugFix-Accounting) |  |
