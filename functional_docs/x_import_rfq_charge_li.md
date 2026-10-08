# BugFix-Studio-Misc — `x_import_rfq_charge_li`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_import_rfq_charge_li` — Import RFQ Charge Line

*Extends a model created by `BugFix-Purchase`.*

Other repos that use this model: `access right BugFix-Purchase.access_1255_import_rfq_charge_line_group_system` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_1256_import_rfq_charge_line_group_user` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_x_import_rfq_charge_li_user` (BugFix-Purchase)<br>`automation BugFix-Purchase.base_automation_288_jin_company_id_import_rfq_line` (BugFix-Purchase)<br>`purchase.order._compute_import_rfq_charge_li_count()` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_520_jin_multi_company_import_rfq_charge_line` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_import_rfq_charge_li_jin_company_id_in_import_rfq_charge_line` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1212_imp_allocate_header_charges` (BugFix-Purchase)<details><summary>+8 more</summary>`server action BugFix-Purchase.server_action_1699_imp_reset_header_charges` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2375_reverse_pr_status_in_po_2` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2616_jin_company_id_in_import_rfq_charge_line` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_1213_import_rfq_charge_line` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_1214_line_charges` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2228_indent_costing` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2846_import_rfq_charge_line` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2856_import_rfq_charge_line` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:x_import_rfq_charge_li -->
This repo adds a PDF report, Import RFQ Charge Line Report, from a Studio template. It also adds an access right that gives Purchase / Jin - Procurement - End User - Imports (defined in this repo) full access to Import RFQ Charge Lines.
<!-- /SUMMARY -->

**Reports (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Import RFQ Charge Line Report | `action_report_2232_import_rfq_charge_line_report` | Prints **Import RFQ Charge Line Report** (qweb-pdf) for x_import_rfq_charge_li records using template `studio_customization.studio_report_docume_889bd190-016a-4aa3-a1aa-dad6e31bf4d3`. | `model x_import_rfq_charge_li` (BugFix-Purchase)<br>`record studio_customization.studio_report_docume_889bd190-016a-4aa3-a1aa-dad6e31bf4d3` (studio_customization) |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_import_rfq_charge_li | `access_g_x_import_rfq_charge_li_x_import_rfq_charge_li_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create/delete access to Import RFQ Charge Line records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_import_rfq_charge_li` (BugFix-Purchase) |  |
