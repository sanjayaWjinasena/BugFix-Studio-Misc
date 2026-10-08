# BugFix-Studio-Misc — `x_test02`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_test02` — TEST02

*Created by this repo.* Python: `models/x_test02.py`, `models/x_test02_gap.py`. Record name field: `x_name`.

Other repos that use this model: `server action BugFix-Stock.sa_f5_stock_picking_user_location_validation_test` (BugFix-Stock)<br>`server action BugFix-Stock.server_action_2489_user_location_validation_test` (BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:x_test02 -->
TEST02 is a Studio sandbox model for trying out fields, layouts, approvals and automated actions. It has many test fields (statuses, numbers, charges links, Test Layout lines) and 17 server actions. Two automations are attached: the CHK sample automation, and the archived Test - Layout Changes. Three test approval rules gate the sample server actions. Some of its server actions are dangerous data clean-up scripts (MST - ODOO Data Clean-up 001, 002 and 004, and the multi-company and stock.quant fixes), which can delete purchase requests or BoMs or reassign companies in bulk if run.
<!-- /SUMMARY -->

**Fields (52):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_test02.activity_summary`<br>`x_test02.activity_type_icon`<br>`x_test02.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_test02.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_test02.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_test02.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag of TEST02 records (defaults to active via an ir.default); unticking archives the record and hides it from default searches. Shown in the form and search views. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_31_x_test02_x_active`<br>`view BugFix-Studio-Misc.view_2414_default_form_view_for_x_test02`<br>`view BugFix-Studio-Misc.view_2415_default_search_view_for_x_test02` |
| `x_currency_id` | Currency | many2one → `res.currency` | Currency of a TEST02 record (default set by an ir.default), used for its monetary test fields; shown on the Studio form. Sandbox model. | stored | `model res.currency` (base) | `default BugFix-Studio-Misc.default_578_x_test02_x_currency_id`<br>`view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_name` | Name | char | Name of a TEST02 sandbox record; shown in its list, form, search and kanban views. The 'User Location Validation-TEST' action in BugFix-Stock writes transfer source locations into it. Part of a Studio test/sandbox model. | stored |  | `server action BugFix-Studio-Misc.server_action_2268_sample_server_action_2`<br>`view BugFix-Studio-Misc.view_2413_default_list_view_for_x_test02`<br>`view BugFix-Studio-Misc.view_2414_default_form_view_for_x_test02`<br>`view BugFix-Studio-Misc.view_2415_default_search_view_for_x_test02`<br>`view BugFix-Studio-Misc.view_2955_default_kanban_view_for_ir_model_782` |
| `x_studio_charges_1` | Charges-1 | many2many → `x_trf_charges` | Many2many test link from TEST02 to TRF charges (`x_trf_charges`), shown on the Studio form; used in sample server action experiments. Sandbox model. | stored | `model x_trf_charges` (BugFix-Purchase) | `server action BugFix-Studio-Misc.server_action_1743_sample_server_action`<br>`server action BugFix-Studio-Misc.server_action_2268_sample_server_action_2`<br>`view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_charges_2` | Charges-2 | many2many → `x_trf_charges` | Many2many test link from TEST02 to TRF charges (`x_trf_charges`), shown on the Studio form; used in sample server action-2 experiments. Sandbox model. | stored | `model x_trf_charges` (BugFix-Purchase) | `server action BugFix-Studio-Misc.server_action_2268_sample_server_action_2`<br>`view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_chk_atomated_action` | CHK Atomated Action | integer | Test integer (default via ir.default) set by the CHK Sample Automated Action to Test Value + Testing02 + 100; shown on the TEST02 Studio form. Sandbox model used to time automated actions. | stored |  | `default BugFix-Studio-Misc.default_575_x_test02_x_studio_chk_atomated_action`<br>`server action BugFix-Studio-Misc.sa_f5_x_test02_chk_sample_automated_action`<br>`server action BugFix-Studio-Misc.server_action_2798_chk_sample_automated_action`<br>`view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_chk_server_action` | CHK Server Action | integer | Test integer (default via ir.default) set by the CHK Sample Server Action to Test Value + Testing02; shown on the TEST02 Studio form. Sandbox model. | stored |  | `default BugFix-Studio-Misc.default_576_x_test02_x_studio_chk_server_action`<br>`server action BugFix-Studio-Misc.server_action_2797_chk_sample_server_action`<br>`view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_company_id` | Company | many2one → `res.company` | Many2one link labelled 'Company' to `res.company` records, chosen by the user. Shown in the form view. Part of a Studio test/sandbox model. | stored | `model res.company` (base) | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_date` | Date | datetime | Test date-time on a TEST02 record, entered by the user; read by sample server action 1 (shows its difference from now). Shown on the Studio form. Sandbox model. | stored |  | `server action BugFix-Studio-Misc.server_action_1743_sample_server_action`<br>`server action BugFix-Studio-Misc.server_action_2223_sample_server_action_1`<br>`view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_float_field_skhh9` | Test Number | float | User-entered float value labelled 'Test Number'. Not used by any view or logic in this repo. Part of a Studio test/sandbox model. | stored |  |  |
| `x_studio_jam` | New Text | char | User-entered char value labelled 'New Text'. Not used by any view or logic in this repo. Part of a Studio test/sandbox model. | stored |  |  |
| `x_studio_jam_1` | JAM | char | User-entered char value labelled 'JAM'. Shown in the form view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_jin` | JIN | char | User-entered char value labelled 'JIN'. Not used by any view or logic in this repo. Part of a Studio test/sandbox model. | stored |  |  |
| `x_studio_jin_2` | JIN | char | User-entered char value labelled 'JIN'. Shown in the form view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_many2many_field_JKvVx` | Misc Charge Codes | many2many → `x_misc_charge_codes` | Many2many link labelled 'Misc Charge Codes' to `x_misc_charge_codes` records, chosen by the user. Not used by any view or logic in this repo. Part of a Studio test/sandbox model. | stored | `model x_misc_charge_codes` (BugFix-Stock) |  |
| `x_studio_many2many_field_c0IAp` | Charges | many2many → `x_trf_charges` | Many2many link labelled 'Charges' to `x_trf_charges` records, chosen by the user. Shown in the form view. Part of a Studio test/sandbox model. | stored | `model x_trf_charges` (BugFix-Purchase) | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_name_1` | Name-1 | char | Second name text on TEST02; the 'User Location Validation-TEST' action (BugFix-Stock) writes a transfer's destination location into it. Shown in the Studio list view. Sandbox model. | stored |  | `view BugFix-Studio-Misc.view_5420_odoo_studio_default_list_view_for_x_test02_customization_ext` |
| `x_studio_one2many_field_51FSD` | New One2many | one2many → `x_test_layout` | One2many list 'New One2many' of `x_test_layout` records belonging to this record. Shown in the form view. Part of a Studio test/sandbox model. | stored | `model x_test_layout` | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_one2many_field_D3cuD` | New One2many | one2many → `x_test_layout` | One2many list 'New One2many' of `x_test_layout` records belonging to this record. Not used by any view or logic in this repo. Part of a Studio test/sandbox model. | stored | `model x_test_layout` |  |
| `x_studio_one2many_field_Q8Xws` | New One2many | one2many → `x_test_layout` | One2many list 'New One2many' of `x_test_layout` records belonging to this record. Shown in the form view. Part of a Studio test/sandbox model. | stored | `model x_test_layout` | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_pipeline_status_bar` | Pipeline status bar | selection: status1=First Status; status2=Second Status; status3=Third Status; Fourth Status=Fourth Status | Pipeline status of a TEST02 record (First/Second/Third/Fourth Status), default set by an ir.default; set to Second Status by the Update Status action. Sandbox model. | stored |  | `default BugFix-Studio-Misc.default_243_x_test02_x_studio_pipeline_status_bar`<br>`server action BugFix-Studio-Misc.server_action_1575_update_status` |
| `x_studio_sequence` | Sequence | integer | Integer sort order for TEST02 records (default set by an ir.default), used to order them in lists. Shown in the list view. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_32_x_test02_x_studio_sequence`<br>`view BugFix-Studio-Misc.view_2413_default_list_view_for_x_test02` |
| `x_studio_status` | Status | selection: S1=S1; S2=S2; S3=S3 | Test status selection (S1/S2/S3) on TEST02, shown on its forms; referenced by the MST data clean-up scripts. Sandbox model. | stored |  | `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up`<br>`server action BugFix-Studio-Misc.server_action_2831_mst_odoo_data_clean_up_001`<br>`server action BugFix-Studio-Misc.server_action_2883_mst_odoo_data_clean_up_004`<br>`view BugFix-Studio-Misc.view_2414_default_form_view_for_x_test02`<br>`view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_status2` | Status2 | selection: S5=S5; S6=S6 | User-entered selection value labelled 'Status2'. Shown in the form view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_status_1` | Status | selection: Status 01=Status 01; Status 02=Status 02 | Test status selection (Status 01/Status 02) on TEST02, shown on the Studio form; the Test - Layout Changes action raises 'Found1' or 'Found2' depending on it. Sandbox model. | stored |  | `server action BugFix-Studio-Misc.sa_f5_x_test02_test_layout_changes`<br>`server action BugFix-Studio-Misc.server_action_2108_test_layout_changes`<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up`<br>`server action BugFix-Studio-Misc.server_action_2883_mst_odoo_data_clean_up_004`<br>`view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_test_03` | Test 03 | monetary | Test monetary amount on TEST02 (in the record's Currency), shown on the Studio form. Sandbox model. | stored |  | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_test_char` | Test Char | char | Test text on TEST02 shown on the Studio form; referenced only by sample server action-2 experiments. Sandbox model. | stored |  | `server action BugFix-Studio-Misc.server_action_2268_sample_server_action_2`<br>`view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_test_number_1` | Test Number | float | User-entered float value labelled 'Test Number'. Shown in the form view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_test_number_2` | Test Number 2 | float | User-entered float value labelled 'Test Number 2'. Shown in the form view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_test_value` | Test Value | integer | Test integer on TEST02 (default via ir.default), shown on the Studio form; summed by the CHK sample server/automated actions. Sandbox model. | stored |  | `default BugFix-Studio-Misc.default_472_x_test02_x_studio_test_value`<br>`server action BugFix-Studio-Misc.sa_f5_x_test02_chk_sample_automated_action`<br>`server action BugFix-Studio-Misc.server_action_2797_chk_sample_server_action`<br>`server action BugFix-Studio-Misc.server_action_2798_chk_sample_automated_action`<br>`view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_testing` | Testing | text | User-entered text value labelled 'Testing' (default set by an ir.default). Shown in the form view. Part of a Studio test/sandbox model. | stored |  | `default BugFix-Studio-Misc.default_476_x_test02_x_studio_testing`<br>`view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_testing_02` | Testing02 | float | Test float on TEST02 (default via ir.default), shown on the Studio form; summed by the CHK sample server/automated actions. Sandbox model. | stored |  | `default BugFix-Studio-Misc.default_490_x_test02_x_studio_testing_02`<br>`server action BugFix-Studio-Misc.sa_f5_x_test02_chk_sample_automated_action`<br>`server action BugFix-Studio-Misc.server_action_2797_chk_sample_server_action`<br>`server action BugFix-Studio-Misc.server_action_2798_chk_sample_automated_action`<br>`view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_text_field_eKlfk` | X Studio Text Field Eklfk | text | User-entered text value labelled 'X Studio Text Field Eklfk'. Shown in the form view. Part of a Studio test/sandbox model. | stored |  | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_studio_types` | Types | many2one → `helpdesk.ticket.type` | Many2one link labelled 'Types' to `helpdesk.ticket.type` records, chosen by the user. Shown in the form view. Part of a Studio test/sandbox model. | stored | `model helpdesk.ticket.type` (helpdesk) | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` |
| `x_test123` | test123 | float | Test float on TEST02 with a default set by an ir.default; not shown on any view. Sandbox model. | stored |  | `default BugFix-Studio-Misc.default_533_x_test02_x_test123` |

**Server actions (17):**

- **CHK - Sample Automated Action** (`sa_f5_x_test02_chk_sample_automated_action`, type `code`)
  - Function: Test action on TEST02: logs a timestamp and sets CHK Automated Action to Test Value + Testing02 + 100. Used to time automated actions; sandbox only.
  - Depends on: `model x_test02`, `x_test02.x_studio_chk_atomated_action`, `x_test02.x_studio_test_value`, `x_test02.x_studio_testing_02`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (15 lines)</summary>

```python

_logger.info("JLD Automated Action Start Time: %s", datetime.datetime.now())
#record.message_post(body="JLD Automated Action Start Time: %s" % datetime.datetime.now())
#record['x_start_time'] = datetime.datetime.now()


#start_time = datetime.datetime.now()
record.write({'x_studio_chk_atomated_action': record.x_studio_test_value + record.x_studio_testing_02 + 100})
#end_time = datetime.datetime.now()


_logger.info("JLD Automated Action Start Time: %s", datetime.datetime.now())
#record.message_post(body="JLD Automated Action End Time: %s" % datetime.datetime.now())
#record['x_endt_time'] = datetime.datetime.now()
#raise UserError("Automated Action Start Time: %s, End Time: %s" % (start_time, end_time))
```
  </details>
- **CHK - Sample Server Action** (`server_action_2797_chk_sample_server_action`, type `code`)
  - Function: Test action on TEST02 that sets CHK Server Action to Test Value + Testing02. Sandbox only.
  - Depends on: `model x_test02`, `x_test02.x_studio_chk_server_action`, `x_test02.x_studio_test_value`, `x_test02.x_studio_testing_02`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python

record.write({'x_studio_chk_server_action': record.x_studio_test_value + record.x_studio_testing_02})
```
  </details>
- **Execute Code** (`server_action_2798_chk_sample_automated_action`, type `code`)
  - Function: Run by the CHK Sample Automated Action automation on TEST02: logs timestamps and sets CHK Automated Action to Test Value + Testing02 + 100. Sandbox only.
  - Depends on: `model x_test02`, `x_test02.x_studio_chk_atomated_action`, `x_test02.x_studio_test_value`, `x_test02.x_studio_testing_02`
  - Used by: `automation BugFix-Studio-Misc.base_automation_332_chk_sample_automated_action`
  <details><summary>code (16 lines)</summary>

```python


_logger.info("JLD Automated Action Start Time: %s", datetime.datetime.now())
#record.message_post(body="JLD Automated Action Start Time: %s" % datetime.datetime.now())
#record['x_start_time'] = datetime.datetime.now()


#start_time = datetime.datetime.now()
record.write({'x_studio_chk_atomated_action': record.x_studio_test_value + record.x_studio_testing_02 + 100})
#end_time = datetime.datetime.now()


_logger.info("JLD Automated Action Start Time: %s", datetime.datetime.now())
#record.message_post(body="JLD Automated Action End Time: %s" % datetime.datetime.now())
#record['x_endt_time'] = datetime.datetime.now()
#raise UserError("Automated Action Start Time: %s, End Time: %s" % (start_time, end_time))
```
  </details>
- **Execute Code** (`server_action_2108_test_layout_changes`, type `code`)
  - Function: Run by the Test - Layout Changes automation on TEST02: always raises 'Found1' or 'Found2' depending on Status. Sandbox only.
  - Depends on: `model x_test02`, `x_test02.x_studio_status_1`
  - Used by: `automation BugFix-Studio-Misc.base_automation_183_test_layout_changes`
  <details><summary>code (9 lines)</summary>

```python

if record.id:
  if record.x_studio_status_1 == 'Status 02':
    #record.blocked  = False
    #record.readonly  = True 
    raise UserError("Found2")
  else:
    #record.blocked  = True
    raise UserError("Found1")
```
  </details>
- **MST - ODOO Data Clean-up** (`server_action_2799_mst_odoo_data_clean_up`, type `code`)
  - Function: Data clean-up script run from TEST02 (very long, mostly commented-out) for resetting and deleting transactional records such as purchase requests and consignments. Dangerous one-off maintenance tool.
  - Depends on: `model account.bank.statement` (account), `model account.move.line` (account), `model account.move` (account), `model helpdesk.ticket` (helpdesk), `model hr.attendance.overtime` (hr_attendance)<details><summary>+70 more</summary>`model mrp.production` (mrp), `model planning.slot` (planning), `model pos.config` (point_of_sale), `model pos.order` (point_of_sale), `model pos.payment` (point_of_sale), `model pos.session` (point_of_sale), `model project.milestone` (project), `model project.project` (project), `model project.sale.line.employee.map` (sale_timesheet), `model project.task` (project), `model project.update` (project), `model repair.order` (repair), `model stock.landed.cost` (stock_landed_costs), `model x_con_consolidated_hea` (BugFix-Stock), `model x_con_consolidated_lin` (BugFix-Stock), `model x_consignment_charge_h` (BugFix-Stock), `model x_consignment_charge_l` (BugFix-Stock), `model x_consignment_header` (BugFix-Stock), `model x_consignment_line` (BugFix-Stock), `model x_import_rfq_charge_he` (BugFix-Purchase), `model x_import_rfq_charge_li` (BugFix-Purchase), `model x_lc_header` (BugFix-Accounting), `model x_mass_produce_serial_` (BugFix-MRP), `model x_mass_produce_serial` (BugFix-MRP), `model x_material_request` (BugFix-Stock), `model x_mr_config` (BugFix-Stock), `model x_mrp_bom_general_cost` (BugFix-MRP), `model x_mrp_bom_labour_cost` (BugFix-MRP), `model x_mrp_bom_material_cos` (BugFix-MRP), `model x_mrp_bom_overhead_cos` (BugFix-MRP), `model x_po_line_non_inventor` (BugFix-Purchase), `model x_po_non_inventory` (BugFix-Purchase), `model x_pr_line_cash` (BugFix-Purchase), `model x_pr_non_inventory` (BugFix-Purchase), `model x_pump_price_costing` (BugFix-Accounting), `model x_purchase_request_cas` (BugFix-Purchase), `model x_purchase_request_lin` (BugFix-Purchase), `model x_purchase_request` (BugFix-Purchase), `model x_rm_cust_invoice_s1` (BugFix-Accounting), `model x_rm_customer_wise_inv` (BugFix-Accounting), `model x_rm_daily_s1` (BugFix-Accounting), `model x_rm_daily_s2` (BugFix-Accounting), `model x_rm_daily_s3` (BugFix-Accounting), `model x_rm_daily_sales_repor` (BugFix-Accounting), `model x_rm_gross_margin_actu` (BugFix-Accounting), `model x_rm_gross_margin_comp` (BugFix-Accounting), `model x_rm_gross_margin_esti_line_7e86d` (BugFix-Accounting), `model x_rm_gross_margin_esti` (BugFix-Accounting), `model x_rm_gross_margin_invo` (BugFix-Accounting), `model x_rm_none_moving` (BugFix-Accounting), `model x_rm_prod_summary_spli` (BugFix-Accounting), `model x_rm_production_orders` (BugFix-Accounting), `model x_rm_production_varian` (BugFix-Accounting), `model x_rm_sales_order_line` (BugFix-Accounting), `model x_rm_sales_prod_purch` (BugFix-Accounting), `model x_sales_model_debug`, `model x_sales_report_model` (Jinasena_Masterdata_Reporting), `model x_task_diagnosis` (Fix-repair), `model x_temp_estimated` (BugFix-Accounting), `model x_temp_tp_invoice_head` (BugFix-Accounting), `model x_temp_tp_invoice_line` (BugFix-Accounting), `model x_test02`, `model x_test_layout`, `model x_test_model_link_2`, `model x_test_model_link`, `model x_test_model_primary`, `model x_tp_invoice_header` (BugFix-Accounting), `model x_tp_invoice_line` (BugFix-Accounting), `x_test02.x_studio_status_1`, `x_test02.x_studio_status`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (638 lines)</summary>

```python

#charge_lines = env['pos.config'].search([])

#charge_lines = env['pos.order'].search([])

#charge_lines = env['pos.payment'].search([])

#charge_lines = env['pos.session'].search([])

#charge_lines = env['account.move.line'].search([])

#charge_lines = env['account.move'].search([])

#charge_lines = env['mrp.production'].search([])



#charge_lines_1 = env['x_purchase_request'].search([])

#for loop_lines in charge_lines_1:

#  loop_lines.write({'x_studio_status':'Draft'})

#  loop_lines.unlink()

  

#charge_lines_2 = env['x_purchase_request_lin'].search([])

#for loop_lines in charge_lines_2:

#  loop_lines.write({'x_studio_status_1':'Draft'})

#  loop_lines.unlink()

  

#charge_lines_3 = env['x_pr_non_inventory'].search([])  

#for loop_lines in charge_lines_3:

#  loop_lines.write({'x_studio_status':'Draft'})

#  loop_lines.unlink()

  

#charge_lines_4 = env['x_purchase_request_cas'].search([])

#for loop_lines in charge_lines_4:

#  loop_lines.write({'x_studio_status':'Draft'})

#  loop_lines.unlink()

  

#charge_lines_5 = env['x_pr_line_cash'].search([])

#for loop_lines in charge_lines_5:

#  loop_lines.write({'x_studio_status':'Draft'})

#  loop_lines.unlink()



#charge_lines_6 = env['x_consignment_line'].search([])

#for loop_lines in charge_lines_6:

#  loop_lines.write({'x_studio_status':'Draft'})

#  loop_lines.unlink()

  

#charge_lines_7 = env['x_consignment_header'].search([])

#for loop_lines in charge_lines_7:

#  loop_lines.write({'x_studio_status':'Draft'})

#  loop_lines.unlink()

  

#charge_lines_8 = env['x_consignment_charge_l'].search([])

#for loop_lines in charge_lines_8:

#  loop_lines.unlink()

  

#charge_lines_9 = env['x_consignment_charge_h'].search([])

#for loop_lines in charge_lines_9:

#  loop_lines.unlink()



#charge_lines_10 = env['x_import_rfq_charge_li'].search([])

#for loop_lines in charge_lines_10:

#  loop_lines.unlink()

  

#charge_lines_11 = env['x_import_rfq_charge_he'].search([])

#for loop_lines in charge_lines_11:

#  loop_lines.unlink()

  

#charge_lines_10 = env['x_import_rfq_charge_li'].search([])
# … 518 more lines
```
  </details>
- **MST - ODOO Data Clean-up - 001** (`server_action_2831_mst_odoo_data_clean_up_001`, type `code`)
  - Function: Data clean-up script run from TEST02 made up almost entirely of commented-out one-off fixes (journal deletion, company reassignment, BoM changes). Maintenance tool.
  - Depends on: `model account.move` (account), `model mail.activity` (mail), `model mrp.eco.bom.change` (mrp_plm), `model mrp.workcenter` (mrp), `model product.template` (product)<details><summary>+5 more</summary>`model res.users` (base), `model stock.rule` (stock), `model x_structure_master` (BugFix-Purchase), `model x_test02`, `x_test02.x_studio_status`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (96 lines)</summary>

```python

c = 0

#raise UserError('done')

#journals_to_delete = env['account.move'].search([('state', 'in', ['draft', 'posted'])])

#for journal in journals_to_delete:

#    journal_line_ids = journal.line_ids



#    journal_line_ids.unlink()

#    journal.unlink()

#    journal.line_ids.with_context(force_delete=True).unlink()

#    journal.with_context(force_delete=True).unlink()

    



# Get the user record

#user = env['res.users'].search([('id', '=', 33)])  # Replace user_id with the actual user's ID



# Set the related partner field to False (unlink it)

#user.write({'partner_id': False})





#item = env['product.template'].search([('company_id', '=', 2)])

#for items in item:

#  items.write({'categ_id': 1})

  #items.write({'company_id': 3})



#charge_lines_100 = env['mrp.eco.bom.change'].search([])

#for loop_lines in charge_lines_100:

#  #loop_lines.write({'state':'open'})

#  loop_lines.unlink()

 



#charge_lines_101 = env['stock.rule'].search(['warehouse_id', '=', 41])

#for loop_lines in charge_lines_101:

#  c += 1

#  #loop_lines.write({'state':'open'})

#  #loop_lines.unlink()

#raise UserError(str(c))



#workcentre = env['mrp.workcenter'].search([('company_id', '=', 3)])

#for lines in workcentre:

#  lines.write({'company_id': 1})



#sturcture = env['x_structure_master'].search([])

#for lines in sturcture:

#  lines.write({'x_studio_status': 'Draft', 'x_studio_selection_field_ba7aA': 'Draft'})



charge_lines_6 = env['mail.activity'].search([])

for loop_lines in charge_lines_6:

  loop_lines.unlink()
```
  </details>
- **MST - ODOO Data Clean-up - 002** (`server_action_2836_mst_odoo_data_clean_up_002`, type `code`)
  - Function: One-off clean-up: deletes all BoMs of product template id 334394, then raises an error showing the count (which rolls the deletion back). Maintenance tool.
  - Depends on: `model mrp.bom` (mrp), `model x_test02`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (18 lines)</summary>

```python

c=0



charge_lines_102 = env['mrp.bom'].search([('product_tmpl_id', '=', 334394)])

for loop_lines in charge_lines_102:

  c += 1

  #loop_lines.write({'state':'open'})

  loop_lines.unlink()

  #loop_lines.with_context(force_delete=True).unlink()

raise UserError(str(c))
```
  </details>
- **MST - ODOO Data Clean-up - 004** (`server_action_2883_mst_odoo_data_clean_up_004`, type `code`)
  - Function: Destructive clean-up: sets every Purchase Request and Purchase Request Line to Draft and deletes them all. Dangerous one-off maintenance tool.
  - Depends on: `model account.move.line` (account), `model account.move` (account), `model mrp.production` (mrp), `model pos.config` (point_of_sale), `model pos.order` (point_of_sale)<details><summary>+7 more</summary>`model pos.payment` (point_of_sale), `model pos.session` (point_of_sale), `model x_purchase_request_lin` (BugFix-Purchase), `model x_purchase_request` (BugFix-Purchase), `model x_test02`, `x_test02.x_studio_status_1`, `x_test02.x_studio_status`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (34 lines)</summary>

```python

#charge_lines = env['pos.config'].search([])

#charge_lines = env['pos.order'].search([])

#charge_lines = env['pos.payment'].search([])

#charge_lines = env['pos.session'].search([])

#charge_lines = env['account.move.line'].search([])

#charge_lines = env['account.move'].search([])

#charge_lines = env['mrp.production'].search([])



charge_lines_1 = env['x_purchase_request'].search([])

for loop_lines in charge_lines_1:

  loop_lines.write({'x_studio_status':'Draft'})

  loop_lines.unlink()

  

charge_lines_2 = env['x_purchase_request_lin'].search([])

for loop_lines in charge_lines_2:

  loop_lines.write({'x_studio_status_1':'Draft'})

  loop_lines.unlink()
```
  </details>
- **TEST SERVER ACTION** (`server_action_1630_test_server_action`, type `code`)
  - Function: Test action on TEST02 that only raises 'Error 123'. Sandbox/debug only.
  - Depends on: `model x_test02`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python

raise UserError('Error 123')
```
  </details>
- **Test - Layout Changes** (`sa_f5_x_test02_test_layout_changes`, type `code`)
  - Function: Test action on TEST02 that always raises an error, 'Found2' when Status is 'Status 02' otherwise 'Found1'. Sandbox/debug only.
  - Depends on: `model x_test02`, `x_test02.x_studio_status_1`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (8 lines)</summary>

```python
if record.id:
  if record.x_studio_status_1 == 'Status 02':
    #record.blocked  = False
    #record.readonly  = True 
    raise UserError("Found2")
  else:
    #record.blocked  = True
    raise UserError("Found1")
```
  </details>
- **Update Status** (`server_action_1575_update_status`, type `object_write`)
  - Function: Update-record action that sets the TEST02 Pipeline status bar to 'Second Status'. Sandbox only.
  - Depends on: `model x_test02`, `x_test02.x_studio_pipeline_status_bar`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **sample server action** (`server_action_1743_sample_server_action`, type `code`)
  - Function: Sandbox action on TEST02 that raises an error showing today's end-of-day timestamp; the rest is commented-out experiments. Linked from two test approval rules.
  - Depends on: `model product.template` (product), `model res.currency.rate` (base), `model res.currency` (base), `model sale.order` (sale), `model x_test02`<details><summary>+3 more</summary>`model x_trf_charges` (BugFix-Purchase), `x_test02.x_studio_charges_1`, `x_test02.x_studio_date`</details>
  - Used by: `approval rule BugFix-Studio-Misc.ar_final_test02_sample_server_action_technical_a_warning_can_be_set_o`, `approval rule BugFix-Studio-Misc.ar_final_test02_sample_server_action_user_types_internal_user_44`
  <details><summary>code (168 lines)</summary>

```python

c = 0

line_ids = []



target_date = datetime.date.today()

target_date = target_date.strftime('%Y-%m-%d')

date_start = f'{target_date} 00:00:00'

date_end = f'{target_date} 23:59:59'

raise UserError(date_end)

  

#stock.quant

#currentdate = datetime.datetime.today()

#currentdate = record.x_studio_date.date()

"""currentdate = datetime.date.today()

raise UserError(currentdate)





custom_currency = env['sale.order'].search([('name', '=', 'S00706')],limit=1)

if custom_currency:

  custom_currency.write({'x_studio_quotation_type':'Repair','x_studio_order_payment_method':custom_currency.partner_id.x_studio_payment_method})

"""

"""currentdate = datetime.datetime.today()

    

firstdayOfmonth = datetime.date(currentdate.year, currentdate.month, 1)

next_month = currentdate.replace(day=28) + datetime.timedelta(days=4)

lastdayOfmonth = next_month - datetime.timedelta(days=next_month.day)

    

if firstdayOfmonth.month != 1:

  firstdayOfmonth2 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-1, 1)

else:

  firstdayOfmonth2 = datetime.date(firstdayOfmonth.year-1, 12, 1)

  

next_month2 = firstdayOfmonth2.replace(day=28) + datetime.timedelta(days=4)

lastdayOfmonth2 = next_month2 - datetime.timedelta(days=next_month2.day)



if firstdayOfmonth.month > 2:

  firstdayOfmonth3 = datetime.date(firstdayOfmonth.year, firstdayOfmonth.month-2, 1)

else:

  if firstdayOfmonth.month == 2:

    firstdayOfmonth3 = datetime.date(firstdayOfmonth.year-1, 12, 1)

  else:

    firstdayOfmonth3 = datetime.date(firstdayOfmonth.year-1, 11, 1)

        

next_month3 = firstdayOfmonth3.replace(day=28) + datetime.timedelta(days=4)

lastdayOfmonth3 = next_month3 - datetime.timedelta(days=next_month3.day)

  

raise UserError(str(firstdayOfmonth3) + "   " + str(lastdayOfmonth3))"""



"""custom_currency = env['res.currency'].search([('id', '=', 2),('active', '=', True)],limit=1)

if custom_currency:

  custom_currency_rate = env['res.currency.rate'].search([('currency_id', '=', custom_currency.id),('name', '<=', datetime.datetime.today())],order='name desc',limit=1)

  if custom_currency_rate.inverse_company_rate != 0:

    raise UserError(str(custom_currency_rate.inverse_company_rate))"""







"""product = env['product.template'].search([('default_code', '=', '02BB 023')], limit=1)

if product:

  whs = ''

  for routes in product.route_ids:

    if routes.supplier_wh_id:
# … 48 more lines
```
  </details>
- **sample server action - 1** (`server_action_2223_sample_server_action_1`, type `code`)
  - Function: Sandbox action on TEST02 that raises an error showing the difference between the record's Date and now.
  - Depends on: `model x_test02`, `x_test02.x_studio_date`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (3 lines)</summary>

```python

if record.id:
  raise UserError(str(record.x_studio_date - datetime.datetime.now()))
```
  </details>
- **sample server action - multi company** (`server_action_2578_sample_server_action_multi_company`, type `code`)
  - Function: Sandbox action that sets company_id = 1 on ALL contacts in the database. Destructive one-off data fix; dangerous if run.
  - Depends on: `model res.partner` (base), `model x_test02`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (8 lines)</summary>

```python

partner = env['res.partner'].search([]) 

if partner:

  for partners in partner:

    partners.write({'company_id':1})
```
  </details>
- **sample server action - to get company id** (`server_action_2586_sample_server_action_to_get_company_id`, type `code`)
  - Function: Sandbox action that raises an error showing the active company name; the duplicate product-code check after it is unreachable.
  - Depends on: `model product.template` (product), `model res.company` (base), `model x_test02`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (13 lines)</summary>

```python

#raise UserError(user.company_id.name)

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

raise UserError(company.name)

product = env['product.template'].search([('default_code', '=ilike', record.default_code),('company_id', '=', company.id)], limit=1)
if product:
  for p in product:
   if p.id != record.id:
      raise UserError("Duplicate Found Try Another Code!")
```
  </details>
- **sample server action - update stock.quant** (`server_action_2599_sample_server_action_update_stock_quant`, type `code`)
  - Function: Sandbox one-off data fix: sets company_id = 1 on every stock quant that has no company. Dangerous if run.
  - Depends on: `model stock.quant` (stock), `model x_test02`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (8 lines)</summary>

```python

stock = env['stock.quant'].search([('company_id', '=', False)]) 

c= 0

for stocks in stock:

  stocks.write({'company_id':1})
```
  </details>
- **sample server action-2** (`server_action_2268_sample_server_action_2`, type `code`)
  - Function: Sandbox action on TEST02 containing mostly commented-out many2many write experiments with charges; linked from a test approval rule.
  - Depends on: `model sale.order.line` (sale), `model sale.order` (sale), `model stock.picking` (stock), `model x_test02`, `model x_trf_charges` (BugFix-Purchase)<details><summary>+4 more</summary>`x_test02.x_name`, `x_test02.x_studio_charges_1`, `x_test02.x_studio_charges_2`, `x_test02.x_studio_test_char`</details>
  - Used by: `approval rule BugFix-Studio-Misc.ar_final_test02_sample_server_action_2_sales_test_sales_2_76`
  <details><summary>code (134 lines)</summary>

```python

c = 0

line_ids = []

line_ids1 = []

line_ids2 = []



#line_ids = record.x_studio_many2many_field_c0IAp

#line_ids1 = record.x_studio_charges_1

#line_ids2 = line_ids + line_ids1

#line_ids2 = "TEST-1"

#line_ids2.append("TEST-1")

#new_val = "TEST-1"

#line_ids2.append([0,0,new_val])



#record.write({'x_studio_charges_2':[(6, 0, record.x_studio_many2many_field_c0IAp.id)]})

#record.write({'x_studio_charges_2':record.x_studio_many2many_field_c0IAp})

#record.write({'x_studio_charges_2':line_ids + line_ids1})

#record.write({'x_studio_charges_2':[(4, line_ids2, 0)]})

  

  



#charge_lines = env['x_trf_charges'].search([]) 

#if charge_lines:

#  for loop_lines in charge_lines:

    #line_ids = [(6, 0, [loop_lines.id])]

    #line_ids.append([0,0,loop_lines.id])

    #line_ids.append((0, 0, loop_lines.id))

    #line_ids.append(loop_lines.id)

    #record.write({'x_studio_many2many_field_c0IAp': [(6, 0, loop_lines.id)]})

    #record.write({'x_studio_many2many_field_c0IAp':[(6, 0, [loop_lines.id])]})

    #record.write({'x_studio_many2many_field_c0IAp': [(6, 0, loop_lines.id)]})

    #record.write({'x_studio_many2many_field_c0IAp':[(4, 0, [loop_lines.id])]})

    #record.write({'x_studio_many2many_field_c0IAp':[(4, [loop_lines.id])]})

    #[(4, new_value_id, 0)]



#line_ids = [19,20,21]

#line_ids = [19]

#record.write({'x_studio_many2many_field_c0IAp':[(6, 0, line_ids)]})

  #template.write({'attachment_ids':[(6, 0, [attachment.id])]})

  #record.write({'x_studio_many2many_field_c0IAp':line_ids})

  

  #raise UserError(line_ids)



#trf = env['x_trf_charges'].create({'x_name':"Test-1", 'x_studio_description':"Test-1"})

#line_ids.append(trf.id)

#record.write({'x_studio_many2many_field_c0IAp':[(6, 0, line_ids)]})



#for lins in record.x_studio_charges_1:

 #line_ids.append(lins.id)

 

#record.write({'x_studio_charges_2':[(6, 0, line_ids)]})



#free_items = env['sale.order.line'].search([('order_id', '=', 1395)])

#if free_items:

    #raise UserError(str(free_items.product_id.display_name))

  #for del_items in free_items:

    #del_items.unlink()

    #raise UserError(str(del_items.id))

    #line_ids.append(del_items.product_uom_qty)

  #record.write({'x_studio_test_char':line_ids})

expired_so = env['sale.order'].search([('id', '=', 1404)])
# … 14 more lines
```
  </details>
**Automations (2):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| CHK - Sample Automated Action | `base_automation_332_chk_sample_automated_action` |  | When a record is created or updated on TEST02, runs _Execute Code_. | `model x_test02`<br>`server action BugFix-Studio-Misc.server_action_2798_chk_sample_automated_action` |  |
| Test - Layout Changes | `base_automation_183_test_layout_changes` | archived | When a record is created or updated on TEST02, runs _Execute Code_. **Archived — does not run.** | `model x_test02`<br>`server action BugFix-Studio-Misc.server_action_2108_test_layout_changes` |  |

**Approval rules (3):**

| Name | Record name | Approver group | Function | Depends on | Used by |
|---|---|---|---|---|---|
| TEST02/sample server action (Technical / A warning can be set on a partner (Stock)) (45) | `ar_final_test02_sample_server_action_technical_a_warning_can_be_set_o` | Technical / A warning can be set on a partner (Stock) | Before action _sample server action_ on TEST02 runs, an approval from **Technical / A warning can be set on a partner (Stock)** is required (step 1). | `group stock.group_warning_stock` (stock)<br>`model x_test02`<br>`server action BugFix-Studio-Misc.server_action_1743_sample_server_action` |  |
| TEST02/sample server action (User types / Internal User) (44) | `ar_final_test02_sample_server_action_user_types_internal_user_44` | User types / Internal User | Before action _sample server action_ on TEST02 runs, an approval from **User types / Internal User** is required (step 1). | `group base.group_user` (base)<br>`model x_test02`<br>`server action BugFix-Studio-Misc.server_action_1743_sample_server_action` |  |
| TEST02/sample server action-2 (sales / TEST - SALES - 2) (76) | `ar_final_test02_sample_server_action_2_sales_test_sales_2_76` | TEST - SALES - 2 | Before action _sample server action-2_ on TEST02 runs, an approval from **TEST - SALES - 2** is required (step 1). | `group BugFix-Approvals.group_204_test_sales_2` (BugFix-Approvals)<br>`model x_test02`<br>`server action BugFix-Studio-Misc.server_action_2268_sample_server_action_2` |  |

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TEST02 | `act_window_848_test02` | Opens **TEST02** records (tree,form). | `model x_test02` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_test02` |
| TEST02 | `act_window_3279_test02` | Opens **TEST02** records (kanban,tree,form). | `model x_test02` |  |
| TEST02 | `act_window_846_test02` | Opens **TEST02** records (tree,form,kanban). | `model x_test02` |  |

**Views (8):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_test02 | `view_2414_default_form_view_for_x_test02` | form | full form layout with 3 fields | Default Studio form for the test model x_test02: required Name, archived ribbon, and a 'Move to Second' header button (hidden once Status is 'S2') that runs the action with id 1575; chatter fields stripped. | `window action sale_loyalty.sale_loyalty_coupon_wizard_action` (sale_loyalty)<br>`x_test02.x_active`<br>`x_test02.x_name`<br>`x_test02.x_studio_status` | `view BugFix-Studio-Misc.view_3267_odoo_studio_default_form_view_for_x_test02_customization_e`<br>`view BugFix-Studio-Misc.view_3919_test_inherited_view_e` |
| Default kanban view for ir.model(782,) | `view_2955_default_kanban_view_for_ir_model_782` | kanban | full kanban layout with 1 fields | Default Studio kanban view for x_test02 showing each record's Name on a card. | `x_test02.x_name` | `view BugFix-Studio-Misc.view_2956_odoo_studio_default_kanban_view_for_ir_model_782_customizati_ext` |
| Default list view for x_test02 | `view_2413_default_list_view_for_x_test02` | tree | full tree layout with 2 fields | Default Studio list view for x_test02: drag-handle Sequence and Name. | `x_test02.x_name`<br>`x_test02.x_studio_sequence` | `view BugFix-Studio-Misc.view_5420_odoo_studio_default_list_view_for_x_test02_customization_ext` |
| Default search view for x_test02 | `view_2415_default_search_view_for_x_test02` | search | full search layout with 1 fields | Default Studio search view for x_test02: search by Name plus an 'Archived' filter. | `x_test02.x_active`<br>`x_test02.x_name` |  |
| Odoo Studio: Default form view for x_test02 customization | `view_3267_odoo_studio_default_form_view_for_x_test02_customization_e` | form | replace `//div[@name='oe_chatter']`: add notebook; inside `//group[@name='studio_group_a1036a_left']`: add field x_studio_status_1, field x_studio_status, field x_studio_date, field x_studio_status2, field x_studio_test_number_1; inside `//group[@name='studio_group_a1036a_right']`: add field x_studio_types, field x_studio_many2many_field_c0IAp, field x_studio_charges_1, field x_studio_charges_2, field x_studio_test_char, field x_studio_test_value, field x_studio_testing, field x_studio_testing_02, field x_studio_jin_2, field x_studio_jam_1, field x_studio_company_id, field x_studio_chk_atomated_action … | Extends the x_test02 test form: replaces the chatter with a notebook of two one2many tabs ('Layout', 'New Page') and adds many test fields (status, date, types, charges, test values, company-dependent JIN/JAM fields, currency). Some button xpaths were stripped in the port. | `view BugFix-Studio-Misc.view_2414_default_form_view_for_x_test02`<br>`x_test02.x_currency_id`<br>`x_test02.x_studio_charges_1`<br>`x_test02.x_studio_charges_2`<br>`x_test02.x_studio_chk_atomated_action`<details><summary>+20 more</summary>`x_test02.x_studio_chk_server_action`<br>`x_test02.x_studio_company_id`<br>`x_test02.x_studio_date`<br>`x_test02.x_studio_jam_1`<br>`x_test02.x_studio_jin_2`<br>`x_test02.x_studio_many2many_field_c0IAp`<br>`x_test02.x_studio_one2many_field_51FSD`<br>`x_test02.x_studio_one2many_field_Q8Xws`<br>`x_test02.x_studio_status2`<br>`x_test02.x_studio_status_1`<br>`x_test02.x_studio_status`<br>`x_test02.x_studio_test_03`<br>`x_test02.x_studio_test_char`<br>`x_test02.x_studio_test_number_1`<br>`x_test02.x_studio_test_number_2`<br>`x_test02.x_studio_test_value`<br>`x_test02.x_studio_testing_02`<br>`x_test02.x_studio_testing`<br>`x_test02.x_studio_text_field_eKlfk`<br>`x_test02.x_studio_types`</details> |  |
| Odoo Studio: Default kanban view for ir.model(782,) customization | `view_2956_odoo_studio_default_kanban_view_for_ir_model_782_customizati_ext` | kanban | set default_group_by=x_name on `//kanban[1]` | Makes the x_test02 kanban view group cards by Name by default. | `view BugFix-Studio-Misc.view_2955_default_kanban_view_for_ir_model_782` |  |
| Odoo Studio: Default list view for x_test02 customization | `view_5420_odoo_studio_default_list_view_for_x_test02_customization_ext` | tree | after `//field[@name='x_name']`: add field x_studio_name_1 | Adds an optional 'Name-1' column after Name in the x_test02 list. | `view BugFix-Studio-Misc.view_2413_default_list_view_for_x_test02`<br>`x_test02.x_studio_name_1` |  |
| TEST Inherited View | `view_3919_test_inherited_view_e` | form |  | Extension of the x_test02 form whose every xpath was stripped during the port (numeric button refs could not be resolved); it has no effect. | `view BugFix-Studio-Misc.view_2414_default_form_view_for_x_test02` |  |

**Access rights (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TEST02 GROUP | `access_1154_test02_group` | Gives **PR Approval** no access to TEST02 records. | `group BugFix-Approvals.group_107_pr_approval` (BugFix-Approvals)<br>`model x_test02` |  |
| TEST02 GROUP | `access_f3_test02_group` | Gives **PR Approval** no access to TEST02 records. | `group BugFix-Approvals.group_107_pr_approval` (BugFix-Approvals)<br>`model x_test02` |  |
| TEST02 group_system | `access_1151_test02_group_system` | Gives **Administration / Settings** read/write/create/delete access to TEST02 records. | `group base.group_system` (base)<br>`model x_test02` |  |
| TEST02 group_user | `access_1152_test02_group_user` | Gives **User types / Internal User** read access to TEST02 records. | `group base.group_user` (base)<br>`model x_test02` |  |
| x_test02 admin | `access_x_test02_admin` | Gives **Administration / Settings** read/write/create/delete access to TEST02 records. | `group base.group_system` (base)<br>`model x_test02` |  |
