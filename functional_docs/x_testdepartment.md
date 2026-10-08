# BugFix-Studio-Misc — `x_testdepartment`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_testdepartment` — TestDepartment

*Created by this repo.* Python: `models/x_testdepartment.py`, `models/x_testdepartment_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_testdepartment -->
TestDepartment is a Studio sandbox model with a code, three description fields and a signature image, shown on its customized form. It has a window action. Only administrators have access to it, and no logic uses it.
<!-- /SUMMARY -->

**Fields (25):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_testdepartment.activity_summary`<br>`x_testdepartment.activity_type_icon`<br>`x_testdepartment.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_testdepartment.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_testdepartment.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_testdepartment.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_Description2` | Description 2 | char | User-entered char value labelled 'Description 2'. Shown in the form view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_2396_odoo_studio_default_form_view_for_x_testdepartment_customiza_ext` |
| `x_Description3` | Description 3 | char | Third description text on TestDepartment, added to the form by the 'test departmet desc 3' extension view. Sandbox model. | stored |  | `view BugFix-Studio-Misc.view_2397_test_departmet_desc_3_ext` |
| `x_active` | Active | boolean | Archive flag of TestDepartment records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_18_x_testdepartment_x_active`<br>`view BugFix-Studio-Misc.view_2394_default_form_view_for_x_testdepartment`<br>`view BugFix-Studio-Misc.view_2395_default_search_view_for_x_testdepartment` |
| `x_name` | Name | char | Name of a TestDepartment record, entered by the user and used as its display name. Shown in the list, form and search views. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_2393_default_list_view_for_x_testdepartment`<br>`view BugFix-Studio-Misc.view_2394_default_form_view_for_x_testdepartment`<br>`view BugFix-Studio-Misc.view_2395_default_search_view_for_x_testdepartment` |
| `x_studio_code` | Code | char | User-entered char value labelled 'Code'. Shown in the form view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_2396_odoo_studio_default_form_view_for_x_testdepartment_customiza_ext` |
| `x_studio_description` | Description | char | User-entered char value labelled 'Description'. Shown in the form view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_2396_odoo_studio_default_form_view_for_x_testdepartment_customiza_ext` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for TestDepartment records (default set by an ir.default), used to order them in lists. Shown in the list view. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_19_x_testdepartment_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_2393_default_list_view_for_x_testdepartment` |
| `x_studio_sig` | Sig | binary | Binary signature/image field on TestDepartment, shown on its Studio form. Sandbox model. | stored |  | `view BugFix-Studio-Misc.view_2396_odoo_studio_default_form_view_for_x_testdepartment_customiza_ext` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TestDepartment | `act_window_812_testdepartment` | Opens **TestDepartment** records (tree,form). | `model x_testdepartment` |  |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_testdepartment | `view_2394_default_form_view_for_x_testdepartment` | form | full form layout with 2 fields | Default Studio form for the test model x_testdepartment: required Name and archived ribbon; chatter fields stripped because the model has no mail support. | `x_testdepartment.x_active`<br>`x_testdepartment.x_name` | `view BugFix-Studio-Misc.view_2396_odoo_studio_default_form_view_for_x_testdepartment_customiza_ext`<br>`view BugFix-Studio-Misc.view_2397_test_departmet_desc_3_ext` |
| Default list view for x_testdepartment | `view_2393_default_list_view_for_x_testdepartment` | tree | full tree layout with 2 fields | Default Studio list view for x_testdepartment: drag-handle Sequence and Name. | `x_testdepartment.x_name`<br>`x_testdepartment.x_studio_sequence` |  |
| Default search view for x_testdepartment | `view_2395_default_search_view_for_x_testdepartment` | search | full search layout with 1 fields | Default Studio search view for x_testdepartment: search by Name plus an 'Archived' filter. | `x_testdepartment.x_active`<br>`x_testdepartment.x_name` |  |
| Odoo Studio: Default form view for x_testdepartment customization | `view_2396_odoo_studio_default_form_view_for_x_testdepartment_customiza_ext` | form | inside `//group[@name='studio_group_5691c0_left']`: add field x_studio_code, field x_studio_description, field x_Description2; before `/form[1]/sheet[1]/group[1]/group[1]/field[1]`: add field x_studio_sig; set string=Sig on `/form[1]/sheet[1]/group[1]/group[1]/field[1]`; set required=1 on `/form[1]/sheet[1]/group[1]/group[1]/field[1]`; remove `/form[1]/sheet[1]/group[1]/group[1]/field[1]` | Extends the x_testdepartment form: adds Code, Description and Description 2; a signature field is inserted and then removed again by the same positional xpaths, so it does not show. | `view BugFix-Studio-Misc.view_2394_default_form_view_for_x_testdepartment`<br>`x_testdepartment.x_Description2`<br>`x_testdepartment.x_studio_code`<br>`x_testdepartment.x_studio_description`<br>`x_testdepartment.x_studio_sig` |  |
| test_departmet_desc_3 | `view_2397_test_departmet_desc_3_ext` | form | inside `//group[@name='studio_group_5691c0_left']`: add field x_Description3 | Adds 'Description 3' to the left group of the x_testdepartment form. | `view BugFix-Studio-Misc.view_2394_default_form_view_for_x_testdepartment`<br>`x_testdepartment.x_Description3` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TestDepartment group_system | `access_1143_testdepartment_group_system` | Gives **Administration / Settings** read/write/create/delete access to TestDepartment records. | `group base.group_system` (base)<br>`model x_testdepartment` |  |
| TestDepartment group_user | `access_1144_testdepartment_group_user` | Gives **User types / Internal User** no access to TestDepartment records. | `group base.group_user` (base)<br>`model x_testdepartment` |  |
| x_testdepartment admin | `access_x_testdepartment_admin` | Gives **Administration / Settings** read/write/create/delete access to TestDepartment records. | `group base.group_system` (base)<br>`model x_testdepartment` |  |
