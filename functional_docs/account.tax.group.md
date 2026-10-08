# BugFix-Studio-Misc — `account.tax.group`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.tax.group` — Tax Group

*Extends a model created by `account`.*

Other repos that use this model: `access right BugFix-Accounting.access_f3_access_account_tax_group_rohana_read` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_g_access_account_tax_group_rohana_read_group_rohana` (BugFix-Accounting)<br>`record rule BugFix-Accounting.rule_768_tax_group_multi_company` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_1891_tax_groups` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:account.tax.group -->
This repo adds five read-only access rights on Tax Groups for its own security groups: the two Accounting Billing Limited groups, Accounting Test - Inheritance, Sales Jin - Sales - View Only and Sales User - New. No fields, views or actions are added.
<!-- /SUMMARY -->

**Access rights (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| account.tax.group | `access_g_account_tax_group_group_accounting_billing_limited_archived` | Gives **Accounting / Billing Limited (archived)** read access to Tax Group records. | `group BugFix-Studio-Misc.group_g_accounting_billing_limited_archived`<br>`model account.tax.group` (account) |  |
| account.tax.group | `access_g_account_tax_group_group_accounting_billing_limited_cashier` | Gives **Accounting / Billing limited - Cashier** read access to Tax Group records. | `group BugFix-Studio-Misc.group_g_accounting_billing_limited_cashier`<br>`model account.tax.group` (account) |  |
| account.tax.group | `access_g_account_tax_group_group_accounting_test_inheritance` | Gives **Accounting / Test - Inheritance** read access to Tax Group records. | `group BugFix-Studio-Misc.group_g_accounting_test_inheritance`<br>`model account.tax.group` (account) |  |
| account.tax.group sale manager | `access_g_account_tax_group_sale_manager_group_sales_jin_sales_view_only` | Gives **Sales / Jin - Sales - View Only** read access to Tax Group records. | `group BugFix-Studio-Misc.group_g_sales_jin_sales_view_only`<br>`model account.tax.group` (account) |  |
| account.tax.group sale manager | `access_g_account_tax_group_sale_manager_group_sales_user_new` | Gives **Sales User - New** read access to Tax Group records. | `group BugFix-Studio-Misc.group_g_misc_sales_user_new`<br>`model account.tax.group` (account) |  |
