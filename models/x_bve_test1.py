# -*- coding: utf-8 -*-
from odoo import models, fields

class XBveTest1(models.Model):
    _name = 'x_bve.test1'
    _description = 'Test 1'

    x_bve_t1_code_prefix_end = fields.Char(string='Code Prefix End', readonly=True)
    x_bve_t1_name = fields.Char(string='Name', readonly=True)
