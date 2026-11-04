from odoo import fields, models


class XTest1Gap(models.Model):
    _inherit = "x_test_1"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
