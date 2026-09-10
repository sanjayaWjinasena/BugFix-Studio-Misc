# -*- coding: utf-8 -*-
from odoo import models, fields

class XTest02Gap(models.Model):
    _inherit = 'x_test02'

    x_active = fields.Boolean(string='Active')
    x_currency_id = fields.Many2one(comodel_name='res.currency', string='Currency')
    x_name = fields.Char(string='Name')
    x_studio_charges_1 = fields.Many2many(comodel_name='x_trf_charges', relation='x_test02_x_trf_charges_x_studio_charges_1_rel', string='Charges-1')
    x_studio_charges_2 = fields.Many2many(comodel_name='x_trf_charges', relation='x_test02_x_trf_charges_x_studio_charges_2_rel', string='Charges-2')
    x_studio_many2many_field_JKvVx = fields.Many2many(comodel_name='x_misc_charge_codes', string='Misc Charge Codes')
    x_studio_many2many_field_c0IAp = fields.Many2many(comodel_name='x_trf_charges', relation='x_test02_x_trf_charges_x_studio_many2many_field_c0IAp_rel', string='Charges')
    x_studio_types = fields.Many2one(comodel_name='helpdesk.ticket.type', string='Types')
    x_test123 = fields.Float(string='test123')
