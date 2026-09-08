# -*- coding: utf-8 -*-
from odoo import models, fields

class XSalesModelDebug(models.Model):
    _name = 'x_sales_model_debug'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Sales Model Debug'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Method Name')
    x_studio_end_time = fields.Datetime(string='End Time')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_start_time = fields.Datetime(string='Start Time')
