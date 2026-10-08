# BugFix-Studio-Misc — `res.groups`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `res.groups` — Access Groups

*Extends a model created by `base`.*

Other repos that use this model: `automation studio_usermodel_migration.base_automation_208_janitha_ranasinghe` (studio_usermodel_migration)<br>`mail template studio_usermodel_migration.mail_template_55_janitha_ranasinghe` (studio_usermodel_migration)<br>`mail template studio_usermodel_migration.mail_template_74_user_group_updation` (studio_usermodel_migration)<br>`server action studio_usermodel_migration.server_action_2266_janitha_ranasinghe` (studio_usermodel_migration)

**Summary:**

<!-- SUMMARY:model:res.groups -->
This repo adds a server action, User Group Change - Notify, that emails 'Access Rights have Changed' to a hard-coded address (rohana.b@jinasena.com.lk). Nothing in this repo links that action to a button, menu or automation. It also adds three automations on access groups, but none of them has an action linked, so they do nothing. Two of them are archived.
<!-- /SUMMARY -->

**Server actions (1):**

- **User Group Change - Notify** (`sa_f5_res_groups_user_group_change_notify`, type `code`)
  - Function: Sends an 'Access Rights have Changed' email to a hard-coded address (rohana.b@jinasena.com.lk) when run on a user group; workaround for the original post-message action since groups have no chatter.
  - Depends on: `model mail.mail` (mail), `model res.groups` (base)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (8 lines)</summary>

```python
# Workaround: original mail_post SA can't run on res.groups (no mail.thread).
# Manual mail.mail create + send.
env['mail.mail'].sudo().create({
    'subject': 'Access Rights have Changed',
    'body_html': '<p>Access Rights have Changed.....</p>',
    'email_to': 'rohana.b@jinasena.com.lk',
    'auto_delete': True,
}).send()
```
  </details>
**Automations (3):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| Janitha Ranasinghe | `base_automation_208_janitha_ranasinghe_d7` |  | When a record is created or updated on Access Groups, runs nothing (no action linked). | `model res.groups` (base) |  |
| User Group Change - Notify | `base_automation_244_user_group_change_notify_d7` | archived | When a record is updated on Access Groups, runs nothing (no action linked). **Archived — does not run.** | `model res.groups` (base) |  |
| User Group updation | `base_automation_245_user_group_updation_d7` | archived | When a record is updated on Access Groups, runs nothing (no action linked). **Archived — does not run.** | `model res.groups` (base) |  |
