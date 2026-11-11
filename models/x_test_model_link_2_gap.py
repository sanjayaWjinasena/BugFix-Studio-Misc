from odoo import fields, models


class XTestModelLink2Gap(models.Model):
    _inherit = "x_test_model_link_2"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
