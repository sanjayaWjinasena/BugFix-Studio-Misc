from odoo import fields, models


class X_x_studio_request_line(models.Model):
    _name = "request_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "x_studio_request_line"

    name = fields.Char()


class XXStudioRequestLineGap(models.Model):
    _inherit = "request_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char()
