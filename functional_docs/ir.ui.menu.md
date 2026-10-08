# BugFix-Studio-Misc — `ir.ui.menu`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.ui.menu` — Menu

*Extends a model created by `base`.*

Other repos that use this model: `bugfix_sales.minimum_sales_margin.seed._cleanup_orphan_studio_menu_pins()` (BugFix-Sales)<br>`bugfix_sales.minimum_sales_margin.seed._hide_minimum_sales_margin_menus()` (BugFix-Sales)

**Summary:**

<!-- SUMMARY:model:ir.ui.menu -->
This repo adds optional Parent Menu and ID columns to the Menu Items list view. Nothing else is changed on the model; the repo's 309 menus are listed in the root document.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: ir.ui.menu tree customization | `view_std_ir_ui_menu_5317` | tree | after `//field[@name='sequence']`: add field parent_id; after `//field[@name='complete_name']`: add field id | In the Menu Items list view, adds optional Parent Menu and ID columns. | `ir.ui.menu.parent_id` (base)<br>`view base.edit_menu` (base) |  |
