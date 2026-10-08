# BugFix-Studio-Misc — `mrp.eco.bom.change`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `mrp.eco.bom.change` — ECO BoM changes

*Extends a model created by `mrp_plm`.*

Other repos that use this model: `window action BugFix-MRP.act_window_2306_ecos` (BugFix-MRP)<br>`window action BugFix-MRP.act_window_2834_mrp_eco_bom_change` (BugFix-MRP)

**Summary:**

<!-- SUMMARY:model:mrp.eco.bom.change -->
This repo adds two window actions on ECO BoM changes: ECOs, which lists the changes of the current ECO, and a form-only action linked from the Test App 05 menu tree. Nothing else is changed.
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| ECOs | `act_window_2306_ecos_d7` | Opens **ECO BoM changes** records (tree,form), filtered to `[('eco_id', '=', active_id)]`. | `model mrp.eco.bom.change` (mrp_plm)<br>`mrp.eco.bom.change.eco_id` (mrp_plm) |  |
| mrp.eco.bom.change | `act_window_2834_mrp_eco_bom_change_d7` | Opens **ECO BoM changes** records (form). | `model mrp.eco.bom.change` (mrp_plm) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_mrp_eco_bom_change` |
