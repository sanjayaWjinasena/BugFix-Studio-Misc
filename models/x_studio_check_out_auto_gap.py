# -*- coding: utf-8 -*-
from odoo import models, fields

class XStudioCheckOutAutoGap(models.Model):
    _inherit = 'x_studio_check_out_auto'

    x_name = fields.Char(string='Name')
