"""Add parent-side O2M material_request_tes_line_ids_661d3 via _inherit.
Same load-order-safety pattern as material_request_mt_o2m.py.
"""

from odoo import fields, models


class XMaterialRequestTes(models.Model):
    _inherit = "material_request_tes"

    material_request_tes_line_ids_661d3 = fields.One2many(
        comodel_name="material_request_tes_line_3301b",
        inverse_name="material_request_tes_id",
        string="New Lines",
    )
