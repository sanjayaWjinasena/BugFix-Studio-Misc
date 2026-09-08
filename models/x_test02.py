# -*- coding: utf-8 -*-
from odoo import models, fields

class X_test02(models.Model):
    _name = 'x_test02'
    _description = 'TEST02'

    x_active = fields.Boolean(string='Active')
    x_currency_id = fields.Many2one(comodel_name='res.currency', string='Currency')
    x_name = fields.Char(string='Name')
    x_studio_chk_atomated_action = fields.Integer(string='CHK Atomated Action')
    x_studio_chk_server_action = fields.Integer(string='CHK Server Action')
    x_studio_company_id = fields.Many2one(comodel_name='res.company', string='Company', copy=False)
    x_studio_date = fields.Datetime(string='Date')
    x_studio_float_field_skhh9 = fields.Float(string='Test Number')
    x_studio_jam = fields.Char(string='New Text')
    x_studio_jam_1 = fields.Char(string='JAM')
    x_studio_jin = fields.Char(string='JIN')
    x_studio_jin_2 = fields.Char(string='JIN')
    x_studio_name_1 = fields.Char(string='Name-1')
    x_studio_one2many_field_51FSD = fields.One2many(comodel_name='x_test_layout', inverse_name='x_studio_line_ids', string='New One2many', copy=False)
    x_studio_one2many_field_D3cuD = fields.One2many(comodel_name='x_test_layout', inverse_name='x_studio_line_ids', string='New One2many', copy=False)
    x_studio_one2many_field_Q8Xws = fields.One2many(comodel_name='x_test_layout', inverse_name='x_studio_line_ids', string='New One2many', copy=False)
    x_studio_pipeline_status_bar = fields.Selection(selection=[('status1', 'First Status'), ('status2', 'Second Status'), ('status3', 'Third Status'), ('Fourth Status', 'Fourth Status')], string='Pipeline status bar')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_status = fields.Selection(selection=[('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3')], string='Status')
    x_studio_status2 = fields.Selection(selection=[('S5', 'S5'), ('S6', 'S6')], string='Status2')
    x_studio_status_1 = fields.Selection(selection=[('Status 01', 'Status 01'), ('Status 02', 'Status 02')], string='Status')
    x_studio_test_03 = fields.Monetary(string='Test 03', copy=False, currency_field='x_currency_id')
    x_studio_test_char = fields.Char(string='Test Char')
    x_studio_test_number_1 = fields.Float(string='Test Number', copy=False)
    x_studio_test_number_2 = fields.Float(string='Test Number 2')
    x_studio_test_value = fields.Integer(string='Test Value', copy=False)
    x_studio_testing = fields.Text(string='Testing')
    x_studio_testing_02 = fields.Float(string='Testing02')
    x_studio_text_field_eKlfk = fields.Text(string='X Studio Text Field Eklfk')
    x_test123 = fields.Float(string='test123')
