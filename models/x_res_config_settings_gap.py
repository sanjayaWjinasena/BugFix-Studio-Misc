# -*- coding: utf-8 -*-
from odoo import models, fields

class XResConfigSettingsGap(models.Model):
    _inherit = 'x_res_config_settings'

    x_name = fields.Char(string='Name')
