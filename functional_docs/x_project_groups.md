# BugFix-Studio-Misc — `x_project_groups`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_project_groups` — Project Groups

*Extends a model created by `BugFix-Project`.*

Other repos that use this model: `access right BugFix-Project.access_1700_project_groups_group_system` (BugFix-Project)<br>`access right BugFix-Project.access_1701_project_groups_group_user` (BugFix-Project)<br>`access right BugFix-Project.access_x_project_groups_user` (BugFix-Project)<br>`project.project.x_studio_project_group` (BugFix-Project)<br>`sale.order.x_studio_project_group` (BugFix-Sales)<br>`window action BugFix-Project.action_2027_project_groups` (BugFix-Project)

**Summary:**

<!-- SUMMARY:model:x_project_groups -->
Project Groups is created by BugFix-Project. This repo only adds one access right, which gives Accounting / Jin - ProjectInvoice read access.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Proj. Groups | `access_g_proj_groups_x_project_groups_accounting_jin_projectinvoice` | Gives **Accounting / Jin - ProjectInvoice** read access to Project Groups records. | `group BugFix-Studio-Misc.group_g_accounting_jin_projectinvoice`<br>`model x_project_groups` (BugFix-Project) |  |
