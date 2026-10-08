# BugFix-Studio-Misc — `x_test_model_link_2`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_test_model_link_2` — Test Model Link 2

*Created by this repo.* Python: `models/x_test_model_link_2.py`, `models/x_test_model_link_2_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_test_model_link_2 -->
Test Model Link 2 is a Studio sandbox model that links to TEST MODEL PRIMARY records through both a many2many field and a many2one field, shown on its form. It has a window action. Only administrators have access to it, and no logic uses it.
<!-- /SUMMARY -->

**Fields (35):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Studio-Misc.view_3840_default_form_view_for_x_test_model_link_2`<br>`x_test_model_link_2.activity_summary`<br>`x_test_model_link_2.activity_type_icon`<br>`x_test_model_link_2.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_test_model_link_2.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_test_model_link_2.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_test_model_link_2.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Studio-Misc.view_3840_default_form_view_for_x_test_model_link_2` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Studio-Misc.view_3840_default_form_view_for_x_test_model_link_2` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of Test Model Link 2 records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_271_x_test_model_link_2_x_active`<br>`view BugFix-Studio-Misc.view_3840_default_form_view_for_x_test_model_link_2`<br>`view BugFix-Studio-Misc.view_3841_default_search_view_for_x_test_model_link_2` |
| `x_name` | Name | char | Name of a Test Model Link 2 record, entered by the user and used as its display name. Shown in the list, form and search views. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_3839_default_list_view_for_x_test_model_link_2`<br>`view BugFix-Studio-Misc.view_3840_default_form_view_for_x_test_model_link_2`<br>`view BugFix-Studio-Misc.view_3841_default_search_view_for_x_test_model_link_2` |
| `x_studio_many2many_field_2PxmY` | TEST MODEL PRIMARY | many2many → `x_test_model_primary` | Many2many link labelled 'TEST MODEL PRIMARY' to `x_test_model_primary` records, chosen by the user. Shown in the form view. Part of a Studio test/sandbox model. | stored | `model x_test_model_primary` | `view BugFix-Studio-Misc.view_3842_odoo_studio_default_form_view_for_x_test_model_link_2_custom_ext` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for Test Model Link 2 records (default set by an ir.default), used to order them in lists. Shown in the list view. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_272_x_test_model_link_2_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_3839_default_list_view_for_x_test_model_link_2` |
| `x_studio_test_model_primary_2` | TEST MODEL PRIMARY 2 | many2one → `x_test_model_primary` | Many2one link labelled 'TEST MODEL PRIMARY 2' to `x_test_model_primary` records, chosen by the user. Shown in the form view. Part of a Studio test/sandbox model. | stored | `model x_test_model_primary` | `view BugFix-Studio-Misc.view_3842_odoo_studio_default_form_view_for_x_test_model_link_2_custom_ext` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Test Model Link 2 | `act_window_1687_test_model_link_2` | Opens **Test Model Link 2** records (tree,form). | `model x_test_model_link_2` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_test_model_link_2` |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_test_model_link_2 | `view_3840_default_form_view_for_x_test_model_link_2` | form | full form layout with 5 fields | Default Studio form for the test model x_test_model_link_2: required Name, archived ribbon and chatter. | `x_test_model_link_2.activity_ids`<br>`x_test_model_link_2.message_follower_ids`<br>`x_test_model_link_2.message_ids`<br>`x_test_model_link_2.x_active`<br>`x_test_model_link_2.x_name` | `view BugFix-Studio-Misc.view_3842_odoo_studio_default_form_view_for_x_test_model_link_2_custom_ext` |
| Default list view for x_test_model_link_2 | `view_3839_default_list_view_for_x_test_model_link_2` | tree | full tree layout with 2 fields | Default Studio list view for x_test_model_link_2: drag-handle Sequence and Name. | `x_test_model_link_2.x_name`<br>`x_test_model_link_2.x_studio_sequence` |  |
| Default search view for x_test_model_link_2 | `view_3841_default_search_view_for_x_test_model_link_2` | search | full search layout with 1 fields | Default Studio search view for x_test_model_link_2: search by Name plus an 'Archived' filter. | `x_test_model_link_2.x_active`<br>`x_test_model_link_2.x_name` |  |
| Odoo Studio: Default form view for x_test_model_link_2 customization | `view_3842_odoo_studio_default_form_view_for_x_test_model_link_2_custom_ext` | form | inside `//group[@name='studio_group_861128_left']`: add field x_studio_many2many_field_2PxmY, field x_studio_test_model_primary_2 | Adds a many2many tags field and a 'TEST MODEL PRIMARY 2' link field to the x_test_model_link_2 form. | `view BugFix-Studio-Misc.view_3840_default_form_view_for_x_test_model_link_2`<br>`x_test_model_link_2.x_studio_many2many_field_2PxmY`<br>`x_test_model_link_2.x_studio_test_model_primary_2` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Test Model Link 2 group_system | `access_1518_test_model_link_2_group_system` | Gives **Administration / Settings** read/write/create/delete access to Test Model Link 2 records. | `group base.group_system` (base)<br>`model x_test_model_link_2` |  |
| Test Model Link 2 group_user | `access_1519_test_model_link_2_group_user` | Gives **User types / Internal User** no access to Test Model Link 2 records. | `group base.group_user` (base)<br>`model x_test_model_link_2` |  |
| x_test_model_link_2 admin | `access_x_test_model_link_2_admin` | Gives **Administration / Settings** read/write/create/delete access to Test Model Link 2 records. | `group base.group_system` (base)<br>`model x_test_model_link_2` |  |
