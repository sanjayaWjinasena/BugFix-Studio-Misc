from odoo import fields, models


class X_product_product(models.Model):
    _name = "x_product_product"
    _rec_name = "x_name"  # Clear-DB Studio model: records are named by x_name
    _description = "product.product"

    x_name = fields.Char(string="Name")
