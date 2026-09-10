# -*- coding: utf-8 -*-
from odoo import models, fields

class XProductTestGap(models.Model):
    _inherit = 'x_product_test'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
