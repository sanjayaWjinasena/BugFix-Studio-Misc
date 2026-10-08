# BugFix-Studio-Misc — `ir.property`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.property` — Company Property

*Extends a model created by `base`.*

**Summary:**

<!-- SUMMARY:model:ir.property -->
This repo adds one window action, Company Property, that opens company properties in list and form views and is linked from a Studio-Misc menu. Nothing else is changed.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Company Property | `aw_f4x_ir_property_company_property` | Opens **Company Property** records (tree,form). | `model ir.property` (base) | `menu BugFix-Studio-Misc.menu_f6f_company_property` |
