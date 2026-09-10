# -*- coding: utf-8 -*-
from odoo import models, fields

class XTestModelLinkGap(models.Model):
    _inherit = 'x_test_model_link'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
