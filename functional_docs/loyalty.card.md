# BugFix-Studio-Misc — `loyalty.card`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `loyalty.card` — Loyalty Coupon

*Extends a model created by `loyalty`.*

**Summary:**

<!-- SUMMARY:model:loyalty.card -->
This repo gives the Sales / Jin - Sales - POS Users group (owned by BugFix-Approvals) read access to Loyalty Coupons. It also adds a global multi-company record rule that limits coupons to the user's companies and their parent companies.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| coupon.coupon | `access_6857_coupon_coupon` | Gives **Sales / Jin - Sales - POS Users** read access to Loyalty Coupon records. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model loyalty.card` (loyalty) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Loyalty card multi company rule | `rule_654_loyalty_card_multi_company_rule` | For everyone (global rule): read/write/create/delete on Loyalty Coupon only where `['|', ('company_id', 'in', company_ids + [False]), ('company_id', 'parent_of', company_ids)]`. | `loyalty.card.company_id` (loyalty)<br>`model loyalty.card` (loyalty) |  |
