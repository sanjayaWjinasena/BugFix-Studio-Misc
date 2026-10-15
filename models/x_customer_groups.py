from odoo import fields, models


class XCustomerGroups(models.Model):
    _name = "x_customer_groups"
    _rec_name = "x_name"  # Clear-DB Studio model: records are named by x_name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Customer Groups"

    x_name = fields.Char(string="Group Description")
    x_studio_sequence = fields.Integer(string="Sequence")


class XCustomerGroupsGap(models.Model):
    _inherit = "x_customer_groups"
    _rec_name = "x_name"  # Clear-DB Studio model: records are named by x_name

    x_name = fields.Char(string="Group Description")
