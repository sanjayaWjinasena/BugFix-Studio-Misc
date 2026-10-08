# BugFix-Studio-Misc — `calendar.filters`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `calendar.filters` — Calendar Filters

*Extends a model created by `calendar`.*

**Summary:**

<!-- SUMMARY:model:calendar.filters -->
This repo adds window actions that open Calendar Filters in list and form views, linked from the Test App 05 and other Studio-Misc menus. It also adds a minimal list view that shows only the record ID.
<!-- /SUMMARY -->

**Window actions (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Calendar.filters | `act_window_2830_calendar_filters` | Opens **Calendar Filters** records (tree,form). | `model calendar.filters` (calendar) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_calendar_filters` |
| Calendar.filters | `act_window_2830_calendar_filters_d7` | Opens **Calendar Filters** records (tree,form). | `model calendar.filters` (calendar) |  |
| calendar.filters | `act_window_2832_calendar_filters` | Opens **Calendar Filters** records (tree,form). | `model calendar.filters` (calendar) |  |
| calendar.filters | `act_window_2832_calendar_filters_d7` | Opens **Calendar Filters** records (tree,form). | `model calendar.filters` (calendar) | `menu BugFix-Studio-Misc.menu_f6f_calendar_filters` |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default tree view for ir.model(747,) | `view_6070_default_tree_view_for_ir_model_747` | tree | full tree layout with 1 fields | Minimal list view for Calendar Filters showing only the record ID. |  |  |
