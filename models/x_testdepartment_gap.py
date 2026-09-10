# -*- coding: utf-8 -*-
from odoo import models, fields

class XTestdepartmentGap(models.Model):
    _inherit = 'x_testdepartment'

    x_Description2 = fields.Char(string='Description 2')
    x_Description3 = fields.Char(string='Description 3')
    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
