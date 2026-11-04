from odoo import fields, models


class X_testapp(models.Model):
    _name = "x_testapp"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "TestApp"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    sequence = fields.Integer(string="Sequence")
