# BugFix-Studio-Misc — `project.milestone`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `project.milestone` — Project Milestone

*Extends a model created by `project`.*

Other repos that use this model: `record rule BugFix-Project.rule_407_project_milestone_multi_company` (BugFix-Project)<br>`record rule BugFix-Project.rule_408_project_milestone_employees_follow_required_for_follower_onl` (BugFix-Project)<br>`record rule BugFix-Project.rule_409_project_milestone_project_manager_can_see_all_project_milest` (BugFix-Project)<br>`record rule BugFix-Project.rule_688_project_milestone_portal_users_portal_user_can_read_with_pro` (BugFix-Project)<br>`window action BugFix-Project.act_window_2805_project_milestone` (BugFix-Project)

**Summary:**

<!-- SUMMARY:model:project.milestone -->
This repo only adds a window action that opens Project Milestone records in list and form views, linked to a project.milestone entry under the TEST APP 05 menu. No fields, views or logic are changed.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| project.milestone | `act_window_2805_project_milestone_d7` | Opens **Project Milestone** records (tree,form). | `model project.milestone` (project) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_projects_project_milestone` |
