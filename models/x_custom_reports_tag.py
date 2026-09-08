# -*- coding: utf-8 -*-
from odoo import models, fields

class XCustomReportsTag(models.Model):
    _name = 'x_custom_reports_tag'
    _description = 'Custom Reports Tags'

    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Name', required=True)
