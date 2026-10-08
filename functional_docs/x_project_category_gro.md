# BugFix-Studio-Misc — `x_project_category_gro`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_project_category_gro` — Project Category Group

*Extends a model created by `BugFix-Project`.*

Other repos that use this model: `access right BugFix-Project.access_1696_project_category_group_group_system` (BugFix-Project)<br>`access right BugFix-Project.access_1697_project_category_group_group_user` (BugFix-Project)<br>`access right BugFix-Project.access_x_project_category_gro_user` (BugFix-Project)<br>`window action BugFix-Project.act_window_2025_project_category_group` (BugFix-Project)<br>`x_project_category.x_studio_category_group` (BugFix-Project)

**Summary:**

<!-- SUMMARY:model:x_project_category_gro -->
Project Category Group is created by BugFix-Project. This repo only adds one access right, which gives Accounting / Jin - ProjectInvoice read access.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Proj. Category Group | `access_g_proj_category_group_x_project_category_gro_accounting_jin_projectinvoice` | Gives **Accounting / Jin - ProjectInvoice** read access to Project Category Group records. | `group BugFix-Studio-Misc.group_g_accounting_jin_projectinvoice`<br>`model x_project_category_gro` (BugFix-Project) |  |
