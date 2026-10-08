# BugFix-Studio-Misc — `product.template.attribute.exclusion`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `product.template.attribute.exclusion` — Product Template Attribute Exclusion

*Extends a model created by `product`.*

**Summary:**

<!-- SUMMARY:model:product.template.attribute.exclusion -->
This repo only adds one access right, giving the Ajith - Super group (defined in this repo) full read, write, create and delete access to attribute exclusion records. No fields, views or logic are changed.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| product.attribute manager filter line | `access_g_product_attribute_manager_filter_line_exclusion_ajith_super` | Gives **Ajith - Super** read/write/create/delete access to Product Template Attribute Exclusion records. | `group BugFix-Studio-Misc.group_g_misc_ajith_super`<br>`model product.template.attribute.exclusion` (product) |  |
