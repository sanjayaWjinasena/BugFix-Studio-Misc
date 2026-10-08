# BugFix-Studio-Misc — `x_test_model_link`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_test_model_link` — TEST MODEL LINK

*Created by this repo.* Python: `models/x_test_model_link.py`, `models/x_test_model_link_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_test_model_link -->
TEST MODEL LINK is a Studio sandbox model that links each record to one TEST MODEL PRIMARY record. These records appear as the Line IDs list on the primary record. It has a window action and form and list customizations. No logic uses it.
<!-- /SUMMARY -->

**Fields (34):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Studio-Misc.view_3833_default_form_view_for_x_test_model_link`<br>`x_test_model_link.activity_summary`<br>`x_test_model_link.activity_type_icon`<br>`x_test_model_link.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_test_model_link.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_test_model_link.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_test_model_link.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Studio-Misc.view_3833_default_form_view_for_x_test_model_link` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Studio-Misc.view_3833_default_form_view_for_x_test_model_link` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of TEST MODEL LINK records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_269_x_test_model_link_x_active`<br>`view BugFix-Studio-Misc.view_3833_default_form_view_for_x_test_model_link`<br>`view BugFix-Studio-Misc.view_3834_default_search_view_for_x_test_model_link` |
| `x_name` | Name | char | Name of a TEST MODEL LINK record, entered by the user and used as its display name. Shown in the list, form and search views. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_3830_odoo_studio_default_form_view_for_x_test_model_primary_custo_ext`<br>`view BugFix-Studio-Misc.view_3832_default_list_view_for_x_test_model_link`<br>`view BugFix-Studio-Misc.view_3833_default_form_view_for_x_test_model_link`<br>`view BugFix-Studio-Misc.view_3834_default_search_view_for_x_test_model_link` |
| `x_studio_many2one_field_sctrD` | TEST MODEL PRIMARY | many2one → `x_test_model_primary` | Many2one link labelled 'TEST MODEL PRIMARY' to `x_test_model_primary` records, chosen by the user. Shown in the form and list views. Part of a Studio test/sandbox model. | stored | `model x_test_model_primary` | `view BugFix-Studio-Misc.view_3830_odoo_studio_default_form_view_for_x_test_model_primary_custo_ext`<br>`view BugFix-Studio-Misc.view_3835_odoo_studio_default_form_view_for_x_test_model_link_customiz_ext`<br>`view BugFix-Studio-Misc.view_3836_odoo_studio_default_list_view_for_x_test_model_link_customiz_ext` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for TEST MODEL LINK records (default set by an ir.default), used to order them in lists. Shown in the list view. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_270_x_test_model_link_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_3830_odoo_studio_default_form_view_for_x_test_model_primary_custo_ext`<br>`view BugFix-Studio-Misc.view_3832_default_list_view_for_x_test_model_link` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TEST MODEL LINK | `act_window_1686_test_model_link` | Opens **TEST MODEL LINK** records (tree,form). | `model x_test_model_link` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_test_model_link` |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_test_model_link | `view_3833_default_form_view_for_x_test_model_link` | form | full form layout with 5 fields | Default Studio form for the test model x_test_model_link: required Name, archived ribbon and chatter. | `x_test_model_link.activity_ids`<br>`x_test_model_link.message_follower_ids`<br>`x_test_model_link.message_ids`<br>`x_test_model_link.x_active`<br>`x_test_model_link.x_name` | `view BugFix-Studio-Misc.view_3835_odoo_studio_default_form_view_for_x_test_model_link_customiz_ext` |
| Default list view for x_test_model_link | `view_3832_default_list_view_for_x_test_model_link` | tree | full tree layout with 2 fields | Default Studio list view for x_test_model_link: drag-handle Sequence and Name. | `x_test_model_link.x_name`<br>`x_test_model_link.x_studio_sequence` | `view BugFix-Studio-Misc.view_3836_odoo_studio_default_list_view_for_x_test_model_link_customiz_ext` |
| Default search view for x_test_model_link | `view_3834_default_search_view_for_x_test_model_link` | search | full search layout with 1 fields | Default Studio search view for x_test_model_link: search by Name plus an 'Archived' filter. | `x_test_model_link.x_active`<br>`x_test_model_link.x_name` |  |
| Odoo Studio: Default form view for x_test_model_link customization | `view_3835_odoo_studio_default_form_view_for_x_test_model_link_customiz_ext` | form | inside `//group[@name='studio_group_61934b_left']`: add field x_studio_many2one_field_sctrD | Adds a Studio Many2one link field to the x_test_model_link form. | `view BugFix-Studio-Misc.view_3833_default_form_view_for_x_test_model_link`<br>`x_test_model_link.x_studio_many2one_field_sctrD` |  |
| Odoo Studio: Default list view for x_test_model_link customization | `view_3836_odoo_studio_default_list_view_for_x_test_model_link_customiz_ext` | tree | after `//field[@name='x_name']`: add field x_studio_many2one_field_sctrD, field id | Adds the Studio Many2one link field and record ID columns to the x_test_model_link list. | `view BugFix-Studio-Misc.view_3832_default_list_view_for_x_test_model_link`<br>`x_test_model_link.x_studio_many2one_field_sctrD` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TEST MODEL LINK group_system | `access_1516_test_model_link_group_system` | Gives **Administration / Settings** read/write/create/delete access to TEST MODEL LINK records. | `group base.group_system` (base)<br>`model x_test_model_link` |  |
| TEST MODEL LINK group_user | `access_1517_test_model_link_group_user` | Gives **User types / Internal User** read access to TEST MODEL LINK records. | `group base.group_user` (base)<br>`model x_test_model_link` |  |
| x_test_model_link admin | `access_x_test_model_link_admin` | Gives **Administration / Settings** read/write/create/delete access to TEST MODEL LINK records. | `group base.group_system` (base)<br>`model x_test_model_link` |  |
