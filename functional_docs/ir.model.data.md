# BugFix-Studio-Misc — `ir.model.data`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.model.data` — Model Data

*Extends a model created by `base`.*

Other repos that use this model: `bugfix_sales.minimum_sales_margin.seed._attach_c01_intro_conclusion_view()` (BugFix-Sales)<br>`bugfix_sales.minimum_sales_margin.seed._cleanup_orphan_studio_menu_pins()` (BugFix-Sales)<br>`helpdesk.stage._migrate_studio_stage_cluster_to_base()` (Fix-repair)<br>`helpdesk.ticket._fix_studio_report_template_keys()` (Fix-repair)<br>`helpdesk.ticket._migrate_studio_audit_cluster_to_base()` (Fix-repair)<br>`helpdesk.ticket._migrate_studio_cancel_cluster_to_base()` (Fix-repair)<br>`helpdesk.ticket._migrate_studio_leftover_repair_fields()` (Fix-repair)<br>`helpdesk.ticket._migrate_studio_location_cluster_to_base()` (Fix-repair)<details><summary>+12 more</summary>`helpdesk.ticket._migrate_studio_misc_cluster_to_base()` (Fix-repair)<br>`helpdesk.ticket._migrate_studio_reports_to_native()` (Fix-repair)<br>`helpdesk.ticket._migrate_studio_rug_cluster_to_base()` (Fix-repair)<br>`helpdesk.ticket._migrate_studio_serial_product_cluster_to_base()` (Fix-repair)<br>`helpdesk.ticket._migrate_studio_stage_marker_cluster_to_base()` (Fix-repair)<br>`helpdesk.ticket._migrate_studio_stage_validation_cluster_to_base()` (Fix-repair)<br>`helpdesk.ticket._migrate_studio_views_to_native()` (Fix-repair)<br>`helpdesk.ticket._repin_delegated_server_actions_to_native()` (Fix-repair)<br>`helpdesk.ticket.type._migrate_studio_ticket_type_cluster_to_base()` (Fix-repair)<br>`project.task._migrate_studio_project_task_repair_cluster_to_base()` (Fix-repair)<br>`res.users._migrate_studio_res_users_cluster_to_base()` (Fix-repair)<br>`x_repair_master_data.migration._migrate_studio_repair_master_data_to_base()` (Fix-repair)</details>

**Summary:**

<!-- SUMMARY:model:ir.model.data -->
This repo adds a second Record ID search field in the External Identifiers search view, which duplicates the existing one. Nothing else is changed.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: ir.model.data search customization | `view_std_ir_model_data_3847` | search | after `//search[1]/field[@name='res_id']`: add field res_id | Adds a second Record ID (res_id) search field in the External Identifiers search view; it duplicates the existing one. | `ir.model.data.res_id` (base)<br>`view base.view_model_data_search` (base) |  |
