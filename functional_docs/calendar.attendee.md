# BugFix-Studio-Misc — `calendar.attendee`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `calendar.attendee` — Calendar Attendee Information

*Extends a model created by `calendar`.*

**Summary:**

<!-- SUMMARY:model:calendar.attendee -->
This repo adds window actions that open Calendar Attendee records in list and form views, two of them linked from the Test App 05 menu tree. It also adds the record rule Own attendees, which gives portal users full access to attendee records (the domain allows all records).
<!-- /SUMMARY -->

**Window actions (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Calendar Attendee Information - (calendar.attendee) | `act_window_2829_calendar_attendee_information_calendar_attendee` | Opens **Calendar Attendee Information** records (tree,form). | `model calendar.attendee` (calendar) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_calendar_attendee_information_calendar_attendee` |
| Calendar Attendee Information - (calendar.attendee) | `act_window_2829_calendar_attendee_information_calendar_attendee_d7` | Opens **Calendar Attendee Information** records (tree,form). | `model calendar.attendee` (calendar) |  |
| calendar.attendee | `act_window_2833_calendar_attendee` | Opens **Calendar Attendee Information** records (tree,form). | `model calendar.attendee` (calendar) |  |
| calendar.attendee | `act_window_2833_calendar_attendee_d7` | Opens **Calendar Attendee Information** records (tree,form). | `model calendar.attendee` (calendar) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_calendar_attendee` |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Own attendees | `rule_246_own_attendees` | For User types / Portal: read/write/create/delete on Calendar Attendee Information with no record filter (empty domain = all records). | `group base.group_portal` (base)<br>`model calendar.attendee` (calendar) |  |
