from odoo import fields, models


class XCustomReportsTag(models.Model):
    _name = "custom_reports_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Custom Reports Tags"

    color = fields.Integer()
    name = fields.Char(required=True)


class XCustomReportsTagGap(models.Model):
    _inherit = "custom_reports_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    color = fields.Integer()
    name = fields.Char(required=True)
