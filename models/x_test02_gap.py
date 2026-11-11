from odoo import fields, models


class XTest02Gap(models.Model):
    _inherit = "x_test02"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    name = fields.Char(string="Name")
    x_studio_charges_1 = fields.Many2many(
        comodel_name="trf_charges",
        column1="x_test02_id",
        column2="x_trf_charges_id",
        relation="x_test02_x_trf_charges_x_studio_charges_1_rel",
        string="Charges-1",
    )
    x_studio_charges_2 = fields.Many2many(
        comodel_name="trf_charges",
        column1="x_test02_id",
        column2="x_trf_charges_id",
        relation="x_test02_x_trf_charges_x_studio_charges_2_rel",
        string="Charges-2",
    )
    x_studio_many2many_field_JKvVx = fields.Many2many(
        comodel_name="misc_charge_codes",
        relation="x_misc_charge_codes_x_test02_rel",
        column1="x_test02_id",
        column2="x_misc_charge_codes_id",
        string="Misc Charge Codes",
    )
    x_studio_many2many_field_c0IAp = fields.Many2many(
        comodel_name="trf_charges",
        column1="x_test02_id",
        column2="x_trf_charges_id",
        relation="x_test02_x_trf_charges_x_studio_many2many_field_c0IAp_rel",
        string="Charges",
    )
    x_studio_types = fields.Many2one(
        comodel_name="helpdesk.ticket.type", string="Types"
    )
    x_test123 = fields.Float(string="test123")
