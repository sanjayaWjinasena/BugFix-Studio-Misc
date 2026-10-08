# BugFix-Studio-Misc — `x_bve.salesreport`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_bve.salesreport` — Sales Report

*Created by this repo.* Python: `models/x_bve_salesreport.py`, `models/x_bve_salesreport_gap.py`.

**Summary:**

<!-- SUMMARY:model:x_bve.salesreport -->
A read-only BI view-editor report, Sales Report, built as an SQL view over sales orders and their lines. Each row shows the customer, currency, credit limit, invoice status, pricelist, sales team, salesperson, warehouse, the Studio total, the product, and ordered and delivered quantities. Users open it from the Sales Report window action in list, graph and pivot views. All users can read it; only Administration / Settings has full access.
<!-- /SUMMARY -->

**Fields (18):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_bve_t1_currency_id` | Currency | many2one → `res.currency` | Column 'Currency' (from the sale order) of the BI view-editor report 'Sales Report', a read-only SQL-view model; used in the pivot, graph, search and list views. | stored | `model res.currency` (base) | `view BugFix-Studio-Misc.view_9387_pivot_analysis_e`<br>`view BugFix-Studio-Misc.view_9388_graph_analysis_e`<br>`view BugFix-Studio-Misc.view_9389_search_bi_view_e`<br>`view BugFix-Studio-Misc.view_9390_tree_analysis_e` |
| `x_bve_t1_invoice_status` | Invoice Status | selection: upselling=Upselling Opportunity; invoiced=Fully Invoiced; to invoice=To Invoice; no=Nothing to Invoice | Column 'Invoice Status' (from the sale order) of the BI view-editor report 'Sales Report', a read-only SQL-view model; used in the pivot, graph, search and list views. | stored |  | `view BugFix-Studio-Misc.view_9387_pivot_analysis_e`<br>`view BugFix-Studio-Misc.view_9388_graph_analysis_e`<br>`view BugFix-Studio-Misc.view_9389_search_bi_view_e`<br>`view BugFix-Studio-Misc.view_9390_tree_analysis_e` |
| `x_bve_t1_partner_id` | Customer | many2one → `res.partner` | Column 'Customer' (from the sale order) of the BI view-editor report 'Sales Report', a read-only SQL-view model; used in the list view. | stored | `model res.partner` (base) | `view BugFix-Studio-Misc.view_9390_tree_analysis_e` |
| `x_bve_t1_pricelist_id` | Pricelist | many2one → `product.pricelist` | Column 'Pricelist' (from the sale order) of the BI view-editor report 'Sales Report', a read-only SQL-view model; used in the pivot, graph, search and list views. | stored | `model product.pricelist` (product) | `view BugFix-Studio-Misc.view_9387_pivot_analysis_e`<br>`view BugFix-Studio-Misc.view_9388_graph_analysis_e`<br>`view BugFix-Studio-Misc.view_9389_search_bi_view_e`<br>`view BugFix-Studio-Misc.view_9390_tree_analysis_e` |
| `x_bve_t1_team_id` | Sales Team | many2one → `crm.team` | Column 'Sales Team' (from the sale order) of the BI view-editor report 'Sales Report', a read-only SQL-view model; used in the list view. | stored | `model crm.team` (sales_team) | `view BugFix-Studio-Misc.view_9390_tree_analysis_e` |
| `x_bve_t1_user_id` | Salesperson | many2one → `res.users` | Column 'Salesperson' (from the sale order) of the BI view-editor report 'Sales Report', a read-only SQL-view model; used in the pivot, graph, search and list views. | stored | `model res.users` (base) | `view BugFix-Studio-Misc.view_9387_pivot_analysis_e`<br>`view BugFix-Studio-Misc.view_9388_graph_analysis_e`<br>`view BugFix-Studio-Misc.view_9389_search_bi_view_e`<br>`view BugFix-Studio-Misc.view_9390_tree_analysis_e` |
| `x_bve_t1_warehouse_id` | Warehouse | many2one → `stock.warehouse` | Column 'Warehouse' (from the sale order) of the BI view-editor report 'Sales Report', a read-only SQL-view model; used in the pivot, graph, search and list views. | stored | `model stock.warehouse` (stock) | `view BugFix-Studio-Misc.view_9387_pivot_analysis_e`<br>`view BugFix-Studio-Misc.view_9388_graph_analysis_e`<br>`view BugFix-Studio-Misc.view_9389_search_bi_view_e`<br>`view BugFix-Studio-Misc.view_9390_tree_analysis_e` |
| `x_bve_t1_x_studio_customer_credit_limit` | Customer Credit Limit | float | Column 'Customer Credit Limit' (from the sale order) of the BI view-editor report 'Sales Report', a read-only SQL-view model; used in the list view. | stored |  | `view BugFix-Studio-Misc.view_9390_tree_analysis_e` |
| `x_bve_t1_x_studio_total` | Total | char | Column 'Total' (text, from the sale order's Studio Total field) of the BI view-editor Sales Report, a read-only SQL-view model; used in its pivot, graph, search and list views. | stored |  | `view BugFix-Studio-Misc.view_9387_pivot_analysis_e`<br>`view BugFix-Studio-Misc.view_9388_graph_analysis_e`<br>`view BugFix-Studio-Misc.view_9389_search_bi_view_e`<br>`view BugFix-Studio-Misc.view_9390_tree_analysis_e` |
| `x_bve_t2_product_id` | Product | many2one → `product.product` | Column 'Product' (from the sale order line) of the BI view-editor report 'Sales Report', a read-only SQL-view model; used in the pivot, graph, search and list views. | stored | `model product.product` (product) | `view BugFix-Studio-Misc.view_9387_pivot_analysis_e`<br>`view BugFix-Studio-Misc.view_9388_graph_analysis_e`<br>`view BugFix-Studio-Misc.view_9389_search_bi_view_e`<br>`view BugFix-Studio-Misc.view_9390_tree_analysis_e` |
| `x_bve_t2_product_uom_qty` | Quantity | float | Column 'Quantity' (from the sale order line) of the BI view-editor report 'Sales Report', a read-only SQL-view model; used in the list view. | stored |  | `view BugFix-Studio-Misc.view_9390_tree_analysis_e` |
| `x_bve_t2_qty_delivered` | Delivery Quantity | float | Column 'Delivery Quantity' (from the sale order line) of the BI view-editor report 'Sales Report', a read-only SQL-view model; used in the list view. | stored |  | `view BugFix-Studio-Misc.view_9390_tree_analysis_e` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales Report | `act_window_3592_sales_report` | Opens **Sales Report** records (tree,graph,pivot). | `model x_bve.salesreport` |  |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Graph Analysis | `view_9388_graph_analysis_e` | graph | full graph layout with 7 fields | Bar-chart (stacked) analysis of the x_bve.salesreport BI dataset, grouped by currency, invoice status, pricelist, salesperson, warehouse, Studio total and product. | `x_bve.salesreport.x_bve_t1_currency_id`<br>`x_bve.salesreport.x_bve_t1_invoice_status`<br>`x_bve.salesreport.x_bve_t1_pricelist_id`<br>`x_bve.salesreport.x_bve_t1_user_id`<br>`x_bve.salesreport.x_bve_t1_warehouse_id`<details><summary>+2 more</summary>`x_bve.salesreport.x_bve_t1_x_studio_total`<br>`x_bve.salesreport.x_bve_t2_product_id`</details> |  |
| Pivot Analysis | `view_9387_pivot_analysis_e` | pivot | full pivot layout with 7 fields | Pivot analysis of the x_bve.salesreport BI dataset with rows by currency, invoice status, pricelist, salesperson, warehouse, Studio total and product. | `x_bve.salesreport.x_bve_t1_currency_id`<br>`x_bve.salesreport.x_bve_t1_invoice_status`<br>`x_bve.salesreport.x_bve_t1_pricelist_id`<br>`x_bve.salesreport.x_bve_t1_user_id`<br>`x_bve.salesreport.x_bve_t1_warehouse_id`<details><summary>+2 more</summary>`x_bve.salesreport.x_bve_t1_x_studio_total`<br>`x_bve.salesreport.x_bve_t2_product_id`</details> |  |
| Search BI View | `view_9389_search_bi_view_e` | search | full search layout with 7 fields | Search view for the x_bve.salesreport BI dataset allowing search by currency, invoice status, pricelist, salesperson, warehouse, Studio total and product. | `x_bve.salesreport.x_bve_t1_currency_id`<br>`x_bve.salesreport.x_bve_t1_invoice_status`<br>`x_bve.salesreport.x_bve_t1_pricelist_id`<br>`x_bve.salesreport.x_bve_t1_user_id`<br>`x_bve.salesreport.x_bve_t1_warehouse_id`<details><summary>+2 more</summary>`x_bve.salesreport.x_bve_t1_x_studio_total`<br>`x_bve.salesreport.x_bve_t2_product_id`</details> |  |
| Tree Analysis | `view_9390_tree_analysis_e` | tree | full tree layout with 12 fields | Read-only list (no create) of the x_bve.salesreport BI dataset: customer, currency, customer credit limit, invoice status, pricelist, sales team, salesperson, warehouse, total, product, delivered and ordered quantity. | `x_bve.salesreport.x_bve_t1_currency_id`<br>`x_bve.salesreport.x_bve_t1_invoice_status`<br>`x_bve.salesreport.x_bve_t1_partner_id`<br>`x_bve.salesreport.x_bve_t1_pricelist_id`<br>`x_bve.salesreport.x_bve_t1_team_id`<details><summary>+7 more</summary>`x_bve.salesreport.x_bve_t1_user_id`<br>`x_bve.salesreport.x_bve_t1_warehouse_id`<br>`x_bve.salesreport.x_bve_t1_x_studio_customer_credit_limit`<br>`x_bve.salesreport.x_bve_t1_x_studio_total`<br>`x_bve.salesreport.x_bve_t2_product_id`<br>`x_bve.salesreport.x_bve_t2_product_uom_qty`<br>`x_bve.salesreport.x_bve_t2_qty_delivered`</details> |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| read access to x_bve.salesreport | `access_8538_read_access_to_x_bve_salesreport` | Gives **all users** read access to Sales Report records. | `model x_bve.salesreport` |  |
| x_bve.salesreport admin | `access_x_bve_salesreport_admin` | Gives **Administration / Settings** read/write/create/delete access to Sales Report records. | `group base.group_system` (base)<br>`model x_bve.salesreport` |  |
