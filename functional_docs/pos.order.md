# BugFix-Studio-Misc — `pos.order`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `pos.order` — Point of Sale Orders

*Extends a model created by `point_of_sale`.*

**Summary:**

<!-- SUMMARY:model:pos.order -->
This repo adds a pos.order window action that opens POS Orders in kanban, list, form and pivot views, linked from the Test App 05 menu tree. It also adds a global rule that limits POS orders to the user's companies.
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| pos.order | `act_window_2819_pos_order` | Opens **Point of Sale Orders** records (kanban,tree,form,pivot). | `model pos.order` (point_of_sale) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_pos_order` |
| pos.order | `act_window_2819_pos_order_d7` | Opens **Point of Sale Orders** records (kanban,tree,form,pivot). | `model pos.order` (point_of_sale) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Point Of Sale Order | `rule_151_point_of_sale_order` | For everyone (global rule): read/write/create/delete on Point of Sale Orders only where `[('company_id', 'in', company_ids)]`. | `model pos.order` (point_of_sale)<br>`pos.order.company_id` (point_of_sale) |  |
