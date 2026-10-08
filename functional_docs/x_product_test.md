# BugFix-Studio-Misc — `x_product_test`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_product_test` — product.test

*Created by this repo.* Python: `models/x_product_test.py`, `models/x_product_test_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_product_test -->
A Studio test (sandbox) model labelled product.test, with test links to products, product templates, a journal entry and a stock move, plus a Journal Name text. It has a window action and Studio form and list customizations. Its TEST-TEST-TEST server action replaces a non-empty name with the next purchase.request.seq number, which uses up purchase request numbers. The action is not linked to any button, menu or automation.
<!-- /SUMMARY -->

**Fields (26):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_product_test.activity_summary`<br>`x_product_test.activity_type_icon`<br>`x_product_test.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_product_test.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_product_test.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_product_test.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of product.test records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_78_x_product_test_x_active`<br>`view BugFix-Studio-Misc.view_2587_default_form_view_for_x_product_test`<br>`view BugFix-Studio-Misc.view_2588_default_search_view_for_x_product_test` |
| `x_name` | Name | char | Name of a product.test sandbox record; shown in its list, form and search views and overwritten with a 'purchase.request.seq' number by the TEST-TEST-TEST server action. Part of a Studio test/sandbox model. | stored |  | `server action BugFix-Studio-Misc.server_action_1140_test_test_test`<br>`view BugFix-Studio-Misc.view_2586_default_list_view_for_x_product_test`<br>`view BugFix-Studio-Misc.view_2587_default_form_view_for_x_product_test`<br>`view BugFix-Studio-Misc.view_2588_default_search_view_for_x_product_test` |
| `x_studio_journal_name` | Journal Name | char | User-entered char value labelled 'Journal Name'. Shown in the list view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_2590_odoo_studio_default_list_view_for_x_product_test_customizati_ext` |
| `x_studio_many2many_field_R1u9s` | Product | many2many → `product.product` | Many2many link labelled 'Product' to `product.product` records, chosen by the user. Shown in the form view. Part of a Studio test/sandbox model. | stored | `model product.product` (product) | `view BugFix-Studio-Misc.view_2589_odoo_studio_default_form_view_for_x_product_test_customizati_ext` |
| `x_studio_many2one_field_cmfRx` | Product | many2one → `product.product` | Many2one link labelled 'Product' to `product.product` records, chosen by the user. Shown in the form and list views. Part of a Studio test/sandbox model. | stored | `model product.product` (product) | `view BugFix-Studio-Misc.view_2589_odoo_studio_default_form_view_for_x_product_test_customizati_ext`<br>`view BugFix-Studio-Misc.view_2590_odoo_studio_default_list_view_for_x_product_test_customizati_ext` |
| `x_studio_many2one_field_wTxgi` | Journal Entry | many2one → `account.move` | Many2one link labelled 'Journal Entry' to `account.move` records, chosen by the user. Shown in the list view. Part of a Studio test/sandbox model. | stored | `model account.move` (account) | `view BugFix-Studio-Misc.view_2590_odoo_studio_default_list_view_for_x_product_test_customizati_ext` |
| `x_studio_product_1` | Product_1 | many2one → `product.template` | Many2one link labelled 'Product_1' to `product.template` records, chosen by the user. Shown in the form and list views. Part of a Studio test/sandbox model. | stored | `model product.template` (product) | `view BugFix-Studio-Misc.view_2589_odoo_studio_default_form_view_for_x_product_test_customizati_ext`<br>`view BugFix-Studio-Misc.view_2590_odoo_studio_default_list_view_for_x_product_test_customizati_ext` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for product.test records (default set by an ir.default), used to order them in lists. Shown in the list view. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_79_x_product_test_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_2586_default_list_view_for_x_product_test` |
| `x_studio_stock_move` | Stock Move | many2one → `stock.move` | Many2one link labelled 'Stock Move' to `stock.move` records, chosen by the user. Shown in the list view. Part of a Studio test/sandbox model. | stored | `model stock.move` (stock) | `view BugFix-Studio-Misc.view_2590_odoo_studio_default_list_view_for_x_product_test_customizati_ext` |

