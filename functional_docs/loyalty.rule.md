# BugFix-Studio-Misc — `loyalty.rule`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `loyalty.rule` — Loyalty Rule

*Extends a model created by `loyalty`.*

**Summary:**

<!-- SUMMARY:model:loyalty.rule -->
This repo adds a coupon.rule window action that opens Loyalty Rules in list and form views, linked from the Test App 05 menu tree, and a global multi-company record rule on loyalty rules.
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| coupon.rule | `act_window_2841_coupon_rule` | Opens **Loyalty Rule** records (tree,form). | `model loyalty.rule` (loyalty) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_coupon_rule` |
| coupon.rule | `act_window_2841_coupon_rule_d7` | Opens **Loyalty Rule** records (tree,form). | `model loyalty.rule` (loyalty) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Loyalty rule multi company rule | `rule_655_loyalty_rule_multi_company_rule` | For everyone (global rule): read/write/create/delete on Loyalty Rule only where `['|', ('company_id', 'in', company_ids + [False]), ('company_id', 'parent_of', company_ids)]`. | `loyalty.rule.company_id` (loyalty)<br>`model loyalty.rule` (loyalty) |  |
