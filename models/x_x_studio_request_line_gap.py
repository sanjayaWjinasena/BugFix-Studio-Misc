# -*- coding: utf-8 -*-
from odoo import models, fields

class XXStudioRequestLineGap(models.Model):
    _inherit = 'x_x_studio_request_line'

    x_name = fields.Char(string='Name')
