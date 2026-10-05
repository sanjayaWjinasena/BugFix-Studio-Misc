# -*- coding: utf-8 -*-
from odoo import models, fields

class XResConfigSettingsGap(models.Model):
    _inherit = 'x_res_config_settings'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_name = fields.Char(string='Name')
