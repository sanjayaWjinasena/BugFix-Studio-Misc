# BugFix-Studio-Misc — `x_tp_invoice_line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_tp_invoice_line` — TP Invoice Line

*Extends a model created by `BugFix-Accounting`.*

Other repos that use this model: `access right BugFix-Accounting.access_1372_tp_invoice_line_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_1373_tp_invoice_line_group_user` (BugFix-Accounting)<br>`automation BugFix-Accounting.base_automation_242_tp_invoice_linetax_update` (BugFix-Accounting)<br>`server action BugFix-Accounting.sa_f5_x_tp_invoice_line_tp_invoice_linetax_update` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2432_tp_invoice_linetax_update` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_post` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_1380_tp_invoice_line` (BugFix-Accounting)<details><summary>+2 more</summary>`window action BugFix-Accounting.action_2865_tp_invoice_line` (BugFix-Accounting)<br>`x_tp_invoice_header.x_studio_tp_lines` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:x_tp_invoice_line -->
TP Invoice Line is created by BugFix-Accounting. This repo only adds read/write/create access for Purchase / Jin - PO Invoicing & Payment - Imports.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_tp_invoice_line | `access_g_x_tp_invoice_line_x_tp_invoice_line_purchase_jin_po_invoicing_payment_import` | Gives **Purchase / Jin - PO Invoicing & Payment - Imports** read/write/create access to TP Invoice Line records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_imports`<br>`model x_tp_invoice_line` (BugFix-Accounting) |  |
