# BugFix-Studio-Misc — `hr.attendance.overtime`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `hr.attendance.overtime` — Attendance Overtime

*Extends a model created by `hr_attendance`.*

Other repos that use this model: `record rule BugFix-HR.rule_384_employee_multi_company_rule` (BugFix-HR)<br>`record rule BugFix-HR.rule_747_attendance_officer_restrict_overtime_to_managed_employees` (BugFix-HR)<br>`record rule BugFix-HR.rule_748_attendance_admin_full_access` (BugFix-HR)<br>`record rule BugFix-HR.rule_749_attendance_base_user_read_his_own_overtime` (BugFix-HR)<br>`window action BugFix-HR.act_window_2557_hr_attendance_overtime` (BugFix-HR)

**Summary:**

<!-- SUMMARY:model:hr.attendance.overtime -->
This repo adds one window action that opens Attendance Overtime records in a list view, linked from the Test App 05 menu tree. Nothing else is changed.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| hr.attendance.overtime | `act_window_2557_hr_attendance_overtime_d7` | Opens **Attendance Overtime** records (tree). | `model hr.attendance.overtime` (hr_attendance) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_hr_attendance_overtime` |
