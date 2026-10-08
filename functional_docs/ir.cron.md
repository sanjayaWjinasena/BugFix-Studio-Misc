# BugFix-Studio-Misc — `ir.cron`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `ir.cron` — Scheduled Actions

*Extends a model created by `base`.*

**Summary:**

<!-- SUMMARY:model:ir.cron -->
This repo adds a Studio tweak to the Scheduled Actions list view that moves the Active column after Number of Calls and adds an optional ID column. Nothing else is changed.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: ir.cron tree customization | `view_std_ir_cron_6148` | tree | after `//field[@name='numbercall']`: add xpath, field id | In the Scheduled Actions list view, moves the Active column after Number of Calls and adds an optional ID column. | `view base.ir_cron_view_tree` (base) |  |
