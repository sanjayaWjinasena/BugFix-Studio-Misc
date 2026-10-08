# BugFix-Studio-Misc — `ir.default`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.default` — Default Values

*Extends a model created by `base`.*

**Summary:**

<!-- SUMMARY:model:ir.default -->
This repo adds an optional Created by column in the User-defined Defaults list view. Nothing else is changed on the model; the repo's default values themselves are listed in the root document.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: ir.default tree view customization | `view_std_ir_default_6116` | tree | after `//field[@name='json_value']`: add field create_uid | Adds an optional Created by column after the default value in the User-defined Defaults list view. | `view base.ir_default_tree_view` (base) |  |
