# BugFix-Studio-Misc — `account.tax`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.tax` — Tax

*Extends a model created by `account`.*

Other repos that use this model: `record rule BugFix-Accounting.rule_84_tax_multi_company` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_tp_invoice_line_tp_invoice_linetax_update` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_tp_invoice_linetax_update` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_taxes` (BugFix-Accounting)<br>`po_line_non_inventor.taxes` (BugFix-Purchase)<br>`tp_invoice_line.taxes` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:account.tax -->
This repo adds one window action, Taxes, that opens Taxes in kanban, list and form views. It is not linked to a menu here. Nothing else is changed.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Taxes | `action_taxes_d7` | Opens **Tax** records (kanban,tree,form). | `model account.tax` (account) |  |
