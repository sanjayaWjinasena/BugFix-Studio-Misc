# BugFix-Studio-Misc — `loyalty.reward`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `loyalty.reward` — Loyalty Reward

*Extends a model created by `loyalty`.*

**Summary:**

<!-- SUMMARY:model:loyalty.reward -->
This repo adds a coupon.reward window action that opens Loyalty Rewards in list and form views, linked from the Test App 05 menu tree, and a global multi-company record rule on rewards.
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| coupon.reward | `act_window_2842_coupon_reward` | Opens **Loyalty Reward** records (tree,form). | `model loyalty.reward` (loyalty) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_coupon_reward` |
| coupon.reward | `act_window_2842_coupon_reward_d7` | Opens **Loyalty Reward** records (tree,form). | `model loyalty.reward` (loyalty) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Loyalty reward multi company rule | `rule_656_loyalty_reward_multi_company_rule` | For everyone (global rule): read/write/create/delete on Loyalty Reward only where `['|', ('company_id', 'in', company_ids + [False]), ('company_id', 'parent_of', company_ids)]`. | `loyalty.reward.company_id` (loyalty)<br>`model loyalty.reward` (loyalty) |  |
