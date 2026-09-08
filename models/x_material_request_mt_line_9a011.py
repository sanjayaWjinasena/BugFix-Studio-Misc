# -*- coding: utf-8 -*-
from odoo import models, fields

class XMaterialRequestMtLine9a011(models.Model):
    _name = 'x_material_request_mt_line_9a011'
    _description = 'material_request_mt_line'

    x_material_request_mt_id = fields.Many2one(comodel_name='x_material_request_mt', string='X Material Request Mt')
    x_name = fields.Char(string='Description', required=True)
    x_studio_sequence = fields.Integer(string='Sequence')
