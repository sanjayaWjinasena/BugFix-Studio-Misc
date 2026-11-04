from odoo import fields, models


class X_test_model_link(models.Model):
    _name = "x_test_model_link"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "TEST MODEL LINK"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    x_studio_many2one_field_sctrD = fields.Many2one(
        comodel_name="x_test_model_primary", string="TEST MODEL PRIMARY"
    )
    sequence = fields.Integer(string="Sequence")
