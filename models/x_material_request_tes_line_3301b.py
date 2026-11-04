from odoo import fields, models


class XMaterialRequestTesLine3301b(models.Model):
    _name = "x_material_request_tes_line_3301b"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "material_request_tes_line"

    x_material_request_tes_id = fields.Many2one(comodel_name="x_material_request_tes")
    name = fields.Char(string="Description", required=True)
    sequence = fields.Integer(string="Sequence")


class XMaterialRequestTesLine3301bGap(models.Model):
    _inherit = "x_material_request_tes_line_3301b"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    x_material_request_tes_id = fields.Many2one(comodel_name="x_material_request_tes")
    name = fields.Char(string="Description", required=True)
