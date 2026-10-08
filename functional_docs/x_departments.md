# BugFix-Studio-Misc — `x_departments`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_departments` — Departments

*Extends a model created by `BugFix-Project`.*

Other repos that use this model: `access right BugFix-Project.access_x_departments_user` (BugFix-Project)<br>`record rule BugFix-Project.rule_271_test_users_records_only` (BugFix-Project)<br>`window action BugFix-Project.action_784_departments` (BugFix-Project)

**Summary:**

<!-- SUMMARY:model:x_departments -->
This repo only adds two access rights on Departments, for test groups defined in this repo. Test_Department gets read access and Test_Department_2 gets full access. The model itself comes from BugFix-Project.
<!-- /SUMMARY -->

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| test_access_rights | `access_g_test_access_rights_x_departments_test_department` | Gives **Test_Department** read access to Departments records. | `group BugFix-Studio-Misc.group_g_misc_test_department`<br>`model x_departments` (BugFix-Project) |  |
| test_access_rights_2 | `access_g_test_access_rights_2_x_departments_test_department_2` | Gives **Test_Department_2** read/write/create/delete access to Departments records. | `group BugFix-Studio-Misc.group_g_misc_test_department_2`<br>`model x_departments` (BugFix-Project) |  |
