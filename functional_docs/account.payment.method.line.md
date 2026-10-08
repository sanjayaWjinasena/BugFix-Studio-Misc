# BugFix-Studio-Misc — `account.payment.method.line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.payment.method.line` — Payment Methods

*Extends a model created by `account`.*

Other repos that use this model: `sale.order._seed_advance_payment_method_lines()` (Fix-repair)<br>`window action BugFix-Accounting.act_window_2741_account_payment_method_line` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:account.payment.method.line -->
This repo adds one window action that opens Payment Methods in list and form views. It is not linked to a menu here. Nothing else is changed.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| account.payment.method.line | `act_window_2741_account_payment_method_line_d7` | Opens **Payment Methods** records (tree,form). | `model account.payment.method.line` (account) |  |
