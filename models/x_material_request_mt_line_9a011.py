from odoo import fields, models


class XMaterialRequestMtLine9a011(models.Model):
    _name = "x_material_request_mt_line_9a011"
    _rec_name = "x_name"  # Clear-DB Studio model: records are named by x_name
    _description = "material_request_mt_line"

    x_material_request_mt_id = fields.Many2one(comodel_name="x_material_request_mt")
    x_name = fields.Char(string="Description", required=True)
    x_studio_sequence = fields.Integer(string="Sequence")


class XMaterialRequestMtLine9a011Gap(models.Model):
    _inherit = "x_material_request_mt_line_9a011"
    _rec_name = "x_name"  # Clear-DB Studio model: records are named by x_name

    x_material_request_mt_id = fields.Many2one(comodel_name="x_material_request_mt")
    x_name = fields.Char(string="Description", required=True)
