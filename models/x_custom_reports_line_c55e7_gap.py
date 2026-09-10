# -*- coding: utf-8 -*-
from odoo import models, fields

class XCustomReportsLineC55e7Gap(models.Model):
    _inherit = 'x_custom_reports_line_c55e7'

    x_custom_reports_id = fields.Many2one(comodel_name='x_custom_reports', string='X Custom Reports')
    x_name = fields.Char(string='Description', required=True)
