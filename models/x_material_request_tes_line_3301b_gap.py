# -*- coding: utf-8 -*-
from odoo import models, fields

class XMaterialRequestTesLine3301bGap(models.Model):
    _inherit = 'x_material_request_tes_line_3301b'

    x_material_request_tes_id = fields.Many2one(comodel_name='x_material_request_tes', string='X Material Request Tes')
    x_name = fields.Char(string='Description', required=True)
