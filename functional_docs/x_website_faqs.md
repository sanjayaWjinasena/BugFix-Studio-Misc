# BugFix-Studio-Misc — `x_website_faqs`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_website_faqs` — website FAQs

*Created by this repo.* Python: `models/x_website_faqs.py`, `models/x_website_faqs_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_website_faqs -->
A website FAQ entry (website FAQs) with a question, an answer, an HTML website description and a Website Published flag. It has a window action and customized Studio form and list views. Four website qweb templates show the FAQs on the website as a searchable listing in grid or list layout, with pagination and a detail page. Public website visitors get read access through a public-access right.
<!-- /SUMMARY -->

**Fields (39):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Studio-Misc.view_8033_default_form_view_for_x_website_faqs`<br>`x_website_faqs.activity_summary`<br>`x_website_faqs.activity_type_icon`<br>`x_website_faqs.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_website_faqs.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_website_faqs.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_website_faqs.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Studio-Misc.view_8033_default_form_view_for_x_website_faqs` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Studio-Misc.view_8033_default_form_view_for_x_website_faqs` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of website FAQs records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. | stored |  | `default BugFix-Studio-Misc.default_584_x_website_faqs_x_active`<br>`view BugFix-Studio-Misc.view_8033_default_form_view_for_x_website_faqs`<br>`view BugFix-Studio-Misc.view_8034_default_search_view_for_x_website_faqs` |
| `x_name` | Description | char | Description of a website FAQs entry, entered by the user and used as its display name; shown in the default list, form and search views. | stored; required |  | `view BugFix-Studio-Misc.view_8032_default_list_view_for_x_website_faqs`<br>`view BugFix-Studio-Misc.view_8033_default_form_view_for_x_website_faqs`<br>`view BugFix-Studio-Misc.view_8034_default_search_view_for_x_website_faqs` |
| `x_studio_active` | Active | boolean | Second 'Active' checkbox on website FAQs (separate from the archive flag `x_active`), shown on the Studio form; no logic uses it. | stored |  | `view BugFix-Studio-Misc.view_8035_odoo_studio_default_form_view_for_x_website_faqs_customizati_ext` |
| `x_studio_answer` | Answer | char | Answer text of a website FAQs entry, entered by the user; shown on its Studio form and list. | stored |  | `view BugFix-Studio-Misc.view_8035_odoo_studio_default_form_view_for_x_website_faqs_customizati_ext`<br>`view BugFix-Studio-Misc.view_8036_odoo_studio_default_list_view_for_x_website_faqs_customizati_ext` |
| `x_studio_boolean_field_1ap_1iph4t6ob` | New CheckBox | boolean | Unnamed Studio checkbox ('New CheckBox') on website FAQs; not used by any view or logic in this repo. | stored |  |  |
| `x_studio_question` | Question | char | Question text of a website FAQs entry, entered by the user; shown on its Studio form and list. | stored |  | `view BugFix-Studio-Misc.view_8035_odoo_studio_default_form_view_for_x_website_faqs_customizati_ext`<br>`view BugFix-Studio-Misc.view_8036_odoo_studio_default_list_view_for_x_website_faqs_customizati_ext` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for website FAQs records (default set by an ir.default), used to order them in lists. Shown in the list view. | stored |  | `default BugFix-Studio-Misc.default_585_x_website_faqs_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_8032_default_list_view_for_x_website_faqs` |
| `x_studio_website_description` | Website Description | html | HTML website description for a website FAQs entry; not used by any view or logic in this repo. | stored |  |  |
| `x_studio_website_published` | Website Published | boolean | Checkbox marking a website FAQs entry as published on the website; shown on the Studio form. No logic in this repo acts on it. | stored |  | `view BugFix-Studio-Misc.view_8035_odoo_studio_default_form_view_for_x_website_faqs_customizati_ext` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| website FAQs | `act_window_3206_website_faqs` | Opens **website FAQs** records (tree,form). | `model x_website_faqs` | `menu BugFix-Studio-Misc.menu_f6r3_website_faq_website_faqs` |

**Views (9):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_website_faqs | `view_8033_default_form_view_for_x_website_faqs` | form | full form layout with 5 fields | Default Studio form for website FAQs (x_website_faqs): required Name, archived ribbon and chatter. | `x_website_faqs.activity_ids`<br>`x_website_faqs.message_follower_ids`<br>`x_website_faqs.message_ids`<br>`x_website_faqs.x_active`<br>`x_website_faqs.x_name` | `view BugFix-Studio-Misc.view_8035_odoo_studio_default_form_view_for_x_website_faqs_customizati_ext` |
| Default list view for x_website_faqs | `view_8032_default_list_view_for_x_website_faqs` | tree | full tree layout with 2 fields | Default Studio list view for website FAQs (x_website_faqs): drag-handle Sequence and Name. | `x_website_faqs.x_name`<br>`x_website_faqs.x_studio_sequence` | `view BugFix-Studio-Misc.view_8036_odoo_studio_default_list_view_for_x_website_faqs_customizati_ext` |
| Default search view for x_website_faqs | `view_8034_default_search_view_for_x_website_faqs` | search | full search layout with 1 fields | Default Studio search view for website FAQs (x_website_faqs): search by Name plus an 'Archived' filter. | `x_website_faqs.x_active`<br>`x_website_faqs.x_name` |  |
| Odoo Studio: Default form view for x_website_faqs customization | `view_8035_odoo_studio_default_form_view_for_x_website_faqs_customizati_ext` | form | inside `//group[@name='studio_group_f67068_left']`: add field x_studio_question, field x_studio_answer; inside `//group[@name='studio_group_f67068_right']`: add field x_studio_active, field x_studio_website_published | Extends the website FAQs (x_website_faqs) form: adds Question and Answer on the left, Active and Website Published on the right. | `view BugFix-Studio-Misc.view_8033_default_form_view_for_x_website_faqs`<br>`x_website_faqs.x_studio_active`<br>`x_website_faqs.x_studio_answer`<br>`x_website_faqs.x_studio_question`<br>`x_website_faqs.x_studio_website_published` |  |
| Odoo Studio: Default list view for x_website_faqs customization | `view_8036_odoo_studio_default_list_view_for_x_website_faqs_customizati_ext` | tree | replace `//field[@name='x_name']`: add field x_studio_answer; before `//field[@name='x_studio_sequence']`: add field x_studio_question | Changes the website FAQs (x_website_faqs) list to show Question before Sequence and Answer in place of Name. | `view BugFix-Studio-Misc.view_8032_default_list_view_for_x_website_faqs`<br>`x_website_faqs.x_studio_answer`<br>`x_website_faqs.x_studio_question` |  |
| faq | `view_8241_qweb_faq` | qweb | full t layout with 0 fields | Website page template for a single FAQ record (x_website_faqs): breadcrumb back to the listing, the record title and its website description. |  |  |
| faq | `view_8246_qweb_faq` | qweb | full t layout with 0 fields | Partial website template rendering the FAQ section: a search box with result count, FAQ cards (Question and Answer) in grid or list layout, and pagination. |  |  |
| faq | `view_8247_qweb_faq` | qweb | full t layout with 0 fields | Website listing page for FAQs: search bar, grid/list layout switcher, a card per record linking to its detail page, and pagination. |  |  |
| faq | `view_8248_qweb_faq` | qweb | full t layout with 0 fields | Main website FAQ listing page: search box, FAQ cards showing Question and Answer in grid or list layout, and pagination. |  |  |

**Access rights (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Website integration: public model access | `access_7883_website_integration_public_model_access` | Gives **Technical / Public access to arbitrary exposed model** read access to website FAQs records. | `group website.website_page_controller_expose` (website)<br>`model x_website_faqs` |  |
| website FAQs group_system | `access_7831_website_faqs_group_system` | Gives **Administration / Settings** read/write/create/delete access to website FAQs records. | `group base.group_system` (base)<br>`model x_website_faqs` |  |
| website FAQs group_user | `access_7832_website_faqs_group_user` | Gives **User types / Internal User** read/write/create access to website FAQs records. | `group base.group_user` (base)<br>`model x_website_faqs` |  |
| x_website_faqs admin | `access_x_website_faqs_admin` | Gives **Administration / Settings** read/write/create/delete access to website FAQs records. | `group base.group_system` (base)<br>`model x_website_faqs` |  |
