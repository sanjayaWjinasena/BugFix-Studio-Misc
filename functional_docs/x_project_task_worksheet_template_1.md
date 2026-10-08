# BugFix-Studio-Misc — `x_project_task_worksheet_template_1`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_project_task_worksheet_template_1` — Default Worksheet

*Created by this repo.* Python: `models/x_project_task_worksheet_template_1.py`, `models/x_project_task_worksheet_template_1_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_project_task_worksheet_template_1 -->
The Default Worksheet of a project task, used as a field-service worksheet template. Each worksheet is linked to a required project task, takes its name from the task's name, and holds free-text comments. It has a Worksheets window action and a worksheet form that does not allow creating records. Project administrators (and Field Service users) can access all worksheets, while project users can only access worksheets they created.
<!-- /SUMMARY -->

**Fields (9):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_comments` | Comments | text | Free-text comments entered on the Default Worksheet of a field-service task; shown on the worksheet template form. | stored |  | `view BugFix-Studio-Misc.view_4653_template_view_default_worksheet_e` |
| `x_name` | Name | char | Name of the Default Worksheet, copied via related from the linked task's name (`x_project_task_id.name`). | related `x_project_task_id.name`; not stored | `project.task.name` (project)<br>`x_project_task_worksheet_template_1.x_project_task_id` |  |
| `x_project_task_id` | Task | many2one → `project.task` | Project task this Default Worksheet belongs to; shown on the worksheet form and source of the worksheet's name. | stored; required | `model project.task` (project) | `view BugFix-Studio-Misc.view_4653_template_view_default_worksheet_e`<br>`x_project_task_worksheet_template_1.x_name` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Worksheets | `act_window_2014_worksheets` | Opens **Default Worksheet** records (tree,form). | `model x_project_task_worksheet_template_1` |  |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| template_view_Default_Worksheet | `view_4653_template_view_default_worksheet_e` | form | full form layout with 2 fields | Default project task worksheet form (no create): shows the linked task as title (hidden in Studio or when opened from a task) and a Comments field. | `x_project_task_worksheet_template_1.x_comments`<br>`x_project_task_worksheet_template_1.x_project_task_id` |  |

**Access rights (7):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_project_task_worksheet_template_1 admin | `access_x_project_task_worksheet_template_1_admin` | Gives **Administration / Settings** read/write/create/delete access to Default Worksheet records. | `group base.group_system` (base)<br>`model x_project_task_worksheet_template_1` |  |
| x_project_task_worksheet_template_1_access | `access_1680_x_project_task_worksheet_template_1_access` | Gives **Project / Administrator** read/write/create/delete access to Default Worksheet records. | `group project.group_project_manager` (project)<br>`model x_project_task_worksheet_template_1` |  |
| x_project_task_worksheet_template_1_access | `access_1681_x_project_task_worksheet_template_1_access` | Gives **Project / User** read/write/create/delete access to Default Worksheet records. | `group project.group_project_user` (project)<br>`model x_project_task_worksheet_template_1` |  |
| x_project_task_worksheet_template_1_access | `access_f3_x_project_task_worksheet_template_1_access` | Gives **Project / Administrator** read/write/create/delete access to Default Worksheet records. | `group project.group_project_manager` (project)<br>`model x_project_task_worksheet_template_1` |  |
| x_project_task_worksheet_template_1_access | `access_g_x_project_task_worksheet_template_1_acce_x_project_task_worksheet_template_1_proj` | Gives **Project / Administrator** read/write/create/delete access to Default Worksheet records. | `group project.group_project_manager` (project)<br>`model x_project_task_worksheet_template_1` |  |
| x_project_task_worksheet_template_1_access | `access_g_x_project_task_worksheet_template_1_acce_x_project_task_worksheet_template_1_proj_1` | Gives **Project / User** read/write/create/delete access to Default Worksheet records. | `group project.group_project_user` (project)<br>`model x_project_task_worksheet_template_1` |  |
| x_project_task_worksheet_template_1_access_user | `access_f3_x_project_task_worksheet_template_1_access_user` | Gives **Project / User** read/write/create/delete access to Default Worksheet records. | `group project.group_project_user` (project)<br>`model x_project_task_worksheet_template_1` |  |

**Record rules (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_project_task_worksheet_template_1_all | `rule_426_x_project_task_worksheet_template_1_all` | For Project / Administrator, Field Service / User: read/write/create/delete on Default Worksheet with no record filter (empty domain = all records). | `group industry_fsm.group_fsm_user` (industry_fsm)<br>`group project.group_project_manager` (project)<br>`model x_project_task_worksheet_template_1` |  |
| x_project_task_worksheet_template_1_own | `rule_425_x_project_task_worksheet_template_1_own` | For Project / User: read/write/create/delete on Default Worksheet only where `[('create_uid', '=', user.id)]`. | `group project.group_project_user` (project)<br>`model x_project_task_worksheet_template_1` |  |
