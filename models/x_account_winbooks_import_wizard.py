# -*- coding: utf-8 -*-
from odoo import models, fields

class X_account_winbooks_import_wizard(models.Model):
    _name = 'x_account_winbooks_import_wizard'
    _description = 'Account Winbooks import wizard'

    x_name = fields.Char(string='Name')
