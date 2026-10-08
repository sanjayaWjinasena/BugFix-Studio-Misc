# BugFix-Studio-Misc — `loyalty.generate.wizard`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `loyalty.generate.wizard` — Generate Coupons

*Extends a model created by `loyalty`.*

**Summary:**

<!-- SUMMARY:model:loyalty.generate.wizard -->
This repo adds a global record rule that lets users see and use only the Generate Coupons wizard records they created themselves. Nothing else is changed.
<!-- /SUMMARY -->

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Generate Sales Coupon Rule | `rule_428_generate_sales_coupon_rule` | For everyone (global rule): read/write/create/delete on Generate Coupons only where `[('create_uid', '=', user.id)]`. | `model loyalty.generate.wizard` (loyalty) |  |
