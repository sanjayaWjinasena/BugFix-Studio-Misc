# -*- coding: utf-8 -*-
from odoo import models, fields

class XAccountWinbooksImportWizardGap(models.Model):
    _inherit = 'x_account_winbooks_import_wizard'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_name = fields.Char(string='Name')
