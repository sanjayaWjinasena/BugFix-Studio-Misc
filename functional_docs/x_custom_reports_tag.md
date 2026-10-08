# BugFix-Studio-Misc — `x_custom_reports_tag`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_custom_reports_tag` — Custom Reports Tags

*Created by this repo.* Python: `models/x_custom_reports_tag.py`, `models/x_custom_reports_tag_gap.py`. Record name field: `x_name`.

Other repos that use this model: `x_custom_reports.x_studio_tag_ids` (BugFix-Custom-Reports)

**Summary:**

<!-- SUMMARY:model:x_custom_reports_tag -->
A tag used to label Custom Reports records. It has a required Name and a colour index for the tag badge, and BugFix-Custom-Reports uses it in a tags field on Custom Reports. Users maintain tags from the Jinasena Custom Reports Tags window action, which is linked to two menus including one under Jinasena reports configuration. Internal users can read, write and create tags; Administration / Settings has full access.
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
| `x_color` | Color | integer | Color index of a Custom Reports Tags record, used to color its tag badge. Shown in the list view. | stored |  | `view BugFix-Studio-Misc.view_8643_default_list_view_for_x_custom_reports_tag_e` |
| `x_name` | Name | char | Name of a Custom Reports Tags record, entered by the user and used as its display name. Shown in the list, form and search views. | stored; required |  | `view BugFix-Studio-Misc.view_8643_default_list_view_for_x_custom_reports_tag_e`<br>`view BugFix-Studio-Misc.view_8644_default_form_view_for_x_custom_reports_tag_e`<br>`view BugFix-Studio-Misc.view_8645_default_search_view_for_x_custom_reports_tag_e` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Jinasena Custom Reports Tags | `act_window_3349_jinasena_custom_reports_tags` | Opens **Custom Reports Tags** records (tree,form). | `model x_custom_reports_tag` | `menu BugFix-Studio-Misc.menu_f6_jinasena_custom_reports_tags`<br>`menu BugFix-Studio-Misc.menu_f6r3_jinasena_reports_configuration_jinasena_custom_reports_tags` |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_custom_reports_tag | `view_8644_default_form_view_for_x_custom_reports_tag_e` | form | full form layout with 1 fields | Default Studio form for Custom Reports Tags: a single required Name field. | `x_custom_reports_tag.x_name` |  |
| Default list view for x_custom_reports_tag | `view_8643_default_list_view_for_x_custom_reports_tag_e` | tree | full tree layout with 2 fields | Inline-editable list of Custom Reports Tags showing Name and a colour picker. | `x_custom_reports_tag.x_color`<br>`x_custom_reports_tag.x_name` |  |
| Default search view for x_custom_reports_tag | `view_8645_default_search_view_for_x_custom_reports_tag_e` | search | full search layout with 1 fields | Default Studio search view for Custom Reports Tags allowing search by Name. | `x_custom_reports_tag.x_name` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Custom Reports Tags group_system | `access_8265_custom_reports_tags_group_system` | Gives **Administration / Settings** read/write/create/delete access to Custom Reports Tags records. | `group base.group_system` (base)<br>`model x_custom_reports_tag` |  |
| Custom Reports Tags group_user | `access_8266_custom_reports_tags_group_user` | Gives **User types / Internal User** read/write/create access to Custom Reports Tags records. | `group base.group_user` (base)<br>`model x_custom_reports_tag` |  |
| x_custom_reports_tag admin | `access_x_custom_reports_tag_admin` | Gives **Administration / Settings** read/write/create/delete access to Custom Reports Tags records. | `group base.group_system` (base)<br>`model x_custom_reports_tag` |  |
