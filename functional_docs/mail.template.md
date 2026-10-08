# BugFix-Studio-Misc — `mail.template`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `mail.template` — Email Templates

*Extends a model created by `mail`.*

Other repos that use this model: `helpdesk.ticket._repair_send_stage13_email()` (Fix-repair)<br>`sale.order.action_quotation_send()` (Fix-Repair-Wizard-Nav, Fix-repair)<br>`server action BugFix-Purchase.server_action_2259_proj_send_specification_by_email` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2287_send_specification_by_email_user_manual` (BugFix-Purchase)

**Summary:**

<!-- SUMMARY:model:mail.template -->
This repo adds an optional ID column after To (Partners) in the Email Templates list view. Nothing else is changed.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: email.template.tree customization | `view_std_mail_template_5042` | tree | after `//field[@name="partner_to"]`: add field id | Adds an optional (shown by default) ID column after the To (Partners) field in the Email Templates list view. | `view mail.email_template_tree` (mail) |  |
