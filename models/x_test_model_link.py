# -*- coding: utf-8 -*-
from odoo import models, fields

class X_test_model_link(models.Model):
    _name = 'x_test_model_link'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'TEST MODEL LINK'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_many2one_field_sctrD = fields.Many2one(comodel_name='x_test_model_primary', string='TEST MODEL PRIMARY')
    x_studio_sequence = fields.Integer(string='Sequence')
