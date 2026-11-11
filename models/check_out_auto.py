from odoo import fields, models


class X_studio_check_out_auto(models.Model):
    _name = "check_out_auto"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Check Out Auto"

    name = fields.Char(string="Name")


class XStudioCheckOutAutoGap(models.Model):
    _inherit = "check_out_auto"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Name")
