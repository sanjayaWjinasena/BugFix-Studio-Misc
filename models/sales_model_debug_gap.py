from odoo import fields, models


class XSalesModelDebugGap(models.Model):
    _inherit = "sales_model_debug"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char(string="Method Name")
