# BugFix-Studio-Misc — `x_sales_model_debug`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_sales_model_debug` — Sales Model Debug

*Created by this repo.* Python: `models/x_sales_model_debug.py`, `models/x_sales_model_debug_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_sales_model_debug -->
A timing and debug log model. Each record logs a method name (`x_name`, shown as Method Name) with a start time and an end time. It has mail chatter and activities, a window action, and an inline-editable list that shows the start and end times. The Jin Sales POS users and Sales View Only groups can read and create records, and administrators have full access.
<!-- /SUMMARY -->

**Fields (35):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Studio-Misc.view_5293_default_form_view_for_x_sales_model_debug_e`<br>`x_sales_model_debug.activity_summary`<br>`x_sales_model_debug.activity_type_icon`<br>`x_sales_model_debug.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_sales_model_debug.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_sales_model_debug.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_sales_model_debug.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Studio-Misc.view_5293_default_form_view_for_x_sales_model_debug_e` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Studio-Misc.view_5293_default_form_view_for_x_sales_model_debug_e` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of Sales Model Debug records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. | stored |  | `default BugFix-Studio-Misc.default_379_x_sales_model_debug_x_active`<br>`view BugFix-Studio-Misc.view_5293_default_form_view_for_x_sales_model_debug_e`<br>`view BugFix-Studio-Misc.view_5294_default_search_view_for_x_sales_model_debug_e` |
| `x_name` | Method Name | char | Method Name logged in a Sales Model Debug record (a timing/debug log model); shown in its default views. | stored |  | `view BugFix-Studio-Misc.view_5292_default_list_view_for_x_sales_model_debug_e`<br>`view BugFix-Studio-Misc.view_5293_default_form_view_for_x_sales_model_debug_e`<br>`view BugFix-Studio-Misc.view_5294_default_search_view_for_x_sales_model_debug_e` |
| `x_studio_end_time` | End Time | datetime | End time logged on a Sales Model Debug record; shown on its Studio form. Debug log model. | stored |  | `view BugFix-Studio-Misc.view_final_x_sales_model_debug_odoo_studio_default_list_view_for_x_sales_model_debug_custo` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for Sales Model Debug records (default set by an ir.default), used to order them in lists. Shown in the list view. | stored |  | `default BugFix-Studio-Misc.default_380_x_sales_model_debug_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_5292_default_list_view_for_x_sales_model_debug_e` |
| `x_studio_start_time` | Start Time | datetime | Start time logged on a Sales Model Debug record; shown on its Studio form. Debug log model. | stored |  | `view BugFix-Studio-Misc.view_final_x_sales_model_debug_odoo_studio_default_list_view_for_x_sales_model_debug_custo` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales Model Debug | `act_window_2380_sales_model_debug` | Opens **Sales Model Debug** records (tree,form). | `model x_sales_model_debug` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_sales_model_debug` |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_sales_model_debug | `view_5293_default_form_view_for_x_sales_model_debug_e` | form | full form layout with 5 fields | Default Studio form for Sales Model Debug records: required Name, archived ribbon and chatter. | `x_sales_model_debug.activity_ids`<br>`x_sales_model_debug.message_follower_ids`<br>`x_sales_model_debug.message_ids`<br>`x_sales_model_debug.x_active`<br>`x_sales_model_debug.x_name` |  |
| Default list view for x_sales_model_debug | `view_5292_default_list_view_for_x_sales_model_debug_e` | tree | full tree layout with 2 fields | Default Studio list view for Sales Model Debug: drag-handle Sequence and Name. | `x_sales_model_debug.x_name`<br>`x_sales_model_debug.x_studio_sequence` | `view BugFix-Studio-Misc.view_final_x_sales_model_debug_odoo_studio_default_list_view_for_x_sales_model_debug_custo` |
| Default search view for x_sales_model_debug | `view_5294_default_search_view_for_x_sales_model_debug_e` | search | full search layout with 1 fields | Default Studio search view for Sales Model Debug: search by Name plus an 'Archived' filter. | `x_sales_model_debug.x_active`<br>`x_sales_model_debug.x_name` |  |
| Odoo Studio: Default list view for x_sales_model_debug customization | `view_final_x_sales_model_debug_odoo_studio_default_list_view_for_x_sales_model_debug_custo` | tree | set editable=bottom on `//tree[1]`; set string=Method Name on `//field[@name='x_name']`; after `//field[@name='x_name']`: add field x_studio_start_time, field x_studio_end_time | Makes the Sales Model Debug list inline-editable, relabels Name as 'Method Name' and adds optional Start Time and End Time columns. | `view BugFix-Studio-Misc.view_5292_default_list_view_for_x_sales_model_debug_e`<br>`x_sales_model_debug.x_studio_end_time`<br>`x_sales_model_debug.x_studio_start_time` |  |

**Access rights (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales Model Debug group_system | `access_1874_sales_model_debug_group_system` | Gives **Administration / Settings** read/write/create/delete access to Sales Model Debug records. | `group base.group_system` (base)<br>`model x_sales_model_debug` |  |
| Sales Model Debug group_user | `access_1875_sales_model_debug_group_user` | Gives **User types / Internal User** read access to Sales Model Debug records. | `group base.group_user` (base)<br>`model x_sales_model_debug` |  |
| x_sales_model_debug | `access_6851_x_sales_model_debug` | Gives **Sales / Jin - Sales - POS Users** read/create access to Sales Model Debug records. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model x_sales_model_debug` |  |
| x_sales_model_debug | `access_g_x_sales_model_debug_x_sales_model_debug_sales_jin_sales_view_only` | Gives **Sales / Jin - Sales - View Only** read/create access to Sales Model Debug records. | `group BugFix-Studio-Misc.group_g_sales_jin_sales_view_only`<br>`model x_sales_model_debug` |  |
| x_sales_model_debug admin | `access_x_sales_model_debug_admin` | Gives **Administration / Settings** read/write/create/delete access to Sales Model Debug records. | `group base.group_system` (base)<br>`model x_sales_model_debug` |  |
