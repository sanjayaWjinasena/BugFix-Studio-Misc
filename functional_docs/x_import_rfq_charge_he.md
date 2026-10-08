# BugFix-Studio-Misc — `x_import_rfq_charge_he`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_import_rfq_charge_he` — Import RFQ Charge Header

*Extends a model created by `BugFix-Purchase`.*

Other repos that use this model: `access right BugFix-Purchase.access_1253_import_rfq_charge_header_group_system` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_1254_import_rfq_charge_header_group_user` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_x_import_rfq_charge_he_user` (BugFix-Purchase)<br>`automation BugFix-Purchase.base_automation_287_jin_company_id_import_rfq_header` (BugFix-Purchase)<br>`purchase.order._compute_import_rfq_charge_he_count()` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_519_jin_multi_company_import_rfq_charge_header` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_import_rfq_charge_he_jin_company_id_in_import_rfq_charge_header` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1209_imp_create_header_charges` (BugFix-Purchase)<details><summary>+10 more</summary>`server action BugFix-Purchase.server_action_1212_imp_allocate_header_charges` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1699_imp_reset_header_charges` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2375_reverse_pr_status_in_po_2` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2615_jin_company_id_in_import_rfq_charge_header` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_1210_import_rfq_charge_header` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_1211_header_charges` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2229_indent_costing_header` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2845_import_rfq_charge_header` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2855_import_rfq_charge_header` (BugFix-Purchase)<br>`x_import_rfq_charge_li.x_studio_rfq_charge_header_id` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:x_import_rfq_charge_he -->
This repo adds a PDF report, Import RFQ Charge Header Report, from a Studio template. It also adds an access right that gives Purchase / Jin - Procurement - End User - Imports (defined in this repo) read, write and create access to Import RFQ Charge Headers.
<!-- /SUMMARY -->

**Reports (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Import RFQ Charge Header Report | `action_report_1631_import_rfq_charge_header_report` | Prints **Import RFQ Charge Header Report** (qweb-pdf) for x_import_rfq_charge_he records using template `studio_customization.studio_report_docume_df0fd28d-9e06-4113-a4d2-7b8efb8250a4`. | `model x_import_rfq_charge_he` (BugFix-Purchase)<br>`record studio_customization.studio_report_docume_df0fd28d-9e06-4113-a4d2-7b8efb8250a4` (studio_customization) |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_import_rfq_charge_he | `access_g_x_import_rfq_charge_he_x_import_rfq_charge_he_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create access to Import RFQ Charge Header records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_import_rfq_charge_he` (BugFix-Purchase) |  |
