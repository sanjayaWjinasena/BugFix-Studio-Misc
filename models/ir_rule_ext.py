# -*- coding: utf-8 -*-
"""Studio field ports for ir.rule (auto-ported from CDB)."""
from odoo import fields, models


class XIrRuleExt(models.Model):
    _inherit = 'ir.rule'

    x_studio_description = fields.Text(string='Description')
