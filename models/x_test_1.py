from odoo import fields, models


class X_test_1(models.Model):
    _name = "x_test_1"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "TEST-1"

    active = fields.Boolean()
    name = fields.Char()
    sequence = fields.Integer()
    value = fields.Float()
