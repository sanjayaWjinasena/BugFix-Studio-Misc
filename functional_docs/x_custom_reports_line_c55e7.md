# BugFix-Studio-Misc — `x_custom_reports_line_c55e7`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_custom_reports_line_c55e7` — custom_reports_line

*Created by this repo.* Python: `models/x_custom_reports_line_c55e7.py`, `models/x_custom_reports_line_c55e7_gap.py`. Record name field: `x_name`.

Other repos that use this model: `x_custom_reports.x_custom_reports_line_ids_7ee39` (BugFix-Custom-Reports)

**Summary:**

<!-- SUMMARY:model:x_custom_reports_line_c55e7 -->
A line record for Custom Reports. It has a required Description and a Sequence that sets the order of the lines. BugFix-Custom-Reports lists these lines on a Custom Reports record. This repo ships the default Studio list, form and search views. Internal users can read, write and create these lines; Administration / Settings has full access.
<!-- /SUMMARY -->

**Fields (8):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_name` | Description | char | Description of a custom reports line (Studio line model), entered by the user; shown in its default list, form and search views. | stored; required |  | `view BugFix-Studio-Misc.view_8637_default_list_view_for_x_custom_reports_line_c55e7_e`<br>`view BugFix-Studio-Misc.view_8638_default_form_view_for_x_custom_reports_line_c55e7_e`<br>`view BugFix-Studio-Misc.view_8639_default_search_view_for_x_custom_reports_line_c55e7_e` |
| `x_studio_sequence` | Sequence | integer | Sort order of custom reports lines, used to order them in the list view. | stored |  | `view BugFix-Studio-Misc.view_8637_default_list_view_for_x_custom_reports_line_c55e7_e` |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_custom_reports_line_c55e7 | `view_8638_default_form_view_for_x_custom_reports_line_c55e7_e` | form | full form layout with 1 fields | Default Studio form for Custom Reports lines (x_custom_reports_line_c55e7): a single required Name field. | `x_custom_reports_line_c55e7.x_name` |  |
| Default list view for x_custom_reports_line_c55e7 | `view_8637_default_list_view_for_x_custom_reports_line_c55e7_e` | tree | full tree layout with 2 fields | Default Studio inline-editable list for Custom Reports lines: drag-handle Sequence and Name. | `x_custom_reports_line_c55e7.x_name`<br>`x_custom_reports_line_c55e7.x_studio_sequence` |  |
| Default search view for x_custom_reports_line_c55e7 | `view_8639_default_search_view_for_x_custom_reports_line_c55e7_e` | search | full search layout with 1 fields | Default Studio search view for Custom Reports lines allowing search by Name. | `x_custom_reports_line_c55e7.x_name` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| custom_reports_line group_system | `access_8261_custom_reports_line_group_system` | Gives **Administration / Settings** read/write/create/delete access to custom_reports_line records. | `group base.group_system` (base)<br>`model x_custom_reports_line_c55e7` |  |
| custom_reports_line group_user | `access_8262_custom_reports_line_group_user` | Gives **User types / Internal User** read/write/create access to custom_reports_line records. | `group base.group_user` (base)<br>`model x_custom_reports_line_c55e7` |  |
| x_custom_reports_line_c55e7 admin | `access_x_custom_reports_line_c55e7_admin` | Gives **Administration / Settings** read/write/create/delete access to custom_reports_line records. | `group base.group_system` (base)<br>`model x_custom_reports_line_c55e7` |  |
