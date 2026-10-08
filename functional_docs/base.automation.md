# BugFix-Studio-Misc — `base.automation`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `base.automation` — Automation Rule

*Extends a model created by `base_automation`.*

Other repos that use this model: `bugfix_sales.minimum_sales_margin.seed._convert_line_margin_flag_to_computed()` (BugFix-Sales)<br>`bugfix_sales.minimum_sales_margin.seed._suppress_validate_sales_lines_button()` (BugFix-Sales)<br>`helpdesk.ticket._deactivate_clearing_serial_automation()` (Fix-repair)<br>`helpdesk.ticket._deactivate_migrated_other_automations()` (Fix-repair)<br>`helpdesk.ticket._deactivate_migrated_ticket_automations()` (Fix-repair)<br>`sale.order._restrict_notify_transfer_completion_automation()` (Fix-repair)

**Summary:**

<!-- SUMMARY:model:base.automation -->
This repo adds a Studio tweak to the Automation Rules list view that shows the record ID column after Model. Nothing else is changed on this model; the post-install hook does write trigger and action links on automations owned by other repos.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: base.automation.tree customization | `view_std_base_automation_4868` | tree | after `//field[@name='model_id']`: add field id | Adds an optional (shown by default) ID column after Model in the Automation Rules list view. | `view base_automation.view_base_automation_tree` (base_automation) |  |
