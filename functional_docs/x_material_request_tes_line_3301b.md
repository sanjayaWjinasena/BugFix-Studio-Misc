# BugFix-Studio-Misc — `x_material_request_tes_line_3301b`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_material_request_tes_line_3301b` — material_request_tes_line

*Created by this repo.* Python: `models/x_material_request_tes_line_3301b.py`, `models/x_material_request_tes_line_3301b_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_material_request_tes_line_3301b -->
A line of a Material Request Test, linked to its parent through `x_material_request_tes_id` and holding a required description (`x_name`) and a sort order. It has default Studio form, inline-editable list and search views. Administrators and internal users can maintain it; no logic in this repo uses it.
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
| `x_material_request_tes_id` | X Material Request Tes | many2one → `x_material_request_tes` | Link from a Material Request Test line to its parent Material Request Test; inverse of the parent's lines field. Not shown on any view. | stored | `model x_material_request_tes` (BugFix-Stock) |  |
| `x_name` | Description | char | Description of a Material Request Test line, entered by the user; shown in the line's default list, form and search views. | stored; required |  | `view BugFix-Studio-Misc.view_8717_default_list_view_for_x_material_request_tes_line_3301b_e`<br>`view BugFix-Studio-Misc.view_8718_default_form_view_for_x_material_request_tes_line_3301b_e`<br>`view BugFix-Studio-Misc.view_8719_default_search_view_for_x_material_request_tes_line_3301b_e` |
| `x_studio_sequence` | Sequence | integer | Sort order of Material Request Test lines in the list view. | stored |  | `view BugFix-Studio-Misc.view_8717_default_list_view_for_x_material_request_tes_line_3301b_e` |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_material_request_tes_line_3301b | `view_8718_default_form_view_for_x_material_request_tes_line_3301b_e` | form | full form layout with 1 fields | Default Studio form for Material Request (TES) lines (x_material_request_tes_line_3301b): a single required Name field. | `x_material_request_tes_line_3301b.x_name` |  |
| Default list view for x_material_request_tes_line_3301b | `view_8717_default_list_view_for_x_material_request_tes_line_3301b_e` | tree | full tree layout with 2 fields | Default Studio inline-editable list for Material Request (TES) lines: drag-handle Sequence and Name. | `x_material_request_tes_line_3301b.x_name`<br>`x_material_request_tes_line_3301b.x_studio_sequence` |  |
| Default search view for x_material_request_tes_line_3301b | `view_8719_default_search_view_for_x_material_request_tes_line_3301b_e` | search | full search layout with 1 fields | Default Studio search view for Material Request (TES) lines allowing search by Name. | `x_material_request_tes_line_3301b.x_name` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| material_request_tes_line group_system | `access_8269_material_request_tes_line_group_system` | Gives **Administration / Settings** read/write/create/delete access to material_request_tes_line records. | `group base.group_system` (base)<br>`model x_material_request_tes_line_3301b` |  |
| material_request_tes_line group_user | `access_8270_material_request_tes_line_group_user` | Gives **User types / Internal User** read/write/create access to material_request_tes_line records. | `group base.group_user` (base)<br>`model x_material_request_tes_line_3301b` |  |
| x_material_request_tes_line_3301b admin | `access_x_material_request_tes_line_3301b_admin` | Gives **Administration / Settings** read/write/create/delete access to material_request_tes_line records. | `group base.group_system` (base)<br>`model x_material_request_tes_line_3301b` |  |
