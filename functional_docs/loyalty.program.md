# BugFix-Studio-Misc — `loyalty.program`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `loyalty.program` — Loyalty Program

*Extends a model created by `loyalty`.*

**Summary:**

<!-- SUMMARY:model:loyalty.program -->
This repo adds two global multi-company record rules on Loyalty Programs that limit programs to the user's companies (one also allows parent companies). Nothing else is changed.
<!-- /SUMMARY -->

**Record rules (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Coupon Program | `rule_628_jin_multi_company_coupon_program` | For everyone (global rule): read/write/create/delete on Loyalty Program only where `[('company_id', 'in', company_ids + [False])]`. | `loyalty.program.company_id` (loyalty)<br>`model loyalty.program` (loyalty) |  |
| Loyalty program multi company rule | `rule_653_loyalty_program_multi_company_rule` | For everyone (global rule): read/write/create/delete on Loyalty Program only where `['|', ('company_id', 'in', company_ids + [False]), ('company_id', 'parent_of', company_ids)]`. | `loyalty.program.company_id` (loyalty)<br>`model loyalty.program` (loyalty) |  |
