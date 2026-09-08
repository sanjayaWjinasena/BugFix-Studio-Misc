# -*- coding: utf-8 -*-
from odoo import models, fields

class X_studio_check_out_auto(models.Model):
    _name = 'x_studio_check_out_auto'
    _description = 'Check Out Auto'

    x_name = fields.Char(string='Name')
