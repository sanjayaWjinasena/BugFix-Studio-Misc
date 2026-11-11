from odoo import fields, models


class X_product_product(models.Model):
    _name = "misc_product_product"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "product.product"

    name = fields.Char(string="Name")


class XProductProductGap(models.Model):
    _inherit = "misc_product_product"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Name")
