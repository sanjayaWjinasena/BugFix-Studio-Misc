# BugFix-Studio-Misc — `uom.category`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `uom.category` — Product UoM Categories

*Extends a model created by `uom`.*

**Summary:**

<!-- SUMMARY:model:uom.category -->
This repo only adds two UoM Categories window actions in list and form views. One is linked to a UoM Categories menu under the Inventory configuration menu (BugFix-Stock).
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| UoM Categories | `act_window_2472_uom_categories` | Opens **Product UoM Categories** records (tree,form). | `model uom.category` (uom) | `menu BugFix-Studio-Misc.menu_f6_uom_categories` |
| UoM Categories | `act_window_2472_uom_categories_d7` | Opens **Product UoM Categories** records (tree,form). | `model uom.category` (uom) |  |
