# BugFix-Studio-Misc — `x_po_line_non_inventor`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_po_line_non_inventor` — Purchase Order Line (Non-Inventory)

*Extends a model created by `BugFix-Purchase`.*

Other repos that use this model: `access right BugFix-Purchase.access_1200_po_line_non_inventory_group_system` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_1201_po_line_non_inventory_group_user` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_x_po_line_non_inventor_user` (BugFix-Purchase)<br>`automation BugFix-Purchase.base_automation_278_jin_company_id_in_non_inventory_purchase_order` (BugFix-Purchase)<br>`automation BugFix-Purchase.base_automation_278_jin_company_id_po_line_non_inv` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_510_jin_multi_company_non_inventory_purchase_order` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_po_line_non_inventor_jin_company_id_in_non_inventory_purchase_order` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_pr_line_non_inventor_update_last_npo_details_in_npr` (BugFix-Purchase)<details><summary>+10 more</summary>`server action BugFix-Purchase.server_action_2605_jin_company_id_in_non_inventory_purchase_order` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_976_confirm_npo` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_988_npo_invoice_journal` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_997_update_last_npo_details_in_npr` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_1009_related_pos_line` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2073_non_inv_purchase_order_lines` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2603_x_po_line_non_inventor` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_962_po_line_non_inventory` (BugFix-Purchase)<br>`x_po_non_inventory.x_studio_one2many_field_Ff7zp` (BugFix-Purchase)<br>`x_pr_non_inventory._compute_related_po_line_non_inventor_count()` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:x_po_line_non_inventor -->
Purchase Order Line (Non-Inventory) is created by BugFix-Purchase. This repo only adds access rights: the Jin procurement end-user groups (Imports and Local) get read/write/create, and the procurement view-only and PR view-only groups get read-only access.
<!-- /SUMMARY -->

**Access rights (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Non Inventory PO Lines | `access_g_non_inventory_po_lines_x_po_line_non_inventor_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create access to Purchase Order Line (Non-Inventory) records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model x_po_line_non_inventor` (BugFix-Purchase) |  |
| Non Inventory PO Lines | `access_g_non_inventory_po_lines_x_po_line_non_inventor_purchase_jin_procurement_end_user_l` | Gives **Purchase / Jin - Procurement - End User - Local** read/write/create access to Purchase Order Line (Non-Inventory) records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_local`<br>`model x_po_line_non_inventor` (BugFix-Purchase) |  |
| Non Inventory PO Lines | `access_g_non_inventory_po_lines_x_po_line_non_inventor_purchase_jin_procurement_view_only` | Gives **Purchase / Jin - Procurement - View Only** read access to Purchase Order Line (Non-Inventory) records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_view_only`<br>`model x_po_line_non_inventor` (BugFix-Purchase) |  |
| Purchase Order Line (Non-Inventory) | `access_g_purchase_order_line_non_inventory_x_po_line_non_inventor_purchase_jin_pr_view_onl` | Gives **Purchase / Jin - PR View Only** read access to Purchase Order Line (Non-Inventory) records. | `group BugFix-Studio-Misc.group_g_purchase_jin_pr_view_only`<br>`model x_po_line_non_inventor` (BugFix-Purchase) |  |
