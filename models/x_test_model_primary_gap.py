# -*- coding: utf-8 -*-
from odoo import models, fields

class XTestModelPrimaryGap(models.Model):
    _inherit = 'x_test_model_primary'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
