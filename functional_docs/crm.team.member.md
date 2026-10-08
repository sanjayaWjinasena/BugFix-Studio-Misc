# BugFix-Studio-Misc — `crm.team.member`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `crm.team.member` — Sales Team Member

*Extends a model created by `sales_team`.*

**Summary:**

<!-- SUMMARY:model:crm.team.member -->
This repo adds a Sales Team Member window action, linked from two Studio-Misc menus, and an optional Company column in the Sales Team Members list. Nothing else is changed.
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales Team Member | `act_window_2882_sales_team_member` | Opens **Sales Team Member** records (kanban,tree,form). | `model crm.team.member` (sales_team) |  |
| Sales Team Member | `act_window_2882_sales_team_member_d7` | Opens **Sales Team Member** records (kanban,tree,form). | `model crm.team.member` (sales_team) | `menu BugFix-Studio-Misc.menu_f6_sales_team_member`<br>`menu BugFix-Studio-Misc.menu_f6r2_test_app_05_sales_sales_team_member` |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: crm.team.member.view.tree customization | `view_6118_odoo_studio_crm_team_member_view_tree_customization_ext` | tree | after `//field[@name='lead_month_count']`: add field company_id | Adds an optional Company column to the Sales Team Members list. | `crm.team.member.company_id` (sales_team)<br>`view crm.crm_team_member_view_tree` (crm) |  |
