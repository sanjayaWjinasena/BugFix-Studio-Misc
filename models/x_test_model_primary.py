# -*- coding: utf-8 -*-
from odoo import models, fields

class X_test_model_primary(models.Model):
    _name = 'x_test_model_primary'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'TEST MODEL PRIMARY'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_date_1 = fields.Date(string='Date')
    x_studio_one2many_field_5VwpV = fields.One2many(comodel_name='x_test_model_link', inverse_name='x_studio_many2one_field_sctrD', string='Line IDs', copy=False)
    x_studio_sequence = fields.Integer(string='Sequence')
