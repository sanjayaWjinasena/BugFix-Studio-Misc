from odoo import fields, models


class XMaterialRequestTesLine3301b(models.Model):
    _name = "material_request_tes_line_3301b"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "material_request_tes_line"

    material_request_tes_id = fields.Many2one(comodel_name="material_request_tes")
    name = fields.Char(string="Description", required=True)
    sequence = fields.Integer()


class XMaterialRequestTesLine3301bGap(models.Model):
    _inherit = "material_request_tes_line_3301b"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    material_request_tes_id = fields.Many2one(comodel_name="material_request_tes")
    name = fields.Char(string="Description", required=True)
