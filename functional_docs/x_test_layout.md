# BugFix-Studio-Misc — `x_test_layout`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_test_layout` — Test Layout

*Created by this repo.* Python: `models/x_test_layout.py`, `models/x_test_layout_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_test_layout -->
Test Layout is a Studio sandbox line model. Each line links back to a TEST02 record and holds a product and a quantity, and its list is inline-editable. It is shown in the one2many lists on TEST02. Only administrators have access to it.
<!-- /SUMMARY -->

**Fields (23):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_test_layout.activity_summary`<br>`x_test_layout.activity_type_icon`<br>`x_test_layout.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_test_layout.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_test_layout.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_test_layout.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of Test Layout records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_314_x_test_layout_x_active`<br>`view BugFix-Studio-Misc.view_4883_default_form_view_for_x_test_layout`<br>`view BugFix-Studio-Misc.view_4884_default_search_view_for_x_test_layout` |
| `x_name` | Name | char | Name of a Test Layout record, entered by the user and used as its display name. Shown in the list, form and search views. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_4882_default_list_view_for_x_test_layout`<br>`view BugFix-Studio-Misc.view_4883_default_form_view_for_x_test_layout`<br>`view BugFix-Studio-Misc.view_4884_default_search_view_for_x_test_layout` |
| `x_studio_line_ids` | Line Ids | many2one → `x_test02` | Link from a Test Layout line back to its parent TEST02 record (inverse of the TEST02 one2many line fields); shown in the Studio list view. Sandbox model. | stored | `model x_test02` | `view BugFix-Studio-Misc.view_4886_odoo_studio_default_list_view_for_x_test_layout_customizatio_ext` |
| `x_studio_product_id` | Product Id | many2one → `product.product` | Many2one link labelled 'Product Id' to `product.product` records, chosen by the user. Shown in the list view. Part of a Studio test/sandbox model. | stored | `model product.product` (product) | `view BugFix-Studio-Misc.view_4886_odoo_studio_default_list_view_for_x_test_layout_customizatio_ext` |
| `x_studio_quantity` | Quantity | float | User-entered float value labelled 'Quantity'. Shown in the list view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_4886_odoo_studio_default_list_view_for_x_test_layout_customizatio_ext` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for Test Layout records (default set by an ir.default), used to order them in lists. Shown in the list view. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_315_x_test_layout_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_4882_default_list_view_for_x_test_layout` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Test Layout | `act_window_2109_test_layout` | Opens **Test Layout** records (tree,form). | `model x_test_layout` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_test_layout` |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_test_layout | `view_4883_default_form_view_for_x_test_layout` | form | full form layout with 2 fields | Default Studio form for the test model x_test_layout: required Name and archived ribbon; chatter fields stripped because the model has no mail support. | `x_test_layout.x_active`<br>`x_test_layout.x_name` |  |
| Default list view for x_test_layout | `view_4882_default_list_view_for_x_test_layout` | tree | full tree layout with 2 fields | Default Studio list view for x_test_layout: drag-handle Sequence and Name. | `x_test_layout.x_name`<br>`x_test_layout.x_studio_sequence` | `view BugFix-Studio-Misc.view_4886_odoo_studio_default_list_view_for_x_test_layout_customizatio_ext` |
| Default search view for x_test_layout | `view_4884_default_search_view_for_x_test_layout` | search | full search layout with 1 fields | Default Studio search view for x_test_layout: search by Name plus an 'Archived' filter. | `x_test_layout.x_active`<br>`x_test_layout.x_name` |  |
| Odoo Studio: Default list view for x_test_layout customization | `view_4886_odoo_studio_default_list_view_for_x_test_layout_customizatio_ext` | tree | set editable=bottom on `//tree[1]`; after `//field[@name='x_studio_sequence']`: add field x_studio_line_ids; set column_invisible=1 on `//field[@name='x_name']`; after `//field[@name='x_name']`: add field x_studio_product_id, field x_studio_quantity | Turns the x_test_layout list into an inline-editable list (new rows at bottom), hides Name and Line Ids, and adds Product Id and Quantity columns. | `view BugFix-Studio-Misc.view_4882_default_list_view_for_x_test_layout`<br>`x_test_layout.x_studio_line_ids`<br>`x_test_layout.x_studio_product_id`<br>`x_test_layout.x_studio_quantity` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Test Layout group_system | `access_1737_test_layout_group_system` | Gives **Administration / Settings** read/write/create/delete access to Test Layout records. | `group base.group_system` (base)<br>`model x_test_layout` |  |
| Test Layout group_user | `access_1738_test_layout_group_user` | Gives **User types / Internal User** no access to Test Layout records. | `group base.group_user` (base)<br>`model x_test_layout` |  |
| x_test_layout admin | `access_x_test_layout_admin` | Gives **Administration / Settings** read/write/create/delete access to Test Layout records. | `group base.group_system` (base)<br>`model x_test_layout` |  |
