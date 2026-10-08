# BugFix-Studio-Misc — `crossovered.budget`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `crossovered.budget` — Budget

*Extends a model created by `account_budget`.*

Other repos that use this model: `access right BugFix-Accounting.access_6854_crossovered_budget` (BugFix-Accounting)<br>`automation BugFix-Accounting.base_automation_197_proj_validate_delete` (BugFix-Accounting)<br>`automation BugFix-Accounting.base_automation_256_proj_validate_confirm` (BugFix-Accounting)<br>`record rule BugFix-Accounting.rule_331_budget_multi_company` (BugFix-Accounting)<br>`sale.order.x_studio_project_budget` (BugFix-Sales)<br>`server action BugFix-Accounting.sa_f5_crossovered_budget_proj_validate_confirm` (BugFix-Accounting)<br>`server action BugFix-Accounting.sa_f5_crossovered_budget_proj_validate_delete` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2183_proj_validate_delete` (BugFix-Accounting)<details><summary>+6 more</summary>`server action BugFix-Accounting.server_action_2570_proj_validate_confirm` (BugFix-Accounting)<br>`server action BugFix-Sales.server_action_2178_proj_create_budget_entries` (BugFix-Sales)<br>`window action BugFix-Accounting.act_window_2180_budget` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_2180_budget` (BugFix-Accounting)<br>`window action BugFix-Accounting.aw_f4_crossovered_budget_budget` (BugFix-Accounting)<br>`x_temp_actual_budget.x_studio_crossovered_budget_id` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:crossovered.budget -->
This repo adds the Budget Report, a PDF report printed from Budget records using a Studio report template. Nothing else is changed.
<!-- /SUMMARY -->

**Reports (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Budget Report | `action_report_2792_budget_report` | Prints **Budget Report** (qweb-pdf) for crossovered.budget records using template `studio_customization.studio_report_docume_d573c563-728c-4341-ab10-9845f7d721f0`. | `model crossovered.budget` (account_budget)<br>`record studio_customization.studio_report_docume_d573c563-728c-4341-ab10-9845f7d721f0` (studio_customization) |  |
