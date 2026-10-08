# BugFix-Studio-Misc — `account.payment.term`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.payment.term` — Payment Terms

*Extends a model created by `account`.*

Other repos that use this model: `automation BugFix-Accounting.base_automation_335_jin_company_id_in_payment_terms` (BugFix-Accounting)<br>`record rule BugFix-Accounting.rule_92_account_payment_term_company_rule` (BugFix-Accounting)<br>`res.users.x_studio_payment_term` (studio_usermodel_migration)<br>`res.users.x_studio_related_field_j3X4Q` (studio_usermodel_migration)<br>`res.users.x_studio_related_field_ngmve` (studio_usermodel_migration)<br>`res.users.x_studio_related_field_tLbBY` (studio_usermodel_migration)<br>`res.users.x_studio_terms_of_payment` (studio_usermodel_migration)<br>`server action BugFix-Accounting.server_action_2827_jin_company_id_in_payment_terms` (BugFix-Accounting)<details><summary>+2 more</summary>`x_customer_group.x_studio_payment_term` (studio_usermodel_migration)<br>`x_vendor_group.x_studio_payment_term` (studio_usermodel_migration)</details>

**Summary:**

<!-- SUMMARY:model:account.payment.term -->
This repo adds the server action JIN - Company Id in Payment Terms, which sets a payment term's company to the user's currently active company. It is not linked to any button, menu or automation in this repo; BugFix-Accounting has a matching automation for payment terms.
<!-- /SUMMARY -->

**Server actions (1):**

- **JIN - Company Id in Payment Terms** (`server_action_2827_jin_company_id_in_payment_terms_d7`, type `code`)
  - Function: Sets the Company of a payment term to the user's currently active company.
  - Depends on: `model account.payment.term` (account), `model res.company` (base)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['company_id'] = company.id
```
  </details>