**Server actions (1):**

- **TEST-TEST-TEST** (`server_action_1140_test_test_test`, type `code`)
  - Function: Test action on product.test: replaces a non-empty name with the next 'purchase.request.seq' number (consuming purchase request numbers). Sandbox only.
  - Depends on: `model ir.sequence` (base), `model x_product_test`, `x_product_test.x_name`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (6 lines)</summary>

```python

#record['x_name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.x_name:
 seq = env['ir.sequence'].next_by_code('purchase.request.seq')
 record.write({'x_name': seq})
```
  </details>
**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| product.test | `act_window_1139_product_test` | Opens **product.test** records (tree,form). | `model x_product_test` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_product_test` |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_product_test | `view_2587_default_form_view_for_x_product_test` | form | full form layout with 2 fields | Default Studio form for the test model x_product_test: required Name, archived ribbon driven by Active; chatter fields were stripped because the model has no mail support. | `x_product_test.x_active`<br>`x_product_test.x_name` | `view BugFix-Studio-Misc.view_2589_odoo_studio_default_form_view_for_x_product_test_customizati_ext` |
| Default list view for x_product_test | `view_2586_default_list_view_for_x_product_test` | tree | full tree layout with 2 fields | Default Studio list view for x_product_test: drag-handle Sequence and Name. | `x_product_test.x_name`<br>`x_product_test.x_studio_sequence` | `view BugFix-Studio-Misc.view_2590_odoo_studio_default_list_view_for_x_product_test_customizati_ext` |
| Default search view for x_product_test | `view_2588_default_search_view_for_x_product_test` | search | full search layout with 1 fields | Default Studio search view for x_product_test: search by Name plus an 'Archived' filter. | `x_product_test.x_active`<br>`x_product_test.x_name` |  |
| Odoo Studio: Default form view for x_product_test customization | `view_2589_odoo_studio_default_form_view_for_x_product_test_customizati_ext` | form | set required= on `//field[@name='x_name']`; inside `//group[@name='studio_group_2ae04f_left']`: add field x_studio_many2one_field_cmfRx, field x_studio_product_1; inside `//group[@name='studio_group_2ae04f_right']`: add field x_studio_many2many_field_R1u9s | Extends the x_product_test form: clears the required flag on Name and adds a Many2one field, 'Product_1' and a many2many tags field. | `view BugFix-Studio-Misc.view_2587_default_form_view_for_x_product_test`<br>`x_product_test.x_studio_many2many_field_R1u9s`<br>`x_product_test.x_studio_many2one_field_cmfRx`<br>`x_product_test.x_studio_product_1` |  |
| Odoo Studio: Default list view for x_product_test customization | `view_2590_odoo_studio_default_list_view_for_x_product_test_customizati_ext` | tree | after `//field[@name='x_name']`: add field x_studio_many2one_field_wTxgi, field x_studio_journal_name, field x_studio_stock_move, field x_studio_many2one_field_cmfRx, field x_studio_product_1 | Extends the x_product_test list: adds a Many2one field, Journal Name, Stock Move, another Many2one and Product_1 columns after Name. | `view BugFix-Studio-Misc.view_2586_default_list_view_for_x_product_test`<br>`x_product_test.x_studio_journal_name`<br>`x_product_test.x_studio_many2one_field_cmfRx`<br>`x_product_test.x_studio_many2one_field_wTxgi`<br>`x_product_test.x_studio_product_1`<details><summary>+1 more</summary>`x_product_test.x_studio_stock_move`</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| product.test group_system | `access_1212_product_test_group_system` | Gives **Administration / Settings** read/write/create/delete access to product.test records. | `group base.group_system` (base)<br>`model x_product_test` |  |
| product.test group_user | `access_1213_product_test_group_user` | Gives **User types / Internal User** read/write access to product.test records. | `group base.group_user` (base)<br>`model x_product_test` |  |
| x_product_test admin | `access_x_product_test_admin` | Gives **Administration / Settings** read/write/create/delete access to product.test records. | `group base.group_system` (base)<br>`model x_product_test` |  |
