from odoo import fields, models


class XTestdepartmentGap(models.Model):
    _inherit = "x_testdepartment"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    x_Description2 = fields.Char(string="Description 2")
    x_Description3 = fields.Char(string="Description 3")
    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
