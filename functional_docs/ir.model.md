# BugFix-Studio-Misc — `ir.model`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.model` — Models

*Extends a model created by `base`.*

Other repos that use this model: `x_repair_master_data.migration._migrate_studio_repair_master_data_to_base()` (Fix-repair)

**Summary:**

<!-- SUMMARY:model:ir.model -->
This repo adds an empty Studio customization of the Model form that has no visible effect. Nothing else is changed.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: ir.model form customization | `view_std_ir_model_3111` | form | after `//form[1]/sheet[1]/notebook[1]/page[@name='fields']/field[@name='field_id']/tree[1]/field[@name='ttype']`: add | Empty Studio customization of the Model form (xpath after the fields table's Type column adds nothing); has no visible effect. | `view base.view_model_form` (base) |  |
