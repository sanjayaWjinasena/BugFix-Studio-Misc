"""res.users Many2ones to customer_groups, moved here from
studio_usermodel_migration (v1.0.60) in v0.0.112.

customer_groups is owned by BugFix-Studio-Misc, which loads AFTER
studio_usermodel_migration. Declared upstream, these four fields were
rewritten to comodel '_unknown' at that module's setup pass and never
recovered during upgrade-mode registry builds (Odoo 17 reuses the Field
object). A declaration in the comodel-owning module is the only
load-order-proof fix. Strings and flags are verbatim from the source.

Column data is preserved: the source module's pre-migrate drops its
ir.model.data pointers so Odoo's end-of-load cleanup never unlinks the
fields; this module's reflection re-attaches the xmlids.
"""

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    customer_group2 = fields.Many2one("customer_groups")
    many2one_field_3LBKs = fields.Many2one("customer_groups", string="Group")
    many2one_field_9xxxo = fields.Many2one(
        "customer_groups", string="Customer Groups XXX"
    )
    many2one_field_V9cmo = fields.Many2one("customer_groups", string="Customer Groups")
