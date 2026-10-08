# BugFix-Studio-Misc — `crm.activity.report`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `crm.activity.report` — CRM Activity Analysis

*Extends a model created by `crm`.*

**Summary:**

<!-- SUMMARY:model:crm.activity.report -->
This repo adds three record rules on the CRM Activity Analysis report: users with All Documents see every activity, users with Own Documents Only see activities assigned to them or unassigned, and a global multi-company rule limits records to the user's companies.
<!-- /SUMMARY -->

**Record rules (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| All Activities | `rule_314_all_activities` | For Sales / User: All Documents: read/write/create/delete on CRM Activity Analysis with no record filter (empty domain = all records). | `group sales_team.group_sale_salesman_all_leads` (sales_team)<br>`model crm.activity.report` (crm) |  |
| CRM Lead Multi-Company | `rule_316_crm_lead_multi_company` | For everyone (global rule): read/write/create/delete on CRM Activity Analysis only where `[('company_id', 'in', company_ids + [False])]`. | `crm.activity.report.company_id` (crm)<br>`model crm.activity.report` (crm) |  |
| Personal Activities | `rule_315_personal_activities` | For Sales / User: Own Documents Only: read/write/create/delete on CRM Activity Analysis only where `['|',('user_id','=',user.id),('user_id','=',False)]`. | `crm.activity.report.user_id` (crm)<br>`group sales_team.group_sale_salesman` (sales_team)<br>`model crm.activity.report` (crm) |  |
