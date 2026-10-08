# BugFix-Studio-Misc — `x_product_product`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_product_product` — product.product

*Created by this repo.* Python: `models/x_product_product.py`, `models/x_product_product_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_product_product -->
Purpose not evident from code. It is a Studio model labelled product.product, but it is not linked to real products. It holds only a name (`x_name`) and has default Studio form, list and search views. Internal users can read it and administrators have full access.
<!-- /SUMMARY -->

**Fields (7):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_name` | Name | char | Name of a record in the Studio model `x_product_product` (labelled product.product but unrelated to real products); shown in its default list, form and search views. | stored |  | `view BugFix-Studio-Misc.view_2607_default_list_view_for_x_product_product`<br>`view BugFix-Studio-Misc.view_2608_default_form_view_for_x_product_product`<br>`view BugFix-Studio-Misc.view_2609_default_search_view_for_x_product_product` |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_product_product | `view_2608_default_form_view_for_x_product_product` | form | full form layout with 1 fields | Default Studio form for the x_product_product model: a single required Name field with empty groups. | `x_product_product.x_name` |  |
| Default list view for x_product_product | `view_2607_default_list_view_for_x_product_product` | tree | full tree layout with 1 fields | Default Studio list view for x_product_product showing only Name. | `x_product_product.x_name` |  |
| Default search view for x_product_product | `view_2609_default_search_view_for_x_product_product` | search | full search layout with 1 fields | Default Studio search view for x_product_product allowing search by Name. | `x_product_product.x_name` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| product.product group_user | `access_f3_product_product_group_user` | Gives **User types / Internal User** read access to product.product records. | `group base.group_user` (base)<br>`model x_product_product` |  |
| product.product group_user | `access_g_product_product_group_user_x_product_product_user_types_internal_user` | Gives **User types / Internal User** read access to product.product records. | `group base.group_user` (base)<br>`model x_product_product` |  |
| x_product_product admin | `access_x_product_product_admin` | Gives **Administration / Settings** read/write/create/delete access to product.product records. | `group base.group_system` (base)<br>`model x_product_product` |  |
