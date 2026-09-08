# -*- coding: utf-8 -*-
from odoo import models, fields

class X_test_form(models.Model):
    _name = 'x_test_form'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'TEST FORM'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_char_field_3aVUG = fields.Char(string='New Text')
    x_studio_sequence = fields.Integer(string='Sequence')
