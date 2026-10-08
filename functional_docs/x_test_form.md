# BugFix-Studio-Misc — `x_test_form`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_test_form` — TEST FORM

*Created by this repo.* Python: `models/x_test_form.py`, `models/x_test_form_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_test_form -->
TEST FORM is a Studio sandbox model with a name, a sort order, chatter and one extra text field on its form. It has a single window action. Internal users can read it and administrators have full access. No logic uses it.
<!-- /SUMMARY -->

**Fields (34):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Studio-Misc.view_3780_default_form_view_for_x_test_form`<br>`x_test_form.activity_summary`<br>`x_test_form.activity_type_icon`<br>`x_test_form.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_test_form.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_test_form.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_test_form.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Studio-Misc.view_3780_default_form_view_for_x_test_form` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Studio-Misc.view_3780_default_form_view_for_x_test_form` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of TEST FORM records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_248_x_test_form_x_active`<br>`view BugFix-Studio-Misc.view_3780_default_form_view_for_x_test_form`<br>`view BugFix-Studio-Misc.view_3781_default_search_view_for_x_test_form` |
| `x_name` | Name | char | Name of a TEST FORM record, entered by the user and used as its display name. Shown in the list, form and search views. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_3779_default_list_view_for_x_test_form`<br>`view BugFix-Studio-Misc.view_3780_default_form_view_for_x_test_form`<br>`view BugFix-Studio-Misc.view_3781_default_search_view_for_x_test_form` |
| `x_studio_char_field_3aVUG` | New Text | char | User-entered char value labelled 'New Text'. Shown in the form view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_3782_odoo_studio_default_form_view_for_x_test_form_customization_ext` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for TEST FORM records (default set by an ir.default), used to order them in lists. Shown in the list view. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_249_x_test_form_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_3779_default_list_view_for_x_test_form` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TEST FORM | `act_window_1666_test_form` | Opens **TEST FORM** records (tree,form). | `model x_test_form` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_test_form` |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_test_form | `view_3780_default_form_view_for_x_test_form` | form | full form layout with 5 fields | Default Studio form for the test model x_test_form: required Name, archived ribbon, and chatter (followers, messages, activities). | `x_test_form.activity_ids`<br>`x_test_form.message_follower_ids`<br>`x_test_form.message_ids`<br>`x_test_form.x_active`<br>`x_test_form.x_name` | `view BugFix-Studio-Misc.view_3782_odoo_studio_default_form_view_for_x_test_form_customization_ext` |
| Default list view for x_test_form | `view_3779_default_list_view_for_x_test_form` | tree | full tree layout with 2 fields | Default Studio list view for x_test_form: drag-handle Sequence and Name. | `x_test_form.x_name`<br>`x_test_form.x_studio_sequence` |  |
| Default search view for x_test_form | `view_3781_default_search_view_for_x_test_form` | search | full search layout with 1 fields | Default Studio search view for x_test_form: search by Name plus an 'Archived' filter. | `x_test_form.x_active`<br>`x_test_form.x_name` |  |
| Odoo Studio: Default form view for x_test_form customization | `view_3782_odoo_studio_default_form_view_for_x_test_form_customization_ext` | form | inside `//group[@name='studio_group_7e1a9f_left']`: add field x_studio_char_field_3aVUG | Adds a Studio char field to the left group of the x_test_form form. | `view BugFix-Studio-Misc.view_3780_default_form_view_for_x_test_form`<br>`x_test_form.x_studio_char_field_3aVUG` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TEST FORM group_system | `access_1496_test_form_group_system` | Gives **Administration / Settings** read/write/create/delete access to TEST FORM records. | `group base.group_system` (base)<br>`model x_test_form` |  |
| TEST FORM group_user | `access_1497_test_form_group_user` | Gives **User types / Internal User** read access to TEST FORM records. | `group base.group_user` (base)<br>`model x_test_form` |  |
| x_test_form admin | `access_x_test_form_admin` | Gives **Administration / Settings** read/write/create/delete access to TEST FORM records. | `group base.group_system` (base)<br>`model x_test_form` |  |
