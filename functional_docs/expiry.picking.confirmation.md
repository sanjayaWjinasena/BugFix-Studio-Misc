# BugFix-Studio-Misc — `expiry.picking.confirmation`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `expiry.picking.confirmation` — Confirm Expiry

*Extends a model created by `product_expiry`.*

**Summary:**

<!-- SUMMARY:model:expiry.picking.confirmation -->
This repo adds four read-only access rights on the Confirm Expiry wizard for its Manufacturing groups (MO Operator, Production Orders Dismantler, view-only users) and the Purchase / Jin - PO Goods Receivers group. Nothing else is changed.
<!-- /SUMMARY -->

**Access rights (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| access.expiry.picking.confirmation | `access_g_access_expiry_picking_confirmation_confirmation_manufacturing_jin_manufacturing_m` | Gives **Manufacturing / Jin - Manufacturing - MO Operator** read access to Confirm Expiry records. | `group BugFix-Studio-Misc.group_g_manufacturing_jin_manufacturing_mo_operator`<br>`model expiry.picking.confirmation` (product_expiry) |  |
| access.expiry.picking.confirmation | `access_g_access_expiry_picking_confirmation_confirmation_manufacturing_jin_manufacturing_p` | Gives **Manufacturing / Jin - Manufacturing - Production Orders Dismantler** read access to Confirm Expiry records. | `group BugFix-Studio-Misc.group_g_manufacturing_jin_manufacturing_production_orders_dismantler`<br>`model expiry.picking.confirmation` (product_expiry) |  |
| access.expiry.picking.confirmation | `access_g_access_expiry_picking_confirmation_confirmation_manufacturing_jin_manufacturing_t` | Gives **Manufacturing / Jin - Manufacturing - Those with only view Rights** read access to Confirm Expiry records. | `group BugFix-Studio-Misc.group_g_manufacturing_jin_manufacturing_those_with_only_view_rights`<br>`model expiry.picking.confirmation` (product_expiry) |  |
| access.expiry.picking.confirmation | `access_g_access_expiry_picking_confirmation_confirmation_purchase_jin_po_goods_receivers` | Gives **Purchase / Jin - PO Goods Receivers** read access to Confirm Expiry records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_goods_receivers`<br>`model expiry.picking.confirmation` (product_expiry) |  |
