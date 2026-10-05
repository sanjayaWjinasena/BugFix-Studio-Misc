# -*- coding: utf-8 -*-
from odoo import models, fields

class XWorkCenterCostingGap(models.Model):
    _inherit = 'x_work_center_costing'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
