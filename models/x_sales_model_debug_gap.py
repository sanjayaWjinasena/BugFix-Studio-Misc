from odoo import fields, models


class XSalesModelDebugGap(models.Model):
    _inherit = "x_sales_model_debug"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Method Name")
