# -*- coding: utf-8 -*-
from odoo import models, fields

class XCustomerGroupsGap(models.Model):
    _inherit = 'x_customer_groups'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_name = fields.Char(string='Group Description')
