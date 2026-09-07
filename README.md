# Jinasena : Module : Studio-Misc

Landing zone for Studio-created artefacts on the Jinasena Odoo 17
installation that don't fit any domain-specific companion module.

## Scope

Owns:

- Orphan `x_*` custom models: test/scratch models
  (`x_test02`, `x_test_layout`, `x_test_form`, `x_website_faq*`,
  `x_sales_model_debug`, etc.)
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
