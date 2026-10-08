# BugFix-Studio-Misc — `product.category`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `product.category` — Product Category

*Extends a model created by `product`.* Python: `models/product_category.py`.

Other repos that use this model: `account.analytic.account.bugfix_analytics_product_category_id` (BugFix-Analytics)<br>`account.move.line.x_studio_product_category` (BugFix-Accounting)<br>`automation BugFix-Sales.base_automation_291_jin_company_id_in_product_category` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2623_jin_company_id_in_product_category` (BugFix-Sales)<br>`x_rm_none_moving.x_studio_product_category` (BugFix-Accounting)<br>`x_rm_sales_order_line.x_studio_product_category` (BugFix-Accounting)<br>`x_rm_sales_prod_purch.x_studio_product_category` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:product.category -->
This repo adds two Studio fields: a Company link, which a BugFix-Sales server action fills with the user's active company, and a free-text Description that is not shown anywhere. It also adds a Product Categories window action and two Studio view customizations. The list customization adds an optional ID column; the form customization is empty and has no visible effect.
<!-- /SUMMARY -->

**Fields (2):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_company_id` | Company | many2one → `res.company` | Company owning the product category; set to the user's active company by the 'JIN - Company Id in Product Category' server action. | stored | `model res.company` (base) | `server action BugFix-Sales.server_action_2623_jin_company_id_in_product_category` (BugFix-Sales) |
| `x_studio_description` | Description | char | Free-text description of a product category; not shown on any view or used by logic in this repo. | stored |  |  |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Product Categories | `act_window_2471_product_categories_d7` | Opens **Product Category** records (tree,form). | `model product.category` (product) |  |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: product.category.form customization | `view_std_product_category_5548` | form | before `//field[@name='parent_id']`: add ; after `//field[@name='removal_strategy_id']`: add | Empty Studio customization of the Product Category form (xpaths around Parent Category and Removal Strategy add nothing); has no visible effect. | `view product.product_category_form_view` (product) |  |
| Odoo Studio: product.category.list customization | `view_std_product_category_5552` | tree | after `//field[@name='display_name']`: add field id | Adds an optional (shown by default) ID column after the name in the Product Categories list view. | `view product.product_category_list_view` (product) |  |
