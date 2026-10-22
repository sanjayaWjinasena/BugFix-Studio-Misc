# -*- coding: utf-8 -*-
from odoo import fields, models


class MrpEco(models.Model):
    _inherit = 'mrp.eco'

    # Clear-DB: related to the product's "Item Approved". The port (BugFix-MRP) made it a plain
    # boolean, so an ECO never saw the approval: Bill of Materials stayed read-only, the ECO saved
    # without one, and Start Revision failed with "Expected singleton: mrp.bom()" (bug sheet PLM,
    # 22/Oct, Kapila). Declared here because the product field comes from BugFix-Sales, which
    # BugFix-MRP does not depend on; this module depends on both.
    x_studio_item_approved = fields.Boolean(
        string='Approved Item', related='product_tmpl_id.x_studio_item_approved', store=True)
