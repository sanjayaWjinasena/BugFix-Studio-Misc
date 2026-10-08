# BugFix-Studio-Misc — `project.sale.line.employee.map`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `project.sale.line.employee.map` — Project Sales line, employee mapping

*Extends a model created by `sale_timesheet`.*

**Summary:**

<!-- SUMMARY:model:project.sale.line.employee.map -->
This repo adds a window action that opens the project sale-line and employee mapping records in list and form views. The action is linked to a menu under Projects and to another under the TEST APP 05 menu. It also ships a Studio list view showing only the record ID, but that view is archived and not used.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| project.sale.line.employee.map | `act_window_2806_project_sale_line_employee_map_d7` | Opens **Project Sales line, employee mapping** records (tree,form). | `model project.sale.line.employee.map` (sale_timesheet) | `menu BugFix-Studio-Misc.menu_f6_project_sale_line_employee_map`<br>`menu BugFix-Studio-Misc.menu_f6r2_test_app_05_projects_project_sale_line_employee_map` |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| project.sale.line.employee.map.tree.studio | `view_project_sale_line_employee_map_tree_studio` | tree | full tree layout with 1 fields | Studio list view for project sale-line/employee mappings showing only the read-only record ID; it is archived (active = False), so it is not used. |  |  |
