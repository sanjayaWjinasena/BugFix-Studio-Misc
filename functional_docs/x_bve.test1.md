# BugFix-Studio-Misc — `x_bve.test1`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_bve.test1` — Test 1

*Created by this repo.* Python: `models/x_bve_test1.py`, `models/x_bve_test1_gap.py`.

**Summary:**

<!-- SUMMARY:model:x_bve.test1 -->
A test BI view-editor report, Test 1, built as a read-only SQL view. It has only two columns, Name and Code Prefix End, which are shown in its list view. Its graph, pivot and search views are empty. It opens from the Test 1 window action.
<!-- /SUMMARY -->

**Fields (8):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_bve_t1_code_prefix_end` | Code Prefix End | char | Column 'Code Prefix End' of the BI view-editor report 'Test 1', a read-only SQL-view model; used in the list view. | stored |  | `view BugFix-Studio-Misc.view_9314_tree_analysis_e` |
| `x_bve_t1_name` | Name | char | Column 'Name' of the BI view-editor report 'Test 1', a read-only SQL-view model; used in the list view. | stored |  | `view BugFix-Studio-Misc.view_9314_tree_analysis_e` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Test 1 | `act_window_3573_test_1` | Opens **Test 1** records (tree,graph,pivot). | `model x_bve.test1` |  |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Graph Analysis | `view_9312_graph_analysis_e` | graph | full graph layout with 0 fields | Empty bar-chart view for the test BI dataset x_bve.test1; defines no fields. |  |  |
| Pivot Analysis | `view_9311_pivot_analysis_e` | pivot | full pivot layout with 0 fields | Empty pivot view for the test BI dataset x_bve.test1; defines no fields. |  |  |
| Search BI View | `view_9313_search_bi_view_e` | search | full search layout with 0 fields | Empty search view for the test BI dataset x_bve.test1; defines no fields. |  |  |
| Tree Analysis | `view_9314_tree_analysis_e` | tree | full tree layout with 2 fields | Read-only list (no create) of the test BI dataset x_bve.test1 showing Code Prefix End and Name. | `x_bve.test1.x_bve_t1_code_prefix_end`<br>`x_bve.test1.x_bve_t1_name` |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| read access to x_bve.test1 | `access_8519_read_access_to_x_bve_test1` | Gives **all users** read access to Test 1 records. | `model x_bve.test1` |  |
| x_bve.test1 admin | `access_x_bve_test1_admin` | Gives **Administration / Settings** read/write/create/delete access to Test 1 records. | `group base.group_system` (base)<br>`model x_bve.test1` |  |
