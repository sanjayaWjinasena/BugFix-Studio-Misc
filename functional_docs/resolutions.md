# BugFix-Studio-Misc — `resolutions`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `resolutions` — Resolutions

*Extends a model created by `Fix-repair`.*

Other repos that use this model: `access right Fix-repair.access_1794_resolutions_group_system` (Fix-repair)<br>`access right Fix-repair.access_1795_resolutions_group_user` (Fix-repair)<br>`access right Fix-repair.access_x_resolutions_manager` (Fix-repair)<br>`access right Fix-repair.access_x_resolutions_user` (Fix-repair)<br>`automation Fix-repair.base_automation_305_jin_company_id_in_resolutions` (Fix-repair)<br>`record rule Fix-repair.rule_560_jin_multi_company_resolutions` (Fix-repair)<br>`record rule Fix-repair.rule_f7_x_resolutions_jin_multi_company_resolutions` (Fix-repair)<br>`server action Fix-repair.sa_f5_x_resolutions_jin_company_id_in_resolutions` (Fix-repair)<details><summary>+4 more</summary>`server action Fix-repair.server_action_2669_jin_company_id_in_resolutions` (Fix-repair)<br>`window action Fix-repair.act_window_2215_resolutions` (Fix-repair)<br>`window action Fix-repair.action_resolutions` (Fix-repair)<br>`task_diagnosis.resolution` (Fix-repair)</details>

**Summary:**

<!-- SUMMARY:model:resolutions -->
Resolutions is created by Fix-repair. This repo only adds the Resolutions Report qweb-pdf print action, which uses a Studio report template.
<!-- /SUMMARY -->

**Reports (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Resolutions Report | `action_report_3490_resolutions_report` | Prints **Resolutions Report** (qweb-pdf) for resolutions records using template `studio_customization.studio_report_docume_e996c666-0ac8-4b32-a472-c92b4d11fdc1`. | `model resolutions` (Fix-repair)<br>`record studio_customization.studio_report_docume_e996c666-0ac8-4b32-a472-c92b4d11fdc1` (studio_customization) |  |
