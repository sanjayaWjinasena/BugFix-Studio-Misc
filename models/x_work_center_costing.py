# -*- coding: utf-8 -*-
from odoo import models, fields

class XWorkCenterCosting(models.Model):
    _name = 'x_work_center_costing'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Work Center Costing'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_general_cost_credit_account = fields.Many2one(comodel_name='account.account', string='General Cost Credit Account')
    x_studio_general_cost_debit_account = fields.Many2one(comodel_name='account.account', string='General Cost Debit Account')
    x_studio_labour_cost_credit_account = fields.Many2one(comodel_name='account.account', string='Labour Cost Credit Account')
    x_studio_labour_cost_debit_account = fields.Many2one(comodel_name='account.account', string='Labour Cost Debit Account')
    x_studio_labour_ot_cost_credit_account = fields.Many2one(comodel_name='account.account', string='Labour OT Cost Credit Account ')
    x_studio_labour_ot_cost_debit_account = fields.Many2one(comodel_name='account.account', string='Labour OT Cost Debit Account ')
    x_studio_overhead_cost_credit_account = fields.Many2one(comodel_name='account.account', string='Overhead Cost Credit Account')
    x_studio_overhead_cost_debit_account = fields.Many2one(comodel_name='account.account', string='Overhead Cost Debit Account')
    x_studio_sequence = fields.Integer(string='Sequence')
