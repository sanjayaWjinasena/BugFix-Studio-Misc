# -*- coding: utf-8 -*-
from odoo import models, fields

class XBveTest1Gap(models.Model):
    _inherit = 'x_bve.test1'

    x_bve_t1_code_prefix_end = fields.Char(string='Code Prefix End', readonly=True)
    x_bve_t1_name = fields.Char(string='Name', readonly=True)
