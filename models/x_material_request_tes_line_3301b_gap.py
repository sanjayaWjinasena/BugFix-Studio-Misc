from odoo import fields, models


class XMaterialRequestTesLine3301bGap(models.Model):
    _inherit = "x_material_request_tes_line_3301b"
    _rec_name = "x_name"  # Clear-DB Studio model: records are named by x_name

    x_material_request_tes_id = fields.Many2one(comodel_name="x_material_request_tes")
    x_name = fields.Char(string="Description", required=True)
