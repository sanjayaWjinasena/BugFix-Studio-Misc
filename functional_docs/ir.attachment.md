# BugFix-Studio-Misc — `ir.attachment`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.attachment` — Attachment

*Extends a model created by `base`.*

Other repos that use this model: `hr.payslip.action_export_bank_data_csv()` (bank-data)<br>`jinasena.paymaster.wizard.action_generate()` (bank-data)<br>`purchase.order.x_studio_photos` (BugFix-Purchase)<br>`purchase.order.x_studio_project_photos` (BugFix-Purchase)<br>`purchase.order.x_studio_specifications` (BugFix-Purchase)

**Summary:**

<!-- SUMMARY:model:ir.attachment -->
This repo adds the automation Restrict Attachment Delete for Approved Expenses: when an attachment is deleted, its server action blocks the deletion if the attachment belongs to an expense whose report is past Draft or Submitted. A second copy of the same server action is also shipped but is not linked to anything.
<!-- /SUMMARY -->

**Server actions (2):**

- **Execute Code** (`server_action_2598_restrict_attachment_delete_for_approved_expenses`, type `code`)
  - Function: Run by the Restrict Attachment Delete automation: blocks deleting attachments of expenses whose report is past Draft/Submitted.
  - Depends on: `model hr.expense` (hr_expense), `model ir.attachment` (base)
  - Used by: `automation BugFix-Studio-Misc.base_automation_274_restrict_attachment_delete_for_approved_expenses`
  <details><summary>code (8 lines)</summary>

```python

attach = env['ir.attachment'].search([('id', '=', record.id)])
if attach:
  for attachment in attach:
    if attachment.res_model == 'hr.expense' and attachment.res_id:
      expense = env['hr.expense'].browse(attachment.res_id)
      if expense.sheet_id.state not in ['draft', 'submit']:
        raise UserError("You cannot delete attachments from approved expenses.")
```
  </details>
- **Restrict Attachment Delete for Approved Expenses** (`sa_f5_ir_attachment_restrict_attachment_delete_for_approved_expenses`, type `code`)
  - Function: Blocks deleting an attachment of an expense whose expense report is beyond Draft/Submitted, raising 'You cannot delete attachments from approved expenses'.
  - Depends on: `model hr.expense` (hr_expense), `model ir.attachment` (base)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (7 lines)</summary>

```python
attach = env['ir.attachment'].search([('id', '=', record.id)])
if attach:
  for attachment in attach:
    if attachment.res_model == 'hr.expense' and attachment.res_id:
      expense = env['hr.expense'].browse(attachment.res_id)
      if expense.sheet_id.state not in ['draft', 'submit']:
        raise UserError("You cannot delete attachments from approved expenses.")
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| Restrict Attachment Delete for Approved Expenses | `base_automation_274_restrict_attachment_delete_for_approved_expenses` |  | When a record is deleted on Attachment, runs _Execute Code_. | `model ir.attachment` (base)<br>`server action BugFix-Studio-Misc.server_action_2598_restrict_attachment_delete_for_approved_expenses` |  |
