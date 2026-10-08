# BugFix-Studio-Misc — `pos.session`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `pos.session` — Point of Sale Session

*Extends a model created by `point_of_sale`.*

**Summary:**

<!-- SUMMARY:model:pos.session -->
This repo only adds two window actions that open Point of Sale Session records in kanban, list and form views. One of them is linked to a pos.session entry under the TEST APP 05 menu. No fields, views or logic are changed.
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| pos.session | `act_window_2822_pos_session` | Opens **Point of Sale Session** records (kanban,tree,form). | `model pos.session` (point_of_sale) |  |
| pos.session | `act_window_2822_pos_session_d7` | Opens **Point of Sale Session** records (kanban,tree,form). | `model pos.session` (point_of_sale) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_pos_session` |
