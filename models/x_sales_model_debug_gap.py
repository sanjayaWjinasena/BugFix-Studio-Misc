# -*- coding: utf-8 -*-
from odoo import models, fields

class XSalesModelDebugGap(models.Model):
    _inherit = 'x_sales_model_debug'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Method Name')
