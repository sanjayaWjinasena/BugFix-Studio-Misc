# BugFix-Studio-Misc — `x_res_config_settings`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_res_config_settings` — res.config.settings

*Created by this repo.* Python: `models/x_res_config_settings.py`, `models/x_res_config_settings_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_res_config_settings -->
A custom Studio settings table labelled res.config.settings. It is separate from Odoo's own res.config.settings. Besides a name, it stores a Minimum Sales Margin % value, which is entered on its Studio form and opened from the config.settings window action. No logic in this repo reads the margin value.
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
| `x_name` | Name | char | Name of a record in the Studio model `x_res_config_settings` (a custom settings table, not Odoo's res.config.settings); shown in its default views. | stored |  | `view BugFix-Studio-Misc.view_3923_default_list_view_for_x_res_config_settings_e`<br>`view BugFix-Studio-Misc.view_3924_default_form_view_for_x_res_config_settings_e`<br>`view BugFix-Studio-Misc.view_3925_default_search_view_for_x_res_config_settings_e` |
| `x_studio_minimum_sales_margin_` | Minimum Sales Margin % | float | Minimum Sales Margin % stored on the custom `x_res_config_settings` record, entered on its Studio form. No logic in this repo reads it. | stored |  | `view BugFix-Studio-Misc.view_final_x_res_config_settings_odoo_studio_default_form_view_for_x_res_config_settings_c` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| config.settings | `act_window_1749_config_settings` | Opens **res.config.settings** records (tree,form). | `model x_res_config_settings` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_config_settings` |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_res_config_settings | `view_3924_default_form_view_for_x_res_config_settings_e` | form | full form layout with 1 fields | Default Studio form for the x_res_config_settings model: a single required Name field. | `x_res_config_settings.x_name` | `view BugFix-Studio-Misc.view_final_x_res_config_settings_odoo_studio_default_form_view_for_x_res_config_settings_c` |
| Default list view for x_res_config_settings | `view_3923_default_list_view_for_x_res_config_settings_e` | tree | full tree layout with 1 fields | Default Studio list view for x_res_config_settings showing Name. | `x_res_config_settings.x_name` |  |
| Default search view for x_res_config_settings | `view_3925_default_search_view_for_x_res_config_settings_e` | search | full search layout with 1 fields | Default Studio search view for x_res_config_settings allowing search by Name. | `x_res_config_settings.x_name` |  |
| Odoo Studio: Default form view for x_res_config_settings customization | `view_final_x_res_config_settings_odoo_studio_default_form_view_for_x_res_config_settings_c` | form | inside `//group[@name='studio_group_8804bd_left']`: add field x_studio_minimum_sales_margin_ | Adds a 'Minimum Sales Margin %' field to the x_res_config_settings form. | `view BugFix-Studio-Misc.view_3924_default_form_view_for_x_res_config_settings_e`<br>`x_res_config_settings.x_studio_minimum_sales_margin_` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| res.config.settings group_user | `access_f3_res_config_settings_group_user` | Gives **User types / Internal User** read/write/create access to res.config.settings records. | `group base.group_user` (base)<br>`model x_res_config_settings` |  |
| res.config.settings group_user | `access_g_res_config_settings_group_user_x_res_config_settings_user_types_internal_user` | Gives **User types / Internal User** read/write/create access to res.config.settings records. | `group base.group_user` (base)<br>`model x_res_config_settings` |  |
| x_res_config_settings admin | `access_x_res_config_settings_admin` | Gives **Administration / Settings** read/write/create/delete access to res.config.settings records. | `group base.group_system` (base)<br>`model x_res_config_settings` |  |
