# -*- coding: utf-8 -*-
from odoo import models, fields

class XTestModelLink2Gap(models.Model):
    _inherit = 'x_test_model_link_2'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
