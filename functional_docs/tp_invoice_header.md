# BugFix-Studio-Misc — `tp_invoice_header`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `tp_invoice_header` — TP Invoice Header

*Extends a model created by `BugFix-Accounting`.*

Other repos that use this model: `access right BugFix-Accounting.access_tp_invoice_header_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_tp_invoice_header_group_user` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_tp_invoice_header_user` (BugFix-Accounting)<br>`account.bank.statement.line.created_from_tp_invoice` (BugFix-Accounting)<br>`account.bank.statement.line.many2one_field_KKFaY` (BugFix-Accounting)<br>`account.bank.statement.line.many2one_field_aIXMs` (BugFix-Accounting)<br>`account.bank.statement.line.tp_id` (BugFix-Accounting)<br>`account.move.tp_id` (BugFix-Accounting)<details><summary>+21 more</summary>`account.payment.created_from_tp_invoice` (BugFix-Accounting)<br>`account.payment.many2one_field_KKFaY` (BugFix-Accounting)<br>`account.payment.many2one_field_aIXMs` (BugFix-Accounting)<br>`account.payment.tp_id` (BugFix-Accounting)<br>`account.payment.tp_invoice_no` (BugFix-Accounting)<br>`automation BugFix-Accounting.automation_tp_invoice_currency_update` (BugFix-Accounting)<br>`automation BugFix-Accounting.base_automation_65_jin_third_party_tp_invoice_seq_no` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_tp_invoice_header_tp_invoice_currency_update` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_tp_invoice_header_tp_invoice_seq_no` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_apply_selected_charge_lines_to_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_tp_invoice_seq_no` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_post_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_tp_invoice_currency_update` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_apply_charges` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_post` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_tp_invoice_header` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_tp_invoices` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_tp_invoices_2` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_tp_invoice_header_2` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_tp_invoice_header_2_2` (BugFix-Accounting)<br>`tp_invoice_line.tp_invoice_header_id` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:tp_invoice_header -->
TP Invoice Header is created by BugFix-Accounting. This repo only adds read/write/create access for Purchase / Jin - PO Invoicing & Payment - Imports.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| tp_invoice_header | `access_g_tp_invoice_header_tp_invoice_header_purchase_jin_po_invoicing_payment_import` | Gives **Purchase / Jin - PO Invoicing & Payment - Imports** read/write/create access to TP Invoice Header records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_imports`<br>`model tp_invoice_header` (BugFix-Accounting) |  |
