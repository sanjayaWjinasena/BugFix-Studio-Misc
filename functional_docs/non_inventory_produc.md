# BugFix-Studio-Misc — `non_inventory_produc`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `non_inventory_produc` — Non Inventory Product Code

*Extends a model created by `BugFix-Purchase`.*

Other repos that use this model: `access right BugFix-Purchase.access_1196_non_inventory_product_code_group_system` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_1197_non_inventory_product_code_group_user` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_x_non_inventory_produc_user` (BugFix-Purchase)<br>`automation BugFix-Purchase.base_automation_279_jin_company_id_non_inv_product` (BugFix-Purchase)<br>`record rule BugFix-Purchase.rule_511_jin_multi_company_non_inventory_product_code` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_non_inventory_produc_jin_company_id_in_non_inventory_product_code` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2606_jin_company_id_in_non_inventory_product_code` (BugFix-Purchase)<br>`window action BugFix-Purchase.action_944_non_inventory_product_code` (BugFix-Purchase)<details><summary>+6 more</summary>`po_line_non_inventor.many2one_field_pQKBN` (BugFix-Purchase)<br>`pr_line_cash.non_inventory_code` (BugFix-Purchase)<br>`pr_line_non_inventor.non_inventory_code` (BugFix-Purchase)<br>`purchase.request.line.make.purchase.order.item.cpnpr_non_inventory_code` (BugFix-Purchase)<br>`purchase.request.line.make.purchase.order.item.ncp_non_inventory_code` (BugFix-Purchase)<br>`purchase.request.line.make.purchase.order.item.npr_non_inventory_code` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:non_inventory_produc -->
Non Inventory Product Code is created by BugFix-Purchase. This repo only adds access rights: the Jin PR creator and Non-Inventory Credit invoicing/payment groups get read/write/create, and the NI invoice journal group gets read-only access.
<!-- /SUMMARY -->

**Access rights (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| non_inventory_produc | `access_g_x_non_inventory_produc_x_non_inventory_produc_purchase_jin_create_ni_invoice_jour` | Gives **Purchase / Jin - Create NI Invoice Journal for NI Ca PO** read access to Non Inventory Product Code records. | `group BugFix-Studio-Misc.group_g_purchase_jin_create_ni_invoice_journal_for_ni_ca_po`<br>`model non_inventory_produc` (BugFix-Purchase) |  |
| non_inventory_produc | `access_g_x_non_inventory_produc_x_non_inventory_produc_purchase_jin_inv_pr_creators` | Gives **Purchase / Jin - Inv PR Creators** read/write/create access to Non Inventory Product Code records. | `group BugFix-Studio-Misc.group_g_purchase_jin_inv_pr_creators`<br>`model non_inventory_produc` (BugFix-Purchase) |  |
| non_inventory_produc | `access_g_x_non_inventory_produc_x_non_inventory_produc_purchase_jin_non_inv_pr_creators` | Gives **Purchase / Jin - Non-Inv PR Creators** read/write/create access to Non Inventory Product Code records. | `group BugFix-Studio-Misc.group_g_purchase_jin_non_inv_pr_creators`<br>`model non_inventory_produc` (BugFix-Purchase) |  |
| non_inventory_produc | `access_g_x_non_inventory_produc_x_non_inventory_produc_purchase_jin_po_invoicing_payment_n` | Gives **Purchase / Jin - PO Invoicing & Payment - Non-Inventory Credit** read/write/create access to Non Inventory Product Code records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_non_inventory_credit`<br>`model non_inventory_produc` (BugFix-Purchase) |  |
| non_inventory_produc | `access_g_x_non_inventory_produc_x_non_inventory_produc_purchase_jin_po_invoicing_payment_n_1` | Gives **Purchase / Jin - PO Invoicing & Payment - Non-Inventory Credit (copy)** read/write/create access to Non Inventory Product Code records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_non_inventory_credit_copy`<br>`model non_inventory_produc` (BugFix-Purchase) |  |
