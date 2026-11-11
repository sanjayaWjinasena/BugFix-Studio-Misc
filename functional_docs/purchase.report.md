# BugFix-Studio-Misc — `purchase.report`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `purchase.report` — Purchase Report

*Extends a model created by `purchase`.*

Other repos that use this model: `record rule BugFix-Purchase.rule_purchase_order_report_multi_company` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_purchase_request_lin_update_last_po_details_in_pr` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_update_last_po_details_in_pr_2` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_update_last_po_details_in_pr` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_996_test_456` (BugFix-Purchase)

**Summary:**

<!-- SUMMARY:model:purchase.report -->
This repo only adds one PDF report, Purchase Report Report, that prints purchase analysis records from a Studio report template. No fields or logic are changed.
<!-- /SUMMARY -->

**Reports (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Purchase Report Report | `report_purchase_report_report` | Prints **Purchase Report Report** (qweb-pdf) for purchase.report records using template `studio_customization.studio_report_docume_e6601e89-775c-4221-ae07-7bdeb3b6ea53`. | `model purchase.report` (purchase)<br>`record studio_customization.studio_report_docume_e6601e89-775c-4221-ae07-7bdeb3b6ea53` (studio_customization) |  |
