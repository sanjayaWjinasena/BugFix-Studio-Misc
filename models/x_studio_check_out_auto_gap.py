# -*- coding: utf-8 -*-
from odoo import models, fields

class XStudioCheckOutAutoGap(models.Model):
    _inherit = 'x_studio_check_out_auto'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_name = fields.Char(string='Name')
