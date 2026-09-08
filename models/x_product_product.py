# -*- coding: utf-8 -*-
from odoo import models, fields

class X_product_product(models.Model):
    _name = 'x_product_product'
    _description = 'product.product'

    x_name = fields.Char(string='Name')
