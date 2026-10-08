# BugFix-Studio-Misc — `ir.module.category`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.module.category` — Application

*Extends a model created by `base`.*

**Summary:**

<!-- SUMMARY:model:ir.module.category -->
This repo adds three window actions that open Application categories in list and form views, each linked from a Studio-Misc menu. Nothing else is changed.
<!-- /SUMMARY -->

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Application-1 | `aw_f4x_ir_module_category_application_1` | Opens **Application** records (tree,form). | `model ir.module.category` (base) | `menu BugFix-Studio-Misc.menu_f6f_application_1` |
| ir.module.category | `aw_f4x_ir_module_category_ir_module_category` | Opens **Application** records (tree,form). | `model ir.module.category` (base) | `menu BugFix-Studio-Misc.menu_f6f_ir_module_category` |
| ir.module.cateory | `aw_f4x_ir_module_category_ir_module_cateory` | Opens **Application** records (tree,form). | `model ir.module.category` (base) | `menu BugFix-Studio-Misc.menu_f6f_ir_module_cateory` |
