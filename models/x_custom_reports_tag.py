from odoo import fields, models


class XCustomReportsTag(models.Model):
    _name = "x_custom_reports_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Custom Reports Tags"

    color = fields.Integer(string="Color")
    name = fields.Char(string="Name", required=True)


class XCustomReportsTagGap(models.Model):
    _inherit = "x_custom_reports_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    color = fields.Integer(string="Color")
    name = fields.Char(string="Name", required=True)
