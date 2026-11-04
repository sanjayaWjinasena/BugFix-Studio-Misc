from odoo import fields, models


class X_test_form(models.Model):
    _name = "x_test_form"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "TEST FORM"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    x_studio_char_field_3aVUG = fields.Char(string="New Text")
    sequence = fields.Integer(string="Sequence")
