# -*- coding: utf-8 -*-
"""v17.0.0.0.110: set evaluation_type='equation' on object_write actions
whose `value` is a Python expression (not a literal).

v0.0.109 back-filled update_path from update_field_id.name, which unblocked
the KeyError('') crash. But the next error path hit was:

  ValueError: could not convert string to float:
    'record.x_studio_quantity - (record.x_studio_po_quantity + record.x_studio_cash_quantity)'

Odoo's object_write handler reads `value` and, with evaluation_type='value'
(the default), tries to coerce it to the field's native type. For a numeric
field it calls float(value); the Studio equation strings don't parse.

CDB has these actions as evaluation_type='equation' — in that mode Odoo
runs safe_eval on `value` with the record in scope. On target the eval type
got lost in the 15->17 migration.

Fix: for every object_write action whose `value` contains Python-expression
hints (`record.`, `env.`, `self.`, arithmetic operators, assignment),
switch evaluation_type to 'equation'. Idempotent — only touches rows where
eval_type != 'equation' already.

ORM only, no cr.execute.
"""
import logging
import re

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

# Signals that a value is a Python expression, not a literal:
#   record.x_...   env['...']   self.id   + - * /   assignment
EXPR_HINT = re.compile(r'record\.|\benv\[|\benv\.|\bself\.|[+\-*/()]|^[a-zA-Z_]+\s*=')


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    Action = env['ir.actions.server'].sudo()
    candidates = Action.search([
        ('state', '=', 'object_write'),
        ('value', '!=', False),
        ('evaluation_type', '!=', 'equation'),
    ])
    fixed = 0
    for act in candidates:
        val = act.value or ''
        if not EXPR_HINT.search(val):
            continue
        try:
            act.evaluation_type = 'equation'
            fixed += 1
            _logger.info(
                '[BugFix-Studio-Misc v110] action id=%s %r: evaluation_type '
                '<- equation (value=%r)',
                act.id, act.name, val[:80],
            )
        except Exception as e:
            _logger.warning(
                '[BugFix-Studio-Misc v110] action id=%s %r: skip, %s',
                act.id, act.name, e,
            )
    _logger.info(
        '[BugFix-Studio-Misc v110] fixed %d of %d candidate object_write actions.',
        fixed, len(candidates),
    )
