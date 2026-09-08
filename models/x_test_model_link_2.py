# -*- coding: utf-8 -*-
from odoo import models, fields

class X_test_model_link_2(models.Model):
    _name = 'x_test_model_link_2'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Test Model Link 2'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_many2many_field_2PxmY = fields.Many2many(comodel_name='x_test_model_primary', string='TEST MODEL PRIMARY')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_test_model_primary_2 = fields.Many2one(comodel_name='x_test_model_primary', string='TEST MODEL PRIMARY 2')
