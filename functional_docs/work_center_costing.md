# BugFix-Studio-Misc — `work_center_costing`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `work_center_costing` — Work Center Costing

*Created by this repo.* Python: `models/work_center_costing.py`, `models/x_work_center_costing_gap.py`. Record name field: `name`.

Other repos that use this model: `server action BugFix-Accounting.action_sls_payment_reconciliation_automate` (BugFix-Accounting)<br>`server action BugFix-Stock.action_work_center_costing_model_create_journal_entries` (BugFix-Stock)<br>`server action BugFix-Stock.action_work_center_costing_model_create_journal_entries_original` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:work_center_costing -->
A Work Center Costing setup record. For general, labour, labour overtime and overhead costs, it stores debit and credit accounts plus analytic accounts. Its customized form and list do not allow creating or deleting records. Internal users can read it and administrators have full access. No logic in this repo reads these accounts.
<!-- /SUMMARY -->

**Fields (44):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Studio-Misc.view_work_center_costing_form`<br>`work_center_costing.activity_summary`<br>`work_center_costing.activity_type_icon`<br>`work_center_costing.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`work_center_costing.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`work_center_costing.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`work_center_costing.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Studio-Misc.view_work_center_costing_form` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Studio-Misc.view_work_center_costing_form` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag of Work Center Costing records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. | stored |  | `default BugFix-Studio-Misc.default_76_work_center_costing_active`<br>`view BugFix-Studio-Misc.view_work_center_costing_form`<br>`view BugFix-Studio-Misc.view_work_center_costing_search` |
| `name` | Name | char | Name of a Work Center Costing setup record, entered by the user; shown in its default list, form and search views. | stored |  | `view BugFix-Studio-Misc.view_work_center_costing_list`<br>`view BugFix-Studio-Misc.view_work_center_costing_form`<br>`view BugFix-Studio-Misc.view_work_center_costing_search` |
| `general_analytic_tag` | General Analytic Tag | many2one → `account.analytic.account` | General analytic account (labelled 'Analytic Tag') for a Work Center Costing setup record; not shown on any view or used by logic in this repo. | stored | `model account.analytic.account` (analytic) |  |
| `general_cost_credit_account` | General Cost Credit Account | many2one → `account.account` | General cost credit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_default_form_view_for_work_center_costing_inherit` |
| `general_cost_debit_account` | General Cost Debit Account | many2one → `account.account` | General cost debit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_default_form_view_for_work_center_costing_inherit` |
| `labour_analytic_tag` | Labour Analytic Tag | many2one → `account.analytic.account` | Labour analytic account (labelled 'Analytic Tag') for a Work Center Costing setup record; not shown on any view or used by logic in this repo. | stored | `model account.analytic.account` (analytic) |  |
| `labour_cost_credit_account` | Labour Cost Credit Account | many2one → `account.account` | Labour cost credit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_default_form_view_for_work_center_costing_inherit` |
| `labour_cost_debit_account` | Labour Cost Debit Account | many2one → `account.account` | Labour cost debit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_default_form_view_for_work_center_costing_inherit` |
| `labour_ot_cost_credit_account` | Labour OT Cost Credit Account | many2one → `account.account` | Labour overtime cost credit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_default_form_view_for_work_center_costing_inherit` |
| `labour_ot_cost_debit_account` | Labour OT Cost Debit Account | many2one → `account.account` | Labour overtime cost debit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_default_form_view_for_work_center_costing_inherit` |
| `overhead_analytic_tag` | Overhead Analytic Tag | many2one → `account.analytic.account` | Overhead analytic account (labelled 'Analytic Tag') for a Work Center Costing setup record; not shown on any view or used by logic in this repo. | stored | `model account.analytic.account` (analytic) |  |
| `overhead_cost_credit_account` | Overhead Cost Credit Account | many2one → `account.account` | Overhead cost credit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_default_form_view_for_work_center_costing_inherit` |
| `overhead_cost_debit_account` | Overhead Cost Debit Account | many2one → `account.account` | Overhead cost debit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_default_form_view_for_work_center_costing_inherit` |
| `sequence` | Sequence | integer | Integer sort order for Work Center Costing records (default set by an ir.default), used to order them in lists. Shown in the list view. | stored |  | `default BugFix-Studio-Misc.default_77_work_center_costing_sequence`<br>`view BugFix-Studio-Misc.view_work_center_costing_list` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Work Center Costing | `action_work_center_costing` | Opens **Work Center Costing** records (tree,form). | `model work_center_costing` | `menu BugFix-Studio-Misc.menu_work_center_costing` |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for work_center_costing | `view_work_center_costing_form` | form | full form layout with 5 fields | Default Studio form for Work Center Costing: required Name, archived ribbon and chatter. | `work_center_costing.activity_ids`<br>`work_center_costing.message_follower_ids`<br>`work_center_costing.message_ids`<br>`work_center_costing.active`<br>`work_center_costing.name` | `view BugFix-Studio-Misc.view_default_form_view_for_work_center_costing_inherit` |
| Default list view for work_center_costing | `view_work_center_costing_list` | tree | full tree layout with 2 fields | Default Studio list view for Work Center Costing: drag-handle Sequence and Name. | `work_center_costing.name`<br>`work_center_costing.sequence` | `view BugFix-Studio-Misc.view_default_list_view_for_work_center_costing_inherit` |
| Default search view for work_center_costing | `view_work_center_costing_search` | search | full search layout with 1 fields | Default Studio search view for Work Center Costing: search by Name plus an 'Archived' filter. | `work_center_costing.active`<br>`work_center_costing.name` |  |
| Odoo Studio: Default form view for work_center_costing customization | `view_default_form_view_for_work_center_costing_inherit` | form | remove `//group[@name='studio_group_f7d0e8_left']`; set create=false, delete=false on `//form[1]`; set force_save=True, readonly=1 on `//field[@name='name']`; set string=Labour Cost Details on `//group[@name='studio_group_f7d0e8_right']`; inside `//group[@name='studio_group_f7d0e8_right']`: add field labour_cost_debit_account, field labour_cost_credit_account, field labour_ot_cost_debit_account, field labour_ot_cost_credit_account; after `//group[@name='studio_group_f7d0e8']`: add group | Reworks the Work Center Costing form: no create/delete, Name read-only, and debit/credit account fields grouped as Labour Cost, Labour OT Cost, Overhead Cost and General Cost details (analytic tag fields commented out). | `view BugFix-Studio-Misc.view_work_center_costing_form`<br>`work_center_costing.general_cost_credit_account`<br>`work_center_costing.general_cost_debit_account`<br>`work_center_costing.labour_cost_credit_account`<br>`work_center_costing.labour_cost_debit_account`<details><summary>+4 more</summary>`work_center_costing.labour_ot_cost_credit_account`<br>`work_center_costing.labour_ot_cost_debit_account`<br>`work_center_costing.overhead_cost_credit_account`<br>`work_center_costing.overhead_cost_debit_account`</details> |  |
| Odoo Studio: Default list view for work_center_costing customization | `view_default_list_view_for_work_center_costing_inherit` | tree | set create=false, delete=false on `//tree[1]`; set column_invisible=1 on `//field[@name='sequence']` | Disables create and delete on the Work Center Costing list and hides the Sequence column. | `view BugFix-Studio-Misc.view_work_center_costing_list` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Work Center Costing group_system | `access_work_center_costing_group_system` | Gives **Administration / Settings** read/write/create/delete access to Work Center Costing records. | `group base.group_system` (base)<br>`model work_center_costing` |  |
| Work Center Costing group_user | `access_work_center_costing_group_user` | Gives **User types / Internal User** read access to Work Center Costing records. | `group base.group_user` (base)<br>`model work_center_costing` |  |
| work_center_costing admin | `access_work_center_costing_admin` | Gives **Administration / Settings** read/write/create/delete access to Work Center Costing records. | `group base.group_system` (base)<br>`model work_center_costing` |  |
