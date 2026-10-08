# BugFix-Studio-Misc — `hr.expense`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `hr.expense` — Expense

*Extends a model created by `hr_expense`.*

**Summary:**

<!-- SUMMARY:model:hr.expense -->
This repo adds the server action EXP - Validate Negative Quantities, which blocks an expense with a negative quantity, but its automation is archived and has no action linked, so the check does not run. It also adds an expense window action, an empty Studio form extension, read-only access for the Jin Cashier and two PO Invoicing and Payment groups, and three global record rules that limit expenses to the user's own (by employee or creator) and make non-draft own expenses read-only.
<!-- /SUMMARY -->

**Server actions (1):**

- **EXP - Validate Negative Quantities** (`server_action_2577_exp_validate_negative_quantities_d7`, type `code`)
  - Function: Blocks an expense with a negative quantity, raising 'Invalid quantity'.
  - Depends on: `hr.expense.quantity` (hr_expense), `model hr.expense` (hr_expense)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.quantity < 0:
  raise UserError("Invalid quantity")
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| EXP - Validate Negative Quantities | `base_automation_261_exp_validate_negative_quantities_d7` | archived | When a record is created or updated on Expense, runs nothing (no action linked). **Archived — does not run.** | `model hr.expense` (hr_expense) |  |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| hr.expense | `act_window_2816_hr_expense_d7` | Opens **Expense** records (kanban,tree,form,pivot,graph,activity). | `model hr.expense` (hr_expense) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_hr_expense` |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| hr.expense.extract.view.form_studio_cus | `view_final_hr_expense_hr_expense_extract_view_form_studio_cus` | form |  | Empty Studio extension of the Expense extract form; contains no changes and has no effect. | `view hr_expense_extract.hr_expense_extract_view_form` (hr_expense_extract) |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| hr.expense | `access_g_hr_expense_expense_purchase_jin_po_invoicing_payment_invent` | Gives **Purchase / # Jin - PO Invoicing & Payment - Inventory Credit** read access to Expense records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_inventory_credit`<br>`model hr.expense` (hr_expense) |  |
| hr.expense | `access_g_hr_expense_expense_accounting_jin_cashier` | Gives **Accounting / Jin - Cashier** read access to Expense records. | `group BugFix-Studio-Misc.group_g_accounting_jin_cashier`<br>`model hr.expense` (hr_expense) |  |
| hr.expense | `access_g_hr_expense_expense_purchase_jin_po_invoicing_payment_non_in` | Gives **Purchase / Jin - PO Invoicing & Payment - Non-Inventory Credit** read access to Expense records. | `group BugFix-Studio-Misc.group_g_purchase_jin_po_invoicing_payment_non_inventory_credit`<br>`model hr.expense` (hr_expense) |  |

**Record rules (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Employee Expense | `rule_f7_hr_expense_employee_expense` | For everyone (global rule): read/write/create/delete on Expense only where `[('employee_id.user_id', '=', user.id)]`. | `hr.employee.user_id` (hr)<br>`hr.expense.employee_id` (hr_expense)<br>`model hr.expense` (hr_expense) |  |
| Employee can't modify expense that is not in draft state | `rule_f7_hr_expense_employee_can_t_modify_expense_that_is_not_in_draft_state` | For everyone (global rule): read on Expense only where `[('employee_id.user_id', '=', user.id), ('state', '!=', 'draft')]`. | `hr.employee.user_id` (hr)<br>`hr.expense.employee_id` (hr_expense)<br>`hr.expense.state` (hr_expense)<br>`model hr.expense` (hr_expense) |  |
| Hr Expense | `rule_f7_hr_expense_hr_expense` | For everyone (global rule): read/write/create/delete on Expense only where `[('create_uid', '=', user.id)]`. | `model hr.expense` (hr_expense) |  |
