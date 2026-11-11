# BugFix-Studio-Misc — `account.journal`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.journal` — Journal

*Extends a model created by `account`.*

Other repos that use this model: `account.move._rug_auto_settle()` (Fix-repair)<br>`hr.contract.related_field_Dj7xv` (BugFix-HR)<br>`record rule BugFix-Accounting.rule_80_journal_multi_company` (BugFix-Accounting)<br>`sale.order._seed_advance_payment_method_lines()` (Fix-repair)<br>`server action BugFix-Accounting.action_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_post_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_pr_validate_cash_issued_in_npo` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi` (BugFix-Accounting)<details><summary>+12 more</summary>`server action BugFix-Accounting.srv_tp_invoice_post` (BugFix-Accounting)<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_cash_purchase_cash_issued` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_cash_purchase_cash_settled` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_npo_invoice_journal` (BugFix-Purchase)<br>`server action BugFix-Sales.action_sls_create_customer_payment` (BugFix-Sales)<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_consignment_custom_duty` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_update_consignment` (BugFix-Stock)<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase` (BugFix-Stock)<br>`window action BugFix-Accounting.action_accounting_dashboard` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_journal` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:account.journal -->
This repo adds one window action, Journal, that opens Journals in kanban, list, form and pivot views. It is not linked to a menu here. Nothing else is changed.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Journal | `action_journal_d7` | Opens **Journal** records (kanban,tree,form,pivot). | `model account.journal` (account) |  |
