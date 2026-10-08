# BugFix-Studio-Misc — `ir.actions.server`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.actions.server` — Server Action

*Extends a model created by `base`.*

Other repos that use this model: `bugfix_sales.minimum_sales_margin.seed._patch_studio_readers_to_use_company()` (BugFix-Sales)<br>`helpdesk.ticket._delegate_studio_server_actions_to_native()` (Fix-repair)<br>`purchase.order._bugfix_purchase_run_update_pr_on_confirm()` (BugFix-Purchase)<br>`sale.order._fix_advance_payment_project_field()` (Fix-repair)<br>`sale.order._optimize_slow_write_automations()` (Fix-repair)

**Summary:**

<!-- SUMMARY:model:ir.actions.server -->
This repo adds Studio tweaks that show the record ID on the Server Action form (before Model) and in the Server Actions list (after Type). Nothing else is changed on the model itself.
<!-- /SUMMARY -->

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: Server Action customization | `view_std_ir_actions_server_5444` | form | before `//field[@name='model_id']`: add field id | Shows the record ID field before Model on the Server Action form. | `view base.view_server_action_form` (base) |  |
| Odoo Studio: Server Actions customization | `view_std_ir_actions_server_2382` | tree | after `//field[@name='state']`: add field id | Adds the record ID column after Type in the Server Actions list view (Settings > Technical). | `view base.view_server_action_tree` (base) |  |
