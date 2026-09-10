# -*- coding: utf-8 -*-
from odoo import models, fields

class XTestappGap(models.Model):
    _inherit = 'x_testapp'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
