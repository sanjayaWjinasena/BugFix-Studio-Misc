# BugFix-Studio-Misc — `x_test_1`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_test_1` — TEST-1

*Created by this repo.* Python: `models/x_test_1.py`, `models/x_test_1_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_test_1 -->
TEST-1 is a Studio sandbox model with a name, a sort order and a required Value column in its list. It is opened from five window actions (TEST 01, TEST APP, TEST-1 and two TEST01 actions). Internal users have read-only access and administrators have full access. No logic uses it.
<!-- /SUMMARY -->

**Fields (21):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_test_1.activity_summary`<br>`x_test_1.activity_type_icon`<br>`x_test_1.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_test_1.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_test_1.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_test_1.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of TEST-1 records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_29_x_test_1_x_active`<br>`view BugFix-Studio-Misc.view_2411_default_form_view_for_x_test_1`<br>`view BugFix-Studio-Misc.view_2412_default_search_view_for_x_test_1` |
| `x_name` | Name | char | Name of a TEST-1 record, entered by the user and used as its display name. Shown in the list, form and search views. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_2410_default_list_view_for_x_test_1`<br>`view BugFix-Studio-Misc.view_2411_default_form_view_for_x_test_1`<br>`view BugFix-Studio-Misc.view_2412_default_search_view_for_x_test_1` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for TEST-1 records (default set by an ir.default), used to order them in lists. Shown in the list view. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_30_x_test_1_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_2410_default_list_view_for_x_test_1` |
| `x_studio_value` | Value | float | User-entered float value labelled 'Value'. Shown in the list view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_3269_odoo_studio_default_list_view_for_x_test_1_customization_ext` |

**Window actions (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TEST 01 | `act_window_845_test_01` | Opens **TEST-1** records (tree,form). | `model x_test_1` |  |
| TEST APP | `act_window_843_test_app` | Opens **TEST-1** records (tree,form). | `model x_test_1` | `menu BugFix-Studio-Misc.menu_f6_test_app` |
| TEST-1 | `act_window_842_test_1` | Opens **TEST-1** records (tree,form). | `model x_test_1` |  |
| TEST01 | `act_window_849_test01` | Opens **TEST-1** records (tree,form). | `model x_test_1` |  |
| TEST01 | `act_window_847_test01` | Opens **TEST-1** records (tree,form). | `model x_test_1` |  |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_test_1 | `view_2411_default_form_view_for_x_test_1` | form | full form layout with 2 fields | Default Studio form for the test model x_test_1: required Name and archived ribbon; chatter fields stripped because the model has no mail support. | `x_test_1.x_active`<br>`x_test_1.x_name` |  |
| Default list view for x_test_1 | `view_2410_default_list_view_for_x_test_1` | tree | full tree layout with 2 fields | Default Studio list view for x_test_1: drag-handle Sequence and Name. | `x_test_1.x_name`<br>`x_test_1.x_studio_sequence` | `view BugFix-Studio-Misc.view_3269_odoo_studio_default_list_view_for_x_test_1_customization_ext` |
| Default search view for x_test_1 | `view_2412_default_search_view_for_x_test_1` | search | full search layout with 1 fields | Default Studio search view for x_test_1: search by Name plus an 'Archived' filter. | `x_test_1.x_active`<br>`x_test_1.x_name` |  |
| Odoo Studio: Default list view for x_test_1 customization | `view_3269_odoo_studio_default_list_view_for_x_test_1_customization_ext` | tree | after `//field[@name='x_name']`: add field x_studio_value | Adds a required 'Value' column after Name in the x_test_1 list. | `view BugFix-Studio-Misc.view_2410_default_list_view_for_x_test_1`<br>`x_test_1.x_studio_value` |  |

**Access rights (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TEST-1 GROUP | `access_1153_test_1_group` | Gives **PR Approval** no access to TEST-1 records. | `group BugFix-Approvals.group_107_pr_approval` (BugFix-Approvals)<br>`model x_test_1` |  |
| TEST-1 GROUP | `access_f3_test_1_group` | Gives **PR Approval** no access to TEST-1 records. | `group BugFix-Approvals.group_107_pr_approval` (BugFix-Approvals)<br>`model x_test_1` |  |
| TEST-1 group_system | `access_1149_test_1_group_system` | Gives **Administration / Settings** read/write/create/delete access to TEST-1 records. | `group base.group_system` (base)<br>`model x_test_1` |  |
| TEST-1 group_user | `access_1150_test_1_group_user` | Gives **User types / Internal User** read access to TEST-1 records. | `group base.group_user` (base)<br>`model x_test_1` |  |
| x_test_1 admin | `access_x_test_1_admin` | Gives **Administration / Settings** read/write/create/delete access to TEST-1 records. | `group base.group_system` (base)<br>`model x_test_1` |  |
