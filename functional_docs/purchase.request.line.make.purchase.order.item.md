# BugFix-Studio-Misc — `purchase.request.line.make.purchase.order.item`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `purchase.request.line.make.purchase.order.item` — Purchase Request Line Make Purchase Order Item

*Extends a model created by `BugFix-Purchase`.*

Other repos that use this model: `access right BugFix-Purchase.access_purchase_request_line_make_purchase_order_item_group_user` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_purchase_request_line_make_purchase_order_item_group_system` (BugFix-Purchase)<br>`automation BugFix-Purchase.base_automation_17_wizard_page_quantity_to_purchase_validate` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_purchase_request_line_make_purchase_order_item_wizard_page_quantity_to` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_select_all_in_create_rfq` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_clear_all_in_create_rfq` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_wizard_page_quantity_to_purchase_validate` (BugFix-Purchase)<br>`window action BugFix-Purchase.act_window_897_pr_test_lines` (BugFix-Purchase)<details><summary>+1 more</summary>`purchase.request.line.make.purchase.order.item_ids` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:purchase.request.line.make.purchase.order.item -->
Purchase Request Line Make Purchase Order Item is created by BugFix-Purchase. This repo only adds access rights: the PR Administrator and procurement end users (Imports and Local) get full access, and the procurement view-only and PR view-only groups get read-only access.
<!-- /SUMMARY -->

**Access rights (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Purchase Request Line Make PO Item | `access_g_purchase_request_line_make_po_item_item_purchase_jin_procurement_end_user_import` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create/delete access to Purchase Request Line Make Purchase Order Item records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model purchase.request.line.make.purchase.order.item` (BugFix-Purchase) |  |
| Purchase Request Line Make PO Item | `access_g_purchase_request_line_make_po_item_item_purchase_jin_procurement_end_user_local` | Gives **Purchase / Jin - Procurement - End User - Local** read/write/create/delete access to Purchase Request Line Make Purchase Order Item records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_local`<br>`model purchase.request.line.make.purchase.order.item` (BugFix-Purchase) |  |
| Purchase Request Line Make PO Item | `access_g_purchase_request_line_make_po_item_item_purchase_jin_procurement_view_only` | Gives **Purchase / Jin - Procurement - View Only** read access to Purchase Request Line Make Purchase Order Item records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_view_only`<br>`model purchase.request.line.make.purchase.order.item` (BugFix-Purchase) |  |
| Purchase Request Line Make Purchase Order Item | `access_g_purchase_request_line_make_purchase_orde_item_purchase_jin_pr_administrator` | Gives **Purchase / Jin - PR Administrator** read/write/create/delete access to Purchase Request Line Make Purchase Order Item records. | `group BugFix-Studio-Misc.group_g_purchase_jin_pr_administrator`<br>`model purchase.request.line.make.purchase.order.item` (BugFix-Purchase) |  |
| Purchase Request Line Make Purchase Order Item | `access_g_purchase_request_line_make_purchase_orde_item_purchase_jin_pr_view_only` | Gives **Purchase / Jin - PR View Only** read access to Purchase Request Line Make Purchase Order Item records. | `group BugFix-Studio-Misc.group_g_purchase_jin_pr_view_only`<br>`model purchase.request.line.make.purchase.order.item` (BugFix-Purchase) |  |
