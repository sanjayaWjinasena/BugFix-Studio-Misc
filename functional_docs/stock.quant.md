# BugFix-Studio-Misc — `stock.quant`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.quant` — Quants

*Extends a model created by `stock`.*

Other repos that use this model: `access right BugFix-Stock.access_6266_inv___administrator` (BugFix-Stock)<br>`record rule BugFix-Stock.rule_52_stock_quant_multi_company` (BugFix-Stock)<br>`server action BugFix-Sales.server_action_2096_rr_insufficient_transfer_inventory_details` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2162_proj_item_related_details_in_project_so` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2188_proj_create_pr_from_sales_quotation` (BugFix-Sales)<br>`window action BugFix-Stock.action_2187_stock_quant` (BugFix-Stock)<br>`x_mr_config._compute_on_hand_qty_2()` (BugFix-Purchase, BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:stock.quant -->
This repo only adds a window action that opens Quants (stock on hand) records in kanban, list, form, pivot and graph views, linked to an entry under the TEST APP 05 menu.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock.quant | `act_window_2187_stock_quant_d7` | Opens **Quants** records (kanban,tree,form,pivot,graph). | `model stock.quant` (stock) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_stock_quant` |
