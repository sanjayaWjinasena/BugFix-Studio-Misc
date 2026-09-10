# -*- coding: utf-8 -*-
from odoo import models, fields

class XTestModelLink2Gap(models.Model):
    _inherit = 'x_test_model_link_2'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
