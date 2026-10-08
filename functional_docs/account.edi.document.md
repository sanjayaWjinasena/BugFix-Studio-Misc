# BugFix-Studio-Misc — `account.edi.document`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.edi.document` — Electronic Document for an account.move

*Extends a model created by `account_edi`.*

**Summary:**

<!-- SUMMARY:model:account.edi.document -->
This repo adds one window action, Sales invoice lines, that opens electronic documents of invoices in a list view. It is reached from the Studio-Misc menu Sales invoice lines. Nothing else is changed.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales invoice lines | `act_window_1570_sales_invoice_lines_d7` | Opens **Electronic Document for an account.move** records (tree). | `model account.edi.document` (account_edi) | `menu BugFix-Studio-Misc.menu_f6_sales_invoice_lines` |
