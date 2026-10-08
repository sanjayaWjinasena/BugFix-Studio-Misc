# BugFix-Studio-Misc — `hr.expense.sheet`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `hr.expense.sheet` — Expense Report

*Extends a model created by `hr_expense`.*

Other repos that use this model: `record rule BugFix-HR.rule_324_manager_expense_sheet` (BugFix-HR)<br>`record rule BugFix-HR.rule_325_approver_expense_sheet` (BugFix-HR)<br>`record rule BugFix-HR.rule_326_employee_expense_sheet` (BugFix-HR)<br>`record rule BugFix-HR.rule_328_expense_report_multi_company_rule` (BugFix-HR)<br>`record rule BugFix-HR.rule_633_employee_can_t_modify_expense_sheet_that_is_not_in_draft_sta` (BugFix-HR)<br>`window action BugFix-HR.act_window_1274_my_reports` (BugFix-HR)<br>`window action BugFix-HR.act_window_2585_hr_expense_sheet` (BugFix-HR)<br>`window action BugFix-HR.act_window_2596_hr_expense_sheet` (BugFix-HR)<details><summary>+1 more</summary>`window action BugFix-HR.act_window_2817_hr_expense_sheet` (BugFix-HR)</details>

**Summary:**

<!-- SUMMARY:model:hr.expense.sheet -->
This repo adds Studio tweaks to the Expense Report form: the name and accounting date become read-only unless the report is an editable draft, the accounting date shows only once approved or later, expense lines are locked outside draft and taxes are always read-only. It also gives read access to Expense Reports to the Jin Cashier and two PO Invoicing and Payment groups.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: hr.expense.sheet.form customization | `view_final_hr_expense_sheet_odoo_studio_hr_expense_sheet_form_customization` | form | set readonly=(not is_editable) or (state != 'draft') on `//form[1]/sheet[1]/div[not(@name)][1]/h1[1]/field[@name='name']`; set invisible=(state not in ['approve', 'post', 'done']) or (state not in ['approve', 'post', 'done']), readonly=(not is_editable) or (state != 'draft') on `//field[@name='accounting_date']`; set readonly=(parent.state != 'draft') or (state not in ['draft', 'reported', 'approved', 'refused']) on `//field[@name='date']`; set readonly=(parent.state != 'draft') or (state not in ['draft', 'reported', 'approved', 'refused']) on `//field[@name='product_id']`; set readonly=(parent.state != 'draft') or (state not in ['draft', 'reported', 'approved', 'refused']) on `//form[1]/sheet[1]/notebook[1]/page[@name='expenses']/field[@name='expense_line_ids']/tree[1]/field[@name='name']`; set invisible=(not can_be_reinvoiced) or (can_be_reinvoiced == False), readonly=(state in ['done', 'refused']) or ((parent.state != 'draft') or (state in ['done', 'refused'])) on `//field[@name='sale_order_id']`; set readonly=True on `//field[@name='tax_ids']` | Studio tweaks to the Expense Report form: sheet name and accounting date read-only unless editable draft, accounting date shown only once approved/posted/done, expense line fields locked outside draft, Sales Order shown only if re-invoiceable, and Taxes always read-only. | `view hr_expense.view_hr_expense_sheet_form` (hr_expense) |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| hr.expense.sheet | `access_g_hr_expense_sheet_sheet_purchase_jin_po_invoicing_payment_invent` | Gives **Purchase / # Jin - PO Invoicing & Payment - Inventory Credit** read access to Expense Report records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_inventory_credit`<br>`model hr.expense.sheet` (hr_expense) |  |
| hr.expense.sheet | `access_g_hr_expense_sheet_sheet_accounting_jin_cashier` | Gives **Accounting / Jin - Cashier** read access to Expense Report records. | `group BugFix-Studio-Misc.group_g_accounting_jin_cashier`<br>`model hr.expense.sheet` (hr_expense) |  |
| hr.expense.sheet | `access_g_hr_expense_sheet_sheet_purchase_jin_po_invoicing_payment_non_in` | Gives **Purchase / Jin - PO Invoicing & Payment - Non-Inventory Credit** read access to Expense Report records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_non_inventory_credit`<br>`model hr.expense.sheet` (hr_expense) |  |
