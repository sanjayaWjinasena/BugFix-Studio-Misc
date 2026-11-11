"""Studio fields on product.category — company scope + description.

CDB added these 2 fields via Studio directly on the core product.category
model. Used by category-level reporting to filter by owning company and
show a longer description than `name`.
"""

from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    accounting_company_id = fields.Many2one(
        "res.company",
        string="Company",
        ondelete="set null",
        copy=True,
    )
    description = fields.Char(copy=True)
