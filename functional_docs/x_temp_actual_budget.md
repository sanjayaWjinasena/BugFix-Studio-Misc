# BugFix-Studio-Misc — `x_temp_actual_budget`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_temp_actual_budget` — Temp_Actual_Budget

*Extends a model created by `BugFix-Accounting`.*

Other repos that use this model: `access right BugFix-Accounting.access_1753_temp_actual_budget_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_1754_temp_actual_budget_group_user` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_x_temp_actual_budget_user` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_2123_temp_actual_budget` (BugFix-Accounting)<br>`x_rm_gross_margin_actu.x_studio_budget_line_ids` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:x_temp_actual_budget -->
Temp_Actual_Budget is created by BugFix-Accounting. This repo only adds read access for Accounting / Jin - ProjectInvoice.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp. Budget | `access_g_temp_budget_x_temp_actual_budget_accounting_jin_projectinvoice` | Gives **Accounting / Jin - ProjectInvoice** read access to Temp_Actual_Budget records. | `group BugFix-Studio-Misc.group_g_accounting_jin_projectinvoice`<br>`model x_temp_actual_budget` (BugFix-Accounting) |  |
