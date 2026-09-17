# -*- coding: utf-8 -*-
"""Studio field ports for base.automation (auto-ported from CDB)."""
from odoo import fields, models


class XBaseAutomationExt(models.Model):
    _inherit = 'base.automation'

    x_studio_comments = fields.Char(string='Comments')
    x_studio_status = fields.Selection([('None', 'None'), ('Active in V15', 'Active in V15'), ('Archived in V15', 'Archived in V15'), ('Reactivated in V15', 'Reactivated in V15')], string='Status')
