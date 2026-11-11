# BugFix-Studio-Misc — `bve.samplebalancemovementreport`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `bve.samplebalancemovementreport` — Sample Balance Movement Report

*Created by this repo.* Python: `models/bve_samplebalancemovementreport.py`, `models/x_bve_samplebalancemovementreport_gap.py`.

**Summary:**

<!-- SUMMARY:model:bve.samplebalancemovementreport -->
A read-only BI view-editor report, Sample Balance Movement Report, built as an SQL view of account movements. Each row shows an account, date, debit, credit, balance and company. Users open it from its window action in list, graph and pivot views to analyse movements by account and date. All users can read it; only Administration / Settings has full access.
<!-- /SUMMARY -->

**Fields (12):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `bve_t1_account_id` | Account | many2one → `account.account` | Column 'Account' of the BI view-editor report 'Sample Balance Movement Report', a read-only SQL-view model; used in the pivot, graph, search and list views. | stored | `model account.account` (account) | `view BugFix-Studio-Misc.view_pivot_analysis_2`<br>`view BugFix-Studio-Misc.view_graph_analysis_2`<br>`view BugFix-Studio-Misc.view_search_bi_view_2`<br>`view BugFix-Studio-Misc.view_tree_analysis_2` |
| `bve_t1_balance` | Balance | float | Column 'Balance' of the BI view-editor report 'Sample Balance Movement Report', a read-only SQL-view model; used in the pivot, graph, search and list views. | stored |  | `view BugFix-Studio-Misc.view_pivot_analysis_2`<br>`view BugFix-Studio-Misc.view_graph_analysis_2`<br>`view BugFix-Studio-Misc.view_search_bi_view_2`<br>`view BugFix-Studio-Misc.view_tree_analysis_2` |
| `bve_t1_company_id` | Company | many2one → `res.company` | Column 'Company' of the BI view-editor report 'Sample Balance Movement Report', a read-only SQL-view model; used in the list view. | stored | `model res.company` (base) | `view BugFix-Studio-Misc.view_tree_analysis_2` |
| `bve_t1_credit` | Credit | float | Column 'Credit' of the BI view-editor report 'Sample Balance Movement Report', a read-only SQL-view model; used in the pivot, graph, search and list views. | stored |  | `view BugFix-Studio-Misc.view_pivot_analysis_2`<br>`view BugFix-Studio-Misc.view_graph_analysis_2`<br>`view BugFix-Studio-Misc.view_search_bi_view_2`<br>`view BugFix-Studio-Misc.view_tree_analysis_2` |
| `bve_t1_date` | Date | date | Column 'Date' of the BI view-editor report 'Sample Balance Movement Report', a read-only SQL-view model; used in the pivot, graph, search and list views. | stored |  | `view BugFix-Studio-Misc.view_pivot_analysis_2`<br>`view BugFix-Studio-Misc.view_graph_analysis_2`<br>`view BugFix-Studio-Misc.view_search_bi_view_2`<br>`view BugFix-Studio-Misc.view_tree_analysis_2` |
| `bve_t1_debit` | Debit | float | Column 'Debit' of the BI view-editor report 'Sample Balance Movement Report', a read-only SQL-view model; used in the pivot, graph, search and list views. | stored |  | `view BugFix-Studio-Misc.view_pivot_analysis_2`<br>`view BugFix-Studio-Misc.view_graph_analysis_2`<br>`view BugFix-Studio-Misc.view_search_bi_view_2`<br>`view BugFix-Studio-Misc.view_tree_analysis_2` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Sample Balance Movement Report | `action_sample_balance_movement_report` | Opens **Sample Balance Movement Report** records (tree,graph,pivot). | `model bve.samplebalancemovementreport` |  |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Graph Analysis | `view_graph_analysis_2` | graph | full graph layout with 5 fields | Stacked bar-chart analysis of the bve.samplebalancemovementreport BI dataset by account and date, measuring debit, credit and balance. | `bve.samplebalancemovementreport.bve_t1_account_id`<br>`bve.samplebalancemovementreport.bve_t1_balance`<br>`bve.samplebalancemovementreport.bve_t1_credit`<br>`bve.samplebalancemovementreport.bve_t1_date`<br>`bve.samplebalancemovementreport.bve_t1_debit` |  |
| Pivot Analysis | `view_pivot_analysis_2` | pivot | full pivot layout with 5 fields | Pivot analysis of the bve.samplebalancemovementreport BI dataset with rows by account and date and debit, credit and balance measures. | `bve.samplebalancemovementreport.bve_t1_account_id`<br>`bve.samplebalancemovementreport.bve_t1_balance`<br>`bve.samplebalancemovementreport.bve_t1_credit`<br>`bve.samplebalancemovementreport.bve_t1_date`<br>`bve.samplebalancemovementreport.bve_t1_debit` |  |
| Search BI View | `view_search_bi_view_2` | search | full search layout with 5 fields | Search view for the bve.samplebalancemovementreport BI dataset (account, date, debit, credit, balance). | `bve.samplebalancemovementreport.bve_t1_account_id`<br>`bve.samplebalancemovementreport.bve_t1_balance`<br>`bve.samplebalancemovementreport.bve_t1_credit`<br>`bve.samplebalancemovementreport.bve_t1_date`<br>`bve.samplebalancemovementreport.bve_t1_debit` |  |
| Tree Analysis | `view_tree_analysis_2` | tree | full tree layout with 6 fields | Read-only list (no create) of the bve.samplebalancemovementreport BI dataset: account, date, debit, credit, balance and company. | `bve.samplebalancemovementreport.bve_t1_account_id`<br>`bve.samplebalancemovementreport.bve_t1_balance`<br>`bve.samplebalancemovementreport.bve_t1_company_id`<br>`bve.samplebalancemovementreport.bve_t1_credit`<br>`bve.samplebalancemovementreport.bve_t1_date`<details><summary>+1 more</summary>`bve.samplebalancemovementreport.bve_t1_debit`</details> |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| read access to bve.samplebalancemovementreport | `access_read_access_to_bve_samplebalancemovementreport` | Gives **all users** read access to Sample Balance Movement Report records. | `model bve.samplebalancemovementreport` |  |
| bve.samplebalancemovementreport admin | `access_bve_samplebalancemovementreport_admin` | Gives **Administration / Settings** read/write/create/delete access to Sample Balance Movement Report records. | `group base.group_system` (base)<br>`model bve.samplebalancemovementreport` |  |
