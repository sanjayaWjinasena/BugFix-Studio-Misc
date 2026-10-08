# BugFix-Studio-Misc — `x_pr_line_cash`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_pr_line_cash` — Purchase Request Line Cash

*Extends a model created by `BugFix-Purchase`.*

Other repos that use this model: `access right BugFix-Purchase.access_1161_pr_line_cash_group_system` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_1162_pr_line_cash_group_user` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_x_pr_line_cash_user` (BugFix-Purchase)<br>`automation BugFix-Purchase.base_automation_272_jin_company_id_pr_line_cash` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_506_jin_multi_company_purchase_request_line_cash` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_pr_line_cash_jin_company_id_in_purchase_request_line_cash` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1005_copy_ncp_to_npo` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2595_jin_company_id_in_purchase_request_line_cash` (BugFix-Purchase)<details><summary>+11 more</summary>`server action BugFix-Purchase.server_action_911_copy_cp_to_po` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_1008_related_cps_line` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_1721_cp_lines` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2084_cash_purchase_lines` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2594_x_pr_line_cash` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_883_cash_purchase_lines` (BugFix-Purchase)<br>`x_pr_non_inventory._compute_related_cp_line_count()` (BugFix-Purchase)<br>`x_purchase.request.line.make.purchase.order.item.x_cp_line_id` (BugFix-Purchase)<br>`x_purchase.request.line.make.purchase.order.item.x_ncp_line_id` (BugFix-Purchase)<br>`x_purchase_request._compute_related_cp_line_count()` (BugFix-Purchase)<br>`x_purchase_request_cas.x_studio_one2many_field_zjo0U` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:x_pr_line_cash -->
Purchase Request Line Cash is created by BugFix-Purchase. This repo only adds access rights: the PR Administrator gets full access, procurement end users (Imports and Local) get read/write/create, and the view-only groups, account executives and cashiers get read-only access.
<!-- /SUMMARY -->

**Access rights (7):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Cash Purchase Lines | `access_g_cash_purchase_lines_x_pr_line_cash_purchase_jin_procurement_end_user_import` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create access to Purchase Request Line Cash records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_pr_line_cash` (BugFix-Purchase) |  |
| Cash Purchase Lines | `access_g_cash_purchase_lines_x_pr_line_cash_purchase_jin_procurement_view_only` | Gives **Purchase / Jin - Procurement - View Only** read access to Purchase Request Line Cash records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_view_only`<br>`model x_pr_line_cash` (BugFix-Purchase) |  |
| PR Line Cash | `access_g_pr_line_cash_x_pr_line_cash_accounting_jin_accountexecutive` | Gives **Accounting / Jin - AccountExecutive** read access to Purchase Request Line Cash records. | `group BugFix-Studio-Misc.group_g_accounting_jin_accountexecutive`<br>`model x_pr_line_cash` (BugFix-Purchase) |  |
| PR Line Cash | `access_g_pr_line_cash_x_pr_line_cash_accounting_jin_cashier` | Gives **Accounting / Jin - Cashier** read access to Purchase Request Line Cash records. | `group BugFix-Studio-Misc.group_g_accounting_jin_cashier`<br>`model x_pr_line_cash` (BugFix-Purchase) |  |
| Purchase  Request Line Cash | `access_g_purchase_request_line_cash_x_pr_line_cash_purchase_jin_pr_view_only` | Gives **Purchase / Jin - PR View Only** read access to Purchase Request Line Cash records. | `group BugFix-Studio-Misc.group_g_purchase_jin_pr_view_only`<br>`model x_pr_line_cash` (BugFix-Purchase) |  |
| Purchase Request Line Cash | `access_g_purchase_request_line_cash_x_pr_line_cash_purchase_jin_pr_administrator` | Gives **Purchase / Jin - PR Administrator** read/write/create/delete access to Purchase Request Line Cash records. | `group BugFix-Studio-Misc.group_g_purchase_jin_pr_administrator`<br>`model x_pr_line_cash` (BugFix-Purchase) |  |
| x_pr_line_cash (Cash Purchase Lines) | `access_g_x_pr_line_cash_cash_purchase_lines_x_pr_line_cash_purchase_jin_procurement_end_us` | Gives **Purchase / Jin - Procurement - End User - Local** read/write/create access to Purchase Request Line Cash records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_local`<br>`model x_pr_line_cash` (BugFix-Purchase) |  |
