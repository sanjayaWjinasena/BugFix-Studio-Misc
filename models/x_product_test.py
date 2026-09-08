# -*- coding: utf-8 -*-
from odoo import models, fields

class X_product_test(models.Model):
    _name = 'x_product_test'
    _description = 'product.test'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_journal_name = fields.Char(string='Journal Name')
    x_studio_many2many_field_R1u9s = fields.Many2many(comodel_name='product.product', string='Product')
    x_studio_many2one_field_cmfRx = fields.Many2one(comodel_name='product.product', string='Product')
    x_studio_many2one_field_wTxgi = fields.Many2one(comodel_name='account.move', string='Journal Entry')
    x_studio_product_1 = fields.Many2one(comodel_name='product.template', string='Product_1')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_stock_move = fields.Many2one(comodel_name='stock.move', string='Stock Move')
