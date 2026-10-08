# BugFix-Studio-Misc — `x_x_studio_request_line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_x_studio_request_line` — x_studio_request_line

*Created by this repo.* Python: `models/x_x_studio_request_line.py`, `models/x_x_studio_request_line_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_x_studio_request_line -->
Purpose not evident from code. x_studio_request_line is a Studio model that has only a name field. Jin maintenance users can read, write and create records, the maintenance minimum-rights group can read them, and administrators have full access. No views or logic in this repo use it.
<!-- /SUMMARY -->

**Fields (7):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_name` | Name | char | Name field of the Studio model `x_x_studio_request_line`; not used by any view or logic in this repo. | stored |  |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Jin - Maintenance + Maintenance users | `access_g_jin_maintenance_maintenance_users_x_x_studio_request_line_maintenance_jin_mainten` | Gives **Maintenance / Jin - Maintenance + Maintenance user** read/write/create access to x_studio_request_line records. | `group BugFix-Studio-Misc.group_g_maintenance_jin_maintenance_maintenance_user`<br>`model x_x_studio_request_line` |  |
| Jin - Maintenance + Maintenance users | `access_g_jin_maintenance_maintenance_users_x_x_studio_request_line_maintenance_jin_mainten_1` | Gives **Maintenance / Jin - Maintenance - Minimum Rights** read access to x_studio_request_line records. | `group BugFix-Studio-Misc.group_g_maintenance_jin_maintenance_minimum_rights`<br>`model x_x_studio_request_line` |  |
| x_x_studio_request_line admin | `access_x_x_studio_request_line_admin` | Gives **Administration / Settings** read/write/create/delete access to x_studio_request_line records. | `group base.group_system` (base)<br>`model x_x_studio_request_line` |  |
