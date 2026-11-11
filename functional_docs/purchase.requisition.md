# BugFix-Studio-Misc — `purchase.requisition`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `purchase.requisition` — Purchase Requisition

*Extends a model created by `purchase_requisition`.*

Other repos that use this model: `record rule BugFix-Purchase.rule_purchase_requisition_multi_company` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_purchase_agreements` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_purchase_requisition_2` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_purchase_requisition` (BugFix-Purchase)

**Summary:**

<!-- SUMMARY:model:purchase.requisition -->
This repo adds an approval rule: an Internal User must approve before the Request for Quotation action runs on a purchase requisition. It also adds three window actions that open requisitions. One is filtered to the vendor the action is opened from, and one is linked to an entry under the TEST APP 05 menu.
<!-- /SUMMARY -->

**Approval rules (1):**

| Name | Record name | Approver group | Function | Depends on | Used by |
|---|---|---|---|---|---|
| Purchase Requisition/Request for Quotation (User types / Internal User) (77) | `approval_rule_ar_relaxed_purchase_requisition_request_for_quotation_user_types_i` | User types / Internal User | Before action _Request for Quotation_ on Purchase Requisition runs, an approval from **User types / Internal User** is required (step 1). | `group base.group_user` (base)<br>`model purchase.requisition` (purchase_requisition)<br>`window action purchase_requisition.action_purchase_requisition_to_so` (purchase_requisition) |  |

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Purchase Agreements | `action_purchase_agreements_d7` | Opens **Purchase Requisition** records (tree,form), filtered to `[('vendor_id', '=', active_id)]`. | `model purchase.requisition` (purchase_requisition)<br>`purchase.requisition.vendor_id` (purchase_requisition) |  |
| Purchase Requisition | `action_purchase_requisition_d7` | Opens **Purchase Requisition** records (kanban,tree,form). | `model purchase.requisition` (purchase_requisition) |  |
| purchase.requisition | `action_purchase_requisition_d7_2` | Opens **Purchase Requisition** records (kanban,tree,form). | `model purchase.requisition` (purchase_requisition) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_purchase_requisition` |
