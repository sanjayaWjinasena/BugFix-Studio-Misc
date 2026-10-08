# BugFix-Studio-Misc — `stock.landed.cost.lines`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.landed.cost.lines` — Stock Landed Cost Line

*Extends a model created by `stock_landed_costs`.*

Other repos that use this model: `window action BugFix-Stock.act_window_2814_stock_landed_cost_line` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:stock.landed.cost.lines -->
This repo only adds a window action that opens Stock Landed Cost Line records in list and form views. It is not linked to any menu in this repo.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock.landed.cost.line | `act_window_2814_stock_landed_cost_line_d7` | Opens **Stock Landed Cost Line** records (tree,form). | `model stock.landed.cost.lines` (stock_landed_costs) |  |
