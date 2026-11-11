# BugFix-Studio-Misc — `project_category`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `project_category` — Project Category

*Extends a model created by `BugFix-Project`.*

Other repos that use this model: `access right BugFix-Project.access_project_category_group_system` (BugFix-Project)<br>`access right BugFix-Project.access_project_category_group_user` (BugFix-Project)<br>`access right BugFix-Project.access_project_category_user` (BugFix-Project)<br>`account.move.line.category` (BugFix-Accounting)<br>`sale.order.line.category` (BugFix-Sales)<br>`server action BugFix-Accounting.action_sales_report_model_srm_rpt_project_gross_margin` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_srm_rpt_project_gross_margin` (BugFix-Accounting)<br>`window action BugFix-Project.action_project_category` (BugFix-Project)<details><summary>+2 more</summary>`window action BugFix-Project.action_project_category_project_category` (BugFix-Project)<br>`temp_estimated.category` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:project_category -->
Project Category is created by BugFix-Project. This repo only adds one access right, which gives Accounting / Jin - ProjectInvoice read/write access.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Proj. Category | `access_g_proj_category_project_category_accounting_jin_projectinvoice` | Gives **Accounting / Jin - ProjectInvoice** read/write access to Project Category records. | `group BugFix-Studio-Misc.group_g_accounting_jin_projectinvoice`<br>`model project_category` (BugFix-Project) |  |
