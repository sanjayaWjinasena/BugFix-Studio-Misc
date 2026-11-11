# BugFix-Studio-Misc — `consignment_charge_h`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `consignment_charge_h` — Consignment Charge Header

*Extends a model created by `BugFix-Stock`.*

Other repos that use this model: `access right BugFix-Accounting.access_consignment_charge_header_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_consignment_charge_header_group_user` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_consignment_charge_h_user` (BugFix-Accounting)<br>`access right BugFix-Stock.access_consignment_charge_h_user` (BugFix-Stock)<br>`automation BugFix-Accounting.automation_jin_company_id_in_consignment_charge_header` (BugFix-Accounting)<br>`automation BugFix-Stock.automation_jin_company_id_in_consignment_charge_header` (BugFix-Stock)<br>`record rule BugFix-Accounting.rule_jin_multi_company_consignment_charge_header` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_apply_selected_charge_lines_to_tp_invoice` (BugFix-Accounting)<details><summary>+22 more</summary>`server action BugFix-Accounting.action_jin_company_id_in_consignment_charge_header` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_apply_charges` (BugFix-Accounting)<br>`server action BugFix-Stock.action_imp_create_consignment_header_charges` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_allocate_consignment_header_charges` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_check_consignment_assessable_value` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_consignment_custom_duty` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_copy_charges_to_tp_invoice` (BugFix-Stock)<br>`server action BugFix-Stock.action_imp_reset_header_charges_consignment` (BugFix-Stock)<br>`server action BugFix-Stock.action_jin_company_id_in_consignment_charge_header` (BugFix-Stock)<br>`window action BugFix-Accounting.action_consignment_charge_header` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_header_charges` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_consignment_charge_header_2` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_consignment_charge_header_3` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_purchase_invoices` (BugFix-Accounting)<br>`window action BugFix-Stock.action_consignment_charge_header` (BugFix-Stock)<br>`window action BugFix-Stock.action_header_charges` (BugFix-Stock)<br>`window action BugFix-Stock.action_consignment_charge_header_2` (BugFix-Stock)<br>`window action BugFix-Stock.action_consignment_charge_header_3` (BugFix-Stock)<br>`window action BugFix-Stock.action_purchase_invoices_2` (BugFix-Stock)<br>`consignment_charge_l.consignment_charge_header_id` (BugFix-Stock)<br>`temp_tp_invoice_line.consignment_charge_header_id` (BugFix-Accounting)<br>`tp_invoice_line.consignment_charge_header_id` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:consignment_charge_h -->
This repo only adds two access rights on Consignment Charge Headers. Purchase / Jin - PO Invoicing & Payment - Imports gets read and write access, and Purchase / Jin - Procurement - End User - Imports gets read, write and create access. Both groups are defined in this repo.
<!-- /SUMMARY -->

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| consignment_charge_h | `access_g_consignment_charge_h_consignment_charge_h_purchase_jin_po_invoicing_payment_i` | Gives **Purchase / Jin - PO Invoicing & Payment - Imports** read/write access to Consignment Charge Header records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_imports`<br>`model consignment_charge_h` (BugFix-Stock) |  |
| consignment_charge_h | `access_g_consignment_charge_h_consignment_charge_h_purchase_jin_procurement_end_user_i` | Gives **Purchase / Jin - Procurement - End User - Imports** read/write/create access to Consignment Charge Header records. | `group BugFix-Studio-Misc.group_g_purchase_jin_procurement_end_user_imports`<br>`model consignment_charge_h` (BugFix-Stock) |  |
