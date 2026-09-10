# -*- coding: utf-8 -*-
from odoo import models, fields

class XProductProductGap(models.Model):
    _inherit = 'x_product_product'

    x_name = fields.Char(string='Name')
