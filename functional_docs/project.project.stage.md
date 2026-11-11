# BugFix-Studio-Misc — `project.project.stage`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `project.project.stage` — Project Stage

*Extends a model created by `project`.*

Other repos that use this model: `record rule BugFix-Project.rule_project_stage_multi_company` (BugFix-Project)<br>`window action BugFix-Project.action_project_stage_project_project_stage` (BugFix-Project)

**Summary:**

<!-- SUMMARY:model:project.project.stage -->
This repo adds a window action that opens Project Stage records, linked to an entry under the TEST APP 05 menu. It also adds a Studio list customization that shows optional ID and Created by columns after Folded in the Project Stages list.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Project Stage (project.project.stage) | `action_project_stage_project_project_stage_d7` | Opens **Project Stage** records (kanban,tree,form). | `model project.project.stage` (project) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_projects_project_stage_project_project_stage` |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: project.project.stage.view.tree customization | `view_project_project_stage_view_tree_inherit` | tree | after `//field[@name='fold']`: add field id, field create_uid | Adds optional ID and Created by columns after Folded in the Project Stages list view. | `view project.project_project_stage_view_tree` (project) |  |
