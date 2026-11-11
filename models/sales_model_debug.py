from odoo import fields, models


class XSalesModelDebug(models.Model):
    _name = "sales_model_debug"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Sales Model Debug"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Method Name")
    end_time = fields.Datetime(string="End Time")
    sequence = fields.Integer(string="Sequence")
    start_time = fields.Datetime(string="Start Time")
