from odoo import fields, models


class XBveSamplebalancemovementreport(models.Model):
    _name = "bve.samplebalancemovementreport"
    _description = "Sample Balance Movement Report"

    bve_t1_account_id = fields.Many2one(
        comodel_name="account.account", string="Account", readonly=True
    )
    bve_t1_balance = fields.Float(string="Balance", readonly=True)
    bve_t1_company_id = fields.Many2one(
        comodel_name="res.company", string="Company", readonly=True
    )
    bve_t1_credit = fields.Float(string="Credit", readonly=True)
    bve_t1_date = fields.Date(string="Date", readonly=True)
    bve_t1_debit = fields.Float(string="Debit", readonly=True)


class XBveSamplebalancemovementreportGap(models.Model):
    _inherit = "bve.samplebalancemovementreport"

    bve_t1_account_id = fields.Many2one(
        comodel_name="account.account", string="Account", readonly=True
    )
    bve_t1_balance = fields.Float(string="Balance", readonly=True)
    bve_t1_company_id = fields.Many2one(
        comodel_name="res.company", string="Company", readonly=True
    )
    bve_t1_credit = fields.Float(string="Credit", readonly=True)
    bve_t1_date = fields.Date(string="Date", readonly=True)
    bve_t1_debit = fields.Float(string="Debit", readonly=True)
