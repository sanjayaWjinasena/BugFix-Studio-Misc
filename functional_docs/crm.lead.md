# BugFix-Studio-Misc — `crm.lead`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `crm.lead` — Lead/Opportunity

*Extends a model created by `crm`.*

**Summary:**

<!-- SUMMARY:model:crm.lead -->
This repo adds the server action Mark as lost, which marks leads as lost directly and opens the standard lost-reason wizard for opportunities; it is not linked to a button, menu or automation. It also adds a My Activities window action and three record rules: all leads for All Documents users, own or unassigned leads for Own Documents Only users, and a global multi-company rule.
<!-- /SUMMARY -->

**Server actions (1):**

- **Mark as lost** (`server_action_1230_mark_as_lost`, type `code`)
  - Function: Marks CRM leads as lost: plain leads are lost directly, while opportunities open the standard 'Mark Lost' reason wizard.
  - Depends on: `model crm.lead` (crm)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (7 lines)</summary>

```python

if not 'opportunity' in records.mapped('type'):
    records.action_set_lost()
elif records:
    action_values = env.ref('crm.crm_lead_lost_action').sudo().read()[0]
    action_values.update({'context': env.context})
    action = action_values
```
  </details>
**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| My Activities | `act_window_1232_my_activities` | Opens **Lead/Opportunity** records (tree,kanban,graph,pivot,calendar,form,activity), filtered to `[("activity_ids.active", "in", [True, False])]`. | `crm.lead.activity_ids` (crm)<br>`mail.activity.active` (mail)<br>`model crm.lead` (crm) |  |

**Record rules (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| All Leads | `rule_313_all_leads` | For Sales / User: All Documents: read/write/create/delete on Lead/Opportunity with no record filter (empty domain = all records). | `group sales_team.group_sale_salesman_all_leads` (sales_team)<br>`model crm.lead` (crm) |  |
| CRM Lead Multi-Company | `rule_312_crm_lead_multi_company` | For everyone (global rule): read/write/create/delete on Lead/Opportunity only where `[('company_id', 'in', company_ids + [False])]`. | `crm.lead.company_id` (crm)<br>`model crm.lead` (crm) |  |
| Personal Leads | `rule_311_personal_leads` | For Sales / User: Own Documents Only: read/write/create/delete on Lead/Opportunity only where `['|',('user_id','=',user.id),('user_id','=',False)]`. | `crm.lead.user_id` (crm)<br>`group sales_team.group_sale_salesman` (sales_team)<br>`model crm.lead` (crm) |  |
