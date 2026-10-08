# BugFix-Studio-Misc — `project.task`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `project.task` — Task

*Extends a model created by `project`.*

Other repos that use this model: `account.payment.register.action_create_payments()` (Fix-Repair-Wizard-Nav, Fix-repair)<br>`automation BugFix-Project.base_automation_179_rr_auto_update_helpdesk_pipeline_status_1` (BugFix-Project)<br>`automation BugFix-Project.base_automation_200_rr_validate_diagnosis_lines` (BugFix-Project)<br>`helpdesk.ticket._compute_task_done()` (Fix-repair)<br>`helpdesk.ticket.x_studio_related_field_FNjnC` (Fix-repair)<br>`record rule BugFix-Project.rule_401_project_see_private_tasks` (BugFix-Project)<br>`record rule BugFix-Project.rule_70_project_task_multi_company` (BugFix-Project)<br>`record rule BugFix-Project.rule_71_project_task_employees_follow_required_for_follower_only_pro` (BugFix-Project)<details><summary>+30 more</summary>`record rule BugFix-Project.rule_72_project_task_project_manager_see_all_tasks_linked_to_a_proje` (BugFix-Project)<br>`record rule BugFix-Project.rule_75_project_task_portal_users_portal_and_following_project_or_po` (BugFix-Project)<br>`record rule BugFix-Project.rule_761_project_task_employees_full_access_to_own_private_task_only` (BugFix-Project)<br>`record rule BugFix-Project.rule_762_project_task_project_users_follow_required_for_follower_only` (BugFix-Project)<br>`sale.order._compute_ticket_repair_stage_state()` (Fix-repair)<br>`sale.order._fix_repair_auto_generate_quotation_type()` (Fix-repair)<br>`sale.order._get_repair_stock_source_locations()` (Fix-repair)<br>`sale.order._move_ticket_to_stage()` (Fix-repair)<br>`sale.order.action_re_estimate()` (Fix-repair)<br>`server action BugFix-Project.server_action_2003_rr_auto_update_helpdesk_pipeline_status_1` (BugFix-Project)<br>`server action BugFix-Project.server_action_2219_rr_validate_diagnosis_lines` (BugFix-Project)<br>`server action BugFix-Project.server_action_2224_rr_repair_diagnosis_validation` (BugFix-Project)<br>`server action BugFix-Project.server_action_2242_rr_repair_image_validation` (BugFix-Project)<br>`server action BugFix-Project.server_action_2316_rr_end_quick_repair` (BugFix-Project)<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos_2` (BugFix-Sales)<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_project_sos` (BugFix-Sales)<br>`server action BugFix-Sales.sa_f5_sale_order_rr_auto_generate_quotation_type_for_repair_sos` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_1995_rr_auto_generate_quotation_type_for_repair_sos` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2114_rr_auto_generate_quotation_type_for_project_sos` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2117_rr_auto_generate_quotation_type_for_project_sos_2` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2572_proj_update_with_main_so` (BugFix-Sales)<br>`server action Fix-repair.action_repair_end_quick_repair` (Fix-repair)<br>`stock.picking._action_done()` (Fix-repair)<br>`window action BugFix-Project.act_window_1916_project_sharing` (BugFix-Project)<br>`window action BugFix-Project.act_window_251_tasks` (BugFix-Project)<br>`window action BugFix-Project.act_window_266_assigned_tasks` (BugFix-Project)<br>`window action BugFix-Project.act_window_2802_project_task` (BugFix-Project)<br>`window action BugFix-Project.action_2802_project_task` (BugFix-Project)<br>`window action BugFix-Project.aw_f4_project_task_project_task` (BugFix-Project)<br>`x_task_diagnosis.x_studio_task_id` (Fix-repair)</details>

**Summary:**

<!-- SUMMARY:model:project.task -->
This repo only adds a cohort view for tasks, which groups tasks by their assignment date. No fields or logic are changed.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default cohort view for project.task | `view_project_task_studio_cohort` | cohort | full cohort layout with 0 fields | Cohort view for project tasks, grouping tasks by their assignment date (`date_assign`). |  |  |
