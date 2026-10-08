# BugFix-Studio-Misc — `helpdesk.team`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `helpdesk.team` — Helpdesk Team

*Extends a model created by `helpdesk`.*

Other repos that use this model: `record rule Fix-repair.rule_360_helpdesk_administrator` (Fix-repair)<br>`record rule Fix-repair.rule_362_helpdesk_user` (Fix-repair)<br>`record rule Fix-repair.rule_365_team_multi_company` (Fix-repair)<br>`record rule Fix-repair.rule_695_public_user_published_helpdesk_team` (Fix-repair)<br>`window action Fix-repair.act_window_2239_customer_letter_report` (Fix-repair)<br>`window action Fix-repair.act_window_2876_helpdesk_team_helpdesk_team` (Fix-repair)

**Summary:**

<!-- SUMMARY:model:helpdesk.team -->
This repo adds two window actions on Helpdesk Teams (Customer Letter Report and Helpdesk Team), an optional ID column in the Helpdesk Teams list and a Helpdesk Team Report PDF. No fields or rules are added.
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Customer Letter Report | `act_window_2239_customer_letter_report_d7` | Opens **Helpdesk Team** records (kanban,tree,form). | `model helpdesk.team` (helpdesk) |  |
| Helpdesk Team (helpdesk.team) | `act_window_2876_helpdesk_team_helpdesk_team_d7` | Opens **Helpdesk Team** records (kanban,tree,form). | `model helpdesk.team` (helpdesk) |  |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: helpdesk.team.tree customization | `view_std_helpdesk_team_5302` | tree | after `//field[@name="use_alias"]`: add field id | Adds an optional (shown by default) ID column after the email alias toggle in the Helpdesk Teams list view. | `view helpdesk.helpdesk_team_view_tree` (helpdesk) |  |

**Reports (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Helpdesk Team Report | `action_report_3491_helpdesk_team_report` | Prints **Helpdesk Team Report** (qweb-pdf) for helpdesk.team records using template `studio_customization.studio_report_docume_50c3b9df-c892-4cb5-97d5-e049b72e9f8b`. | `model helpdesk.team` (helpdesk)<br>`record studio_customization.studio_report_docume_50c3b9df-c892-4cb5-97d5-e049b72e9f8b` (studio_customization) |  |
