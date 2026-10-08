# BugFix-Studio-Misc — `account.tax.unit`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.tax.unit` — Tax Unit

*Extends a model created by `account_reports`.*

**Summary:**

<!-- SUMMARY:model:account.tax.unit -->
This repo adds one read-only access right on Tax Units for its Accounting / Test - Inheritance group. Nothing else is changed.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| access_account_tax_unit_readonly | `access_g_access_account_tax_unit_readonly_unit_accounting_test_inheritance` | Gives **Accounting / Test - Inheritance** read access to Tax Unit records. | `group BugFix-Studio-Misc.group_g_accounting_test_inheritance`<br>`model account.tax.unit` (account_reports) |  |
