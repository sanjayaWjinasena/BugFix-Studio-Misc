# BugFix-Studio-Misc — `ir.model.access`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.model.access` — Model Access

*Extends a model created by `base`.*

**Summary:**

<!-- SUMMARY:model:ir.model.access -->
This repo adds four window actions that open Access Rights in list and form views (User Group Access Rights, ir.model and others), three of them linked from Studio-Misc menus. It also makes the access-right Name searchable and ships an empty Studio customization of the editable Access Rights list. The repo's own access rights are listed under the models they protect.
<!-- /SUMMARY -->

**Window actions (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| User Group - Access Rights | `aw_f4x_ir_model_access_user_group_access_rights_1` | Opens **Model Access** records (tree,form). | `model ir.model.access` (base) |  |
| User Group Access Rights | `aw_f4x_ir_model_access_user_group_access_rights` | Opens **Model Access** records (tree,form). | `model ir.model.access` (base) | `menu BugFix-Studio-Misc.menu_f6f_user_group_access_rights` |
| ir.model | `aw_f4x_ir_model_access_ir_model` | Opens **Model Access** records (tree,form). | `model ir.model.access` (base) | `menu BugFix-Studio-Misc.menu_f6f_ir_model` |
| ir.model.access | `aw_f4x_ir_model_access_ir_model_access` | Opens **Model Access** records (tree,form). | `model ir.model.access` (base) | `menu BugFix-Studio-Misc.menu_f6f_ir_model_access` |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: ir.model.access search customization | `view_std_ir_model_access_2323` | search | after `//field[@name='group_id']`: add field name | Adds the access-right Name as a searchable field in the Access Rights search view. | `ir.model.access.name` (base)<br>`view base.ir_access_view_search` (base) |  |
| Odoo Studio: ir.model.access.view.tree.edition customization | `view_std_ir_model_access_5301` | tree | before `//tree[1]/field[@name='name']`: add ; after `//tree[1]/field[@name='name']`: add | Empty Studio customization of the editable Access Rights list (two xpaths around Name that add nothing); has no visible effect. | `view base.ir_access_view_tree_edition` (base) |  |
