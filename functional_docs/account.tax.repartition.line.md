# BugFix-Studio-Misc — `account.tax.repartition.line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.tax.repartition.line` — Tax Repartition Line

*Extends a model created by `account`.*

Other repos that use this model: `record rule BugFix-Accounting.rule_631_tax_repartition_multi_company` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:account.tax.repartition.line -->
This repo adds three read-only access rights on Tax Repartition Lines for its Accounting groups Billing Limited (archived), Billing limited - Cashier and Test - Inheritance. Nothing else is changed.
<!-- /SUMMARY -->

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| account.tax repartition.line.invoice | `access_g_account_tax_repartition_line_invoice_line_accounting_billing_limited_archived` | Gives **Accounting / Billing Limited (archived)** read access to Tax Repartition Line records. | `group BugFix-Studio-Misc.group_g_accounting_billing_limited_archived`<br>`model account.tax.repartition.line` (account) |  |
| account.tax repartition.line.invoice | `access_g_account_tax_repartition_line_invoice_line_accounting_billing_limited_cashier` | Gives **Accounting / Billing limited - Cashier** read access to Tax Repartition Line records. | `group BugFix-Studio-Misc.group_g_accounting_billing_limited_cashier`<br>`model account.tax.repartition.line` (account) |  |
| account.tax repartition.line.invoice | `access_g_account_tax_repartition_line_invoice_line_accounting_test_inheritance` | Gives **Accounting / Test - Inheritance** read access to Tax Repartition Line records. | `group BugFix-Studio-Misc.group_g_accounting_test_inheritance`<br>`model account.tax.repartition.line` (account) |  |
