# -*- coding: utf-8 -*-
from odoo import models, fields

class XTestFormGap(models.Model):
    _inherit = 'x_test_form'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
