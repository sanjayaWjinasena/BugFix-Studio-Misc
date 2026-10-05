# -*- coding: utf-8 -*-
from odoo import models, fields

class X_studio_check_out_auto(models.Model):
    _name = 'x_studio_check_out_auto'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name
    _description = 'Check Out Auto'

    x_name = fields.Char(string='Name')
