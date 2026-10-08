# BugFix-Studio-Misc — `x_work_center_costing`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_work_center_costing` — Work Center Costing

*Created by this repo.* Python: `models/x_work_center_costing.py`, `models/x_work_center_costing_gap.py`. Record name field: `x_name`.

Other repos that use this model: `server action BugFix-Accounting.server_action_1519_sls_payment_reconciliation_automate` (BugFix-Accounting)<br>`server action BugFix-Stock.server_action_1138_work_center_costing_model_create_journal_entries` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_2566_work_center_costing_model_create_journal_entries_original` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:x_work_center_costing -->
A Work Center Costing setup record. For general, labour, labour overtime and overhead costs, it stores debit and credit accounts plus analytic accounts. Its customized form and list do not allow creating or deleting records. Internal users can read it and administrators have full access. No logic in this repo reads these accounts.
<!-- /SUMMARY -->

**Fields (44):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Studio-Misc.view_2581_default_form_view_for_x_work_center_costing_e`<br>`x_work_center_costing.activity_summary`<br>`x_work_center_costing.activity_type_icon`<br>`x_work_center_costing.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_work_center_costing.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_work_center_costing.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_work_center_costing.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Studio-Misc.view_2581_default_form_view_for_x_work_center_costing_e` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Studio-Misc.view_2581_default_form_view_for_x_work_center_costing_e` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of Work Center Costing records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. | stored |  | `default BugFix-Studio-Misc.default_76_x_work_center_costing_x_active`<br>`view BugFix-Studio-Misc.view_2581_default_form_view_for_x_work_center_costing_e`<br>`view BugFix-Studio-Misc.view_2582_default_search_view_for_x_work_center_costing_e` |
| `x_name` | Name | char | Name of a Work Center Costing setup record, entered by the user; shown in its default list, form and search views. | stored |  | `view BugFix-Studio-Misc.view_2580_default_list_view_for_x_work_center_costing_e`<br>`view BugFix-Studio-Misc.view_2581_default_form_view_for_x_work_center_costing_e`<br>`view BugFix-Studio-Misc.view_2582_default_search_view_for_x_work_center_costing_e` |
| `x_studio_general_analytic_tag` | General Analytic Tag | many2one → `account.analytic.account` | General analytic account (labelled 'Analytic Tag') for a Work Center Costing setup record; not shown on any view or used by logic in this repo. | stored | `model account.analytic.account` (analytic) |  |
| `x_studio_general_cost_credit_account` | General Cost Credit Account | many2one → `account.account` | General cost credit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_final_x_work_center_costing_odoo_studio_default_form_view_for_x_work_center_costing_c` |
| `x_studio_general_cost_debit_account` | General Cost Debit Account | many2one → `account.account` | General cost debit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_final_x_work_center_costing_odoo_studio_default_form_view_for_x_work_center_costing_c` |
| `x_studio_labour_analytic_tag` | Labour Analytic Tag | many2one → `account.analytic.account` | Labour analytic account (labelled 'Analytic Tag') for a Work Center Costing setup record; not shown on any view or used by logic in this repo. | stored | `model account.analytic.account` (analytic) |  |
| `x_studio_labour_cost_credit_account` | Labour Cost Credit Account | many2one → `account.account` | Labour cost credit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_final_x_work_center_costing_odoo_studio_default_form_view_for_x_work_center_costing_c` |
| `x_studio_labour_cost_debit_account` | Labour Cost Debit Account | many2one → `account.account` | Labour cost debit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_final_x_work_center_costing_odoo_studio_default_form_view_for_x_work_center_costing_c` |
| `x_studio_labour_ot_cost_credit_account` | Labour OT Cost Credit Account | many2one → `account.account` | Labour overtime cost credit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_final_x_work_center_costing_odoo_studio_default_form_view_for_x_work_center_costing_c` |
| `x_studio_labour_ot_cost_debit_account` | Labour OT Cost Debit Account | many2one → `account.account` | Labour overtime cost debit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_final_x_work_center_costing_odoo_studio_default_form_view_for_x_work_center_costing_c` |
| `x_studio_overhead_analytic_tag` | Overhead Analytic Tag | many2one → `account.analytic.account` | Overhead analytic account (labelled 'Analytic Tag') for a Work Center Costing setup record; not shown on any view or used by logic in this repo. | stored | `model account.analytic.account` (analytic) |  |
| `x_studio_overhead_cost_credit_account` | Overhead Cost Credit Account | many2one → `account.account` | Overhead cost credit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_final_x_work_center_costing_odoo_studio_default_form_view_for_x_work_center_costing_c` |
| `x_studio_overhead_cost_debit_account` | Overhead Cost Debit Account | many2one → `account.account` | Overhead cost debit account configured on a Work Center Costing setup record, chosen on its Studio form. No logic in this repo reads it. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_final_x_work_center_costing_odoo_studio_default_form_view_for_x_work_center_costing_c` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for Work Center Costing records (default set by an ir.default), used to order them in lists. Shown in the list view. | stored |  | `default BugFix-Studio-Misc.default_77_x_work_center_costing_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_2580_default_list_view_for_x_work_center_costing_e` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Work Center Costing | `act_window_1134_work_center_costing` | Opens **Work Center Costing** records (tree,form). | `model x_work_center_costing` | `menu BugFix-Studio-Misc.menu_f6_work_center_costing` |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_work_center_costing | `view_2581_default_form_view_for_x_work_center_costing_e` | form | full form layout with 5 fields | Default Studio form for Work Center Costing: required Name, archived ribbon and chatter. | `x_work_center_costing.activity_ids`<br>`x_work_center_costing.message_follower_ids`<br>`x_work_center_costing.message_ids`<br>`x_work_center_costing.x_active`<br>`x_work_center_costing.x_name` | `view BugFix-Studio-Misc.view_final_x_work_center_costing_odoo_studio_default_form_view_for_x_work_center_costing_c` |
| Default list view for x_work_center_costing | `view_2580_default_list_view_for_x_work_center_costing_e` | tree | full tree layout with 2 fields | Default Studio list view for Work Center Costing: drag-handle Sequence and Name. | `x_work_center_costing.x_name`<br>`x_work_center_costing.x_studio_sequence` | `view BugFix-Studio-Misc.view_final_x_work_center_costing_odoo_studio_default_list_view_for_x_work_center_costing_c` |
| Default search view for x_work_center_costing | `view_2582_default_search_view_for_x_work_center_costing_e` | search | full search layout with 1 fields | Default Studio search view for Work Center Costing: search by Name plus an 'Archived' filter. | `x_work_center_costing.x_active`<br>`x_work_center_costing.x_name` |  |
| Odoo Studio: Default form view for x_work_center_costing customization | `view_final_x_work_center_costing_odoo_studio_default_form_view_for_x_work_center_costing_c` | form | remove `//group[@name='studio_group_f7d0e8_left']`; set create=false, delete=false on `//form[1]`; set force_save=True, readonly=1 on `//field[@name='x_name']`; set string=Labour Cost Details on `//group[@name='studio_group_f7d0e8_right']`; inside `//group[@name='studio_group_f7d0e8_right']`: add field x_studio_labour_cost_debit_account, field x_studio_labour_cost_credit_account, field x_studio_labour_ot_cost_debit_account, field x_studio_labour_ot_cost_credit_account; after `//group[@name='studio_group_f7d0e8']`: add group | Reworks the Work Center Costing form: no create/delete, Name read-only, and debit/credit account fields grouped as Labour Cost, Labour OT Cost, Overhead Cost and General Cost details (analytic tag fields commented out). | `view BugFix-Studio-Misc.view_2581_default_form_view_for_x_work_center_costing_e`<br>`x_work_center_costing.x_studio_general_cost_credit_account`<br>`x_work_center_costing.x_studio_general_cost_debit_account`<br>`x_work_center_costing.x_studio_labour_cost_credit_account`<br>`x_work_center_costing.x_studio_labour_cost_debit_account`<details><summary>+4 more</summary>`x_work_center_costing.x_studio_labour_ot_cost_credit_account`<br>`x_work_center_costing.x_studio_labour_ot_cost_debit_account`<br>`x_work_center_costing.x_studio_overhead_cost_credit_account`<br>`x_work_center_costing.x_studio_overhead_cost_debit_account`</details> |  |
| Odoo Studio: Default list view for x_work_center_costing customization | `view_final_x_work_center_costing_odoo_studio_default_list_view_for_x_work_center_costing_c` | tree | set create=false, delete=false on `//tree[1]`; set column_invisible=1 on `//field[@name='x_studio_sequence']` | Disables create and delete on the Work Center Costing list and hides the Sequence column. | `view BugFix-Studio-Misc.view_2580_default_list_view_for_x_work_center_costing_e` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Work Center Costing group_system | `access_1210_work_center_costing_group_system` | Gives **Administration / Settings** read/write/create/delete access to Work Center Costing records. | `group base.group_system` (base)<br>`model x_work_center_costing` |  |
| Work Center Costing group_user | `access_1211_work_center_costing_group_user` | Gives **User types / Internal User** read access to Work Center Costing records. | `group base.group_user` (base)<br>`model x_work_center_costing` |  |
| x_work_center_costing admin | `access_x_work_center_costing_admin` | Gives **Administration / Settings** read/write/create/delete access to Work Center Costing records. | `group base.group_system` (base)<br>`model x_work_center_costing` |  |
