from odoo import fields, models


class XSalesModelDebug(models.Model):
    _name = "x_sales_model_debug"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Sales Model Debug"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Method Name")
    x_studio_end_time = fields.Datetime(string="End Time")
    sequence = fields.Integer(string="Sequence")
    x_studio_start_time = fields.Datetime(string="Start Time")
