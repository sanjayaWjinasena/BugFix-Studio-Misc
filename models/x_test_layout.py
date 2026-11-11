from odoo import fields, models


class X_test_layout(models.Model):
    _name = "x_test_layout"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Test Layout"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    x_studio_line_ids = fields.Many2one(comodel_name="x_test02", string="Line Ids")
    product_id = fields.Many2one(
        comodel_name="product.product", string="Product Id"
    )
    quantity = fields.Float(string="Quantity")
    sequence = fields.Integer(string="Sequence")
