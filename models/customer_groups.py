from odoo import fields, models


class XCustomerGroups(models.Model):
    _name = "customer_groups"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Customer Groups"

    name = fields.Char(string="Group Description")
    sequence = fields.Integer()


class XCustomerGroupsGap(models.Model):
    _inherit = "customer_groups"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Group Description")
