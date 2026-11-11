# BugFix-Studio-Misc — `stock.route`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.route` — Inventory Routes

*Extends a model created by `stock`.*

Other repos that use this model: `window action BugFix-Stock.action_stock_location_route` (BugFix-Stock)<br>`window action BugFix-Stock.action_inventory_routes` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:stock.route -->
This repo only adds two window actions that open Inventory Routes in list and form views. Both are linked to entries under the TEST APP 05 menu.
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Inventory routes | `action_inventory_routes_d7` | Opens **Inventory Routes** records (tree,form). | `model stock.route` (stock) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_inventory_routes` |
| stock.location.route | `action_stock_location_route_d7` | Opens **Inventory Routes** records (tree,form). | `model stock.route` (stock) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_stock_location_route` |
