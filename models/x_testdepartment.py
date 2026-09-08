# -*- coding: utf-8 -*-
from odoo import models, fields

class X_testdepartment(models.Model):
    _name = 'x_testdepartment'
    _description = 'TestDepartment'

    x_Description2 = fields.Char(string='Description 2')
    x_Description3 = fields.Char(string='Description 3')
    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_code = fields.Char(string='Code')
    x_studio_description = fields.Char(string='Description')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_sig = fields.Binary(string='Sig')
