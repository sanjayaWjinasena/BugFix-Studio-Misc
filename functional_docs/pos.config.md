# BugFix-Studio-Misc — `pos.config`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `pos.config` — Point of Sale Configuration

*Extends a model created by `point_of_sale`.*

**Summary:**

<!-- SUMMARY:model:pos.config -->
This repo adds four pos.config window actions that open Point of Sale Configurations in kanban, list and form views, one linked from the Test App 05 menu tree. It also adds a global rule that limits POS configurations to the user's companies.
<!-- /SUMMARY -->

**Window actions (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| pos.config | `act_window_2818_pos_config` | Opens **Point of Sale Configuration** records (kanban,tree,form). | `model pos.config` (point_of_sale) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_pos_config` |
| pos.config | `act_window_2821_pos_config` | Opens **Point of Sale Configuration** records (kanban,tree,form). | `model pos.config` (point_of_sale) |  |
| pos.config | `act_window_2821_pos_config_d7` | Opens **Point of Sale Configuration** records (kanban,tree,form). | `model pos.config` (point_of_sale) |  |
| pos.config | `act_window_2818_pos_config_d7` | Opens **Point of Sale Configuration** records (kanban,tree,form). | `model pos.config` (point_of_sale) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Point Of Sale Config | `rule_153_point_of_sale_config` | For everyone (global rule): read/write/create/delete on Point of Sale Configuration only where `[('company_id', 'in', company_ids)]`. | `model pos.config` (point_of_sale)<br>`pos.config.company_id` (point_of_sale) |  |
