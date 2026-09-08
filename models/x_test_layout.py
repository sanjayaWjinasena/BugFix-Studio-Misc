# -*- coding: utf-8 -*-
from odoo import models, fields

class X_test_layout(models.Model):
    _name = 'x_test_layout'
    _description = 'Test Layout'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_line_ids = fields.Many2one(comodel_name='x_test02', string='Line Ids')
    x_studio_product_id = fields.Many2one(comodel_name='product.product', string='Product Id')
    x_studio_quantity = fields.Float(string='Quantity')
    x_studio_sequence = fields.Integer(string='Sequence')
