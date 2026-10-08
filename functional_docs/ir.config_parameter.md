# BugFix-Studio-Misc — `ir.config_parameter`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.config_parameter` — System Parameter

*Extends a model created by `base`.*

Other repos that use this model: `bugfix_sales.minimum_sales_margin.seed._migrate_to_config_parameter()` (BugFix-Sales)<br>`bugfix_sales.minimum_sales_margin.seed._seed_ir_config_parameter_defaults()` (BugFix-Sales)<br>`helpdesk.ticket._get_factory_repair_location()` (Fix-repair)<br>`res.company._compute_bugfix_sales_config()` (BugFix-Sales)<br>`res.company._inverse_bugfix_sales_config()` (BugFix-Sales)<br>`res.config.settings.get_values()` (Fix-repair)<br>`res.config.settings.set_values()` (Fix-repair)<br>`sale.order._get_repair_stock_source_locations()` (Fix-repair)<details><summary>+2 more</summary>`sale.order.action_quotation_send()` (Fix-Repair-Wizard-Nav, Fix-repair)<br>`stock.warehouse._seed_factory_repair_locations()` (Fix-repair)</details>

**Summary:**

<!-- SUMMARY:model:ir.config_parameter -->
This repo adds an optional Created by column after Value in the System Parameters list view. Nothing else is changed.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: ir.config_parameter tree customization | `view_std_ir_config_parameter_6117` | tree | after `//field[@name='value']`: add field create_uid | Adds an optional Created by column after Value in the System Parameters list view. | `view base.view_ir_config_list` (base) |  |
