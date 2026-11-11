from odoo import fields, models


class XTestModelPrimaryGap(models.Model):
    _inherit = "x_test_model_primary"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
