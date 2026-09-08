# -*- coding: utf-8 -*-
from odoo import models, fields

class X_x_studio_request_line(models.Model):
    _name = 'x_x_studio_request_line'
    _description = 'x_studio_request_line'

    x_name = fields.Char(string='Name')
