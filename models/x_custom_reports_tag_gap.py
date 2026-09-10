# -*- coding: utf-8 -*-
from odoo import models, fields

class XCustomReportsTagGap(models.Model):
    _inherit = 'x_custom_reports_tag'

    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Name', required=True)
