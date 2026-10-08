# BugFix-Studio-Misc — `x_website_faq`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_website_faq` — website.faq

*Created by this repo.* Python: `models/x_website_faq.py`, `models/x_website_faq_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_website_faq -->
A website FAQ entry, labelled website.faq, with a description, a question, an answer and a Published on the website checkbox. It has a window action, customized Studio form and list views, and a simple FAQ form that shows only the question and answer. Internal users can create and edit entries. No logic in this repo publishes the entries or acts on them.
<!-- /SUMMARY -->

**Fields (38):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Studio-Misc.view_8027_default_form_view_for_x_website_faq`<br>`x_website_faq.activity_summary`<br>`x_website_faq.activity_type_icon`<br>`x_website_faq.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_website_faq.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_website_faq.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_website_faq.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Studio-Misc.view_8027_default_form_view_for_x_website_faq` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Studio-Misc.view_8027_default_form_view_for_x_website_faq` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of website.faq records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. | stored |  | `default BugFix-Studio-Misc.default_582_x_website_faq_x_active`<br>`view BugFix-Studio-Misc.view_8027_default_form_view_for_x_website_faq`<br>`view BugFix-Studio-Misc.view_8028_default_search_view_for_x_website_faq` |
| `x_faqfield` | FAQ | text | Long-text FAQ field on the website.faq Studio model; not used by any view or logic in this repo. | stored |  |  |
| `x_name` | Description | char | Description of a website FAQ entry, entered by the user and used as its display name; shown in the default list, form and search views. | stored; required |  | `view BugFix-Studio-Misc.view_8026_default_list_view_for_x_website_faq`<br>`view BugFix-Studio-Misc.view_8027_default_form_view_for_x_website_faq`<br>`view BugFix-Studio-Misc.view_8028_default_search_view_for_x_website_faq` |
| `x_studio_answer` | Answer | char | Answer text of a website FAQ entry, entered by the user; shown on the FAQ forms (including the 'website.published' form) and list. | stored |  | `view BugFix-Studio-Misc.view_8029_odoo_studio_default_form_view_for_x_website_faq_customizatio_ext`<br>`view BugFix-Studio-Misc.view_8031_odoo_studio_default_list_view_for_x_website_faq_customizatio_ext`<br>`view BugFix-Studio-Misc.view_8245_website_published` |
| `x_studio_char_field_c3_1ipgu110c` | New Text | char | Unnamed Studio text field ('New Text') on website FAQ, shown on the Studio form; no logic uses it. | stored |  | `view BugFix-Studio-Misc.view_8029_odoo_studio_default_form_view_for_x_website_faq_customizatio_ext` |
| `x_studio_published_on_the_website` | published on the website | boolean | Checkbox marking a website FAQ entry as published on the website; shown on the Studio form. No logic in this repo acts on it. | stored |  | `view BugFix-Studio-Misc.view_8029_odoo_studio_default_form_view_for_x_website_faq_customizatio_ext` |
| `x_studio_question` | Question | char | Question text of a website FAQ entry, entered by the user; shown on the FAQ forms (including the 'website.published' form) and list. | stored |  | `view BugFix-Studio-Misc.view_8029_odoo_studio_default_form_view_for_x_website_faq_customizatio_ext`<br>`view BugFix-Studio-Misc.view_8031_odoo_studio_default_list_view_for_x_website_faq_customizatio_ext`<br>`view BugFix-Studio-Misc.view_8245_website_published` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for website.faq records (default set by an ir.default), used to order them in lists. Shown in the list view. | stored |  | `default BugFix-Studio-Misc.default_583_x_website_faq_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_8026_default_list_view_for_x_website_faq` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| website.faq | `act_window_3205_website_faq` | Opens **website.faq** records (tree,form). | `model x_website_faq` | `menu BugFix-Studio-Misc.menu_f6r3_faqs_website_faq` |

**Views (6):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_website_faq | `view_8027_default_form_view_for_x_website_faq` | form | full form layout with 5 fields | Default Studio form for website FAQ entries (x_website_faq): required Name, archived ribbon and chatter. | `x_website_faq.activity_ids`<br>`x_website_faq.message_follower_ids`<br>`x_website_faq.message_ids`<br>`x_website_faq.x_active`<br>`x_website_faq.x_name` | `view BugFix-Studio-Misc.view_8029_odoo_studio_default_form_view_for_x_website_faq_customizatio_ext` |
| Default list view for x_website_faq | `view_8026_default_list_view_for_x_website_faq` | tree | full tree layout with 2 fields | Default Studio list view for website FAQ entries (x_website_faq): drag-handle Sequence and Name. | `x_website_faq.x_name`<br>`x_website_faq.x_studio_sequence` | `view BugFix-Studio-Misc.view_8031_odoo_studio_default_list_view_for_x_website_faq_customizatio_ext` |
| Default search view for x_website_faq | `view_8028_default_search_view_for_x_website_faq` | search | full search layout with 1 fields | Default Studio search view for website FAQ entries (x_website_faq): search by Name plus an 'Archived' filter. | `x_website_faq.x_active`<br>`x_website_faq.x_name` |  |
| Odoo Studio: Default form view for x_website_faq customization | `view_8029_odoo_studio_default_form_view_for_x_website_faq_customizatio_ext` | form | remove `//field[@name='x_name']`; set invisible=True on `//field[@name='x_active']`; inside `//group[@name='studio_group_50153f_left']`: add field x_studio_char_field_c3_1ipgu110c, field x_studio_question, field x_studio_answer, field x_studio_published_on_the_website | Extends the website FAQ (x_website_faq) form: removes Name, keeps Active hidden, and adds a char field, Question, Answer and 'Published on the website'. | `view BugFix-Studio-Misc.view_8027_default_form_view_for_x_website_faq`<br>`x_website_faq.x_studio_answer`<br>`x_website_faq.x_studio_char_field_c3_1ipgu110c`<br>`x_website_faq.x_studio_published_on_the_website`<br>`x_website_faq.x_studio_question` |  |
| Odoo Studio: Default list view for x_website_faq customization | `view_8031_odoo_studio_default_list_view_for_x_website_faq_customizatio_ext` | tree | after `//field[@name='x_name']`: add field x_studio_question, field x_studio_answer | Adds optional Question and Answer columns to the website FAQ (x_website_faq) list. | `view BugFix-Studio-Misc.view_8026_default_list_view_for_x_website_faq`<br>`x_website_faq.x_studio_answer`<br>`x_website_faq.x_studio_question` |  |
| website.published | `view_8245_website_published` | form | full form layout with 2 fields | Simple 'FAQ' form for x_website_faq showing only Question and Answer. | `x_website_faq.x_studio_answer`<br>`x_website_faq.x_studio_question` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| website.faq group_system | `access_7829_website_faq_group_system` | Gives **Administration / Settings** read/write/create/delete access to website.faq records. | `group base.group_system` (base)<br>`model x_website_faq` |  |
| website.faq group_user | `access_7830_website_faq_group_user` | Gives **User types / Internal User** read/write/create access to website.faq records. | `group base.group_user` (base)<br>`model x_website_faq` |  |
| x_website_faq admin | `access_x_website_faq_admin` | Gives **Administration / Settings** read/write/create/delete access to website.faq records. | `group base.group_system` (base)<br>`model x_website_faq` |  |
