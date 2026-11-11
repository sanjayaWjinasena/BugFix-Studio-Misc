from odoo import fields, models


class XWorkCenterCosting(models.Model):
    _name = "work_center_costing"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Work Center Costing"

    active = fields.Boolean()
    name = fields.Char()
    general_cost_credit_account = fields.Many2one(comodel_name="account.account")
    general_cost_debit_account = fields.Many2one(comodel_name="account.account")
    labour_cost_credit_account = fields.Many2one(comodel_name="account.account")
    labour_cost_debit_account = fields.Many2one(comodel_name="account.account")
    labour_ot_cost_credit_account = fields.Many2one(
        comodel_name="account.account", string="Labour OT Cost Credit Account "
    )
    labour_ot_cost_debit_account = fields.Many2one(
        comodel_name="account.account", string="Labour OT Cost Debit Account "
    )
    overhead_cost_credit_account = fields.Many2one(comodel_name="account.account")
    overhead_cost_debit_account = fields.Many2one(comodel_name="account.account")
    sequence = fields.Integer()
    # v0.0.104: 3 Studio "analytic tag" M2O fields that CDB left with
    # relation='_unknown'. In Odoo 17 the analytic-tag concept was
    # collapsed into account.analytic.account; that's the canonical
    # tag comodel and it fits the model's cost-centre theme.
    general_analytic_tag = fields.Many2one(comodel_name="account.analytic.account")
    labour_analytic_tag = fields.Many2one(comodel_name="account.analytic.account")
    overhead_analytic_tag = fields.Many2one(comodel_name="account.analytic.account")


class XWorkCenterCostingGap(models.Model):
    _inherit = "work_center_costing"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
