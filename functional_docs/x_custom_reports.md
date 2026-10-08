# BugFix-Studio-Misc — `x_custom_reports`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_custom_reports` — Custom Reports

*Extends a model created by `BugFix-Custom-Reports`.*

Other repos that use this model: `access right BugFix-Custom-Reports.access_8259_custom_reports_group_system` (BugFix-Custom-Reports)<br>`access right BugFix-Custom-Reports.access_8260_custom_reports_group_user` (BugFix-Custom-Reports)<br>`access right BugFix-Custom-Reports.access_x_custom_reports_user` (BugFix-Custom-Reports)<br>`record rule BugFix-Custom-Reports.rule_880_custom_reports_multi_company` (BugFix-Custom-Reports)<br>`window action BugFix-Custom-Reports.act_window_3347_jinasena_custom_reports` (BugFix-Custom-Reports)<br>`x_custom_reports_line_c55e7.x_custom_reports_id` (BugFix-Custom-Reports)

**Summary:**

<!-- SUMMARY:model:x_custom_reports -->
This repo only adds three PDF reports, all named Custom Reports Report, that print Custom Reports records from different Studio report templates. The model itself comes from BugFix-Custom-Reports.
<!-- /SUMMARY -->

**Reports (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Custom Reports Report | `action_report_3368_custom_reports_report` | Prints **Custom Reports Report** (qweb-pdf) for x_custom_reports records using template `studio_customization.studio_report_docume_bd0f3923-a7f4-4086-bb6a-899bb01fd315`. | `model x_custom_reports` (BugFix-Custom-Reports)<br>`record studio_customization.studio_report_docume_bd0f3923-a7f4-4086-bb6a-899bb01fd315` (studio_customization) |  |
| Custom Reports Report | `action_report_3435_custom_reports_report` | Prints **Custom Reports Report** (qweb-pdf) for x_custom_reports records using template `studio_customization.studio_report_docume_96136e4a-ca46-4d87-890d-01114a610c91`. | `model x_custom_reports` (BugFix-Custom-Reports)<br>`record studio_customization.studio_report_docume_96136e4a-ca46-4d87-890d-01114a610c91` (studio_customization) |  |
| Custom Reports Report | `action_report_3436_custom_reports_report` | Prints **Custom Reports Report** (qweb-pdf) for x_custom_reports records using template `studio_customization.studio_report_docume_5beecb7c-3184-45c9-b2ed-2b6f709186da`. | `model x_custom_reports` (BugFix-Custom-Reports)<br>`record studio_customization.studio_report_docume_5beecb7c-3184-45c9-b2ed-2b6f709186da` (studio_customization) |  |
