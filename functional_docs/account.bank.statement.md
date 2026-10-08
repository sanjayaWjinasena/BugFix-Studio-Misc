# BugFix-Studio-Misc — `account.bank.statement`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `account.bank.statement` — Bank Statement

*Extends a model created by `account`.*

Other repos that use this model: `record rule BugFix-Accounting.rule_146_point_of_sale_bank_statement_pos_user` (BugFix-Accounting)<br>`record rule BugFix-Accounting.rule_147_point_of_sale_bank_statement_accountant` (BugFix-Accounting)<br>`record rule BugFix-Accounting.rule_87_account_bank_statement_company_rule` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_2815_account_bank_statement` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:account.bank.statement -->
This repo adds one window action (account.bank.statement) that opens Bank Statements in list, form, pivot and graph views. It is not linked to a menu here. Nothing else is changed.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| account.bank.statement | `act_window_2815_account_bank_statement_d7` | Opens **Bank Statement** records (tree,form,pivot,graph). | `model account.bank.statement` (account) |  |
