"""v0.0.130: mrp.eco.item_approved follows the product's approval (import restored).

v0.0.127 made the field related='product_tmpl_id.item_approved' (store=True), as on Clear-DB, but the
model file was not imported on the renamed branches, so databases installed from them kept the plain
boolean. With the import back, recompute the stored column once for every ECO (Odoo does not refill an
existing column). ORM only; no-op when there are no ECOs.
"""

import logging

from odoo import SUPERUSER_ID, api

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    ecos = env["mrp.eco"].with_context(active_test=False).search([])
    if not ecos:
        return
    env.add_to_compute(ecos._fields["item_approved"], ecos)
    ecos.flush_recordset(["item_approved"])
    _logger.info("BugFix-Studio-Misc: recomputed Approved Item on %s ECOs", len(ecos))
