# Jinasena : Module : Studio-Misc

Landing zone for Studio-created artefacts on the Jinasena Odoo 17
installation that don't fit any domain-specific companion module.

## Scope

Owns:

- Orphan `x_*` custom models: test/scratch models
  (`x_test02`, `x_test_layout`, `x_test_form`, `website_faq*`,
  `sales_model_debug`, etc.)
- Standard-Odoo model customisations too small to justify their own
  repo: `crm.*`, `quality.*`, `loyalty.*`, `pos.*`,
  `delivery.carrier`, `crossovered.budget`, etc.
- `ir.sequence` records without a routable model-code prefix
- `ir.ui.menu` records without a routable window-action target

Does NOT own:

- Anything routed to a domain-specific companion module
  (Sales / Purchase / Stock / Accounting / MRP / HR / Project /
  Maintenance / Analytics / Fix-repair /
  Jinasena_Masterdata_Reporting)
- `ir.*` infra records (belong to base Odoo)

## Layout

```
data/          # server_actions, automations, windows, etc.
views/         # primary + inherit view ports
security/      # ACLs + record rules
models/        # x_* model class declarations
static/        # icon, images
```

## Depends

Minimal by design so the module can absorb any x_* model:

- `base_setup`
- `base_automation` (for `usage='base_automation'` selection value)
- `mail` (for `mail.thread` + `mail.activity.mixin` mixin inherits)

Additional module deps will be added as specific ports need them.

## Provenance

Created 2026-09-07 during the migration-routing pass. See
`D:\Odoo Playwright Tests\PlayWrite Testings\UNPORTED_ROUTING.html`
for the routing decisions that placed items here.

<!-- BEGIN rename-studio-names -->
## Naming and upgrade notes

This module was first built in Odoo Studio and later moved to code. On 2026-11-11 (branches `Rename-HelpdeskRepair` for the Repair names, then `Rename-All`) the Studio names were replaced: the Studio prefix `x_studio_` / `x_` was removed and the rest of each name kept (`x_studio_pr_number` -> `pr_number`). Where that name already exists on the model (a field or method of Odoo or of our code, including mixins such as mail.thread), or is a Python keyword or a PostgreSQL reserved word, the repo name is the prefix instead (`x_studio_locked` on sale.order -> `sales_locked`). `x_active` became `active`. Custom models follow the same rule (`x_purchase_request_mt` -> `purchase_request_mt`). Studio-numbered XML ids (`server_action_1234_...`, `view_5678_odoo_studio_...`) got clean names. New custom fields and models follow the same rule: a plain name, and the repo name as prefix only when the plain name is taken.

| Renamed in this module | Example before | Example after |
|---|---|---|
| 62 fields | `x_studio_active` | `accounting_active` |
| 17 custom models (tables follow) | `x_account_winbooks_import_wizard` | `misc_account_winbooks_import_wizard` |
| 1106 XML ids | `rule_246_own_attendees` | `rule_own_attendees` |
| 93 files | `data/x_customer_groups_data.xml` | `data/customer_groups_data.xml` |

Kept with `x_` on purpose: test models and their fields, fields that exist only in the database (not declared in code), `x_planNN_id` (created by Odoo analytic plans) and many2many table and column names (they hold the data; fields between renamed models name their tables explicitly).

Upgrading: the database is renamed by pre-migration scripts before the module loads, so records keep their ids. Version `17.0.0.0.129` runs, in order: the Repair rename of branch `Rename-HelpdeskRepair` (`pre-01` .. `pre-03`, skipped where it already ran), then the fields (`pre-10-fields`), the custom models (`pre-20-models`) and the XML ids (`pre-30-xmlids`). The same scripts ship in every module of the set; upgrading any one of them renames everything once. Log lines start with `Studio field rename:`, `Studio xmlid rename:` and `Studio model rename:`. If a new name already exists in the database the upgrade stops and rolls back (`RenameConflictError`). The full old -> new lists are the CSV files next to each script.
<!-- END rename-studio-names -->
