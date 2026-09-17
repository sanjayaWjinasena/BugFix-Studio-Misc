# -*- coding: utf-8 -*-
"""Studio field ports for ir.model.access (auto-ported from CDB)."""
from odoo import fields, models


class XIrModelAccessExt(models.Model):
    _inherit = 'ir.model.access'

    x_studio_number_of_users = fields.Many2many('res.users', string='Users', readonly=True)
    x_studio_user_name = fields.Char(string='User Name', readonly=True)
