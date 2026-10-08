# BugFix-Studio-Misc — `stock.rule`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.rule` — Stock Rule

*Extends a model created by `stock`.*

Other repos that use this model: `record rule BugFix-Stock.rule_56_product_pulled_flow_multi_company` (BugFix-Stock)<br>`window action BugFix-Stock.act_window_2835_stock_rule` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:stock.rule -->
This repo only adds a window action that opens Stock Rule records in list and form views. It is not linked to any menu in this repo.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock.rule | `act_window_2835_stock_rule_d7` | Opens **Stock Rule** records (tree,form). | `model stock.rule` (stock) |  |
