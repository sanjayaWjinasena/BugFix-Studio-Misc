# BugFix-Studio-Misc — `project_category_gro`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `project_category_gro` — Project Category Group

*Extends a model created by `BugFix-Project`.*

Other repos that use this model: `access right BugFix-Project.access_project_category_group_group_system` (BugFix-Project)<br>`access right BugFix-Project.access_project_category_group_group_user` (BugFix-Project)<br>`access right BugFix-Project.access_project_category_gro_user` (BugFix-Project)<br>`window action BugFix-Project.action_project_category_group` (BugFix-Project)<br>`project_category.category_group` (BugFix-Project)

**Summary:**

<!-- SUMMARY:model:project_category_gro -->
Project Category Group is created by BugFix-Project. This repo only adds one access right, which gives Accounting / Jin - ProjectInvoice read access.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Proj. Category Group | `access_g_proj_category_group_project_category_gro_accounting_jin_projectinvoice` | Gives **Accounting / Jin - ProjectInvoice** read access to Project Category Group records. | `group BugFix-Studio-Misc.group_g_accounting_jin_projectinvoice`<br>`model project_category_gro` (BugFix-Project) |  |
