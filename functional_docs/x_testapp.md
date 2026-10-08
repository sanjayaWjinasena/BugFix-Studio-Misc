# BugFix-Studio-Misc — `x_testapp`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_testapp` — TestApp

*Created by this repo.* Python: `models/x_testapp.py`, `models/x_testapp_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_testapp -->
TestApp is a Studio sandbox model that has only a name, a sort order and an archive flag. It is opened from two window actions (TestApp and Test App 02). Only administrators have access to it, and no logic uses it.
<!-- /SUMMARY -->

**Fields (20):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_testapp.activity_summary`<br>`x_testapp.activity_type_icon`<br>`x_testapp.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_testapp.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_testapp.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_testapp.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of TestApp records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_16_x_testapp_x_active`<br>`view BugFix-Studio-Misc.view_2385_default_form_view_for_x_testapp`<br>`view BugFix-Studio-Misc.view_2386_default_search_view_for_x_testapp` |
| `x_name` | Name | char | Name of a TestApp record, entered by the user and used as its display name. Shown in the list, form and search views. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_2384_default_list_view_for_x_testapp`<br>`view BugFix-Studio-Misc.view_2385_default_form_view_for_x_testapp`<br>`view BugFix-Studio-Misc.view_2386_default_search_view_for_x_testapp` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for TestApp records (default set by an ir.default), used to order them in lists. Shown in the list view. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_17_x_testapp_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_2384_default_list_view_for_x_testapp` |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Test App 02 | `act_window_844_test_app_02` | Opens **TestApp** records (tree,form). | `model x_testapp` | `menu BugFix-Studio-Misc.menu_f6_test_app_02` |
| TestApp | `act_window_809_testapp` | Opens **TestApp** records (tree,form). | `model x_testapp` |  |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_testapp | `view_2385_default_form_view_for_x_testapp` | form | full form layout with 2 fields | Default Studio form for the test model x_testapp: required Name and archived ribbon; chatter fields stripped because the model has no mail support. | `x_testapp.x_active`<br>`x_testapp.x_name` |  |
| Default list view for x_testapp | `view_2384_default_list_view_for_x_testapp` | tree | full tree layout with 2 fields | Default Studio list view for x_testapp: drag-handle Sequence and Name. | `x_testapp.x_name`<br>`x_testapp.x_studio_sequence` |  |
| Default search view for x_testapp | `view_2386_default_search_view_for_x_testapp` | search | full search layout with 1 fields | Default Studio search view for x_testapp: search by Name plus an 'Archived' filter. | `x_testapp.x_active`<br>`x_testapp.x_name` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TestApp group_system | `access_1141_testapp_group_system` | Gives **Administration / Settings** read/write/create/delete access to TestApp records. | `group base.group_system` (base)<br>`model x_testapp` |  |
| TestApp group_user | `access_1142_testapp_group_user` | Gives **User types / Internal User** no access to TestApp records. | `group base.group_user` (base)<br>`model x_testapp` |  |
| x_testapp admin | `access_x_testapp_admin` | Gives **Administration / Settings** read/write/create/delete access to TestApp records. | `group base.group_system` (base)<br>`model x_testapp` |  |
