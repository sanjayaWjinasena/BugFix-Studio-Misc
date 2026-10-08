# BugFix-Studio-Misc — `ir.rule`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.rule` — Rule

*Extends a model created by `base`.*

**Summary:**

<!-- SUMMARY:model:ir.rule -->
This repo adds two empty Studio customizations of the Record Rule form and list that have no visible effect. Nothing else is changed on the model; the repo's own record rules are listed under the models they restrict.
<!-- /SUMMARY -->

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: ir.rule form customization | `view_std_ir_rule_5297` | form | after `//field[@name='perm_create']`: add | Empty Studio customization of the Record Rule form (xpath after Create permission adds nothing); has no visible effect. | `view base.view_rule_form` (base) |  |
| Odoo Studio: ir.rule tree customization | `view_std_ir_rule_5296` | tree | after `//field[@name='domain_force']`: add | Empty Studio customization of the Record Rules list (xpath after Domain adds nothing); has no visible effect. | `view base.view_rule_tree` (base) |  |
