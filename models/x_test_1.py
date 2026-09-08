# -*- coding: utf-8 -*-
from odoo import models, fields

class X_test_1(models.Model):
    _name = 'x_test_1'
    _description = 'TEST-1'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_value = fields.Float(string='Value')
