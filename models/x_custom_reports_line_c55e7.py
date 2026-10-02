# -*- coding: utf-8 -*-
from odoo import models, fields

# NOTE (v0.0.112): the Many2one(s) x_custom_reports_id (-> x_custom_reports) were MOVED to BugFix-Custom-Reports v0.0.18 models/x_custom_reports_line_c55e7.py.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.

class XCustomReportsLineC55e7(models.Model):
    _name = 'x_custom_reports_line_c55e7'
    _description = 'custom_reports_line'

    x_name = fields.Char(string='Description', required=True)
    x_studio_sequence = fields.Integer(string='Sequence')
