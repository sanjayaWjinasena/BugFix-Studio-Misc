# -*- coding: utf-8 -*-
from odoo import models, fields

class XXStudioRequestLineGap(models.Model):
    _inherit = 'x_x_studio_request_line'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_name = fields.Char(string='Name')
