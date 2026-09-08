# -*- coding: utf-8 -*-
from odoo import models, fields

class XCustomReportsLineC55e7(models.Model):
    _name = 'x_custom_reports_line_c55e7'
    _description = 'custom_reports_line'

    x_custom_reports_id = fields.Many2one(comodel_name='x_custom_reports', string='X Custom Reports')
    x_name = fields.Char(string='Description', required=True)
    x_studio_sequence = fields.Integer(string='Sequence')
