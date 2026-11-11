from odoo import fields, models


class X_testdepartment(models.Model):
    _name = "x_testdepartment"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "TestDepartment"

    x_Description2 = fields.Char(string="Description 2")
    x_Description3 = fields.Char(string="Description 3")
    active = fields.Boolean()
    name = fields.Char()
    code = fields.Char()
    description = fields.Char()
    sequence = fields.Integer()
    x_studio_sig = fields.Binary(string="Sig")
