# BugFix-Studio-Misc — `pos.payment`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `pos.payment` — Point of Sale Payments

*Extends a model created by `point_of_sale`.*

**Summary:**

<!-- SUMMARY:model:pos.payment -->
This repo adds a pos.payment window action that opens POS Payments in list and form views, linked from the Test App 05 menu tree. It also adds a global rule that limits POS payments to the user's companies.
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| pos.payment | `act_window_2820_pos_payment` | Opens **Point of Sale Payments** records (tree,form). | `model pos.payment` (point_of_sale) |  |
| pos.payment | `act_window_2820_pos_payment_d7` | Opens **Point of Sale Payments** records (tree,form). | `model pos.payment` (point_of_sale) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_pos_payment` |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| PoS Payment | `rule_156_pos_payment` | For everyone (global rule): read/write/create/delete on Point of Sale Payments only where `[('company_id', 'in', company_ids)]`. | `model pos.payment` (point_of_sale)<br>`pos.payment.company_id` (point_of_sale) |  |
