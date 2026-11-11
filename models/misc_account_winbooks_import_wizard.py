from odoo import fields, models


class X_account_winbooks_import_wizard(models.Model):
    _name = "misc_account_winbooks_import_wizard"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Account Winbooks import wizard"

    name = fields.Char()


class XAccountWinbooksImportWizardGap(models.Model):
    _inherit = "misc_account_winbooks_import_wizard"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char()
