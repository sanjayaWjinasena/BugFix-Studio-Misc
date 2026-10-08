# BugFix-Studio-Misc — `stock.landed.cost`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.landed.cost` — Stock Landed Cost

*Extends a model created by `stock_landed_costs`.*

**Summary:**

<!-- SUMMARY:model:stock.landed.cost -->
This repo only adds a window action that opens Stock Landed Cost records in kanban, list and form views, linked to an entry under the TEST APP 05 menu.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock.landed.cos | `act_window_2813_stock_landed_cos_d7` | Opens **Stock Landed Cost** records (kanban,tree,form). | `model stock.landed.cost` (stock_landed_costs) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_stock_landed_cos` |
