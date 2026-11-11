from odoo import fields, models


class X_test_model_link_2(models.Model):
    _name = "x_test_model_link_2"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Test Model Link 2"

    active = fields.Boolean()
    name = fields.Char()
    x_studio_many2many_field_2PxmY = fields.Many2many(
        comodel_name="x_test_model_primary", string="TEST MODEL PRIMARY"
    )
    sequence = fields.Integer()
    x_studio_test_model_primary_2 = fields.Many2one(
        comodel_name="x_test_model_primary", string="TEST MODEL PRIMARY 2"
    )
