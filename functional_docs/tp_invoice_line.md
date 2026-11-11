# BugFix-Studio-Misc — `tp_invoice_line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `tp_invoice_line` — TP Invoice Line

*Extends a model created by `BugFix-Accounting`.*

Other repos that use this model: `access right BugFix-Accounting.access_tp_invoice_line_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_tp_invoice_line_group_user` (BugFix-Accounting)<br>`automation BugFix-Accounting.automation_tp_invoice_linetax_update` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_tp_invoice_line_tp_invoice_linetax_update` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_post_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_tp_invoice_linetax_update` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_post` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_tp_invoice_line` (BugFix-Accounting)<details><summary>+2 more</summary>`window action BugFix-Accounting.action_tp_invoice_line_2` (BugFix-Accounting)<br>`tp_invoice_header.tp_lines` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:tp_invoice_line -->
TP Invoice Line is created by BugFix-Accounting. This repo only adds read/write/create access for Purchase / Jin - PO Invoicing & Payment - Imports.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| tp_invoice_line | `access_g_tp_invoice_line_tp_invoice_line_purchase_jin_po_invoicing_payment_import` | Gives **Purchase / Jin - PO Invoicing & Payment - Imports** read/write/create access to TP Invoice Line records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_imports`<br>`model tp_invoice_line` (BugFix-Accounting) |  |
