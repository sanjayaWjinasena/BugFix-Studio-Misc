# -*- coding: utf-8 -*-
from odoo import models, fields

class XCustomerGroupsGap(models.Model):
    _inherit = 'x_customer_groups'

    x_name = fields.Char(string='Group Description')
