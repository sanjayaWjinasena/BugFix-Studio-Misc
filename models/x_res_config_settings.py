# -*- coding: utf-8 -*-
from odoo import models, fields

class XResConfigSettings(models.Model):
    _name = 'x_res_config_settings'
    _description = 'res.config.settings'

    x_name = fields.Char(string='Name')
    x_studio_minimum_sales_margin_ = fields.Float(string='Minimum Sales Margin %')
