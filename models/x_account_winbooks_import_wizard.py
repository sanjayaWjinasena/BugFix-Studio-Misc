# -*- coding: utf-8 -*-
from odoo import models, fields

class X_account_winbooks_import_wizard(models.Model):
    _name = 'x_account_winbooks_import_wizard'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name
    _description = 'Account Winbooks import wizard'

    x_name = fields.Char(string='Name')
