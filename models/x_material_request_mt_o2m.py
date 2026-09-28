# -*- coding: utf-8 -*-
"""Add parent-side O2M x_material_request_mt_line_ids_7737e via _inherit.

Declared in this module (not BugFix-Stock where the parent x_material_request_mt
lives) because the child comodel x_material_request_mt_line_9a011 is owned here.
BugFix-Stock loads BEFORE BugFix-Studio-Misc, so a same-module O2M on the parent
raises 'comodel not in registry' at registry setup.
See [[feedback-setup-related-race]].
"""
from odoo import fields, models


class XMaterialRequestMt(models.Model):
    _inherit = 'x_material_request_mt'

    x_material_request_mt_line_ids_7737e = fields.One2many(
        comodel_name='x_material_request_mt_line_9a011',
        inverse_name='x_material_request_mt_id',
        string='New Lines',
    )
