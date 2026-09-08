# -*- coding: utf-8 -*-
from odoo import models, fields

class XMaterialRequestTesLine3301b(models.Model):
    _name = 'x_material_request_tes_line_3301b'
    _description = 'material_request_tes_line'

    x_material_request_tes_id = fields.Many2one(comodel_name='x_material_request_tes', string='X Material Request Tes')
    x_name = fields.Char(string='Description', required=True)
    x_studio_sequence = fields.Integer(string='Sequence')
