# BugFix-Studio-Misc — `x_material_request_mt_line_9a011`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_material_request_mt_line_9a011` — material_request_mt_line

*Created by this repo.* Python: `models/x_material_request_mt_line_9a011.py`, `models/x_material_request_mt_line_9a011_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_material_request_mt_line_9a011 -->
A line record of a Material Request MT, linked to its parent through X Material Request Mt. It has a required Description and a Sequence for ordering. This repo ships the default Studio list, form and search views, but the parent's lines field is not shown on any view. Internal users can read, write and create these lines; Administration / Settings has full access.
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
| `x_material_request_mt_id` | X Material Request Mt | many2one → `x_material_request_mt` | Link from a Material Request MT line to its parent Material Request MT; inverse of the parent's lines field. Not shown on any view. | stored | `model x_material_request_mt` (BugFix-Stock) |  |
| `x_name` | Description | char | Description of a Material Request MT line, entered by the user; shown in the line's default list, form and search views. | stored; required |  | `view BugFix-Studio-Misc.view_8771_default_list_view_for_x_material_request_mt_line_9a011_e`<br>`view BugFix-Studio-Misc.view_8772_default_form_view_for_x_material_request_mt_line_9a011_e`<br>`view BugFix-Studio-Misc.view_8773_default_search_view_for_x_material_request_mt_line_9a011_e` |
| `x_studio_sequence` | Sequence | integer | Sort order of Material Request MT lines in the list view. | stored |  | `view BugFix-Studio-Misc.view_8771_default_list_view_for_x_material_request_mt_line_9a011_e` |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_material_request_mt_line_9a011 | `view_8772_default_form_view_for_x_material_request_mt_line_9a011_e` | form | full form layout with 1 fields | Default Studio form for Material Request (MT) lines (x_material_request_mt_line_9a011): a single required Name field. | `x_material_request_mt_line_9a011.x_name` |  |
| Default list view for x_material_request_mt_line_9a011 | `view_8771_default_list_view_for_x_material_request_mt_line_9a011_e` | tree | full tree layout with 2 fields | Default Studio inline-editable list for Material Request (MT) lines: drag-handle Sequence and Name. | `x_material_request_mt_line_9a011.x_name`<br>`x_material_request_mt_line_9a011.x_studio_sequence` |  |
| Default search view for x_material_request_mt_line_9a011 | `view_8773_default_search_view_for_x_material_request_mt_line_9a011_e` | search | full search layout with 1 fields | Default Studio search view for Material Request (MT) lines allowing search by Name. | `x_material_request_mt_line_9a011.x_name` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| material_request_mt_line group_system | `access_8293_material_request_mt_line_group_system` | Gives **Administration / Settings** read/write/create/delete access to material_request_mt_line records. | `group base.group_system` (base)<br>`model x_material_request_mt_line_9a011` |  |
| material_request_mt_line group_user | `access_8294_material_request_mt_line_group_user` | Gives **User types / Internal User** read/write/create access to material_request_mt_line records. | `group base.group_user` (base)<br>`model x_material_request_mt_line_9a011` |  |
| x_material_request_mt_line_9a011 admin | `access_x_material_request_mt_line_9a011_admin` | Gives **Administration / Settings** read/write/create/delete access to material_request_mt_line records. | `group base.group_system` (base)<br>`model x_material_request_mt_line_9a011` |  |
