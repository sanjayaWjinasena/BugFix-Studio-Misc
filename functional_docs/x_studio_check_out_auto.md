# BugFix-Studio-Misc — `x_studio_check_out_auto`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_studio_check_out_auto` — Check Out Auto

*Created by this repo.* Python: `models/x_studio_check_out_auto.py`, `models/x_studio_check_out_auto_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_studio_check_out_auto -->
Purpose not evident from code. Check Out Auto is a Studio model that has only a name field and an administrator access right. No views or logic in this repo use it.
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
| `x_name` | Name | char | Name field of the Studio model Check Out Auto; not used by any view or logic in this repo. | stored |  |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_studio_check_out_auto admin | `access_x_studio_check_out_auto_admin` | Gives **Administration / Settings** read/write/create/delete access to Check Out Auto records. | `group base.group_system` (base)<br>`model x_studio_check_out_auto` |  |
