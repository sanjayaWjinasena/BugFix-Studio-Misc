# BugFix-Studio-Misc — `crm.team`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `crm.team` — Sales Team

*Extends a model created by `sales_team`.*

Other repos that use this model: `account.move.line.x_studio_sales_team` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1670_rpt_daily_sales_report_generate` (BugFix-Accounting)<br>`x_rm_cust_invoice_s1.x_studio_sales_centre` (BugFix-Accounting)<br>`x_rm_daily_s1.x_studio_sales_centre` (BugFix-Accounting)<br>`x_rm_daily_s2.x_studio_sales_centre` (BugFix-Accounting)<br>`x_rm_daily_s3.x_studio_sales_centre` (BugFix-Accounting)<br>`x_sales_report_model.x_studio_sales_centre` (Jinasena_Masterdata_Reporting)

**Summary:**

<!-- SUMMARY:model:crm.team -->
This repo adds a Sales Teams window action, a members list layout inside the Sales Team form (name, login, language, last login, company, active and audit columns) and an optional Created by column in the Sales Teams list. It also adds three record rules: full access for All Documents salespeople and for POS administrators, and a global multi-company rule.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sales Teams | `act_window_396_sales_teams` | Opens **Sales Team** records (tree,kanban,form). | `model crm.team` (sales_team) |  |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: crm.team.form customization | `view_6053_odoo_studio_crm_team_form_customization_ext` | form | after `//form[1]/sheet[1]/notebook[1]/page[@name='members_users']/field[@name='member_ids']/kanban[1]`: add tree | Extends the Sales Team form: adds a list layout for the team Members field (name, login, language, last login, company, active, created by/on, ID) alongside the standard kanban. | `crm.team.active` (sales_team)<br>`crm.team.company_id` (sales_team)<br>`crm.team.name` (sales_team)<br>`group base.group_multi_company` (base)<br>`view sale.crm_team_salesteams_view_form` (sale) |  |
| Odoo Studio: crm.team.tree customization | `view_6079_odoo_studio_crm_team_tree_customization_ext` | tree | after `//field[@name='company_id']`: add field create_uid | Adds an optional 'Created by' column to the Sales Teams list. | `view sales_team.crm_team_view_tree` (sales_team) |  |

**Record rules (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| All Salesteam | `rule_116_all_salesteam` | For Sales / User: All Documents: read/write/create/delete on Sales Team with no record filter (empty domain = all records). | `group sales_team.group_sale_salesman_all_leads` (sales_team)<br>`model crm.team` (sales_team) |  |
| POS Sales Team | `rule_189_pos_sales_team` | For Point of Sale / Administrator: read/write/create/delete on Sales Team with no record filter (empty domain = all records). | `group point_of_sale.group_pos_manager` (point_of_sale)<br>`model crm.team` (sales_team) |  |
| Sales Team multi-company | `rule_117_sales_team_multi_company` | For everyone (global rule): read/write/create/delete on Sales Team only where `[('company_id', 'in', company_ids + [False])]`. | `crm.team.company_id` (sales_team)<br>`model crm.team` (sales_team) |  |
