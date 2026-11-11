# BugFix-Studio-Misc — `account.account`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.account` — Account

*Extends a model created by `account`.*

Other repos that use this model: `record rule BugFix-Accounting.rule_81_account_multi_company` (BugFix-Accounting)<br>`sale.order._seed_advance_payment_method_lines()` (Fix-repair)<br>`window action BugFix-Accounting.action_1977_stock_picking` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_2190_project_budgeted_cash_flow` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_2191_project_budgeted_cash_flow` (BugFix-Accounting)<br>`advance_payment_acco.advance_account_project` (BugFix-Accounting)<br>`advance_payment_acco.advance_payment_account_purchases_1` (BugFix-Accounting)<br>`advance_payment_acco.advance_payment_account_purchases` (BugFix-Accounting)<details><summary>+23 more</summary>`advance_payment_acco.advance_payment_account_sales` (BugFix-Accounting)<br>`consignment_header.account_charge` (BugFix-Stock)<br>`consignment_header.account_duty` (BugFix-Stock)<br>`consignment_header.account_tax` (BugFix-Stock)<br>`consignment_header.offset_account` (BugFix-Stock)<br>`customer_group.receivable_account` (studio_usermodel_migration)<br>`import_charges.ledger_account` (BugFix-Purchase)<br>`imports_ledger_setup.cash_issue_credit_acc` (BugFix-Purchase)<br>`imports_ledger_setup.cash_settle_debit_acc` (BugFix-Purchase)<br>`imports_ledger_setup.expense_account` (BugFix-Purchase)<br>`imports_ledger_setup.import_tp_vend_acc_non_billable` (BugFix-Purchase)<br>`imports_ledger_setup.import_tp_vend_non_billable_debit_acc` (BugFix-Purchase)<br>`imports_ledger_setup.import_tp_vendor_account` (BugFix-Purchase)<br>`imports_ledger_setup.import_tp_vendor_debit_acc` (BugFix-Purchase)<br>`imports_ledger_setup.purch_packing_slip_offset_account` (BugFix-Purchase)<br>`imports_ledger_setup.vat_receivable_account` (BugFix-Purchase)<br>`imports_ledger_setup.vendor_despatch_credit_account` (BugFix-Purchase)<br>`imports_ledger_setup.vendor_despatch_debit_account` (BugFix-Purchase)<br>`journal_types.offset_account` (BugFix-Maintenance)<br>`misc_charge_codes.credit_account` (BugFix-Stock)<br>`misc_charge_codes.debit_account` (BugFix-Stock)<br>`repair_accounts.rug_account` (Fix-repair)<br>`vendor_group.payable_account` (studio_usermodel_migration)</details>

**Summary:**

<!-- SUMMARY:model:account.account -->
This repo adds three window actions that open Account records in kanban, list and form: two named Project Budgeted Cash Flow and one named stock.picking. None of them is linked to a menu here. No fields, views or rules are added.
<!-- /SUMMARY -->

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Project Budgeted Cash Flow | `act_window_2190_project_budgeted_cash_flow_d7` | Opens **Account** records (kanban,tree,form). | `model account.account` (account) |  |
| Project Budgeted Cash Flow | `act_window_2191_project_budgeted_cash_flow_d7` | Opens **Account** records (kanban,tree,form). | `model account.account` (account) |  |
| stock.picking | `act_window_1977_stock_picking_d7` | Opens **Account** records (kanban,tree,form). | `model account.account` (account) |  |
