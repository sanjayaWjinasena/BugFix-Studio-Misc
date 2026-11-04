from odoo import fields, models


class X_x_studio_request_line(models.Model):
    _name = "x_x_studio_request_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "x_studio_request_line"

    name = fields.Char(string="Name")


class XXStudioRequestLineGap(models.Model):
    _inherit = "x_x_studio_request_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Name")
