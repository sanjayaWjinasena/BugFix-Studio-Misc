# -*- coding: utf-8 -*-
from odoo import models, fields

class XBveSamplebalancemovementreportGap(models.Model):
    _inherit = 'x_bve.samplebalancemovementreport'

    x_bve_t1_account_id = fields.Many2one(comodel_name='account.account', string='Account', readonly=True)
    x_bve_t1_balance = fields.Float(string='Balance', readonly=True)
    x_bve_t1_company_id = fields.Many2one(comodel_name='res.company', string='Company', readonly=True)
    x_bve_t1_credit = fields.Float(string='Credit', readonly=True)
    x_bve_t1_date = fields.Date(string='Date', readonly=True)
    x_bve_t1_debit = fields.Float(string='Debit', readonly=True)
