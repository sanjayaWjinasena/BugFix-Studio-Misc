from odoo import fields, models


class X_account_winbooks_import_wizard(models.Model):
    _name = "x_account_winbooks_import_wizard"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Account Winbooks import wizard"

    name = fields.Char(string="Name")


class XAccountWinbooksImportWizardGap(models.Model):
    _inherit = "x_account_winbooks_import_wizard"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Name")
