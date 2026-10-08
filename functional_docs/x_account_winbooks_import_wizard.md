# BugFix-Studio-Misc — `x_account_winbooks_import_wizard`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_account_winbooks_import_wizard` — Account Winbooks import wizard

*Created by this repo.* Python: `models/x_account_winbooks_import_wizard.py`, `models/x_account_winbooks_import_wizard_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_account_winbooks_import_wizard -->
Purpose not evident from code. This is a Studio-created model with only a Name field and the automatic fields, and no views, actions or logic use it in this repo. Administration / Settings has full access. An access right for Accounting / Accountant grants no permissions.
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
| `x_name` | Name | char | Name field of the Studio-created Account Winbooks import wizard model; not used by any view or logic in this repo. | stored |  |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| access.account.winbooks.import.wizard | `access_7063_access_account_winbooks_import_wizard` | Gives **Accounting / Accountant** no access to Account Winbooks import wizard records. | `group account.group_account_manager` (account)<br>`model x_account_winbooks_import_wizard` |  |
| x_account_winbooks_import_wizard admin | `access_x_account_winbooks_import_wizard_admin` | Gives **Administration / Settings** read/write/create/delete access to Account Winbooks import wizard records. | `group base.group_system` (base)<br>`model x_account_winbooks_import_wizard` |  |
