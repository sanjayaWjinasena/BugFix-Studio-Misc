from odoo import fields, models


class XProductTestGap(models.Model):
    _inherit = "x_product_test"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
