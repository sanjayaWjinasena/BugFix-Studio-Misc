# BugFix-Studio-Misc — `customer_group`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `customer_group` — Customer Group

*Extends a model created by `studio_usermodel_migration`.*

Other repos that use this model: `access right studio_usermodel_migration.access_customer_group_group_system` (studio_usermodel_migration)<br>`access right studio_usermodel_migration.access_customer_group_group_user` (studio_usermodel_migration)<br>`access right studio_usermodel_migration.access_customer_group_system` (studio_usermodel_migration)<br>`access right studio_usermodel_migration.access_customer_group_user` (studio_usermodel_migration)<br>`automation studio_usermodel_migration.automation_jin_company_id_in_customer_group` (studio_usermodel_migration)<br>`record rule studio_usermodel_migration.rule_jin_multi_company_customer_group` (studio_usermodel_migration)<br>`record rule studio_usermodel_migration.rule_f7_customer_group_jin_multi_company_customer_group` (studio_usermodel_migration)<br>`res.partner.customer_group` (studio_usermodel_migration)<details><summary>+7 more</summary>`res.users.customer_group1` (studio_usermodel_migration)<br>`res.users.customer_group` (studio_usermodel_migration)<br>`res.users.many2one_field_hl9yL` (studio_usermodel_migration)<br>`server action studio_usermodel_migration.action_customer_group_jin_company_id_in_customer_group` (studio_usermodel_migration)<br>`server action studio_usermodel_migration.action_jin_company_id_in_customer_group` (studio_usermodel_migration)<br>`window action studio_usermodel_migration.action_customer_groups` (studio_usermodel_migration)<br>`rm_sales_order_line.customer_group` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:customer_group -->
This repo adds a Studio customization to the Customer Group form. The Name field is relabelled as Code, and the form gains a Description, a required Payment Term, a Receivable Account, a Group Type and a read-only Company. It also adds a Customers smart button that counts the linked contacts and a Linked Customers tab that lists those contacts with their payment method and credit.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: Default form view for customer_group customization | `view_customer_group_form_studio_ext` | form | before `//widget[@name='web_ribbon']`: add div; set string=Code on `//field[@name='name']`; inside `//group[@name='studio_group_36e52f_left']`: add field description, field payment_term, field receivable_account, field group_type, field accounting_company_id; after `//group[@name='studio_group_36e52f']`: add notebook | Extends the Customer Group form: adds a 'Customers' smart button (count of linked contacts, hidden when zero), labels Name as 'Code', adds Description, required Payment Term, Receivable Account and Group Type, read-only Company, and a 'Linked Customers' tab listing contacts with payment method and credit. | `res.partner.credit` (account)<br>`res.partner.name` (base)<br>`res.partner.payment_method` (BugFix-Sales)<br>`view studio_usermodel_migration.view_customer_group_form` (studio_usermodel_migration)<br>`window action website_event.event_registration_action_from_visitor` (website_event)<details><summary>+7 more</summary>`customer_group.accounting_company_id` (studio_usermodel_migration)<br>`customer_group.description` (studio_usermodel_migration)<br>`customer_group.group_type` (studio_usermodel_migration)<br>`customer_group.one2many_field_hfDGm` (studio_usermodel_migration)<br>`customer_group.payment_term` (studio_usermodel_migration)<br>`customer_group.receivable_account` (studio_usermodel_migration)<br>`customer_group.customer_group__res_partner_count` (studio_usermodel_migration)</details> |  |
