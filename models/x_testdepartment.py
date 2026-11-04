from odoo import fields, models


class X_testdepartment(models.Model):
    _name = "x_testdepartment"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "TestDepartment"

    x_Description2 = fields.Char(string="Description 2")
    x_Description3 = fields.Char(string="Description 3")
    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    x_studio_code = fields.Char(string="Code")
    description = fields.Char(string="Description")
    sequence = fields.Integer(string="Sequence")
    x_studio_sig = fields.Binary(string="Sig")
