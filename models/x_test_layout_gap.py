from odoo import fields, models


class XTestLayoutGap(models.Model):
    _inherit = "x_test_layout"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
