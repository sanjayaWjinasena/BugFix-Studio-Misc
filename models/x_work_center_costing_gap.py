# -*- coding: utf-8 -*-
from odoo import models, fields

class XWorkCenterCostingGap(models.Model):
    _inherit = 'x_work_center_costing'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
