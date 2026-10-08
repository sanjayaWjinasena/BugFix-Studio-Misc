# BugFix-Studio-Misc — `purchase.requisition.type`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `purchase.requisition.type` — Purchase Requisition Type

*Extends a model created by `purchase_requisition`.*

Other repos that use this model: `access right BugFix-Purchase.access_7075_purchase_requisition_type` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2874_purchase_agreement_type_purchase_requisition_type` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2875_purchase_agreement_types_purchase_requisition_type` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_777_pr_type` (BugFix-Purchase)

**Summary:**

<!-- SUMMARY:model:purchase.requisition.type -->
This repo only adds three window actions that open Purchase Requisition Type (agreement type) records, named PR Type, Purchase Agreement Type and Purchase Agreement Types. The last one is linked to an entry under the TEST APP 05 menu.
<!-- /SUMMARY -->

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| PR Type | `act_window_777_pr_type_d7` | Opens **Purchase Requisition Type** records (kanban,tree,form). | `model purchase.requisition.type` (purchase_requisition) |  |
| Purchase Agreement Type (purchase.requisition.type) | `act_window_2874_purchase_agreement_type_purchase_requisition_type_d7` | Opens **Purchase Requisition Type** records (kanban,tree,form). | `model purchase.requisition.type` (purchase_requisition) |  |
| Purchase Agreement Types (purchase.requisition.type) | `act_window_2875_purchase_agreement_types_purchase_requisition_type_d7` | Opens **Purchase Requisition Type** records (kanban,tree,form). | `model purchase.requisition.type` (purchase_requisition) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_purchase_agreement_types_purchase_requisition_ty` |
