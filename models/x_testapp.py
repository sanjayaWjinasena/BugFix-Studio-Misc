# -*- coding: utf-8 -*-
from odoo import models, fields

class X_testapp(models.Model):
    _name = 'x_testapp'
    _description = 'TestApp'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_sequence = fields.Integer(string='Sequence')
