# -*- coding: utf-8 -*-
from odoo import models, fields

class XAccountWinbooksImportWizardGap(models.Model):
    _inherit = 'x_account_winbooks_import_wizard'

    x_name = fields.Char(string='Name')
