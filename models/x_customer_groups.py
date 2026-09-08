# -*- coding: utf-8 -*-
from odoo import models, fields

class XCustomerGroups(models.Model):
    _name = 'x_customer_groups'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Customer Groups'

    x_name = fields.Char(string='Group Description')
    x_studio_sequence = fields.Integer(string='Sequence')
