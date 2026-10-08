# BugFix-Studio-Misc — `ir.actions.act_window`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.actions.act_window` — Action Window

*Extends a model created by `base`.*

Other repos that use this model: `bugfix_sales.minimum_sales_margin.seed._hide_minimum_sales_margin_menus()` (BugFix-Sales)

**Summary:**

<!-- SUMMARY:model:ir.actions.act_window -->
This repo adds a Studio tweak to the Window Actions list view (Settings, Technical) that shows the record ID after View Ref. Nothing else is changed.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: ir.actions.windows.tree customization | `view_std_ir_actions_act_window_2441` | tree | after `//field[@name='view_id']`: add field id | Adds the record ID column after View Ref. in the Window Actions list view (Settings > Technical). | `view base.view_window_action_tree` (base) |  |
