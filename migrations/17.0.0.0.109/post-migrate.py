# -*- coding: utf-8 -*-
"""v17.0.0.0.109: back-fill ir.actions.server.update_path from update_field_id.name.

Odoo 15 object_write server actions were defined by setting
`update_field_id` alone. Odoo 17 refactored to require a dotted field
path in `update_path`, with `update_field_id` kept only as a convenience
pointer. During the 15→17 migration of CDB, Studio-created object_write
actions got re-created on the target env with `update_field_id` set but
`update_path` empty. Odoo's `_traverse_path` then raises:

  File ".../ir_actions.py", line 656, in _traverse_path
      field = Model._fields[field_name]
  KeyError: ''

…when the action fires. This blocks any create/write path that triggers
one of these actions via base.automation — e.g. creating an
x_purchase_request record whose downstream automations touch
x_purchase_request_lin.

Fix: for every ir.actions.server with state='object_write',
update_field_id set, and empty update_path, write update_path to the
technical name of update_field_id. Matches CDB's values verbatim
(verified via RPC — e.g. "PR Line Order Remainder Update" → path
'x_studio_order_remainder' on CDB).

ORM only, no cr.execute.
"""
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    Action = env['ir.actions.server'].sudo()
    broken = Action.search([
        ('state', '=', 'object_write'),
        ('update_field_id', '!=', False),
        '|', ('update_path', '=', False), ('update_path', '=', ''),
    ])
    if not broken:
        _logger.info(
            '[BugFix-Studio-Misc v109] no broken object_write actions; nothing to do.'
        )
        return
    fixed = 0
    for act in broken:
        field = act.update_field_id
        if not field or not field.name:
            continue
        try:
            act.update_path = field.name
            fixed += 1
            _logger.info(
                '[BugFix-Studio-Misc v109] action id=%s %r: update_path <- %r '
                '(field %r on %r)',
                act.id, act.name, field.name, field.field_description,
                (field.model_id.model if field.model_id else '?'),
            )
        except Exception as e:
            _logger.warning(
                '[BugFix-Studio-Misc v109] action id=%s %r: skip, %s',
                act.id, act.name, e,
            )
    _logger.info(
        '[BugFix-Studio-Misc v109] fixed %d of %d broken object_write actions.',
        fixed, len(broken),
    )
