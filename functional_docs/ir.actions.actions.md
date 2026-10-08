# BugFix-Studio-Misc — `ir.actions.actions`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.actions.actions` — Actions

*Extends a model created by `base`.*

**Summary:**

<!-- SUMMARY:model:ir.actions.actions -->
This repo adds a Studio tweak to the generic Actions list view that shows the record ID after Name. Nothing else is changed.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: ir.actions.actions.tree customization | `view_std_ir_actions_actions_2416` | tree | after `//tree[1]/field[@name='name']`: add field id | Adds the record ID column after Name in the generic Actions list view (Settings > Technical). | `view base.action_view_tree` (base) |  |
