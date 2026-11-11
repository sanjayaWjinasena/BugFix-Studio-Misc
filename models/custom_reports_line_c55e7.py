from odoo import fields, models

# NOTE (v0.0.112): the Many2one(s) custom_reports_id (-> custom_reports) were MOVED
# to BugFix-Custom-Reports v0.0.18 models/custom_reports_line_c55e7.py.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.


class XCustomReportsLineC55e7(models.Model):
    _name = "custom_reports_line_c55e7"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "custom_reports_line"

    name = fields.Char(string="Description", required=True)
    sequence = fields.Integer()


class XCustomReportsLineC55e7Gap(models.Model):
    _inherit = "custom_reports_line_c55e7"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Description", required=True)
