from odoo import fields, models


class XMaterialRequestMtLine9a011(models.Model):
    _name = "x_material_request_mt_line_9a011"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "material_request_mt_line"

    x_material_request_mt_id = fields.Many2one(comodel_name="x_material_request_mt")
    name = fields.Char(string="Description", required=True)
    sequence = fields.Integer(string="Sequence")


class XMaterialRequestMtLine9a011Gap(models.Model):
    _inherit = "x_material_request_mt_line_9a011"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    x_material_request_mt_id = fields.Many2one(comodel_name="x_material_request_mt")
    name = fields.Char(string="Description", required=True)
