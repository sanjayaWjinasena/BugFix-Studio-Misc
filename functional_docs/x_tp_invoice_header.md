# BugFix-Studio-Misc — `x_tp_invoice_header`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_tp_invoice_header` — TP Invoice Header

*Extends a model created by `BugFix-Accounting`.*

Other repos that use this model: `access right BugFix-Accounting.access_1370_tp_invoice_header_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_1371_tp_invoice_header_group_user` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_x_tp_invoice_header_user` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_created_from_tp_invoice` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_many2one_field_KKFaY` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_many2one_field_aIXMs` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_tp_id` (BugFix-Accounting)<br>`account.move.x_studio_tp_id` (BugFix-Accounting)<details><summary>+21 more</summary>`account.payment.x_studio_created_from_tp_invoice` (BugFix-Accounting)<br>`account.payment.x_studio_many2one_field_KKFaY` (BugFix-Accounting)<br>`account.payment.x_studio_many2one_field_aIXMs` (BugFix-Accounting)<br>`account.payment.x_studio_tp_id` (BugFix-Accounting)<br>`account.payment.x_studio_tp_invoice_no` (BugFix-Accounting)<br>`automation BugFix-Accounting.base_automation_184_tp_invoice_currency_update` (BugFix-Accounting)<br>`automation BugFix-Accounting.base_automation_65_jin_third_party_tp_invoice_seq_no` (BugFix-Accounting)<br>`server action BugFix-Accounting.sa_f5_x_tp_invoice_header_tp_invoice_currency_update` (BugFix-Accounting)<br>`server action BugFix-Accounting.sa_f5_x_tp_invoice_header_tp_invoice_seq_no` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1378_imp_apply_selected_charge_lines_to_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1381_tp_invoice_seq_no` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2112_tp_invoice_currency_update` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_apply_charges` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_post` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_1379_tp_invoice_header` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_1382_tp_invoices` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_1383_tp_invoices` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_2430_x_tp_invoice_header` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_2864_tp_invoice_header` (BugFix-Accounting)<br>`x_tp_invoice_line.x_studio_tp_invoice_header_id` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:x_tp_invoice_header -->
TP Invoice Header is created by BugFix-Accounting. This repo only adds read/write/create access for Purchase / Jin - PO Invoicing & Payment - Imports.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_tp_invoice_header | `access_g_x_tp_invoice_header_x_tp_invoice_header_purchase_jin_po_invoicing_payment_import` | Gives **Purchase / Jin - PO Invoicing & Payment - Imports** read/write/create access to TP Invoice Header records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_imports`<br>`model x_tp_invoice_header` (BugFix-Accounting) |  |
