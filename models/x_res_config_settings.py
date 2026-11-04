from odoo import fields, models


class XResConfigSettings(models.Model):
    _name = "x_res_config_settings"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "res.config.settings"

    name = fields.Char(string="Name")
    x_studio_minimum_sales_margin_ = fields.Float(string="Minimum Sales Margin %")


class XResConfigSettingsGap(models.Model):
    _inherit = "x_res_config_settings"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Name")
