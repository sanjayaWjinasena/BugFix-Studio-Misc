# BugFix-Studio-Misc — `import_rfq_charge_he`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `import_rfq_charge_he` — Import RFQ Charge Header

*Extends a model created by `BugFix-Purchase`.*

Other repos that use this model: `access right BugFix-Purchase.access_import_rfq_charge_header_group_system` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_import_rfq_charge_header_group_user` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_import_rfq_charge_he_user` (BugFix-Purchase)<br>`automation BugFix-Purchase.automation_jin_company_id_import_rfq_header` (BugFix-Purchase)<br>`purchase.order._compute_import_rfq_charge_he_count()` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_jin_multi_company_import_rfq_charge_header` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_import_rfq_charge_he_jin_company_id_in_import_rfq_charge_header` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_create_header_charges` (BugFix-Purchase)<details><summary>+10 more</summary>`server action BugFix-Purchase.action_imp_allocate_header_charges` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_reset_header_charges` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_reverse_pr_status_in_po_2` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_jin_company_id_in_import_rfq_charge_header` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_import_rfq_charge_header` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_header_charges` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_indent_costing_header` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_import_rfq_charge_header_2` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_import_rfq_charge_header_3` (BugFix-Purchase)<br>`import_rfq_charge_li.rfq_charge_header_id` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:import_rfq_charge_he -->
This repo adds a PDF report, Import RFQ Charge Header Report, from a Studio template. It also adds an access right that gives Purchase / Jin - Procurement - End User - Imports (defined in this repo) read, write and create access to Import RFQ Charge Headers.
<!-- /SUMMARY -->

**Reports (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Import RFQ Charge Header Report | `report_import_rfq_charge_header_report` | Prints **Import RFQ Charge Header Report** (qweb-pdf) for import_rfq_charge_he records using template `studio_customization.studio_report_docume_df0fd28d-9e06-4113-a4d2-7b8efb8250a4`. | `model import_rfq_charge_he` (BugFix-Purchase)<br>`record studio_customization.studio_report_docume_df0fd28d-9e06-4113-a4d2-7b8efb8250a4` (studio_customization) |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| import_rfq_charge_he | `access_g_import_rfq_charge_he_import_rfq_charge_he_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create access to Import RFQ Charge Header records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model import_rfq_charge_he` (BugFix-Purchase) |  |
