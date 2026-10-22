# -*- coding: utf-8 -*-
"""v0.0.127: mrp.eco.x_studio_item_approved follows the product's approval again.

The field becomes related='product_tmpl_id.x_studio_item_approved' (store=True), as on
Clear-DB. The column already exists from the plain boolean, so Odoo does not fill it;
recompute it once for every ECO. ORM only; no-op when there are no ECOs.
"""
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    ecos = env['mrp.eco'].with_context(active_test=False).search([])
    if not ecos:
        return
    env.add_to_compute(ecos._fields['x_studio_item_approved'], ecos)
    ecos.flush_recordset(['x_studio_item_approved'])
    _logger.info('BugFix-Studio-Misc: recomputed Approved Item on %s ECOs', len(ecos))
