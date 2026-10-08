# BugFix-Studio-Misc — `ir.ui.view`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.ui.view` — View

*Extends a model created by `base`.*

Other repos that use this model: `bugfix_sales.minimum_sales_margin.seed._attach_c01_intro_conclusion_view()` (BugFix-Sales)<br>`helpdesk.ticket._fix_studio_report_template_keys()` (Fix-repair)<br>`helpdesk.ticket._migrate_studio_views_to_native()` (Fix-repair)<br>`helpdesk.ticket._sanitize_broken_studio_task_form_xpath()` (Fix-repair)

**Summary:**

<!-- SUMMARY:model:ir.ui.view -->
This repo adds the record ID column after Model in the Views list view (Settings, Technical). Nothing else is changed.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: ir.ui.view tree customization | `view_std_ir_ui_view_2658` | tree | after `//field[@name='model']`: add field id | Adds the record ID column after Model in the Views list view (Settings > Technical). | `view base.view_view_tree` (base) |  |
