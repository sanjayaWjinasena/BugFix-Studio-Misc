# BugFix-Studio-Misc — `purchase.requisition.line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `purchase.requisition.line` — Purchase Requisition Line

*Extends a model created by `purchase_requisition`.*

Other repos that use this model: `record rule BugFix-Purchase.rule_269_purchase_requisition_line_multi_company` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_2811_purchase_requisition_line` (BugFix-Purchase)

**Summary:**

<!-- SUMMARY:model:purchase.requisition.line -->
This repo only adds a window action that opens Purchase Requisition Line records in list and form views. It is not linked to any menu in this repo.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| purchase.requisition.line | `act_window_2811_purchase_requisition_line_d7` | Opens **Purchase Requisition Line** records (tree,form). | `model purchase.requisition.line` (purchase_requisition) |  |
