# BugFix-Studio-Misc — `account.tax`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.tax` — Tax

*Extends a model created by `account`.*

Other repos that use this model: `record rule BugFix-Accounting.rule_84_tax_multi_company` (BugFix-Accounting)<br>`server action BugFix-Accounting.sa_f5_x_tp_invoice_line_tp_invoice_linetax_update` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2432_tp_invoice_linetax_update` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_2758_taxes` (BugFix-Accounting)<br>`x_po_line_non_inventor.x_studio_taxes` (BugFix-Purchase)<br>`x_tp_invoice_line.x_studio_taxes` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:account.tax -->
This repo adds one window action, Taxes, that opens Taxes in kanban, list and form views. It is not linked to a menu here. Nothing else is changed.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Taxes | `act_window_2758_taxes_d7` | Opens **Tax** records (kanban,tree,form). | `model account.tax` (account) |  |
