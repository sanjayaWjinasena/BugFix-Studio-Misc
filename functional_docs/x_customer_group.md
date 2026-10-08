# BugFix-Studio-Misc — `x_customer_group`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_customer_group` — Customer Group

*Extends a model created by `studio_usermodel_migration`.*

Other repos that use this model: `access right studio_usermodel_migration.access_1386_customer_group_group_system` (studio_usermodel_migration)<br>`access right studio_usermodel_migration.access_1387_customer_group_group_user` (studio_usermodel_migration)<br>`access right studio_usermodel_migration.access_x_customer_group_system` (studio_usermodel_migration)<br>`access right studio_usermodel_migration.access_x_customer_group_user` (studio_usermodel_migration)<br>`automation studio_usermodel_migration.base_automation_312_jin_company_id_in_customer_group` (studio_usermodel_migration)<br>`record rule studio_usermodel_migration.rule_564_jin_multi_company_customer_group` (studio_usermodel_migration)<br>`record rule studio_usermodel_migration.rule_f7_x_customer_group_jin_multi_company_customer_group` (studio_usermodel_migration)<br>`res.partner.x_studio_customer_group` (studio_usermodel_migration)<details><summary>+7 more</summary>`res.users.x_studio_customer_group1` (studio_usermodel_migration)<br>`res.users.x_studio_customer_group` (studio_usermodel_migration)<br>`res.users.x_studio_many2one_field_hl9yL` (studio_usermodel_migration)<br>`server action studio_usermodel_migration.sa_f5_x_customer_group_jin_company_id_in_customer_group` (studio_usermodel_migration)<br>`server action studio_usermodel_migration.server_action_2676_jin_company_id_in_customer_group` (studio_usermodel_migration)<br>`window action studio_usermodel_migration.act_window_1443_customer_groups` (studio_usermodel_migration)<br>`x_rm_sales_order_line.x_studio_customer_group` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:x_customer_group -->
This repo adds a Studio customization to the Customer Group form. The Name field is relabelled as Code, and the form gains a Description, a required Payment Term, a Receivable Account, a Group Type and a read-only Company. It also adds a Customers smart button that counts the linked contacts and a Linked Customers tab that lists those contacts with their payment method and credit.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: Default form view for x_customer_group customization | `view_x_customer_group_form_studio_ext` | form | before `//widget[@name='web_ribbon']`: add div; set string=Code on `//field[@name='x_name']`; inside `//group[@name='studio_group_36e52f_left']`: add field x_studio_description, field x_studio_payment_term, field x_studio_receivable_account, field x_studio_group_type, field x_studio_company_id; after `//group[@name='studio_group_36e52f']`: add notebook | Extends the Customer Group form: adds a 'Customers' smart button (count of linked contacts, hidden when zero), labels Name as 'Code', adds Description, required Payment Term, Receivable Account and Group Type, read-only Company, and a 'Linked Customers' tab listing contacts with payment method and credit. | `res.partner.credit` (account)<br>`res.partner.name` (base)<br>`res.partner.x_studio_payment_method` (BugFix-Sales)<br>`view studio_usermodel_migration.view_3114_default_form_view_for_x_customer_group_e` (studio_usermodel_migration)<br>`window action website_event.event_registration_action_from_visitor` (website_event)<details><summary>+7 more</summary>`x_customer_group.x_studio_company_id` (studio_usermodel_migration)<br>`x_customer_group.x_studio_description` (studio_usermodel_migration)<br>`x_customer_group.x_studio_group_type` (studio_usermodel_migration)<br>`x_customer_group.x_studio_one2many_field_hfDGm` (studio_usermodel_migration)<br>`x_customer_group.x_studio_payment_term` (studio_usermodel_migration)<br>`x_customer_group.x_studio_receivable_account` (studio_usermodel_migration)<br>`x_customer_group.x_x_studio_customer_group__res_partner_count` (studio_usermodel_migration)</details> |  |
